import { z } from "zod";
import { NextResponse } from "next/server";
import { getSession } from "@/server/auth/session";
import { assertOwnsChild } from "@/server/auth/ownership";
import { buildLeilaSystemPrompt, streamLeila } from "@/server/ai/leila";
import { progressRepo } from "@/server/repositories/progress";
import { curriculumRepo } from "@/server/repositories/curriculum";
import { chatRepo } from "@/server/repositories/chat";
import { buildLivingLeilaResponse } from "@/server/leila/living-leila-response";
import { summarizeLearnerMemory } from "@/server/learner-memory/learner-memory-engine";
import { AppError } from "@/server/errors";
import { aiChatLimiter } from "@/server/security/rate-limit";
import { buildPhase40LearningSnapshot } from "@/server/learning-experience/phase40-engine";

const DAILY_LIMIT = 30;

const schema = z.object({
  messages: z.array(z.object({
    role:    z.enum(["user", "assistant"]),
    content: z.string().min(1).max(4000),
  })).min(1).max(50),
  childId:   z.string().uuid(),
  lessonId:  z.string().uuid().optional(),
  sessionId: z.string().uuid().optional(), // resume existing session
  mood:      z.enum(["frustrated", "excited", "neutral"]).optional(),
  attemptCount: z.number().int().min(0).max(20).optional(),
});

function sse(event: Record<string, unknown>) {
  return new TextEncoder().encode(`data: ${JSON.stringify(event)}\n\n`);
}

export async function POST(request: Request) {
  const session = await getSession();
  if (!session) {
    return NextResponse.json({ success: false, message: "يجب تسجيل الدخول", code: "UNAUTHORIZED" }, { status: 401 });
  }

  try {
    const body = schema.parse(await request.json());

    // Rate limit
    const rl = await aiChatLimiter(session.sub);
    if (!rl.allowed) {
      return NextResponse.json({ success: false, message: "طلبات كثيرة. انتظر دقيقة.", code: "RATE_LIMITED" }, { status: 429 });
    }

    // Ownership
    const child = await assertOwnsChild(session.sub, body.childId);

    // Daily quota
    const used = await progressRepo.getDailyAiUsage(session.sub, "leila_text");
    if (used >= DAILY_LIMIT) {
      return NextResponse.json({
        success: false,
        message: `الحد اليومي ${DAILY_LIMIT} محادثة. ارجع غداً أو ارقَّ خطتك.`,
        code: "QUOTA_EXCEEDED",
        remaining: 0,
      }, { status: 429 });
    }

    // Get or create chat session (persistent memory)
    const chatSession = await chatRepo.getOrCreateSession(body.childId, body.lessonId);

    // Load conversation history from DB for context continuity
    const dbHistory = await chatRepo.getRecentMessages(chatSession.id, 16);
    const historyMessages = dbHistory
      .filter((m) => m.role === "user" || m.role === "assistant")
      .map((m) => ({ role: m.role as "user" | "assistant", content: m.content }));

    // The new user message (last in the array)
    const latestUserMsg = body.messages[body.messages.length - 1];

    // Save user message to DB
    await chatRepo.saveMessage(chatSession.id, "user", latestUserMsg.content);

    // Build rich adaptive context
    const [lesson, progressData] = await Promise.all([
      body.lessonId ? curriculumRepo.getLessonWithContent(body.lessonId) : Promise.resolve(null),
      progressRepo.getChildProgress(body.childId),
    ]);

    const completed  = progressData.filter((p) => p.status === "completed");
    const scores     = completed.filter((p) => p.score != null).map((p) => p.score!);
    const avgScore   = scores.length ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : 0;
    const needsReview = progressData.filter((p) => p.status === "needs_review")
      .slice(0, 3).map((p) => p.lesson?.titleAr ?? "").filter(Boolean);

    // Map grade slug to numeric level for persona selection
    const gradeSlug  = (child.grade as { slug?: string } | undefined)?.slug ?? "";
    const gradeLevel = gradeSlug.includes("ap") ? parseInt(gradeSlug.replace("ap","")) :
                       gradeSlug === "1ac" ? 7 : gradeSlug === "2ac" ? 8 :
                       gradeSlug === "3ac" ? 9 : gradeSlug === "tc"  ? 10 :
                       gradeSlug === "bac1" ? 11 : gradeSlug === "bac2" ? 12 : 1;

    const phase40Snapshot = buildPhase40LearningSnapshot({
      childId: body.childId,
      childName: child.name,
      xp: child.xp,
      streak: child.streak,
      progress: progressData,
      weakPoints: needsReview.map((topic) => ({ topic })),
    });

    const context = {
      childName:         child.name,
      gradeName:         child.grade?.titleAr,
      gradeLevel,
      lessonTitle:       lesson?.titleAr,
      lessonContent:     lesson?.content?.explanation,
      lessonVocabulary:  lesson?.content?.vocabulary ?? [],
      lessonExamples:    lesson?.content?.examples ?? [],
      lessonSummary:     lesson?.content?.summary ?? undefined,
      subjectName:       lesson?.unit?.subject?.titleAr,
      weakPoints:     needsReview,
      recentErrors:   needsReview,
      completedCount: completed.length,
      avgScore,
      streak:         child.streak,
      xp:             child.xp,
      mood:           body.mood,
      phase40TeachingMove: phase40Snapshot.nextTeacherMove,
      phase40TutorState: phase40Snapshot.tutorState,
      phase40MasteryScore: phase40Snapshot.masteryScore,
      phase40ConfidenceScore: phase40Snapshot.confidenceScore,
      attemptCount:   body.attemptCount,
      lastMessage:    latestUserMsg.content,
      mode:           body.lessonId ? "lesson" as const : "general" as const,
    };

    // Merge DB history with current messages (prefer DB for continuity)
    const fullHistory = historyMessages.length > 2
      ? historyMessages
      : body.messages.slice(0, -1); // use client-sent history if DB empty

    const messagesForAI = [
      ...fullHistory,
      { role: "user" as const, content: latestUserMsg.content },
    ];

    let totalTokens = 0;
    let fullResponse = "";

    const readableStream = new ReadableStream<Uint8Array>({
      async start(controller) {
        try {
          for await (const delta of streamLeila({ messages: messagesForAI, context })) {
            controller.enqueue(sse({ type: "token", content: delta }));
            totalTokens += Math.ceil(delta.length / 4);
            fullResponse += delta;
          }
          controller.enqueue(sse({ type: "done", sessionId: chatSession.id }));
        } catch (err) {
          const msg = err instanceof Error ? err.message : "حدث خطأ في الاتصال";
          controller.enqueue(sse({ type: "error", content: msg }));
        } finally {
          controller.close();
          // Persist assistant response + log usage
          if (fullResponse) {
            chatRepo.saveMessage(chatSession.id, "assistant", fullResponse).catch(console.error);
          }
          progressRepo.logAiUsage({
            userId:   session.sub,
            feature:  "leila_text",
            tokens:   totalTokens,
            provider: "groq",
            model:    "llama-3.3-70b-versatile",
            success:  true,
          }).catch(console.error);
        }
      },
    });

    return new Response(readableStream, {
      headers: {
        "Content-Type":      "text/event-stream; charset=utf-8",
        "Cache-Control":     "no-cache, no-transform",
        "Connection":        "keep-alive",
        "X-Accel-Buffering": "no",
        "X-Session-Id":      chatSession.id,
        "X-Quota-Used":      String(used + 1),
        "X-Quota-Limit":     String(DAILY_LIMIT),
      },
    });
  } catch (e) {
    if (e instanceof AppError) {
      return NextResponse.json({ success: false, message: e.message, code: e.code }, { status: e.status });
    }
    if (e instanceof z.ZodError) {
      return NextResponse.json({ success: false, message: "بيانات غير صالحة", code: "VALIDATION_ERROR" }, { status: 422 });
    }
    console.error("[Leila API]", e);
    return NextResponse.json({ success: false, message: "حدث خطأ داخلي", code: "INTERNAL_ERROR" }, { status: 500 });
  }
}

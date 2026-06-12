import { NextResponse } from "next/server";
import Groq from "groq-sdk";
import { z } from "zod";
import { getSession } from "@/server/auth/session";
import { aiChatLimiter } from "@/server/security/rate-limit";
import { AGENT_PROMPTS, buildAgentContext } from "@/server/ai/pipeline/prompts";
import { getPipelineAgents } from "@/server/ai/pipeline/config";
import { buildCurriculumGrounding } from "@/server/ai/pipeline/grounding";
import { clarificationMessage, guardAgentOutput } from "@/server/ai/pipeline/quality";
import type { AgentId, PipelineFlowId } from "@/server/ai/pipeline/config";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

const ALLOWED_MODELS = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"] as const;

const inputSchema = z.object({
  input: z.string().min(3, "اكتب طلبًا أو سؤالًا واضحًا").max(5000),
  flow: z.enum(["full", "research", "analysis", "quick", "lesson", "edu"]).default("full"),
  model: z.enum(ALLOWED_MODELS).default("llama-3.3-70b-versatile"),
});

function sse(data: Record<string, unknown>) {
  return new TextEncoder().encode(`data: ${JSON.stringify(data)}\n\n`);
}

function streamResponse(stream: ReadableStream<Uint8Array>) {
  return new Response(stream, {
    headers: {
      "Content-Type": "text/event-stream; charset=utf-8",
      "Cache-Control": "no-cache, no-transform",
      "Connection": "keep-alive",
      "X-Accel-Buffering": "no",
    },
  });
}

export async function POST(request: Request) {
  const session = await getSession();
  if (!session) {
    return NextResponse.json({ success: false, message: "يجب تسجيل الدخول أولًا" }, { status: 401 });
  }

  const limit = await aiChatLimiter(`${session.sub}:pipeline`);
  if (!limit.allowed) {
    return NextResponse.json(
      { success: false, message: "طلبات كثيرة. انتظر دقيقة ثم جرّب مرة أخرى." },
      { status: 429 },
    );
  }

  const parsed = inputSchema.safeParse(await request.json().catch(() => null));
  if (!parsed.success) {
    return NextResponse.json(
      { success: false, message: parsed.error.errors[0]?.message ?? "طلب غير صالح" },
      { status: 400 },
    );
  }

  const { input, flow, model } = parsed.data as {
    input: string;
    flow: PipelineFlowId;
    model: typeof ALLOWED_MODELS[number];
  };
  const agentIds = getPipelineAgents(flow);
  const grounding = await buildCurriculumGrounding(input);

  if (grounding.mode === "clarification_needed") {
    const message = clarificationMessage();
    const stream = new ReadableStream<Uint8Array>({
      start(controller) {
        const runId = crypto.randomUUID();
        controller.enqueue(sse({
          event: "start",
          runId,
          flow,
          agents: [],
          curriculumGrounding: {
            mode: grounding.mode,
            strength: grounding.strength,
            subject: grounding.subject,
            grade: grounding.grade,
            topic: grounding.topic,
            confidence: grounding.confidence,
            warnings: grounding.warnings,
          },
        }));
        controller.enqueue(sse({ event: "end", status: "clarification_needed", finalOutput: message, final_output: message }));
        controller.close();
      },
    });

    return streamResponse(stream);
  }

  const apiKey = process.env.GROQ_API_KEY;
  if (!apiKey) {
    return NextResponse.json({ success: false, message: "GROQ_API_KEY غير موجود في البيئة" }, { status: 503 });
  }

  const groq = new Groq({ apiKey });

  const stream = new ReadableStream<Uint8Array>({
    async start(controller) {
      const runId = crypto.randomUUID();
      const startedAt = Date.now();
      const previousOutputs: Partial<Record<AgentId, string>> = {};

      controller.enqueue(sse({
        event: "start",
        runId,
        flow,
        agents: agentIds,
        curriculumGrounding: {
          mode: grounding.mode,
          strength: grounding.strength,
          subject: grounding.subject,
          grade: grounding.grade,
          topic: grounding.topic,
          matches: grounding.matches.length,
          confidence: grounding.confidence,
          missingDbLesson: grounding.missingDbLesson,
          studentFacingNotice: grounding.studentFacingNotice,
          warnings: grounding.warnings,
        },
      }));

      try {
        for (const agentId of agentIds) {
          const agentStart = Date.now();
          controller.enqueue(sse({ event: "agent_start", agentId, agent_id: agentId, ts: agentStart }));

          const completion = await groq.chat.completions.create({
            model,
            temperature: agentId === "writer" || agentId === "exercise_gen" ? 0.45 : 0.6,
            max_tokens: agentId === "writer" || agentId === "exercise_gen" ? 1900 : 1000,
            stream: true,
            messages: [
              { role: "system", content: AGENT_PROMPTS[agentId] },
              { role: "user", content: buildAgentContext(agentId, input, previousOutputs, grounding) },
            ],
          });

          let output = "";
          for await (const chunk of completion) {
            output += chunk.choices[0]?.delta?.content ?? "";
          }

          const guard = guardAgentOutput({ agentId, output, input, grounding, final: agentId === agentIds[agentIds.length - 1] });
          if (!guard.ok) {
            console.error("[Oqul Pipeline Guard]", { agentId, issues: guard.issues, subject: grounding.subject, topic: grounding.topic });
            controller.enqueue(sse({
              event: "error",
              message: `تم إيقاف النتيجة لأن الوكيل خرج عن السياق المنهجي أو أنتج محتوى ضعيفًا: ${guard.issues.join(", ")}`,
              guardIssues: guard.issues,
              agentId,
              agent_id: agentId,
            }));
            return;
          }

          previousOutputs[agentId] = output;
          controller.enqueue(sse({ event: "agent_delta", agentId, agent_id: agentId, delta: output }));
          controller.enqueue(sse({
            event: "agent_done",
            agentId,
            agent_id: agentId,
            output,
            durationMs: Date.now() - agentStart,
            duration_ms: Date.now() - agentStart,
          }));
        }

        const finalAgent = agentIds[agentIds.length - 1];
        const finalOutput = previousOutputs[finalAgent] ?? "";
        const finalGuard = guardAgentOutput({ agentId: finalAgent, output: finalOutput, input, grounding, final: true });
        if (!finalGuard.ok) {
          controller.enqueue(sse({
            event: "error",
            message: `لم يتم عرض النتيجة النهائية لأنها لم تجتز حارس الجودة: ${finalGuard.issues.join(", ")}`,
            guardIssues: finalGuard.issues,
          }));
          return;
        }

        controller.enqueue(sse({
          event: "end",
          status: "done",
          totalMs: Date.now() - startedAt,
          finalOutput,
          final_output: finalOutput,
        }));
      } catch (error) {
        console.error("[Oqul Pipeline]", error);
        controller.enqueue(sse({
          event: "error",
          message: "حدث خطأ أثناء تشغيل الوكلاء. تحقق من GROQ_API_KEY أو جرّب نموذجًا آخر.",
        }));
      } finally {
        controller.close();
      }
    },
  });

  return streamResponse(stream);
}

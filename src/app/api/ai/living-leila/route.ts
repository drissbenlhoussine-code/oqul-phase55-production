/**
 * /api/ai/living-leila - Cognitive Intelligence Endpoint
 */
import { NextRequest } from "next/server";
import { z } from "zod";
import { assertOwnsChild } from "@/server/auth/ownership";
import { AppError } from "@/server/errors";
import { requireAuth } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";
import { summarizeLearnerMemory } from "@/server/learner-memory/learner-memory-engine";
import { childrenRepo } from "@/server/repositories/children";
import { progressRepo } from "@/server/repositories/progress";
import { buildLivingLeilaResponse } from "@/server/leila/living-leila-response";

const schema = z.object({
  childId: z.string().uuid(),
  emotion: z.enum(["confident", "frustrated", "tired", "curious", "neutral"]).optional(),
});

export async function POST(request: NextRequest) {
  try {
    const session = await requireAuth();
    const body = schema.parse(await request.json());
    await assertOwnsChild(session.sub, body.childId);

    const [child, progress] = await Promise.all([
      childrenRepo.findById(body.childId),
      progressRepo.getChildProgress(body.childId),
    ]);

    if (!child) throw new AppError("Child not found", "NOT_FOUND", 404);

    const completed = progress.filter((p) => p.status === "completed");
    const needsReview = progress.filter((p) => p.status === "needs_review");
    const scores = completed.filter((p) => p.score != null).map((p) => p.score!);
    const avgScore = scores.length
      ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length)
      : 50;

    const signals = progress.slice(0, 15).map((p) => ({
      correct: (p.score ?? 0) >= 60,
      masteryScore: p.score ?? 0,
      emotion: body.emotion,
      skillId: p.lessonId,
    }));

    const memory = summarizeLearnerMemory(signals);

    const confidenceScore = Math.max(
      0,
      Math.min(
        100,
        50 + completed.length * 3 - needsReview.length * 10 + (avgScore > 80 ? 15 : avgScore > 60 ? 5 : -5),
      ),
    );

    const livingResponse = buildLivingLeilaResponse({
      childName: child.name,
      masteryScore: avgScore,
      confidenceScore,
      recentMistakes: needsReview.length,
      emotion: body.emotion,
    });

    return ok({
      childName: child.name,
      livingResponse,
      memory: {
        summary: memory.summary,
        emotionalState: memory.emotionalState,
        confidenceHint: memory.confidenceHint,
        weakSkillCount: memory.weakSkillIds.length,
      },
      sessionRecommendation: {
        maxMinutes: livingResponse.maxSessionMinutes,
        pace: livingResponse.pace,
        challengeLevel: livingResponse.challengeLevel,
        message: livingResponse.message,
        tone: livingResponse.tone,
      },
    });
  } catch (e) {
    return errorResponse(e);
  }
}

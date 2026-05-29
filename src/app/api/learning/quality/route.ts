import { NextRequest, NextResponse } from "next/server";
import { evaluateLearningQuality } from "@/features/quality/quality-engine";
import { buildRemediationPath } from "@/features/quality/remediation-engine";
import { createExerciseBlueprints } from "@/features/quality/exercise-quality";
import { createLearnerMemoryPatch } from "@/features/quality/learner-memory";

export async function POST(req: NextRequest) {
  const body = await req.json().catch(() => ({}));
  const layer = body.layer ?? "middle_school";

  const decision = evaluateLearningQuality({
    layer,
    grade: body.grade,
    subject: body.subject,
    lessonId: body.lessonId,
    answerCorrect: body.answerCorrect,
    responseTimeSeconds: body.responseTimeSeconds,
    hintsUsed: body.hintsUsed,
    retryCount: body.retryCount,
    confidenceSelfRating: body.confidenceSelfRating,
    emotion: body.emotion,
  });

  return NextResponse.json({
    ok: true,
    layer,
    decision,
    remediationPath: buildRemediationPath({
      layer,
      subject: body.subject,
      misconception: body.misconception,
      failedCompetency: body.failedCompetency,
    }),
    exerciseBlueprints: createExerciseBlueprints(layer),
    learnerMemoryPatch: createLearnerMemoryPatch({
      correct: body.answerCorrect === true,
      repeatedMistake: (body.retryCount ?? 0) >= 2,
      layer,
    }),
  });
}
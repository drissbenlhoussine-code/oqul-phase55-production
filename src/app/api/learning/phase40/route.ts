import { NextRequest } from "next/server";
import { requireAuth } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";
import { assertOwnsChild } from "@/server/auth/ownership";
import { progressRepo } from "@/server/repositories/progress";
import { masteryService } from "@/server/services/mastery-service";
import { buildPhase40LearningSnapshot } from "@/server/learning-experience/phase40-engine";
import { AppError } from "@/server/errors";

export async function GET(request: NextRequest) {
  try {
    const session = await requireAuth();
    const childId = request.nextUrl.searchParams.get("childId");
    if (!childId) throw new AppError("childId required", "VALIDATION_ERROR", 422);

    const child = await assertOwnsChild(session.sub, childId);
    const [progress, weakPoints] = await Promise.all([
      progressRepo.getChildProgress(childId),
      masteryService.getWeakPoints(childId),
    ]);

    const snapshot = await buildPhase40LearningSnapshot({
      childId,
      childName: child.name,
      xp: child.xp,
      streak: child.streak,
      progress,
      weakPoints,
    });

    return ok(snapshot);
  } catch (e) {
    return errorResponse(e);
  }
}

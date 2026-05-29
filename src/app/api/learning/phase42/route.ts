import { NextRequest } from "next/server";
import { requireAuth } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";
import { assertOwnsChild } from "@/server/auth/ownership";
import { masteryService } from "@/server/services/mastery-service";
import { buildPhase42MiddleSchoolProfile } from "@/server/middle-school/phase42-engine";
import { AppError } from "@/server/errors";
import type { LearningLanguage, MiddleSchoolSubject } from "@/server/middle-school/types";

export async function GET(request: NextRequest) {
  try {
    const session = await requireAuth();
    const childId = request.nextUrl.searchParams.get("childId");
    if (!childId) throw new AppError("childId required", "VALIDATION_ERROR", 422);

    const [child, weakPoints] = await Promise.all([
      assertOwnsChild(session.sub, childId),
      masteryService.getWeakPoints(childId),
    ]);
    const subject = request.nextUrl.searchParams.get("subject") as MiddleSchoolSubject | null;
    const language = (request.nextUrl.searchParams.get("language") ?? "auto") as LearningLanguage;
    const message = request.nextUrl.searchParams.get("message");

    const profile = await buildPhase42MiddleSchoolProfile({
      childId,
      childName: child.name,
      gradeLevel: child.grade?.slug ?? child.grade?.titleAr,
      subject: subject ?? undefined,
      preferredLanguage: language,
      message,
      weakPoints,
    });

    return ok(profile);
  } catch (e) {
    return errorResponse(e);
  }
}

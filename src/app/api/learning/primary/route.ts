import { NextRequest } from "next/server";
import { requireAuth } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";
import { assertOwnsChild } from "@/server/auth/ownership";
import { AppError } from "@/server/errors";
import { masteryService } from "@/server/services/mastery-service";
import { buildPhase46PrimaryProfile } from "@/server/primary-school/phase46-engine";
import type { PrimaryLanguage, PrimarySubject } from "@/server/primary-school/types";

export async function GET(request: NextRequest) {
  try {
    const session = await requireAuth();
    const childId = request.nextUrl.searchParams.get("childId");
    if (!childId) throw new AppError("childId required", "VALIDATION_ERROR", 422);

    const [child, weakPoints] = await Promise.all([
      assertOwnsChild(session.sub, childId),
      masteryService.getWeakPoints(childId),
    ]);
    const subject = request.nextUrl.searchParams.get("subject") as PrimarySubject | null;
    const language = (request.nextUrl.searchParams.get("language") ?? "auto") as PrimaryLanguage;
    const message = request.nextUrl.searchParams.get("message");

    const profile = await buildPhase46PrimaryProfile({
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

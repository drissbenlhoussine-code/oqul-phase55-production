import { NextRequest } from "next/server";
import { assertOwnsChild } from "@/server/auth/ownership";
import { gamificationService } from "@/server/services/gamification-service";
import { AppError } from "@/server/errors";
import { requireAuth } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";

export async function GET(request: NextRequest) {
  try {
    const session = await requireAuth();
    const childId = request.nextUrl.searchParams.get("childId");
    if (!childId) throw new AppError("childId required", "VALIDATION_ERROR", 422);
    await assertOwnsChild(session.sub, childId);
    const result = await gamificationService.getChildBadges(childId);
    return ok(result);
  } catch (e) {
    return errorResponse(e);
  }
}

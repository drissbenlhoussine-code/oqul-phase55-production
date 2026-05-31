import { NextRequest } from "next/server";
import { assertOwnsChild } from "@/server/auth/ownership";
import { learningAnalyticsService } from "@/server/analytics/learning-analytics";
import { AppError } from "@/server/errors";
import { requireAuth } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";

export async function GET(request: NextRequest) {
  try {
    const session = await requireAuth();
    const childId = request.nextUrl.searchParams.get("childId");
    if (!childId) throw new AppError("childId مطلوب", "VALIDATION_ERROR", 422);
    await assertOwnsChild(session.sub, childId);
    const result = await learningAnalyticsService.getChildSummary(childId);
    return ok(result);
  } catch (e) {
    return errorResponse(e);
  }
}

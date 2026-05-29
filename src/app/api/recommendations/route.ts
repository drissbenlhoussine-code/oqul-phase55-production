import { withAuth } from "@/server/http/with-auth";
import { assertOwnsChild } from "@/server/auth/ownership";
import { recommendationService } from "@/server/services/recommendation-service";
import { AppError } from "@/server/errors";

export const GET = withAuth(async ({ session, request }) => {
  const childId = request.nextUrl.searchParams.get("childId");
  if (!childId) throw new AppError("childId مطلوب", "VALIDATION_ERROR", 422);
  await assertOwnsChild(session.sub, childId);
  return recommendationService.getRecommendations(childId);
});

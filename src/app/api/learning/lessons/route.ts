import { withPublic } from "@/server/http/with-auth";
import { learningService } from "@/server/services/learning-service";
import { AppError } from "@/server/errors";

export const GET = withPublic(async (request) => {
  const subjectId = request.nextUrl.searchParams.get("subjectId");
  if (!subjectId) throw new AppError("subjectId مطلوب", "VALIDATION_ERROR", 422);
  return learningService.listUnitsWithLessons({ subjectId });
});

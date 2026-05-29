import { withPublic } from "@/server/http/with-auth";
import { curriculumRepo } from "@/server/repositories/curriculum";
import { AppError } from "@/server/errors";

// GET /api/curriculum/lessons?unitId=xxx
export const GET = withPublic(async (request) => {
  const unitId = request.nextUrl.searchParams.get("unitId");
  if (!unitId) throw new AppError("unitId مطلوب", "VALIDATION_ERROR", 422);
  return curriculumRepo.getLessonsByUnit(unitId);
});

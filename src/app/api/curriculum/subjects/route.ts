import { withPublic } from "@/server/http/with-auth";
import { curriculumRepo } from "@/server/repositories/curriculum";
import { AppError } from "@/server/errors";

export const GET = withPublic(async (request) => {
  const gradeId = request.nextUrl.searchParams.get("gradeId");
  if (!gradeId) throw new AppError("gradeId مطلوب", "VALIDATION_ERROR", 422);
  return curriculumRepo.getSubjects(gradeId);
});

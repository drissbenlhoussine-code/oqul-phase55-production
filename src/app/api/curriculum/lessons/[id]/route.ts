import { withPublic } from "@/server/http/with-auth";
import { curriculumRepo } from "@/server/repositories/curriculum";
import { AppError } from "@/server/errors";

export const GET = withPublic(async (_request) => {
  const pathname = _request.nextUrl.pathname;
  const id = pathname.split("/").pop();
  if (!id) throw new AppError("id مطلوب", "VALIDATION_ERROR", 422);
  const lesson = await curriculumRepo.getLessonWithContent(id);
  if (!lesson) throw new AppError("الدرس غير موجود", "NOT_FOUND", 404);
  return lesson;
});

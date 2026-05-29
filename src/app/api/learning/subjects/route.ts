import { withPublic } from "@/server/http/with-auth";
import { learningService } from "@/server/services/learning-service";

export const GET = withPublic(async (request) => {
  const gradeId = request.nextUrl.searchParams.get("gradeId") ?? undefined;
  return learningService.listSubjects({ gradeId });
});

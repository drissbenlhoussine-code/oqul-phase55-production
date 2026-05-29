import { withPublic } from "@/server/http/with-auth";
import { curriculumRepo } from "@/server/repositories/curriculum";

// Grades are public — needed for registration flow
export const GET = withPublic(async (request) => {
  const cycle = request.nextUrl.searchParams.get("cycle") ?? undefined;
  return curriculumRepo.getGrades(cycle);
});

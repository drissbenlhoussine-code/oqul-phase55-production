import { requireAdmin } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";
import { getPrimaryMathCurriculumProgress } from "@/server/curriculum/curriculum-progress";

export const dynamic = "force-dynamic";

export async function GET() {
  try {
    await requireAdmin();
    const report = await getPrimaryMathCurriculumProgress();
    return ok(report);
  } catch (error) {
    return errorResponse(error);
  }
}

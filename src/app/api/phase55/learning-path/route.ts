import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { getSession } from "@/server/auth/session";
import { verifyCsrf } from "@/server/security/csrf";
import { buildPersonalizedLearningPath } from "@/features/phase55-adaptive-platform/learning-path-engine";

const bodySchema = z.object({
  subject:          z.string().optional(),
  grade:            z.string().optional(),
  weakPoints:       z.array(z.string()).optional(),
  averageScore:     z.number().optional(),
  confidence:       z.number().optional(),
  completedLessons: z.number().optional(),
});

export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) {
    return NextResponse.json({ ok: false, error: "unauthorized", message: "يجب تسجيل الدخول" }, { status: 401 });
  }

  if (!(await verifyCsrf(req))) {
    return NextResponse.json({ ok: false, error: "csrf_failed", message: "CSRF token غير صالح" }, { status: 403 });
  }

  const parsed = bodySchema.safeParse(await req.json().catch(() => ({})));
  if (!parsed.success) {
    return NextResponse.json({ ok: false, error: "invalid_input", message: parsed.error.errors[0]?.message ?? "طلب غير صالح" }, { status: 422 });
  }

  return NextResponse.json({ ok: true, path: buildPersonalizedLearningPath({ ...parsed.data, childId: session.sub }) });
}

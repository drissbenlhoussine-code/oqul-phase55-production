import { NextRequest, NextResponse } from "next/server";
import { getSession } from "@/server/auth/session";
import { verifyCsrf } from "@/server/security/csrf";
import { buildPersonalizedLearningPath } from "@/features/phase55-adaptive-platform/learning-path-engine";

export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) {
    return NextResponse.json({ ok: false, error: "unauthorized", message: "يجب تسجيل الدخول" }, { status: 401 });
  }

  if (!(await verifyCsrf(req))) {
    return NextResponse.json({ ok: false, error: "csrf_failed", message: "CSRF token غير صالح" }, { status: 403 });
  }

  const body = await req.json().catch(() => ({}));
  return NextResponse.json({ ok:true, path: buildPersonalizedLearningPath({ ...body, userId: session.sub }) });
}

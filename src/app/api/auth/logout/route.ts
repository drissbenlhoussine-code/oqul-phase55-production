import { NextRequest, NextResponse } from "next/server";
import { AUTH_COOKIE } from "@/server/auth/cookies";
import { refreshTokenService } from "@/server/auth/refresh-token";
import { verifyCsrf } from "@/server/security/csrf";

export async function POST(request: NextRequest) {
  if (!(await verifyCsrf(request))) {
    return NextResponse.json({ success: false, error: "csrf_failed" }, { status: 403 });
  }

  const refreshTok = request.cookies.get(refreshTokenService.COOKIE_NAME)?.value;

  // Revoke the refresh token in DB (prevents future rotation)
  if (refreshTok) {
    await refreshTokenService.revoke(refreshTok).catch(console.error);
  }

  const response = NextResponse.json({ success: true });
  response.cookies.delete(AUTH_COOKIE);
  response.cookies.delete(refreshTokenService.COOKIE_NAME);
  return response;
}

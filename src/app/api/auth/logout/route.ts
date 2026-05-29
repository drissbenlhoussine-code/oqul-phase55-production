import { NextRequest, NextResponse } from "next/server";
import { AUTH_COOKIE } from "@/server/auth/cookies";
import { refreshTokenService } from "@/server/auth/refresh-token";

export async function POST(request: NextRequest) {
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

import { NextRequest } from "next/server";
import { requireAuth } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";
import { refreshTokenService } from "@/server/auth/refresh-token";

/** List active sessions (devices) for current user */
export async function GET() {
  try {
    const session = await requireAuth();
    const sessions = await refreshTokenService.getActiveSessions(session.sub);
    return ok(sessions);
  } catch (e) {
    return errorResponse(e);
  }
}

/** Revoke all sessions except current - "logout all other devices" */
export async function DELETE(request: NextRequest) {
  try {
    const session = await requireAuth();
    const currentRefresh = request.cookies?.get(refreshTokenService.COOKIE_NAME)?.value;
    await refreshTokenService.revokeAll(session.sub);
    return ok({ revoked: true, message: "تم تسجيل الخروج من جميع الأجهزة" });
  } catch (e) {
    return errorResponse(e);
  }
}

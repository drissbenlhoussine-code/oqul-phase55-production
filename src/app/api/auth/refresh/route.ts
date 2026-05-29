import { NextRequest, NextResponse } from "next/server";
import { signToken } from "@/server/auth/jwt";
import { AUTH_COOKIE, cookieOptions } from "@/server/auth/cookies";
import { refreshTokenService } from "@/server/auth/refresh-token";
import { usersRepo } from "@/server/repositories/users";
import { refreshLimiter } from "@/server/security/rate-limit";

export async function POST(request: NextRequest) {
  try {
    const ip         = request.headers.get("x-forwarded-for") ?? "unknown";
    const userAgent  = request.headers.get("user-agent") ?? undefined;
    const refreshTok = request.cookies.get(refreshTokenService.COOKIE_NAME)?.value;

    const limit = await refreshLimiter(ip);
    if (!limit.allowed) {
      return NextResponse.json(
        { success: false, message: "طلبات كثيرة — انتظر دقيقة", code: "RATE_LIMITED" },
        { status: 429 }
      );
    }

    if (!refreshTok) {
      return NextResponse.json(
        { success: false, message: "انتهت الجلسة — يرجى تسجيل الدخول مجدداً", code: "UNAUTHORIZED" },
        { status: 401 }
      );
    }

    // Rotate refresh token (detects theft if revoked token is reused)
    const result = await refreshTokenService.rotate(refreshTok, { userAgent, ipAddress: ip });

    if (!result) {
      // Invalid / expired / stolen — clear both cookies
      const response = NextResponse.json(
        { success: false, message: "انتهت الجلسة — يرجى تسجيل الدخول مجدداً", code: "UNAUTHORIZED" },
        { status: 401 }
      );
      response.cookies.delete(AUTH_COOKIE);
      response.cookies.delete(refreshTokenService.COOKIE_NAME);
      return response;
    }

    // Fetch fresh user data (plan/role may have changed)
    const user = await usersRepo.findById(result.userId);
    if (!user) {
      return NextResponse.json(
        { success: false, message: "المستخدم غير موجود", code: "NOT_FOUND" },
        { status: 404 }
      );
    }

    // Issue new access token
    const newAccessToken = await signToken({
      sub:   user.id,
      email: user.email,
      role:  user.role,
      plan:  user.plan,
    });

    const isSecure = process.env.NODE_ENV === "production";
    const response = NextResponse.json({
      success: true,
      data:    { refreshed: true, user: { id: user.id, plan: user.plan } },
    });

    // Rotate: set new access token + new refresh token
    response.cookies.set(AUTH_COOKIE, newAccessToken, cookieOptions(isSecure));
    response.cookies.set(
      refreshTokenService.COOKIE_NAME,
      result.newToken,
      refreshTokenService.cookieOptions(isSecure)
    );

    return response;
  } catch (e) {
    console.error("[Refresh Route]", e);
    return NextResponse.json(
      { success: false, message: "حدث خطأ داخلي", code: "INTERNAL_ERROR" },
      { status: 500 }
    );
  }
}

import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { usersRepo } from "@/server/repositories/users";
import { signToken } from "@/server/auth/jwt";
import { AUTH_COOKIE, cookieOptions } from "@/server/auth/cookies";
import { refreshTokenService } from "@/server/auth/refresh-token";
import { errorResponse, ok } from "@/server/http/response";
import { Errors } from "@/server/errors";
import { loginLimiter } from "@/server/security/rate-limit";
import { audit } from "@/server/security/audit";

const loginSchema = z.object({
  email:    z.string().email("بريد إلكتروني غير صالح"),
  password: z.string().min(1, "كلمة المرور مطلوبة"),
});

export async function POST(request: NextRequest) {
  try {
    const ip        = request.headers.get("x-forwarded-for") ?? "unknown";
    const userAgent = request.headers.get("user-agent") ?? undefined;

    // Rate limit
    const limit = await loginLimiter(ip);
    if (!limit.allowed) {
      return NextResponse.json(
        { success: false, message: "محاولات كثيرة جداً. انتظر 15 دقيقة.", code: "RATE_LIMITED" },
        { status: 429 }
      );
    }

    const body = loginSchema.parse(await request.json());
    const user = await usersRepo.findByEmail(body.email);

    if (!user || !(await usersRepo.verifyPassword(body.password, user.passwordHash))) {
      await audit({ event: "login_failure", meta: { email: body.email, ip } });
      throw Errors.validation("البريد الإلكتروني أو كلمة المرور غير صحيحة");
    }

    // Issue access token (short-lived: 15 min in production, 7d in dev for UX)
    const accessToken = await signToken({
      sub:   user.id,
      email: user.email,
      role:  user.role,
      plan:  user.plan,
    });

    // Issue refresh token (long-lived: 30 days, rotated on use)
    const refreshToken = await refreshTokenService.createSession({
      userId:    user.id,
      userAgent,
      ipAddress: ip,
    });

    await audit({ event: "login_success", userId: user.id, ip });

    const isSecure = process.env.NODE_ENV === "production";
    const response = ok({
      user: { id: user.id, fullName: user.fullName, email: user.email, plan: user.plan },
    });

    // Access token cookie
    response.cookies.set(AUTH_COOKIE, accessToken, cookieOptions(isSecure));

    // Refresh token cookie — narrower path scope
    response.cookies.set(
      refreshTokenService.COOKIE_NAME,
      refreshToken,
      refreshTokenService.cookieOptions(isSecure)
    );

    return response;
  } catch (e) {
    return errorResponse(e);
  }
}

/**
 * POST /api/auth/register
 * Phase 31: Added email verification send + termsAccepted validation.
 * All other logic unchanged.
 */
import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { usersRepo } from "@/server/repositories/users";
import { usersEmailRepo } from "@/server/repositories/users-email-repo";
import { signToken } from "@/server/auth/jwt";
import { AUTH_COOKIE, cookieOptions } from "@/server/auth/cookies";
import { refreshTokenService } from "@/server/auth/refresh-token";
import { errorResponse } from "@/server/http/response";
import { Errors } from "@/server/errors";
import { registerLimiter } from "@/server/security/rate-limit";
import { audit } from "@/server/security/audit";
import { emailService } from "@/server/email/email-service";
import { generateSecureToken } from "@/server/auth/tokens";

const registerSchema = z.object({
  fullName:      z.string().min(2, "الاسم يجب أن يكون حرفين على الأقل").max(160),
  email:         z.string().email("بريد إلكتروني غير صالح"),
  password:      z.string().min(8, "كلمة المرور يجب أن تكون 8 أحرف على الأقل"),
  termsAccepted: z.literal(true, { errorMap: () => ({ message: "يجب الموافقة على الشروط وسياسة الخصوصية" }) }),
});

export async function POST(request: NextRequest) {
  try {
    const ip        = request.headers.get("x-forwarded-for") ?? "unknown";
    const userAgent = request.headers.get("user-agent") ?? undefined;

    const limit = await registerLimiter(ip);
    if (!limit.allowed) {
      return NextResponse.json(
        { success: false, message: "محاولات كثيرة. انتظر ساعة.", code: "RATE_LIMITED" },
        { status: 429 }
      );
    }

    const body = registerSchema.parse(await request.json());

    const existing = await usersRepo.findByEmail(body.email);
    if (existing) throw Errors.validation("البريد الإلكتروني مسجل مسبقًا");

    const user = await usersRepo.create(body);

    // Accept terms
    await usersEmailRepo.acceptTerms(user.id);

    // Send verification email (non-blocking)
    const verificationToken = generateSecureToken();
    await usersEmailRepo.setVerificationToken(user.id, verificationToken, new Date());
    emailService.sendVerification({
      to:    user.email,
      name:  user.fullName,
      token: verificationToken,
    }).catch((err) => console.error("[register] verification email failed:", err));

    await audit({ event: "register", userId: user.id, ip });

    const token = await signToken({ sub: user.id, email: user.email, role: user.role, plan: user.plan });
    const refreshToken = await refreshTokenService.createSession({
      userId: user.id,
      userAgent,
      ipAddress: ip,
    });
    const isSecure = process.env.NODE_ENV === "production";
    const response = NextResponse.json(
      { success: true, data: { user: { id: user.id, fullName: user.fullName, email: user.email, plan: user.plan } } },
      { status: 201 }
    );
    response.cookies.set(AUTH_COOKIE, token, cookieOptions(isSecure));
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

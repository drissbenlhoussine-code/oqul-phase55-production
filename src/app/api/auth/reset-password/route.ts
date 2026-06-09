/**
 * POST /api/auth/reset-password
 * Validates reset token and updates the user's password.
 */
import { type NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { usersEmailRepo } from "@/server/repositories/users-email-repo";
import { hashPassword } from "@/server/auth/password";
import { hashToken, isExpired } from "@/server/auth/tokens";
import { errorResponse } from "@/server/http/response";
import { Errors } from "@/server/errors";
import { audit } from "@/server/security/audit";
import { resetPasswordLimiter } from "@/server/security/rate-limit";

const schema = z.object({
  token:    z.string().length(64, "رابط غير صالح"),
  password: z.string().min(8, "كلمة المرور 8 أحرف على الأقل").max(128),
});

export async function POST(request: NextRequest) {
  try {
    const ip = request.headers.get("x-forwarded-for") ?? "unknown";
    const limit = await resetPasswordLimiter(ip);
    if (!limit.allowed) {
      return NextResponse.json(
        { success: false, code: "RATE_LIMITED", message: "Too many attempts. Try again later." },
        { status: 429 }
      );
    }

    const { token, password } = schema.parse(await request.json());

    // DB stores the SHA-256 hash; look up by hash of the incoming plain token
    const user = await usersEmailRepo.findByResetToken(hashToken(token));

    if (!user) {
      throw Errors.validation("الرابط غير صالح أو منتهي الصلاحية.");
    }

    if (isExpired(user.passwordResetExpiresAt)) {
      throw Errors.validation("انتهت صلاحية الرابط. اطلب رابطاً جديداً.");
    }

    const passwordHash = await hashPassword(password);
    await usersEmailRepo.updatePassword(user.id, passwordHash);

    await audit({
      event:  "password_change",
      userId: user.id,
      meta:   { via: "reset_token" },
    });

    return NextResponse.json({
      success: true,
      message: "تم تغيير كلمة المرور بنجاح. يمكنك تسجيل الدخول الآن.",
    });
  } catch (e) {
    return errorResponse(e);
  }
}

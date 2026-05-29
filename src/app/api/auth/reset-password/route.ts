/**
 * POST /api/auth/reset-password
 * Validates reset token and updates the user's password.
 */
import { type NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { usersEmailRepo } from "@/server/repositories/users-email-repo";
import { hashPassword } from "@/server/auth/password";
import { isExpired } from "@/server/auth/tokens";
import { errorResponse } from "@/server/http/response";
import { Errors } from "@/server/errors";
import { audit } from "@/server/security/audit";

const schema = z.object({
  token:    z.string().length(64, "رابط غير صالح"),
  password: z.string().min(8, "كلمة المرور 8 أحرف على الأقل").max(128),
});

export async function POST(request: NextRequest) {
  try {
    const { token, password } = schema.parse(await request.json());

    const user = await usersEmailRepo.findByResetToken(token);

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

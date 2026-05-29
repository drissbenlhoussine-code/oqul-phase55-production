/**
 * POST /api/auth/forgot-password
 * Sends a password-reset email if the address is registered.
 *
 * Always returns 200 (security: never reveal if email exists).
 */
import { type NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { usersRepo } from "@/server/repositories/users";
import { usersEmailRepo } from "@/server/repositories/users-email-repo";
import { emailService } from "@/server/email/email-service";
import { generateSecureToken, passwordResetExpiry } from "@/server/auth/tokens";
import { errorResponse } from "@/server/http/response";

const schema = z.object({
  email: z.string().email("بريد إلكتروني غير صالح"),
});

const OK_RESPONSE = NextResponse.json({
  success: true,
  message: "إذا كان البريد مسجلاً، ستصل رسالة خلال دقائق.",
});

export async function POST(request: NextRequest) {
  try {
    const { email } = schema.parse(await request.json());

    const user = await usersRepo.findByEmail(email);

    // Always return OK — do not reveal whether email exists
    if (!user) return OK_RESPONSE;

    const token     = generateSecureToken();
    const expiresAt = passwordResetExpiry();

    await usersEmailRepo.setResetToken(user.id, token, expiresAt);

    // Fire-and-forget — don't block the response on email delivery
    emailService.sendPasswordReset({
      to:    user.email,
      name:  user.fullName,
      token,
    }).catch((err) => console.error("[forgot-password] email failed:", err));

    return OK_RESPONSE;
  } catch (e) {
    return errorResponse(e);
  }
}

/**
 * POST /api/auth/forgot-password
 * Sends a password-reset email if the address is registered.
 *
 * Always returns 200 for known/unknown emails (security: never reveal if email exists).
 * Logs use a SHA-256 email hash for correlation — never raw email or tokens.
 */
import { createHash }                                           from "crypto";
import { type NextRequest, NextResponse }                       from "next/server";
import { z, ZodError }                                         from "zod";
import { usersRepo }                                           from "@/server/repositories/users";
import { usersEmailRepo }                                      from "@/server/repositories/users-email-repo";
import { EmailDeliveryError, emailService, getEmailConfigDiagnostics } from "@/server/email/email-service";
import { generateSecureToken, hashToken, passwordResetExpiry } from "@/server/auth/tokens";
import { forgotPasswordIpLimiter, forgotPasswordEmailLimiter } from "@/server/security/rate-limit";

export const dynamic   = "force-dynamic";
export const revalidate = 0;

const JSON_HEADERS = {
  "Cache-Control": "no-store",
  "Content-Type":  "application/json; charset=utf-8",
} as const;

const schema = z.object({
  email: z.string().trim().toLowerCase().email("بريد إلكتروني غير صالح"),
});

/** 16-char hex prefix of SHA-256(email) — safe for log correlation without revealing PII. */
function safeEmailHash(email: string): string {
  return createHash("sha256").update(email.trim().toLowerCase()).digest("hex").slice(0, 16);
}

function jsonResponse(body: Record<string, unknown>, status = 200) {
  return NextResponse.json(body, { status, headers: JSON_HEADERS });
}

function acceptedResponse() {
  return jsonResponse({
    success: true,
    code:    "RESET_EMAIL_REQUEST_ACCEPTED",
    message: "If this email exists, we sent reset instructions.",
  });
}

function forgotPasswordErrorResponse(error: unknown) {
  if (error instanceof ZodError) {
    return jsonResponse(
      {
        success: false,
        code:    "VALIDATION_ERROR",
        message: error.errors.map((e) => e.message).join(". "),
      },
      422
    );
  }

  if (error instanceof Error) {
    console.error("[forgot-password] request failed", {
      code:    "FORGOT_PASSWORD_ERROR",
      message: error.message,
    });
  }

  return jsonResponse(
    {
      success: false,
      code:    "FORGOT_PASSWORD_ERROR",
      message: "Unable to process password reset right now. Please try again later.",
    },
    500
  );
}

function logEmailFailure(error: unknown, emailHash: string) {
  if (error instanceof EmailDeliveryError) {
    console.error("[forgot-password] email failed", {
      code:               error.code,
      status:             error.status,
      details:            error.details,
      emailHash,
      emailSendAttempted: true,
    });
    return;
  }

  console.error("[forgot-password] email failed", {
    code:               "EMAIL_UNKNOWN_ERROR",
    message:            error instanceof Error ? error.message : "Unknown email error",
    emailHash,
    emailSendAttempted: true,
  });
}

export async function POST(request: NextRequest) {
  try {
    // Rate limit by IP (3/hr) — return accepted response to avoid oracle attacks
    const ip = request.headers.get("x-forwarded-for") ?? "unknown";
    const ipLimit = await forgotPasswordIpLimiter(ip);
    if (!ipLimit.allowed) return acceptedResponse();

    console.info("[forgot-password] email config", getEmailConfigDiagnostics());

    const { email } = schema.parse(await request.json());
    const emailHash = safeEmailHash(email);

    // Rate limit by email hash (2/hr) — still return accepted to avoid oracle attacks
    const emailLimit = await forgotPasswordEmailLimiter(emailHash);
    if (!emailLimit.allowed) return acceptedResponse();

    console.info("[forgot-password] submitted", { emailHash });

    const user = await usersRepo.findByEmail(email);
    console.info("[forgot-password] user lookup", { emailHash, userFound: Boolean(user) });

    if (!user) {
      console.info("[forgot-password] flow result", {
        emailHash,
        userFound:          false,
        resetTokenCreated:  false,
        resetTokenStored:   false,
        emailSendAttempted: false,
      });
      return acceptedResponse();
    }

    const token     = generateSecureToken();
    const expiresAt = passwordResetExpiry();
    const tokenHash = hashToken(token);
    console.info("[forgot-password] reset token created", {
      emailHash,
      userFound:         true,
      resetTokenCreated: true,
    });

    // Store only the hash — a DB leak cannot be used to reset accounts
    await usersEmailRepo.setResetToken(user.id, tokenHash, expiresAt);
    console.info("[forgot-password] reset token stored", {
      emailHash,
      userFound:         true,
      resetTokenCreated: true,
      resetTokenStored:  true,
    });

    try {
      console.info("[forgot-password] email send attempting", {
        emailHash,
        emailSendAttempted: true,
      });
      const emailResult = await emailService.sendPasswordReset({
        to:    user.email,
        name:  user.fullName,
        token,
      });
      console.info("[forgot-password] email send accepted", {
        code:               "RESET_EMAIL_SEND_ACCEPTED",
        emailHash,
        emailSendAttempted: true,
        resendId:           emailResult.id,
      });
    } catch (error) {
      logEmailFailure(error, emailHash);
    }

    return acceptedResponse();
  } catch (error) {
    return forgotPasswordErrorResponse(error);
  }
}

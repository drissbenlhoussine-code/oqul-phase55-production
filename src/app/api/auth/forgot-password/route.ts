/**
 * POST /api/auth/forgot-password
 * Sends a password-reset email if the address is registered.
 *
 * Always returns 200 for known/unknown emails (security: never reveal if email exists).
 */
import { type NextRequest, NextResponse } from "next/server";
import { z, ZodError } from "zod";
import { usersRepo } from "@/server/repositories/users";
import { usersEmailRepo } from "@/server/repositories/users-email-repo";
import { EmailDeliveryError, emailService, getEmailConfigDiagnostics } from "@/server/email/email-service";
import { generateSecureToken, hashToken, passwordResetExpiry } from "@/server/auth/tokens";

export const dynamic = "force-dynamic";
export const revalidate = 0;

const JSON_HEADERS = {
  "Cache-Control": "no-store",
  "Content-Type": "application/json; charset=utf-8",
} as const;

const schema = z.object({
  email: z.string().trim().toLowerCase().email("بريد إلكتروني غير صالح"),
});

function jsonResponse(body: Record<string, unknown>, status = 200) {
  return NextResponse.json(body, {
    status,
    headers: JSON_HEADERS,
  });
}

function acceptedResponse() {
  return jsonResponse({
    success: true,
    code: "RESET_EMAIL_REQUEST_ACCEPTED",
    message: "If this email exists, we sent reset instructions.",
  });
}

function forgotPasswordErrorResponse(error: unknown) {
  if (error instanceof ZodError) {
    return jsonResponse(
      {
        success: false,
        code: "VALIDATION_ERROR",
        message: error.errors.map((entry) => entry.message).join(". "),
      },
      422
    );
  }

  if (error instanceof Error) {
    console.error("[forgot-password] request failed", {
      code: "FORGOT_PASSWORD_ERROR",
      message: error.message,
    });
  }

  return jsonResponse(
    {
      success: false,
      code: "FORGOT_PASSWORD_ERROR",
      message: "Unable to process password reset right now. Please try again later.",
    },
    500
  );
}

function logEmailFailure(error: unknown, email: string) {
  if (error instanceof EmailDeliveryError) {
    console.error("[forgot-password] email failed", {
      code: error.code,
      status: error.status,
      details: error.details,
      email,
      emailSendAttempted: true,
    });
    return;
  }

  console.error("[forgot-password] email failed", {
    code: "EMAIL_UNKNOWN_ERROR",
    message: error instanceof Error ? error.message : "Unknown email error",
    email,
    emailSendAttempted: true,
  });
}

export async function POST(request: NextRequest) {
  try {
    console.info("[forgot-password] email config", getEmailConfigDiagnostics());

    const { email } = schema.parse(await request.json());
    console.info("[forgot-password] submitted", {
      email,
    });

    const user = await usersRepo.findByEmail(email);
    console.info("[forgot-password] user lookup", {
      email,
      userFound: Boolean(user),
    });

    if (!user) {
      console.info("[forgot-password] flow result", {
        email,
        userFound: false,
        resetTokenCreated: false,
        resetTokenStored: false,
        emailSendAttempted: false,
      });
      return acceptedResponse();
    }

    const token = generateSecureToken();
    const expiresAt = passwordResetExpiry();
    const tokenHash = hashToken(token);
    console.info("[forgot-password] reset token created", {
      email,
      userFound: true,
      resetTokenCreated: Boolean(token),
    });

    // Store only the hash so a database leak cannot be used to reset accounts.
    await usersEmailRepo.setResetToken(user.id, tokenHash, expiresAt);
    console.info("[forgot-password] reset token stored", {
      email,
      userFound: true,
      resetTokenCreated: true,
      resetTokenStored: true,
    });

    try {
      console.info("[forgot-password] email send attempting", {
        email,
        emailSendAttempted: true,
      });
      const emailResult = await emailService.sendPasswordReset({
        to: user.email,
        name: user.fullName,
        token,
      });
      console.info("[forgot-password] email send accepted", {
        code: "RESET_EMAIL_SEND_ACCEPTED",
        email,
        emailSendAttempted: true,
        resendId: emailResult.id,
      });
    } catch (error) {
      logEmailFailure(error, email);
    }

    return acceptedResponse();
  } catch (error) {
    return forgotPasswordErrorResponse(error);
  }
}

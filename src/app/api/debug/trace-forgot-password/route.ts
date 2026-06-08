/**
 * POST /api/debug/trace-forgot-password
 *
 * Protected by DEBUG_SECRET — replays the exact forgot-password flow and returns
 * step-by-step diagnostic JSON. MAY write a reset token to the DB if the user
 * exists (same as the real route). Never returns the plain token.
 *
 * Body: { email: string }
 */
import { type NextRequest, NextResponse }                       from "next/server";
import { createHash }                                           from "crypto";
import { z, ZodError }                                         from "zod";
import { usersRepo }                                           from "@/server/repositories/users";
import { usersEmailRepo }                                      from "@/server/repositories/users-email-repo";
import { EmailDeliveryError, emailService, getEmailConfigDiagnostics } from "@/server/email/email-service";
import { generateSecureToken, hashToken, passwordResetExpiry } from "@/server/auth/tokens";

export const dynamic   = "force-dynamic";
export const revalidate = 0;

const bodySchema = z.object({
  email: z.string().trim().toLowerCase().email("Invalid email"),
});

function authorized(request: NextRequest): boolean {
  const secret = process.env.DEBUG_SECRET?.trim();
  if (!secret) return false;

  const bearer = request.headers.get("authorization");
  const query  = request.nextUrl.searchParams.get("secret");

  const expected   = createHash("sha256").update(secret).digest("hex");
  const fromBearer = bearer?.startsWith("Bearer ")
    ? createHash("sha256").update(bearer.slice(7).trim()).digest("hex")
    : null;
  const fromQuery  = query
    ? createHash("sha256").update(query).digest("hex")
    : null;

  return fromBearer === expected || fromQuery === expected;
}

function json(body: unknown, status = 200) {
  return NextResponse.json(body, {
    status,
    headers: { "Cache-Control": "no-store", "Content-Type": "application/json; charset=utf-8" },
  });
}

function redactId(id: string): string {
  return createHash("sha256").update(id).digest("hex").slice(0, 12) + "...";
}

export async function POST(request: NextRequest) {
  if (!process.env.DEBUG_SECRET?.trim()) return json({ ok: false, error: "Not Found" }, 404);
  if (!authorized(request)) return json({ ok: false, error: "Unauthorized" }, 401);

  let email: string;
  try {
    const parsed = bodySchema.parse(await request.json());
    email = parsed.email;
  } catch (err) {
    if (err instanceof ZodError) {
      return json({ ok: false, error: "Validation error", details: err.errors }, 422);
    }
    return json({ ok: false, error: "Invalid JSON body" }, 400);
  }

  const emailHash = createHash("sha256").update(email).digest("hex").slice(0, 16);

  const steps: Record<string, unknown> = {
    emailHash,
    emailConfig: getEmailConfigDiagnostics(),
  };

  // Step 1 — DB user lookup
  let user: Awaited<ReturnType<typeof usersRepo.findByEmail>>;
  try {
    user = await usersRepo.findByEmail(email);
    steps.userFound   = Boolean(user);
    steps.userIdHash  = user ? redactId(user.id) : null;
    steps.dbLookup    = "ok";
  } catch (err) {
    steps.userFound = null;
    steps.dbLookup  = "failed";
    steps.dbError   = err instanceof Error ? err.message : String(err);
    return json({ ok: false, steps }, 500);
  }

  if (!user) {
    steps.resetTokenCreated  = false;
    steps.resetTokenStored   = false;
    steps.emailSendAttempted = false;
    return json({ ok: true, steps });
  }

  // Step 2 — Generate & store reset token
  let token: string;
  try {
    token = generateSecureToken();
    const expiresAt  = passwordResetExpiry();
    const tokenHash  = hashToken(token);
    steps.resetTokenCreated = true;

    await usersEmailRepo.setResetToken(user.id, tokenHash, expiresAt);
    steps.resetTokenStored   = true;
    steps.resetTokenExpiresAt = expiresAt.toISOString();
  } catch (err) {
    steps.resetTokenCreated  = steps.resetTokenCreated ?? false;
    steps.resetTokenStored   = false;
    steps.tokenError         = err instanceof Error ? err.message : String(err);
    return json({ ok: false, steps }, 500);
  }

  // Step 3 — Send email (same service as production)
  steps.emailSendAttempted = true;
  try {
    const emailResult = await emailService.sendPasswordReset({
      to:    user.email,
      name:  user.fullName,
      token,
    });
    steps.emailSendAccepted = true;
    steps.resendId          = emailResult.id;
    steps.emailError        = null;
  } catch (err) {
    steps.emailSendAccepted = false;
    if (err instanceof EmailDeliveryError) {
      steps.emailErrorCode    = err.code;
      steps.emailErrorStatus  = err.status;
      steps.emailErrorDetails = err.details;
    } else {
      steps.emailErrorCode    = "EMAIL_UNKNOWN_ERROR";
      steps.emailErrorDetails = err instanceof Error ? err.message : String(err);
    }
  }

  return json({ ok: true, steps });
}

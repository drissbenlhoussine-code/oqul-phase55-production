/**
 * POST /api/debug/send-test-email
 *
 * Protected by DEBUG_SECRET — sends a test email via the same emailService
 * used by forgot-password. Returns resendId or error code.
 *
 * Body: { to: string }   (the recipient address)
 * Never writes to the DB. Never generates a real reset token.
 */
import { type NextRequest, NextResponse } from "next/server";
import { createHash }                     from "crypto";
import { z, ZodError }                    from "zod";
import { emailService, EmailDeliveryError } from "@/server/email/email-service";

export const dynamic   = "force-dynamic";
export const revalidate = 0;

const bodySchema = z.object({
  to: z.string().trim().email("Invalid recipient email"),
});

function authorized(request: NextRequest): boolean {
  const secret = process.env.DEBUG_SECRET?.trim();
  if (!secret) return false;

  const bearer = request.headers.get("authorization");
  const query  = request.nextUrl.searchParams.get("secret");

  const expected    = createHash("sha256").update(secret).digest("hex");
  const fromBearer  = bearer?.startsWith("Bearer ")
    ? createHash("sha256").update(bearer.slice(7).trim()).digest("hex")
    : null;
  const fromQuery   = query
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

export async function POST(request: NextRequest) {
  if (!authorized(request)) {
    return json({ ok: false, error: "Unauthorized" }, 401);
  }

  let to: string;
  try {
    const parsed = bodySchema.parse(await request.json());
    to = parsed.to;
  } catch (err) {
    if (err instanceof ZodError) {
      return json({ ok: false, error: "Validation error", details: err.errors }, 422);
    }
    return json({ ok: false, error: "Invalid JSON body" }, 400);
  }

  // Redact email from logs: only log first 16 chars of SHA-256 hash
  const emailHash = createHash("sha256").update(to.toLowerCase()).digest("hex").slice(0, 16);

  console.info("[debug:send-test-email] attempting", {
    emailHash,
    emailFrom: process.env.EMAIL_FROM ?? "(default: Oqul <no-reply@oqul.tech>)",
    appUrl:    process.env.NEXT_PUBLIC_APP_URL ?? "(missing)",
  });

  try {
    const result = await emailService.sendPasswordReset({
      to,
      name:  "Debug Test User",
      token: "0000000000000000000000000000000000000000000000000000000000000000",
    });

    console.info("[debug:send-test-email] accepted", { emailHash, resendId: result.id });

    return json({
      ok:        true,
      emailHash,
      resendId:  result.id,
      message:   "Test email accepted by Resend. Check the inbox (or Resend dashboard) for delivery status.",
      note:      "The reset link in this test email contains a dummy token and will not work.",
    });
  } catch (err) {
    const code    = err instanceof EmailDeliveryError ? err.code    : "EMAIL_UNKNOWN_ERROR";
    const status  = err instanceof EmailDeliveryError ? err.status  : undefined;
    const details = err instanceof EmailDeliveryError ? err.details : undefined;
    const message = err instanceof Error ? err.message : String(err);

    console.error("[debug:send-test-email] failed", { emailHash, code, status, details });

    return json({
      ok:      false,
      emailHash,
      code,
      message,
      ...(status  && { status }),
      ...(details && { details }),
    }, 500);
  }
}

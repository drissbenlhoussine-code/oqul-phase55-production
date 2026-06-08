/**
 * GET /api/debug/forgot-password-health
 *
 * Protected by DEBUG_SECRET — returns JSON config snapshot for production triage.
 * Never exposes API keys, tokens, or password hashes.
 * Remove or gate behind an env flag when debug is no longer needed.
 */
import { type NextRequest, NextResponse } from "next/server";
import { createHash }                     from "crypto";
import { getEmailConfigDiagnostics }      from "@/server/email/email-service";

export const dynamic   = "force-dynamic";
export const revalidate = 0;

function authorized(request: NextRequest): boolean {
  const secret = process.env.DEBUG_SECRET?.trim();
  if (!secret) return false;

  const bearer = request.headers.get("authorization");
  const query  = request.nextUrl.searchParams.get("secret");

  // Constant-time comparison via hash to avoid timing attacks
  const expected = createHash("sha256").update(secret).digest("hex");
  const fromBearer = bearer?.startsWith("Bearer ")
    ? createHash("sha256").update(bearer.slice(7).trim()).digest("hex")
    : null;
  const fromQuery = query
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

export async function GET(request: NextRequest) {
  if (!process.env.DEBUG_SECRET?.trim()) return json({ error: "Not Found" }, 404);
  if (!authorized(request)) return json({ error: "Unauthorized" }, 401);

  const emailDiag = getEmailConfigDiagnostics();

  // DB connectivity check — read-only ping
  let dbStatus: "connected" | "failed" | "not_configured" = "not_configured";
  let dbHost = "(not configured)";
  let dbError: string | undefined;

  const dbUrl = process.env.DATABASE_URL?.trim();
  if (dbUrl) {
    try {
      const atPart = dbUrl.split("@")[1];
      dbHost = atPart ? atPart.split("/")[0] : "(hidden)";
    } catch {
      dbHost = "(parse error)";
    }

    try {
      const { db }  = await import("@/db");
      const { sql } = await import("drizzle-orm");
      await db.execute(sql`SELECT 1 AS ping`);
      dbStatus = "connected";
    } catch (err) {
      dbStatus = "failed";
      dbError = err instanceof Error ? err.message : String(err);
    }
  }

  const canonicalHost = request.headers.get("host") ?? "(unknown)";
  const xForwardedHost = request.headers.get("x-forwarded-host") ?? "(none)";
  const xForwardedProto = request.headers.get("x-forwarded-proto") ?? "(none)";

  return json({
    ok: true,
    timestamp: new Date().toISOString(),
    runtime: {
      NODE_ENV:    process.env.NODE_ENV,
      VERCEL_ENV:  process.env.VERCEL_ENV ?? "(not set)",
      VERCEL_URL:  process.env.VERCEL_URL ?? "(not set)",
    },
    request: {
      canonicalHost,
      xForwardedHost,
      xForwardedProto,
    },
    email: {
      ...emailDiag,
      EMAIL_FROM: process.env.EMAIL_FROM ? "PRESENT" : "MISSING (will use default: Oqul <no-reply@oqul.tech>)",
    },
    database: {
      DATABASE_URL: dbUrl ? "PRESENT" : "MISSING",
      host:         dbHost,
      status:       dbStatus,
      ...(dbError && { error: dbError }),
    },
    config: {
      DEBUG_SECRET: process.env.DEBUG_SECRET ? "PRESENT" : "MISSING (endpoint disabled — this response should never appear)",
    },
  });
}

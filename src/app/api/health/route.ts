/**
 * Health endpoint — used by docker-compose healthcheck + monitoring.
 * Returns: app status, Redis status, DB status.
 */
import { NextResponse } from "next/server";
import { isRedisAvailable } from "@/server/cache/redis-client";

export const dynamic = "force-dynamic";

export async function GET() {
  const start = Date.now();

  // Check DB
  let dbOk = false;
  try {
    const { db } = await import("@/db");
    const { sql } = await import("drizzle-orm");
    await db.execute(sql`SELECT 1`);
    dbOk = true;
  } catch {
    dbOk = false;
  }

  const status = {
    status:    dbOk ? "ok" : "degraded",
    version:   process.env.npm_package_version ?? "unknown",
    timestamp: new Date().toISOString(),
    latencyMs: Date.now() - start,
    services: {
      db:    dbOk ? "ok" : "error",
      redis: isRedisAvailable() ? "ok" : "unavailable",
    },
  };

  return NextResponse.json(status, {
    status: dbOk ? 200 : 503,
    headers: { "Cache-Control": "no-store" },
  });
}

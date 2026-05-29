/**
 * Prometheus metrics endpoint.
 * Scraped by Prometheus in the runtime stack.
 */
import { NextResponse } from "next/server";

function assertMetricsAccess(request: Request) {
  if (process.env.NODE_ENV !== "production") return null;
  const expected = process.env.METRICS_BEARER_TOKEN;
  if (!expected) {
    return Response.json({ ok: false, error: "Metrics token not configured." }, { status: 404 });
  }
  const header = request.headers.get("authorization") ?? "";
  if (header !== `Bearer ${expected}`) {
    return Response.json({ ok: false, error: "Not found." }, { status: 404 });
  }
  return null;
}


export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  const metricsGuard = assertMetricsAccess(request);
  if (metricsGuard) return metricsGuard;
  try {
    const promClient = await import("prom-client");

    // Default metrics (Node.js runtime)
    promClient.collectDefaultMetrics({ prefix: "oqul_" });

    const metrics = await promClient.register.metrics();
    return new Response(metrics, {
      headers: { "Content-Type": promClient.register.contentType },
    });
  } catch {
    // prom-client not available in this environment
    return NextResponse.json({ error: "metrics not available" }, { status: 503 });
  }
}

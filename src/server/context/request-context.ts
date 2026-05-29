import type { NextRequest } from "next/server";

export type RequestContext = {
  requestId: string;
  ip?: string;
  userAgent?: string;
  locale: string;
  startedAt: number;
};

export function createRequestContext(request: NextRequest): RequestContext {
  return {
    requestId: crypto.randomUUID(),
    ip:
      request.headers.get("x-forwarded-for")?.split(",")[0]?.trim() ??
      request.headers.get("x-real-ip") ??
      undefined,
    userAgent: request.headers.get("user-agent") ?? undefined,
    locale: request.headers.get("accept-language")?.split(",")[0] ?? "ar-MA",
    startedAt: Date.now(),
  };
}

/**
 * withAuth / withPublic — Next.js route wrappers.
 * Auth enforcement is delegated to auth-guard.ts (single source of truth).
 */
import { type NextRequest, NextResponse } from "next/server";
import { requireAuth } from "./guards/auth-guard";
import type { JWTPayload } from "@/server/auth/jwt";
import { AppError } from "@/server/errors";
import { ZodError } from "zod";

export type AuthContext = {
  session: JWTPayload;
  request: NextRequest;
  params?: Record<string, string>;
};

type AuthHandler = (ctx: AuthContext) => Promise<unknown>;

function handleError(error: unknown): NextResponse {
  if (error instanceof AppError) {
    return NextResponse.json(
      { success: false, message: error.message, code: error.code },
      { status: error.status }
    );
  }
  if (error instanceof ZodError) {
    const message = error.errors.map((e) => e.message).join(". ");
    return NextResponse.json({ success: false, message, code: "VALIDATION_ERROR" }, { status: 422 });
  }
  if (error instanceof Error) {
    console.error("[withAuth error]", error.message, error.stack?.slice(0, 400));
  }
  return NextResponse.json(
    { success: false, message: "حدث خطأ داخلي", code: "INTERNAL_ERROR" },
    { status: 500 }
  );
}

function wrap(result: unknown, status = 200): NextResponse {
  if (result instanceof NextResponse) return result;
  return NextResponse.json({ success: true, data: result }, { status });
}

/**
 * Protected route — delegates to requireAuth() from auth-guard.ts
 * Usage: export const GET = withAuth(async ({ session, request }) => { ... });
 */
export function withAuth(
  handler: AuthHandler,
  options?: { roles?: string[] }
) {
  return async function (
    request: NextRequest,
    ctx: { params: Promise<Record<string, string>> }
  ): Promise<NextResponse> {
    try {
      const session = await requireAuth(); // ← single enforcement point

      if (options?.roles && !options.roles.includes(session.role)) {
        throw new AppError("ليس لديك صلاحية للوصول", "FORBIDDEN", 403);
      }

      const params = await ctx.params;
      const result = await handler({ session, request, params });
      return wrap(result);
    } catch (e) {
      return handleError(e);
    }
  };
}

/** Admin-only route */
export function withAdmin(handler: AuthHandler) {
  return withAuth(handler, { roles: ["admin"] });
}

/** Public route — no auth, but uniform error handling */
export function withPublic(
  handler: (request: NextRequest) => Promise<unknown>
) {
  return async function (request: NextRequest): Promise<NextResponse> {
    try {
      const result = await handler(request);
      return wrap(result);
    } catch (e) {
      return handleError(e);
    }
  };
}

/**
 * auth-guard.ts — single source of truth for authentication enforcement.
 * All route wrappers (withAuth, withAdmin) delegate here.
 */
import { getSession } from "@/server/auth/session";
import { AppError } from "@/server/errors";

export type { JWTPayload } from "@/server/auth/jwt";

/** Throws 401 if not authenticated. Returns session. */
export async function requireAuth() {
  const session = await getSession();
  if (!session) {
    throw new AppError("يجب تسجيل الدخول أولاً", "UNAUTHORIZED", 401);
  }
  return session;
}

/** Throws 403 if not admin. */
export async function requireAdmin() {
  const session = await requireAuth();
  if (session.role !== "admin") {
    throw new AppError("ليس لديك صلاحية الوصول", "FORBIDDEN", 403);
  }
  return session;
}

/**
 * CSRF protection via double-submit cookie pattern.
 * For state-changing API calls, the client must include X-CSRF-Token header
 * that matches the csrf cookie value.
 */
import { type NextRequest } from "next/server";
import { cookies } from "next/headers";

const CSRF_COOKIE = "oqul_csrf";
const CSRF_HEADER = "x-csrf-token";

export function generateCsrfToken(): string {
  return crypto.randomUUID().replace(/-/g, "");
}

export async function setCsrfCookie() {
  const store = await cookies();
  let token = store.get(CSRF_COOKIE)?.value;
  if (!token) {
    token = generateCsrfToken();
    store.set(CSRF_COOKIE, token, {
      httpOnly: false, // must be readable by JS to set in header
      secure:   process.env.NODE_ENV === "production",
      sameSite: "strict",
      maxAge:   60 * 60 * 24, // 1 day
      path:     "/",
    });
  }
  return token;
}

/**
 * Verify CSRF token on mutating requests (POST/PUT/DELETE).
 * Returns true if valid, false if not.
 */
export async function verifyCsrf(request: NextRequest): Promise<boolean> {
  const method = request.method.toUpperCase();
  // Only check mutating methods
  if (!["POST", "PUT", "PATCH", "DELETE"].includes(method)) return true;

  // Skip for auth endpoints (they don't require CSRF — they set the session)
  const path = request.nextUrl.pathname;
  if (path.startsWith("/api/auth/login") || path.startsWith("/api/auth/register")) return true;

  const headerToken = request.headers.get(CSRF_HEADER);
  const cookieToken = request.cookies.get(CSRF_COOKIE)?.value;

  if (!headerToken || !cookieToken) return false;
  return headerToken === cookieToken;
}

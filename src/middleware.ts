import { NextRequest, NextResponse } from "next/server";
import { verifyToken } from "@/server/auth/jwt";
import { AUTH_COOKIE } from "@/server/auth/cookies";

/**
 * middleware.ts — Phase 34 Fix
 * Path: src/middleware.ts
 *
 * Fix: PUBLIC_PATHS was missing critical routes causing redirects to /login:
 *   - /forgot-password, /reset-password, /verify-email (auth flows)
 *   - /privacy, /terms, /faq (legal/info pages)
 *   - /api/auth/verify-email, /api/auth/forgot-password, /api/auth/reset-password
 *   - /api/health (monitoring)
 *
 * Auth logic unchanged. CSP logic unchanged.
 */

// ── Public paths — no JWT required ────────────────────────────────────────────
const PUBLIC_PATHS = new Set([
  // Landing & marketing
  "/",
  "/faq",
  "/privacy",
  "/terms",

  // Auth pages (UI)
  "/login",
  "/register",
  "/forgot-password",
  "/reset-password",
  "/verify-email",

  // Auth API endpoints
  "/api/auth/login",
  "/api/auth/register",
  "/api/auth/logout",
  "/api/auth/refresh",
  "/api/auth/verify-email",
  "/api/auth/forgot-password",
  "/api/auth/reset-password",

  // Public curriculum (used in onboarding preview)
  "/api/curriculum/grades",
  "/api/health",
]);

/**
 * Paths that start with these prefixes are always public.
 * Used for dynamic segments like /reset-password?token=...
 */
const PUBLIC_PREFIXES = [
  "/api/auth/",
  "/_next/",
  "/favicon",
];

/** Generate a cryptographically random nonce for CSP */
function generateNonce(): string {
  const array = new Uint8Array(16);
  crypto.getRandomValues(array);
  const binary = Array.from(array, (byte) => String.fromCharCode(byte)).join("");
  return btoa(binary);
}

/** Build strict nonce-based CSP */
function buildCSP(nonce: string, isDev: boolean): string {
  const scriptSrc = isDev
    ? `'nonce-${nonce}' 'unsafe-eval' 'unsafe-inline'`
    : `'nonce-${nonce}' 'strict-dynamic'`;

  return [
    `default-src 'self'`,
    `script-src ${scriptSrc}`,
    `style-src 'self' 'unsafe-inline' https://fonts.googleapis.com`,
    `font-src 'self' https://fonts.gstatic.com`,
    `img-src 'self' data: blob: https:`,
    `connect-src 'self' https://api.groq.com https://*.neon.tech`,
    `media-src 'self'`,
    `frame-ancestors 'none'`,
    `base-uri 'self'`,
    `form-action 'self'`,
  ].join("; ");
}

/** Paths that require admin role — non-admins are redirected to /dashboard */
const ADMIN_PREFIXES = [
  // Content management — can alter official lessons
  "/admin",
  "/dashboard/pipeline",
  "/dashboard/content-enhancement",
  "/dashboard/official-alignment",
  // Quality & monitoring — admin visibility only
  "/dashboard/phase55",
  "/dashboard/curriculum-quality",
  "/dashboard/quality-depth",
  "/dashboard/exam-intelligence",
];

function isPublic(pathname: string): boolean {
  if (PUBLIC_PATHS.has(pathname)) return true;
  if (PUBLIC_PREFIXES.some((p) => pathname.startsWith(p))) return true;
  return false;
}

function isAdminOnly(pathname: string): boolean {
  return ADMIN_PREFIXES.some((p) => pathname === p || pathname.startsWith(p + "/"));
}

export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const isDev = process.env.NODE_ENV === "development";

  // Static files — pass through immediately
  if (
    pathname.startsWith("/_next") ||
    pathname.startsWith("/favicon") ||
    pathname.includes(".")
  ) {
    return NextResponse.next();
  }

  const nonce = generateNonce();

  // Public paths — no auth needed, but still get CSP
  if (isPublic(pathname)) {
    const response = NextResponse.next();
    response.headers.set("x-nonce", nonce);
    response.headers.set("Content-Security-Policy", buildCSP(nonce, isDev));
    return response;
  }

  const token = request.cookies.get(AUTH_COOKIE)?.value;

  // Not authenticated → redirect to login
  if (!token) {
    const loginUrl = new URL("/login", request.url);
    if (pathname !== "/") loginUrl.searchParams.set("redirect", pathname);
    return NextResponse.redirect(loginUrl);
  }

  try {
    const payload = await verifyToken(token);

    // Admin-only routes: non-admin users are redirected to /dashboard
    if (isAdminOnly(pathname) && payload.role !== "admin") {
      return NextResponse.redirect(new URL("/dashboard", request.url));
    }

    const response = NextResponse.next();

    // Forward user context to server components
    response.headers.set("x-user-id",   payload.sub);
    response.headers.set("x-user-role", payload.role);
    response.headers.set("x-user-plan", payload.plan);

    // Nonce-based CSP on every authenticated response
    response.headers.set("x-nonce", nonce);
    response.headers.set("Content-Security-Policy", buildCSP(nonce, isDev));

    return response;
  } catch {
    // Invalid/expired token → clear and redirect
    const loginUrl = new URL("/login", request.url);
    const response = NextResponse.redirect(loginUrl);
    response.cookies.delete(AUTH_COOKIE);
    return response;
  }
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico|.*\\..*).*)" ],
};


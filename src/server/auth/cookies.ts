import { cookies } from "next/headers";

export const AUTH_COOKIE = "oqul_auth";
export const COOKIE_MAX_AGE = 60 * 60 * 24 * 7; // 7 days

export function cookieOptions(secure: boolean) {
  return {
    httpOnly: true,
    secure,
    sameSite: "lax" as const,
    maxAge: COOKIE_MAX_AGE,
    path: "/",
  };
}

/** Set auth cookie from server action / route handler */
export async function setAuthCookie(token: string) {
  const store = await cookies();
  store.set(
    AUTH_COOKIE,
    token,
    cookieOptions(process.env.NODE_ENV === "production")
  );
}

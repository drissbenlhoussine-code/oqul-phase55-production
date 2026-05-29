import { cookies } from "next/headers";
import { AUTH_COOKIE } from "./cookies";
import { verifyToken } from "./jwt";

export type { JWTPayload } from "./jwt";

export async function getSession() {
  try {
    const store = await cookies();
    const token = store.get(AUTH_COOKIE)?.value;
    if (!token) return null;
    return await verifyToken(token);
  } catch {
    return null;
  }
}

/** Alias for backward-compat */
export const getCurrentSession = getSession;

export async function requireSession() {
  const session = await getSession();
  if (!session) throw new Error("UNAUTHORIZED");
  return session;
}

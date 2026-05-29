import { SignJWT, jwtVerify } from "jose";

export interface JWTPayload {
  sub: string;
  email: string;
  role: string;
  plan: string;
  iat?: number;
  exp?: number;
}

function getSecret() {
  const secret = process.env.AUTH_SECRET || process.env.JWT_SECRET || process.env.NEXTAUTH_SECRET;
  if (!secret) {
    if (process.env.NODE_ENV === "production") {
      throw new Error("AUTH_SECRET is required in production");
    }
    return "development-only-secret-minimum-32-chars!!";
  }
  return secret;
}

function secretKey() {
  return new TextEncoder().encode(getSecret());
}

export async function signToken(payload: Omit<JWTPayload, "iat" | "exp">): Promise<string> {
  const expiresIn = process.env.NODE_ENV === "production" ? "15m" : "7d";
  return new SignJWT({ ...payload })
    .setProtectedHeader({ alg: "HS256" })
    .setIssuedAt()
    .setExpirationTime(expiresIn)
    .sign(secretKey());
}

/** Alias kept for backward-compat with auth-service.ts */
export const signAccessToken = signToken;

export async function verifyToken(token: string): Promise<JWTPayload> {
  const { payload } = await jwtVerify(token, secretKey());
  return payload as unknown as JWTPayload;
}

/**
 * Refresh Token Rotation Service
 *
 * Implements secure token rotation with:
 * - Automatic rotation on every use (old token immediately invalidated)
 * - Family-based theft detection (reuse of revoked token = compromise signal)
 * - Device fingerprinting (user-agent + IP)
 * - Configurable expiry (30 days)
 *
 * Flow:
 *   Login → create family → issue [access_token (7d) + refresh_token (30d)]
 *   Refresh → verify token hash → rotate → issue new pair → revoke old
 *   Theft detected → revoke entire family → force re-login
 */
import crypto from "crypto";
import { eq, and, lt } from "drizzle-orm";
import { db, authSessions } from "@/db";

const REFRESH_EXPIRY_DAYS = 30;
const REFRESH_COOKIE      = "oqul_refresh";
const REFRESH_COOKIE_MAX  = 60 * 60 * 24 * REFRESH_EXPIRY_DAYS;

function hashToken(token: string): string {
  return crypto.createHash("sha256").update(token).digest("hex");
}

function generateToken(): string {
  return crypto.randomBytes(40).toString("base64url");
}

export const refreshTokenService = {
  COOKIE_NAME: REFRESH_COOKIE,
  COOKIE_MAX:  REFRESH_COOKIE_MAX,

  /** Create a new session family on login */
  async createSession(data: {
    userId:    string;
    userAgent?: string;
    ipAddress?: string;
  }): Promise<string> {
    const token     = generateToken();
    const tokenHash = hashToken(token);
    const expiresAt = new Date(Date.now() + REFRESH_EXPIRY_DAYS * 86400 * 1000);

    await db.insert(authSessions).values({
      userId:    data.userId,
      tokenHash,
      userAgent: data.userAgent,
      ipAddress: data.ipAddress,
      expiresAt,
    });

    return token;
  },

  /**
   * Rotate refresh token — the core security operation.
   * Returns new token or throws if invalid/stolen/expired.
   */
  async rotate(incomingToken: string, data: {
    userAgent?: string;
    ipAddress?: string;
  }): Promise<{ userId: string; newToken: string } | null> {
    const hash = hashToken(incomingToken);

    const session = await db.query.authSessions.findFirst({
      where: eq(authSessions.tokenHash, hash),
      with:  { user: true },
    });

    if (!session) return null;

    // EXPIRED — reject silently
    if (new Date() > session.expiresAt) {
      await db.update(authSessions)
        .set({ isRevoked: true })
        .where(eq(authSessions.id, session.id));
      return null;
    }

    // REVOKED — token theft detected! Revoke the entire family.
    if (session.isRevoked) {
      await db.update(authSessions)
        .set({ isRevoked: true })
        .where(eq(authSessions.familyId, session.familyId));
      console.warn("[AUTH] Refresh token reuse detected — family revoked", {
        userId:   session.userId,
        familyId: session.familyId,
        ip:       data.ipAddress,
      });
      return null;
    }

    // VALID — rotate
    const newToken    = generateToken();
    const newTokenHash = hashToken(newToken);
    const newExpiry   = new Date(Date.now() + REFRESH_EXPIRY_DAYS * 86400 * 1000);

    // Revoke old token and create new one in the same family
    await db.update(authSessions)
      .set({ isRevoked: true })
      .where(eq(authSessions.id, session.id));

    await db.insert(authSessions).values({
      userId:        session.userId,
      familyId:      session.familyId,
      tokenHash:     newTokenHash,
      userAgent:     data.userAgent ?? session.userAgent,
      ipAddress:     data.ipAddress ?? session.ipAddress,
      rotationCount: session.rotationCount + 1,
      expiresAt:     newExpiry,
    });

    return { userId: session.userId, newToken };
  },

  /** Revoke all sessions for a user (logout all devices) */
  async revokeAll(userId: string): Promise<void> {
    await db.update(authSessions)
      .set({ isRevoked: true })
      .where(and(eq(authSessions.userId, userId), eq(authSessions.isRevoked, false)));
  },

  /** Revoke specific session (logout this device) */
  async revoke(token: string): Promise<void> {
    const hash = hashToken(token);
    await db.update(authSessions)
      .set({ isRevoked: true })
      .where(eq(authSessions.tokenHash, hash));
  },

  /** Get active sessions for a user (for session management UI) */
  async getActiveSessions(userId: string) {
    return db.query.authSessions.findMany({
      where: and(
        eq(authSessions.userId, userId),
        eq(authSessions.isRevoked, false),
      ),
      columns: {
        id: true, userAgent: true, ipAddress: true,
        rotationCount: true, createdAt: true, lastUsedAt: true, expiresAt: true,
      },
    });
  },

  /** Clean up expired sessions (run periodically) */
  async cleanup(): Promise<number> {
    const result = await db.delete(authSessions)
      .where(lt(authSessions.expiresAt, new Date()));
    return (result as unknown as { rowCount: number }).rowCount ?? 0;
  },

  cookieOptions(secure: boolean) {
    return {
      httpOnly: true,
      secure,
      sameSite: "lax" as const,
      maxAge:   REFRESH_COOKIE_MAX,
      path:     "/api/auth",  // narrower scope than auth cookie
    };
  },
};

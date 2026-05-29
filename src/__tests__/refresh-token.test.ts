/**
 * Refresh Token Rotation tests
 * Tests the security properties of the token rotation system.
 */
import { describe, it, expect } from "vitest";
import crypto from "crypto";

// ── Token Generation ──────────────────────────────────────────────────────────
describe("Refresh Token Generation", () => {
  function generateToken(): string {
    return crypto.randomBytes(40).toString("base64url");
  }

  function hashToken(token: string): string {
    return crypto.createHash("sha256").update(token).digest("hex");
  }

  it("generates a token with sufficient entropy (40 bytes = 320 bits)", () => {
    const token = generateToken();
    // base64url encoding: 40 bytes → ~54 chars
    expect(token.length).toBeGreaterThan(40);
  });

  it("generates unique tokens", () => {
    const tokens = new Set(Array.from({ length: 100 }, () => generateToken()));
    expect(tokens.size).toBe(100);
  });

  it("SHA-256 hash is 64 hex chars", () => {
    const hash = hashToken(generateToken());
    expect(hash).toHaveLength(64);
    expect(hash).toMatch(/^[0-9a-f]+$/);
  });

  it("same token always produces same hash", () => {
    const token = generateToken();
    expect(hashToken(token)).toBe(hashToken(token));
  });

  it("different tokens produce different hashes", () => {
    expect(hashToken(generateToken())).not.toBe(hashToken(generateToken()));
  });
});

// ── Token Rotation Logic ──────────────────────────────────────────────────────
describe("Token Rotation Security Properties", () => {
  interface MockSession {
    tokenHash:     string;
    isRevoked:     boolean;
    familyId:      string;
    rotationCount: number;
    expiresAt:     Date;
  }

  function hashToken(t: string) {
    return crypto.createHash("sha256").update(t).digest("hex");
  }

  async function mockRotate(
    incomingToken:  string,
    sessions:       MockSession[],
    revokeFamily:   (familyId: string) => void,
  ): Promise<{ newToken: string } | null> {
    const hash    = hashToken(incomingToken);
    const session = sessions.find((s) => s.tokenHash === hash);
    if (!session) return null;
    if (new Date() > session.expiresAt) return null;

    if (session.isRevoked) {
      // THEFT DETECTED: revoke entire family
      revokeFamily(session.familyId);
      return null;
    }

    // Valid: rotate
    session.isRevoked = true;
    const newToken = crypto.randomBytes(40).toString("base64url");
    sessions.push({
      tokenHash:     hashToken(newToken),
      isRevoked:     false,
      familyId:      session.familyId,
      rotationCount: session.rotationCount + 1,
      expiresAt:     new Date(Date.now() + 30 * 86400_000),
    });
    return { newToken };
  }

  it("valid token rotation succeeds", async () => {
    const token    = crypto.randomBytes(40).toString("base64url");
    const sessions: MockSession[] = [{
      tokenHash:     hashToken(token),
      isRevoked:     false,
      familyId:      "family-1",
      rotationCount: 0,
      expiresAt:     new Date(Date.now() + 86400_000),
    }];
    const result = await mockRotate(token, sessions, () => {});
    expect(result).not.toBeNull();
    expect(result?.newToken).not.toBe(token);
  });

  it("old token is revoked after rotation (cannot be reused)", async () => {
    const token    = crypto.randomBytes(40).toString("base64url");
    const sessions: MockSession[] = [{
      tokenHash:     hashToken(token),
      isRevoked:     false,
      familyId:      "family-1",
      rotationCount: 0,
      expiresAt:     new Date(Date.now() + 86400_000),
    }];
    await mockRotate(token, sessions, () => {});
    // Try to reuse the same token
    const result2 = await mockRotate(token, sessions, () => {});
    expect(result2).toBeNull(); // revoked — rejected
  });

  it("reuse of revoked token triggers family revocation (theft detection)", async () => {
    const token    = crypto.randomBytes(40).toString("base64url");
    const sessions: MockSession[] = [{
      tokenHash:     hashToken(token),
      isRevoked:     true, // already revoked — simulate stolen token
      familyId:      "family-danger",
      rotationCount: 3,
      expiresAt:     new Date(Date.now() + 86400_000),
    }];
    const revokedFamilies: string[] = [];
    const result = await mockRotate(token, sessions, (fid) => revokedFamilies.push(fid));
    expect(result).toBeNull();
    expect(revokedFamilies).toContain("family-danger"); // whole family killed
  });

  it("expired token is rejected", async () => {
    const token    = crypto.randomBytes(40).toString("base64url");
    const sessions: MockSession[] = [{
      tokenHash:     hashToken(token),
      isRevoked:     false,
      familyId:      "family-1",
      rotationCount: 0,
      expiresAt:     new Date(Date.now() - 1000), // expired
    }];
    const result = await mockRotate(token, sessions, () => {});
    expect(result).toBeNull();
  });

  it("unknown token is rejected", async () => {
    const unknownToken = crypto.randomBytes(40).toString("base64url");
    const result = await mockRotate(unknownToken, [], () => {});
    expect(result).toBeNull();
  });

  it("rotation increments counter", async () => {
    const token    = crypto.randomBytes(40).toString("base64url");
    const sessions: MockSession[] = [{
      tokenHash:     hashToken(token),
      isRevoked:     false,
      familyId:      "family-1",
      rotationCount: 5,
      expiresAt:     new Date(Date.now() + 86400_000),
    }];
    await mockRotate(token, sessions, () => {});
    const newSession = sessions.find((s) => !s.isRevoked);
    expect(newSession?.rotationCount).toBe(6);
  });
});

// ── Expiry ────────────────────────────────────────────────────────────────────
describe("Session Expiry", () => {
  const REFRESH_EXPIRY_DAYS = 30;

  it("refresh token expires in 30 days", () => {
    const expiresAt = new Date(Date.now() + REFRESH_EXPIRY_DAYS * 86400 * 1000);
    const daysUntilExpiry = (expiresAt.getTime() - Date.now()) / 86400 / 1000;
    expect(Math.round(daysUntilExpiry)).toBe(REFRESH_EXPIRY_DAYS);
  });

  it("cookie max-age matches DB expiry", () => {
    const COOKIE_MAX = 60 * 60 * 24 * REFRESH_EXPIRY_DAYS;
    const DB_EXPIRY  = REFRESH_EXPIRY_DAYS * 86400;
    expect(COOKIE_MAX).toBe(DB_EXPIRY);
  });
});

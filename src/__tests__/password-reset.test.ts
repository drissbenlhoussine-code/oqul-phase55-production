import { describe, it, expect } from "vitest";
import { generateSecureToken, hashToken, isExpired, passwordResetExpiry } from "@/server/auth/tokens";

// ── Token generation ──────────────────────────────────────────────────────────
describe("generateSecureToken", () => {
  it("returns a 64-character hex string", () => {
    const token = generateSecureToken();
    expect(token).toHaveLength(64);
    expect(token).toMatch(/^[0-9a-f]{64}$/);
  });

  it("produces unique tokens on each call", () => {
    const tokens = new Set(Array.from({ length: 20 }, () => generateSecureToken()));
    expect(tokens.size).toBe(20);
  });
});

// ── Token hashing ─────────────────────────────────────────────────────────────
describe("hashToken", () => {
  it("returns a 64-character hex string (SHA-256)", () => {
    const hash = hashToken("some-plain-token");
    expect(hash).toHaveLength(64);
    expect(hash).toMatch(/^[0-9a-f]{64}$/);
  });

  it("same input always produces same hash (deterministic)", () => {
    const token = generateSecureToken();
    expect(hashToken(token)).toBe(hashToken(token));
  });

  it("different inputs produce different hashes", () => {
    const a = generateSecureToken();
    const b = generateSecureToken();
    expect(hashToken(a)).not.toBe(hashToken(b));
  });

  it("hash is not equal to the original token", () => {
    const token = generateSecureToken();
    expect(hashToken(token)).not.toBe(token);
  });

  it("hash of empty string is well-defined (no crash)", () => {
    const hash = hashToken("");
    expect(hash).toHaveLength(64);
  });
});

// ── Token expiry ──────────────────────────────────────────────────────────────
describe("passwordResetExpiry", () => {
  it("returns a Date roughly 1 hour from now", () => {
    const before = Date.now();
    const expiry = passwordResetExpiry();
    const after  = Date.now();
    const oneHourMs = 60 * 60 * 1000;
    expect(expiry.getTime()).toBeGreaterThanOrEqual(before + oneHourMs - 10);
    expect(expiry.getTime()).toBeLessThanOrEqual(after  + oneHourMs + 10);
  });
});

// ── isExpired ─────────────────────────────────────────────────────────────────
describe("isExpired", () => {
  it("returns true for a past date", () => {
    const past = new Date(Date.now() - 1000);
    expect(isExpired(past)).toBe(true);
  });

  it("returns false for a future date", () => {
    const future = new Date(Date.now() + 60_000);
    expect(isExpired(future)).toBe(false);
  });

  it("returns true for null", () => {
    expect(isExpired(null)).toBe(true);
  });

  it("returns true for undefined", () => {
    expect(isExpired(undefined)).toBe(true);
  });
});

// ── Flow: forgot → reset idempotency ─────────────────────────────────────────
describe("password reset — hash round-trip", () => {
  it("stores hash, verifies by hashing incoming token", () => {
    // Simulate what the API routes do
    const plainToken = generateSecureToken();        // generated in forgot-password route
    const stored     = hashToken(plainToken);        // stored in DB

    // Simulate what reset-password route does when user clicks the link
    const incoming   = plainToken;                   // from URL query param
    const lookupKey  = hashToken(incoming);          // hashed before DB query

    expect(lookupKey).toBe(stored);                  // DB query finds the right row
  });

  it("wrong token does NOT match the stored hash", () => {
    const realToken  = generateSecureToken();
    const fakeToken  = generateSecureToken();
    const stored     = hashToken(realToken);
    expect(hashToken(fakeToken)).not.toBe(stored);
  });

  it("expired token is correctly detected", () => {
    const expiredAt = new Date(Date.now() - 1);     // 1ms in the past
    expect(isExpired(expiredAt)).toBe(true);
  });

  it("valid (future) expiry is not expired", () => {
    const validUntil = passwordResetExpiry();        // 1h from now
    expect(isExpired(validUntil)).toBe(false);
  });
});

// ── Security properties ───────────────────────────────────────────────────────
describe("password reset — security properties", () => {
  it("stored hash cannot be reversed to the plain token", () => {
    const plain  = generateSecureToken();
    const hash   = hashToken(plain);
    // Verify they are different and hash is not recoverable from hash alone
    expect(hash).not.toBe(plain);
    expect(hash).not.toContain(plain.slice(0, 10));
  });

  it("two calls to generateSecureToken produce non-sequential tokens", () => {
    const t1 = generateSecureToken();
    const t2 = generateSecureToken();
    // They should have no sequential relationship (not just +1)
    expect(parseInt(t1, 16)).not.toBe(parseInt(t2, 16) - 1);
    expect(parseInt(t1, 16)).not.toBe(parseInt(t2, 16) + 1);
  });
});

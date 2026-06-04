/**
 * Secure token generator — cryptographically random, URL-safe.
 * Used for email verification and password reset tokens.
 */
import { randomBytes, createHash } from "crypto";

/** 32-byte hex token — 64 chars, URL-safe, cryptographically random */
export function generateSecureToken(): string {
  return randomBytes(32).toString("hex");
}

/** Password reset token expires in 1 hour */
export function passwordResetExpiry(): Date {
  return new Date(Date.now() + 60 * 60 * 1000);
}

/** Email verification token expires in 24 hours */
export function emailVerificationExpiry(): Date {
  return new Date(Date.now() + 24 * 60 * 60 * 1000);
}

/** Check if a Date is expired */
export function isExpired(expiresAt: Date | null | undefined): boolean {
  if (!expiresAt) return true;
  return new Date() > expiresAt;
}

/**
 * One-way SHA-256 hash of a token.
 * Store the hash in DB; send the plain token in emails.
 * On verification: hash the incoming token and compare the hash.
 */
export function hashToken(token: string): string {
  return createHash("sha256").update(token).digest("hex");
}

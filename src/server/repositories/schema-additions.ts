/**
 * schema-additions.ts — Phase 31
 *
 * Drizzle column definitions for the new fields added in migration 017.
 * These extend the existing `users` table definition in schema.ts.
 *
 * HOW TO APPLY:
 * Add these fields inside the users pgTable(...) definition in schema.ts,
 * between `trialEndsAt` and `createdAt`:
 *
 * ```ts
 * // email verification
 * emailVerified:            boolean("email_verified").notNull().default(false),
 * emailVerificationToken:   text("email_verification_token"),
 * emailVerificationSentAt:  timestamp("email_verification_sent_at", { withTimezone: true }),
 * // password reset
 * passwordResetToken:       text("password_reset_token"),
 * passwordResetExpiresAt:   timestamp("password_reset_expires_at", { withTimezone: true }),
 * // legal
 * termsAcceptedAt:          timestamp("terms_accepted_at", { withTimezone: true }),
 * ```
 *
 * This file documents the additions. The actual change is a 6-line edit in schema.ts.
 * See PHASE31_APPLY.md for the exact diff to copy-paste.
 */

export const SCHEMA_ADDITIONS_DOC = `
Fields to add to users table in src/db/schema.ts (after trialEndsAt line):

  // Phase 31 — email & password reset
  emailVerified:            boolean("email_verified").notNull().default(false),
  emailVerificationToken:   text("email_verification_token"),
  emailVerificationSentAt:  timestamp("email_verification_sent_at", { withTimezone: true }),
  passwordResetToken:       text("password_reset_token"),
  passwordResetExpiresAt:   timestamp("password_reset_expires_at", { withTimezone: true }),
  termsAcceptedAt:          timestamp("terms_accepted_at", { withTimezone: true }),
`;

/**
 * users-email-repo.ts
 * Phase 31 — Email verification & password reset DB queries.
 *
 * ADDITIVE ONLY — does not modify usersRepo in users.ts.
 * Import both where needed.
 */
import { eq } from "drizzle-orm";
import { db, users } from "@/db";

export const usersEmailRepo = {
  // ── Email Verification ─────────────────────────────────────────────────────

  async setVerificationToken(userId: string, token: string, sentAt: Date) {
    await db.update(users)
      .set({
        emailVerificationToken:  token,
        emailVerificationSentAt: sentAt,
        updatedAt:               new Date(),
      })
      .where(eq(users.id, userId));
  },

  async findByVerificationToken(token: string) {
    const [user] = await db.select().from(users)
      .where(eq(users.emailVerificationToken, token))
      .limit(1);
    return user ?? null;
  },

  async markEmailVerified(userId: string) {
    await db.update(users)
      .set({
        emailVerified:           true,
        emailVerificationToken:  null,
        emailVerificationSentAt: null,
        updatedAt:               new Date(),
      })
      .where(eq(users.id, userId));
  },

  // ── Password Reset ─────────────────────────────────────────────────────────

  async setResetToken(userId: string, token: string, expiresAt: Date) {
    await db.update(users)
      .set({
        passwordResetToken:     token,
        passwordResetExpiresAt: expiresAt,
        updatedAt:              new Date(),
      })
      .where(eq(users.id, userId));
  },

  async findByResetToken(token: string) {
    const [user] = await db.select().from(users)
      .where(eq(users.passwordResetToken, token))
      .limit(1);
    return user ?? null;
  },

  async updatePassword(userId: string, passwordHash: string) {
    await db.update(users)
      .set({
        passwordHash,
        passwordResetToken:     null,
        passwordResetExpiresAt: null,
        updatedAt:              new Date(),
      })
      .where(eq(users.id, userId));
  },

  // ── Terms ──────────────────────────────────────────────────────────────────

  async acceptTerms(userId: string) {
    await db.update(users)
      .set({ termsAcceptedAt: new Date(), updatedAt: new Date() })
      .where(eq(users.id, userId));
  },
};

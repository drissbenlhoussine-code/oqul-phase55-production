-- Migration 017: Email verification & password reset
-- Phase 31 — Launch Safety
-- Run: psql $DATABASE_URL -f db/migrations/017_email_verification.sql

ALTER TABLE users
  ADD COLUMN IF NOT EXISTS email_verified         BOOLEAN          NOT NULL DEFAULT false,
  ADD COLUMN IF NOT EXISTS email_verification_token TEXT,
  ADD COLUMN IF NOT EXISTS email_verification_sent_at TIMESTAMPTZ,
  ADD COLUMN IF NOT EXISTS password_reset_token   TEXT,
  ADD COLUMN IF NOT EXISTS password_reset_expires_at TIMESTAMPTZ,
  ADD COLUMN IF NOT EXISTS terms_accepted_at      TIMESTAMPTZ;

-- Index for fast token lookups (tokens are queried directly)
CREATE INDEX IF NOT EXISTS users_email_verification_token_idx
  ON users (email_verification_token)
  WHERE email_verification_token IS NOT NULL;

CREATE INDEX IF NOT EXISTS users_password_reset_token_idx
  ON users (password_reset_token)
  WHERE password_reset_token IS NOT NULL;

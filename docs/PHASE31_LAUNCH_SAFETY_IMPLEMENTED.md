# Phase 31 — Launch Safety Implemented

This update integrates the launch-safety work as a cautious product-readiness layer.

## Added

- Email service for verification and reset flows.
- Secure token helpers.
- Email verification API.
- Forgot password API.
- Reset password API.
- Privacy page.
- Terms page.
- Parent consent checkbox in registration.
- Forgot password link and verification banners on login.
- Migration file `017_email_verification.sql`.
- Environment variable examples.

## Backups created

Sensitive replaced files were backed up next to the original with:

```txt
.pre-phase31-backup
```

## Important manual step still required

Before running the new auth flows, add the six email/reset fields to `src/db/schema.ts`.
See:

```txt
src/server/repositories/schema-additions.ts
docs/PHASE31_APPLY.md
```

## Environment variables

Create `.env.local` using `.env.example`, then add:

```env
DATABASE_URL="..."
NEXTAUTH_SECRET="..."
NEXTAUTH_URL="http://localhost:3000"
JWT_SECRET="..."
RESEND_API_KEY=""
EMAIL_FROM="Oqul <no-reply@oqul.ma>"
GROQ_API_KEY="..."
```

In dev, the email service can still log emails if no Resend key is configured.

## Verification

Run:

```powershell
npm run typecheck
npm run lint
npm run build
npm run dev
```

## Production warning

Do not launch publicly before:
- PostgreSQL is connected.
- Migration 017 is applied.
- Email verification is tested.
- Password reset is tested.
- Privacy/Terms links are visible on registration.

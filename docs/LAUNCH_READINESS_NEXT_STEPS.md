# Oqul Launch Readiness — Next Steps

## Current state

This version is the safest base so far:

- clean project zip
- package-lock exists
- no node_modules
- no .next
- Next config updated
- client/server gamification boundary cleaned
- visual demo added
- onboarding/pricing demo added

## Verify locally

```powershell
npm run typecheck
npm run lint
npm run build
npm run dev
```

Open:

```txt
http://localhost:3000/visual-demo
http://localhost:3000/phase31-demo
```

## Required before real registration works

Create `.env.local` with:

```env
DATABASE_URL="your-neon-or-postgres-url"
NEXTAUTH_SECRET="change-me"
NEXTAUTH_URL="http://localhost:3000"
JWT_SECRET="change-me"
GROQ_API_KEY=""
```

Then run the database push/migration command used by the project.

## Product order

1. Get DB/auth working.
2. Confirm register/login.
3. Connect onboarding to real child creation.
4. Connect pricing to Stripe later.
5. Test with 5 real children.

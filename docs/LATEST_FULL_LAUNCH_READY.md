# Oqul Latest Full Launch Ready

This ZIP combines the latest launch-safety, visual experience, onboarding/pricing, privacy/terms, email verification/reset foundations, schema email fields, and Next config cleanup.

Next steps after extraction:

```powershell
npm install
Copy-Item .env.local .env -Force
npm run typecheck
npm run dev
```

Use a clean Neon branch for `db:push`. Do not accept data-loss prompts on a database with valuable data.

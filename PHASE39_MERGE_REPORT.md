# Oqul Phase39 — v13 Voice/Research Merge

Base: Phase38 stable production build.

Merged from `oqul_phase36_merge.zip` carefully:

- Added voice input endpoint: `/api/ai/transcribe` using Groq Whisper.
- Added microphone button to Leila tutor chat.
- Added v13 adaptive Leila context: attempt count, age-group guidance, clarification rule, smarter lesson-context extraction.
- Added research interface: `/dashboard/research`.
- Kept Phase38 `/dashboard/pipeline` as the main advanced multi-agent experience.
- Added `db:seed:v13` script and included `src/db/seed-curriculum-v13.ts` for optional richer v13 curriculum import.

Not merged intentionally:

- `public/sw.js` and service-worker registration, because previous local builds suffered from stale cache/chunk errors.
- PWA cache behavior. This can be reintroduced later after production deployment with strict cache versioning.

Recommended test order:

1. `npm install`
2. Copy `.env.local` from Phase37/38
3. `./db-setup.ps1`
4. Optional: `npm run db:seed:v13`
5. `./start-production-clean.ps1`
6. Test `/dashboard/lessons`, `/dashboard/leila`, `/dashboard/pipeline`, `/dashboard/research`.

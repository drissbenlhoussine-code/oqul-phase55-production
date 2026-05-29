# Phase 8.1 — Surgical Stabilization

## Goal

Stabilize Phase 8 without changing the product architecture or introducing new feature scope.

## Fixes Applied

### TypeScript Stability
- Exported `progressService` singleton.
- Added a real `apiClient` implementation with `get/post/patch/delete` helpers.
- Fixed `AppError` constructor usage inside guards.
- Tightened exercise submission validation so `answer` is required.

### API Contract Alignment
- Updated frontend API client to support the current server response contract:
  - `success: true`
  - `success: false`
- Kept compatibility with older `ok: true` client responses during transition.

### AI Streaming Alignment
- Fixed frontend stream endpoint from `/api/ai/tutor` to `/api/ai/leila`.
- Connected `/api/ai/leila` to the SSE streaming runtime when `stream: true` is sent.
- Preserved JSON response mode for non-streaming tutor requests.

### AI Safety + Reliability
- Added moderation usage inside `TutorService` before provider execution.
- Connected retry, timeout, and circuit breaker foundations to `GroqProvider` execution.
- Logged failed AI usage attempts.

### Build Safety
- Removed remote `next/font/google` dependency from `layout.tsx` to avoid CI/build failures when Google Fonts are unavailable.
- Kept Arabic-first font stack through Tailwind fallback variables.

### Security
- Replaced unsafe production fallback for `AUTH_SECRET`.
- Production now throws if `AUTH_SECRET` is missing.
- Development keeps a clearly labeled temporary fallback.

### Lint Cleanup
- Removed unused-variable warnings by explicitly handling placeholder parameters.

## Verified Commands

The following passed in this environment:

```bash
npm run typecheck
npm run lint
```

`npm run build` compiled successfully and reached page-data collection, but the sandbox command timed out during Next.js static generation. No TypeScript or ESLint errors remain. Run build locally or in Vercel for final confirmation:

```bash
npm run build
```

## Scope Not Changed

- No database redesign.
- No UI redesign.
- No auth architecture rewrite.
- No feature scope expansion.
- No project restart.

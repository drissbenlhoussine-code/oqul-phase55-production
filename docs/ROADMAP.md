# OQUL Roadmap

## Phase 0 — Foundation UI
Status: completed in this artifact.

## Phase 1 — Database Architecture
PostgreSQL + Drizzle schema + seed foundation.

## Phase 2 — Authentication
Custom JWT with httpOnly cookies.

## Phase 3 — Dashboard Shell
Protected app layout, sidebar, child switcher.

## Phase 4 — Curriculum Engine
Cycles, grades, subjects, units, lessons.

## Phase 5 — Lesson Viewer
Exercises, lesson progress, content display.

## Phase 6 — Leila AI Tutor
Server-side Groq integration, contextual tutoring, memory.

## Phase 7 — Quiz System
Assessment, weak points, progress updates.

## Phase 8 — Parent Dashboard
Progress analytics and recommendations.

## Phase 9 — Subscription Foundation
Trial, quotas, soft paywall.

## Phase 10 — QA + Production
Security, build, deployment guide.

## Phase 1 — Database Architecture ✅

Added the PostgreSQL + Drizzle schema foundation:

- identity tables
- child profiles
- curriculum hierarchy
- lesson content
- exercises
- progress
- quiz attempts
- weak points
- chat sessions
- subscriptions
- trials
- AI usage
- feature flags

Phase 2 should build custom JWT authentication on top of this schema.


## Phase 7 — Interactive Product Experience

Added feature architecture, dashboard runtime, AI tutor UI, lesson viewer, parent dashboard foundation, and frontend state/query foundations.

## Phase 8 — Realtime AI Experience & Production Hardening

Completed foundations:
- AI streaming runtime
- tutor stream frontend runtime
- moderation foundation
- retry/timeout/circuit breaker
- domain events
- background jobs
- toast/error/loading UX

## Phase 8.1 — Surgical Stabilization

Completed stabilization fixes:
- TypeScript errors fixed
- Lint warnings fixed
- API response contract aligned
- Leila streaming endpoint aligned
- SSE streaming connected to `/api/ai/leila`
- Moderation connected to tutor service
- Retry/timeout/circuit breaker connected to provider execution
- Google remote font build dependency removed
- Production `AUTH_SECRET` fallback removed

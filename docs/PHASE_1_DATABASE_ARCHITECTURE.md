# Phase 1 — Database Architecture

## Goal
Create the production-ready database foundation for OQUL without touching UI, auth, dashboards, or AI implementation.

This phase defines how OQUL stores:

- users and children
- educational cycles, grades, subjects, units, and lessons
- lesson content and exercises
- progress and quiz attempts
- Leila chat sessions and messages
- weak points and badges
- subscriptions, trials, AI usage, and feature flags

## Files Added

```txt
src/db/schema.ts
src/db/index.ts
src/db/seed.ts
drizzle.config.ts
docs/adr/001-drizzle-postgres.md
docs/PHASE_1_DATABASE_ARCHITECTURE.md
```

## Files Updated

```txt
package.json
.env.example
```

## Database Tables

### Core Identity

- `users`
- `children`
- `user_preferences`

### Curriculum

- `cycles`
- `grades`
- `subjects`
- `units`
- `lessons`
- `lesson_contents`
- `exercises`

### Learning Progress

- `lesson_progress`
- `quiz_attempts`
- `weak_points`
- `badges`
- `child_badges`

### Leila AI

- `chat_sessions`
- `chat_messages`
- `ai_usage_events`

### Monetization / Access Control

- `subscriptions`
- `trial_records`
- `feature_flags`

## Important Architecture Decisions

### 1. Lazy Database Initialization

`src/db/index.ts` does not connect to the database at import time.

This prevents Next.js build from failing when `DATABASE_URL` is missing.

The database connection is created only when a query is executed.

### 2. Curriculum Hierarchy

The hierarchy is:

```txt
Cycle → Grade → Subject → Unit → Lesson → Content / Exercises
```

This supports:

- primary school
- middle school
- high school
- future tracks and specializations
- all Moroccan curriculum subjects including Amazigh

### 3. Progress Is Child-Centered

Progress belongs to a child, not just a user.

This supports family accounts with multiple children.

### 4. Leila AI Is Context-Ready

Chat sessions can optionally link to a lesson, so Leila can answer globally or inside a specific lesson context.

### 5. Monetization Is Prepared But Not Implemented

Subscriptions, trials, AI usage, and feature flags are included now to avoid painful schema redesign later.

## Seed Strategy

`src/db/seed.ts` inserts structural curriculum data only:

- cycles: primary, middle, high
- primary grades 1–6
- middle grades 1–3
- high school levels
- core subjects including Amazigh
- a few sample units and lessons for validation
- starter badges and feature flags

The seed is intentionally not a full curriculum yet. Full official-aligned lesson expansion will happen in later curriculum phases.

## Commands

```bash
npm install
npm run db:push
npm run db:seed
npm run build
```

## Current Limitations

- No auth is implemented yet.
- No UI consumes the database yet.
- Full Moroccan curriculum content is not inserted yet.
- Build was not executed in this environment.

## Quality Notes

This phase is intentionally backend-only. It prepares the project for Phase 2 authentication and later curriculum/AI phases without mixing responsibilities.

## Build Note

This package was prepared in an environment where project dependencies are not installed. The schema and file structure were created carefully, but the real validation step remains:

```bash
npm install
npm run build
```

If build exposes a Drizzle or TypeScript issue, fix it before Phase 2.

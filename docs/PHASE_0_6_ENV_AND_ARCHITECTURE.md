# Phase 0.6 — Environment & Architecture Rules

## Goal

Prepare OQUL for the database/auth phases by adding safe environment validation and clear engineering rules before the codebase grows.

## Added Files

```txt
src/lib/env.ts
docs/ARCHITECTURE_RULES.md
docs/PHASE_0_6_ENV_AND_ARCHITECTURE.md
```

## What Was Added

### 1. Environment Validation

`src/lib/env.ts` centralizes environment parsing with Zod.

It supports:

- `NEXT_PUBLIC_APP_URL`
- `DATABASE_URL`
- `AUTH_SECRET`
- `GROQ_API_KEY`
- `UPSTASH_REDIS_REST_URL`
- `UPSTASH_REDIS_REST_TOKEN`

Important: future server variables remain optional in Phase 0.6 so the landing foundation can build without a database.

### 2. Runtime Safety Helper

`requireEnv()` gives later phases a clear way to fail fast when a feature truly requires an environment variable.

Example for future phases:

```ts
const databaseUrl = requireEnv("DATABASE_URL");
```

### 3. Architecture Rules

`docs/ARCHITECTURE_RULES.md` defines:

- folder boundaries
- naming conventions
- server/client boundaries
- API rules
- design system rules
- quality gates

## What Was Not Added

- No database schema.
- No auth.
- No dashboard.
- No AI.
- No API routes.

## Why This Matters

This phase prevents the most common problems in large AI-generated projects:

- leaking secrets into the client
- mixing server/client code
- inconsistent file names
- scattered API calls
- architecture drift
- random duplicate systems

## Next Phase

```txt
Phase 1 — Database Architecture + Drizzle Schema + Seed
```

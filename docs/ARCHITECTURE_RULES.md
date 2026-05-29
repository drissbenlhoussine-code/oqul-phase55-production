# OQUL Architecture Rules

This document defines the rules that keep OQUL clean as it grows from a landing-page foundation into a full SaaS education platform.

## 1. Execution Model

OQUL is built phase by phase. Each phase must be reviewed before the next one begins.

- Do not add database code before the database phase.
- Do not add authentication code before the auth phase.
- Do not add AI code before the Leila phase.
- Do not rewrite stable foundation files unless there is a clear architectural reason.

## 2. Folder Boundaries

Current foundation:

```txt
src/app/                 App Router pages and layouts
src/components/ui/       Reusable primitive UI components
src/components/layout/   Navbar, footer, app shell, navigation
src/components/landing/  Landing-page sections only
src/lib/                 Shared utilities and framework-agnostic helpers
src/lib/api/             API client helpers and error utilities
src/lib/validators/      Zod validation schemas
src/types/               Shared TypeScript domain types
docs/                    Architecture, roadmap, and phase summaries
```

Future boundaries:

```txt
src/db/                  Drizzle schema, relations, seed, database client
src/features/            Feature-level modules after core systems become large
src/hooks/               Shared client hooks
src/server/              Server-only services if needed
```

## 3. Naming Conventions

- Files and folders: `kebab-case`
- React components: `PascalCase`
- Functions and variables: `camelCase`
- Constants: `SCREAMING_SNAKE_CASE` only for true immutable constants
- TypeScript types/interfaces: `PascalCase`
- Route segments: lowercase kebab-case

Examples:

```txt
button.tsx
section-heading.tsx
lesson-viewer.tsx
parent-dashboard.tsx
```

## 4. Server / Client Boundaries

- Server secrets never go into client components.
- Only variables starting with `NEXT_PUBLIC_` may be used client-side.
- Database access must stay server-side.
- Groq/OpenAI keys must stay server-side.
- Client components must use explicit `"use client"` only when they need state, effects, browser APIs, or event handlers.

## 5. API Rules

- Components must not scatter raw `fetch()` calls everywhere.
- Shared client API calls should use `src/lib/api/client.ts`.
- API errors should be normalized through `src/lib/api/errors.ts`.
- Validation must use Zod before data reaches business logic.

## 6. Design System Rules

- Use shared UI primitives before creating new UI patterns.
- Use `designTokens` for repeated values and design decisions.
- Avoid one-off colors, shadows, and spacing in random components.
- Keep Arabic-first and RTL-first layout decisions.

## 7. Quality Gates

Before a phase is accepted:

- No duplicate systems.
- No broken imports.
- No dead architecture.
- No localStorage auth.
- No secrets in client code.
- `npm run build` must pass in a real Node environment.

## 8. Current Status

- Phase 0: Foundation UI completed.
- Phase 0.5: Design tokens, API foundation, validators, and shared types added.
- Phase 0.6: Environment validation and architecture rules added.

Next planned phase:

```txt
Phase 1 — Database Architecture + Drizzle Schema + Seed
```

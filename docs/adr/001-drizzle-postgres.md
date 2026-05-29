# ADR 001 — PostgreSQL + Drizzle ORM

## Status
Accepted

## Context
OQUL needs a relational data model that can handle users, children, curriculum hierarchy, lessons, progress tracking, AI conversations, quotas, trials, and subscriptions.

## Decision
Use PostgreSQL as the primary database and Drizzle ORM for schema-first TypeScript-safe access.

## Why
- PostgreSQL is reliable for relational educational data.
- Drizzle keeps schema definitions close to TypeScript types.
- Drizzle supports explicit indexes, foreign keys, enums, and relations.
- The model can scale from MVP to SaaS without changing database family.

## Consequences
- All database tables are defined in `src/db/schema.ts`.
- Runtime database access must go through `src/db/index.ts`.
- Database initialization is lazy so build does not fail without `DATABASE_URL`.
- Migrations/Push are managed through Drizzle Kit.

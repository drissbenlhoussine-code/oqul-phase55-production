# ADR 005 — Product API Contracts

## Decision

All product APIs use route handlers, Zod validation, services, and typed responses.

## Why

This prevents duplicated try/catch logic, inconsistent responses, and hidden business logic inside routes.

## Flow

Request → validation → route handler → service → repository → database

## Guardrails

- Routes stay thin.
- Services may orchestrate.
- Repositories must not contain product logic.
- Guards check access only.

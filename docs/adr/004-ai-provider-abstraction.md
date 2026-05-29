# ADR 004 — AI Provider Abstraction

## Decision

OQUL uses a provider abstraction for AI model access.

## Why

Leila must be able to use Groq today and potentially OpenAI, Claude, Gemini, or local models later.

## Consequences

- Providers execute prompts only.
- Business rules stay outside providers.
- Quotas and permissions stay in services/guards.
- Usage logging stays isolated.
- Prompt versioning enables A/B tests and rollback.

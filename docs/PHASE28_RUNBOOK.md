# Phase 28 Runbook

## Apply migration

```bash
psql "$DATABASE_URL" -f db/migrations/016_phase28_human_learning_experience.sql
```

## Run tests

```bash
npm run test:phase28
```

## Preview APIs

```txt
POST /api/contextual-learning/explain-like-home
POST /api/daily-challenge/preview
POST /api/leila/noticed-preview
```

## Rule

Protect the magic:
- Leila should feel personal
- learning should be short and joyful
- parent summaries should be simple
- no new infrastructure expansion

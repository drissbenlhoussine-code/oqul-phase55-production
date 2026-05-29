# Oqul Phase51 — Full Middle School Curriculum Expansion

## Counts

- 1AC: 620 lessons
- 2AC: 660 lessons
- 3AC: 660 lessons
- Total: 1940 lessons

## Commands

```powershell
node scripts/seed-phase51-full-middle-school.mjs --dry-run
node scripts/seed-phase51-full-middle-school.mjs --apply
```

## Safety

- Does not delete old lessons
- Uses transaction
- Adds/updates lessons
- Adds content and exercises
- Generates report
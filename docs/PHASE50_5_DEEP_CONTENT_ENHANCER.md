# Oqul Phase50.5 — Deep Content Enhancer

This phase improves weak or placeholder lessons.

## Commands

Draft only:

```powershell
node scripts/enhance-weak-lessons.mjs --limit=100
```

Apply to database:

```powershell
node scripts/enhance-weak-lessons.mjs --limit=100 --apply
```

Dashboard:

```txt
/dashboard/content-enhancement
```

Safety:
- Does not delete lessons.
- Updates lesson_contents only.
- Can run in batches.
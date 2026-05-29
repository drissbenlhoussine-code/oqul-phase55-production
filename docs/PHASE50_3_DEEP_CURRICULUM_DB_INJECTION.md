# Oqul Phase50.3 — Deep Curriculum DB Injection

This phase safely injects Phase50.2 deep lessons into the database.

## Sequence

1. Phase50.1 — curriculum mapping
2. Phase50.2 — deep lesson reconstruction
3. Phase50.3 — safe database injection

## Safety

- Does not delete old lessons
- Uses upsert behavior where possible
- Runs inside a database transaction
- Has dry-run mode before apply
- Rejects low-quality lessons using a quality threshold
- Writes reports to `reports/`

## Commands

First run dry-run:

```powershell
node scripts/inject-deep-curriculum.mjs --dry-run
```

Then apply:

```powershell
node scripts/inject-deep-curriculum.mjs --apply
```

Optional threshold:

```powershell
$env:PHASE50_MIN_QUALITY_SCORE="70"
node scripts/inject-deep-curriculum.mjs --apply
```

## Required previous step

You must run Phase50.2 first:

```powershell
node scripts/reconstruct-deep-lessons.mjs
```

## Output reports

- `reports/phase50-3-db-injection-dry-run.json`
- `reports/phase50-3-db-injection-apply.json`
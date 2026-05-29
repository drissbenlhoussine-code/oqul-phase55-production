# Oqul Phase50.1 — Real Moroccan Curriculum Mapping

This patch implements the first serious step toward a real Moroccan curriculum:

## What it adds

- `curriculum-registry/sources.json`
- `curriculum-registry/official-curriculum-registry.scaffold.json`
- `scripts/audit-curriculum-coverage.mjs`
- `scripts/import-official-curriculum-titles.mjs`
- `docs/PHASE50_1_REAL_CURRICULUM_MAPPING.md`

## Source policy

Primary source of truth:
- TelmidTICE: https://telmidtice.men.gov.ma/

Cross-check only:
- Moutamadris: https://moutamadris.ma/cours/
- AlloSchool: https://www.alloschool.com/

## Very important

This patch does NOT pretend that all generated titles are official.
It creates a strict registry scaffold with `verificationStatus: needs_official_title_verification`.

The next step is to fill:
`curriculum-registry/verified-official-curriculum.json`

with verified official lesson titles/order from TelmidTICE.

## Run

Copy the folders into your Oqul project, then run:

```powershell
node scripts/audit-curriculum-coverage.mjs
node scripts/import-official-curriculum-titles.mjs
```

## Why this is correct

We should not generate thousands of random titles and call them official.
Phase50.1 separates:

1. Official curriculum mapping
2. Curriculum coverage audit
3. Deep original lesson reconstruction
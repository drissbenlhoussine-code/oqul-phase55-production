# Oqul Phase49 — Full Curriculum Database Seed

This patch adds a large safe database seed that injects structured lessons into the existing Oqul curriculum tables.

It does not change auth, middleware, AI, or schema.

## Run

Copy `scripts/seed-full-curriculum.mjs` into your project `scripts/` folder, then run:

```powershell
node scripts/seed-full-curriculum.mjs
```

Then restart:

```powershell
npm start
```

Or in dev:

```powershell
npm run dev
```

## Expected result

The database will contain many more:
- grades
- subjects
- units
- lessons
- lesson contents
- exercises

The `/dashboard/lessons` page should then show much more than 3-4 lessons per subject.

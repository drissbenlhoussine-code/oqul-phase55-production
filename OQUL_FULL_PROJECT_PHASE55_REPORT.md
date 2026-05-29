# OQUL FULL AI EDUCATION PLATFORM — Phase55 Full Project Build

This is a full project ZIP based on `oqul_PHASE48_QUALITY_DEPTH_ALL_LAYERS.zip` with today's phases merged directly into the project root.

## Merged phases
- Oqul_PHASE49_FULL_CURRICULUM_DB_SEED_PATCH.zip
- Oqul_PHASE50_1_REAL_CURRICULUM_MAPPING_PATCH.zip
- Oqul_PHASE50_2_DEEP_LESSON_RECONSTRUCTION_PATCH.zip
- Oqul_PHASE50_3_DEEP_CURRICULUM_DB_INJECTION_PATCH.zip
- Oqul_PHASE50_4_CURRICULUM_QUALITY_ASSURANCE_PATCH.zip
- Oqul_PHASE50_5_DEEP_CONTENT_ENHANCER_PATCH.zip
- Oqul_PHASE51_FULL_MIDDLE_SCHOOL_CURRICULUM_PATCH.zip
- Oqul_PHASE52_FULL_PRIMARY_SCHOOL_CURRICULUM_PATCH.zip
- Oqul_PHASE53_FULL_SECONDARY_SCHOOL_CURRICULUM_PATCH.zip
- Oqul_PHASE54_OFFICIAL_ALIGNMENT_EXAM_INTELLIGENCE_PATCH.zip
- Oqul_PHASE55_ADAPTIVE_AI_LEARNING_PLATFORM_PATCH.zip

## Missing patches
- None

## What is included
- Original Oqul project files
- Phase49 full curriculum DB seed patch
- Phase50.1 real curriculum mapping
- Phase50.2 deep lesson reconstruction
- Phase50.3 deep curriculum DB injection
- Phase50.4 curriculum quality assurance
- Phase50.5 deep content enhancer
- Phase51 full middle school curriculum
- Phase52 full primary school curriculum
- Phase53 full secondary school curriculum
- Phase54 official alignment + exam intelligence
- Phase55 adaptive AI learning platform

## Install from zero

```powershell
npm install
Copy-Item .env.example .env.local -Force
notepad .env.local
Copy-Item .env.local .env -Force
npm run db:push
```

## Seed/apply curriculum safely

```powershell
node scripts/seed-full-curriculum.mjs
node scripts/seed-phase51-full-middle-school.mjs --dry-run
node scripts/seed-phase51-full-middle-school.mjs --apply
node scripts/seed-phase52-full-primary-school.mjs --dry-run
node scripts/seed-phase52-full-primary-school.mjs --apply
node scripts/seed-phase53-full-secondary-school.mjs --dry-run
node scripts/seed-phase53-full-secondary-school.mjs --apply
```

## Generate intelligence reports

```powershell
node scripts/audit-curriculum-coverage.mjs
node scripts/reconstruct-deep-lessons.mjs
node scripts/inject-deep-curriculum.mjs --dry-run
node scripts/audit-curriculum-quality.mjs
node scripts/audit-phase54-official-alignment.mjs
node scripts/generate-phase55-intelligence-report.mjs
```

## Run

```powershell
npm run build
npm start
```

or development:

```powershell
npm run dev
```

## Dashboards
- /dashboard/lessons
- /dashboard/primary-school
- /dashboard/middle-school
- /dashboard/secondary-school
- /dashboard/curriculum-quality
- /dashboard/content-enhancement
- /dashboard/official-alignment
- /dashboard/exam-intelligence
- /dashboard/phase55
- /dashboard/learning-paths
- /dashboard/exam-prediction

## Safety
This build does not include `node_modules`. Run `npm install` after extracting.

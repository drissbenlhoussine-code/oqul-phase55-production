# Oqul Phase50.2 — Deep Lesson Reconstruction Engine

This phase preserves the sequence:

1. Phase50.1 maps the curriculum.
2. Phase50.2 reconstructs deep lesson objects.
3. Phase50.3 will inject verified deep lessons into the database.

## What this patch adds

- `src/features/curriculum-reconstruction/lesson-shape.ts`
- `src/features/curriculum-reconstruction/reconstruct-deep-lesson.ts`
- `src/features/curriculum-reconstruction/quality-gate.ts`
- `scripts/reconstruct-deep-lessons.mjs`

## Run

After copying the patch into your project:

```powershell
node scripts/reconstruct-deep-lessons.mjs
```

## Output

```txt
generated-curriculum/deep-lessons/
reports/phase50-2-deep-reconstruction-report.json
```

## Important

This does not copy TelmidTICE/Moutamadris/AlloSchool text.

It uses the curriculum map title/order and builds an original Oqul pedagogical structure:
- explanation
- examples
- interactive questions
- common mistakes
- remediation
- exercises
- mini assessment
- Leila hooks

## Safety

No database writes.
No auth changes.
No infrastructure changes.
No build config changes.
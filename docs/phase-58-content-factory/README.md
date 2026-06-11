# Phase 58 — Content Factory Design

## Goal

Phase 58 defines the production standard for generating, reviewing, and accepting 2BAC educational content in OQUL.

This phase is documentation-only. It must be accepted before any new 2BAC lesson generation starts.

## Why This Phase Exists

OQUL is no longer mainly blocked by infrastructure. The platform already has stable systems for authentication, dashboards, Leila, research, learning paths, exam preparation, and lesson viewing.

The main bottleneck is now high-quality Moroccan educational content.

Students and parents will value OQUL because:

- Leila explains clearly.
- Lessons are complete and curriculum-aligned.
- BAC preparation is practical and exam-aware.
- Exercises include answers, corrections, and methodology.
- Content is adapted to the Moroccan classroom context.

## Strategic Rule

Content first, not architecture.

Do not redesign Auth, Leila, Research, Learning Paths, Exam Prep, the database, or the app structure during this phase.

## Deliverables

- `2bac-content-specification.md`: the official lesson production standard.
- `2bac-roadmap.md`: the 2BAC expansion roadmap for Mathematics, Physics-Chemistry, and Philosophy.
- `quality-gates.md`: mandatory acceptance gates before content enters OQUL.
- `pilot-batch-plan.md`: the first safe pilot plan for 2BAC Mathematics.

## Generation Freeze

No 2BAC generation should begin until these standards are reviewed and accepted.

No lesson content should be written to the database during Phase 58.

No scripts should be created during Phase 58 unless a later phase explicitly requests implementation.

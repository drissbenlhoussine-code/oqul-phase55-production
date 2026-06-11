# Phase 58A Generator Safety

This note documents the safe operating rules for:

```bash
npm run db:generate:2bac-math
```

The generator is for 2BAC Mathematics only. It must not be used for Grade 3, primary school, French, Science, or any non-2BAC scope.

## Default Dry-Run

Default mode is dry-run:

```bash
npm run db:generate:2bac-math
```

Default behavior:

- Processes one pilot lesson only.
- Calls AI unless `--skip-ai` is passed.
- Saves the generated artifact to `.generated-lessons/`.
- Runs Phase 58 QA.
- Prints the planned DB action.
- Does not write to PostgreSQL.

## Static Check Without AI

Use this before any generation:

```bash
npm run db:generate:2bac-math -- --skip-ai --lesson=definition-derivee
```

This mode:

- Does not require `GROQ_API_KEY`.
- Does not require `DATABASE_URL`.
- Does not connect to PostgreSQL.
- Prints the matched lesson definition.
- Verifies catalog safety.

## One-Lesson Dry-Run

Generate one lesson artifact without writing to the database:

```bash
npm run db:generate:2bac-math -- --lesson=definition-derivee
```

Use this for the Phase 58 pilot batch before any database insertion.

## Apply Mode

Database writes require the explicit `--apply` flag:

```bash
npm run db:generate:2bac-math -- --lesson=definition-derivee --apply
```

Even with `--apply`, the generator processes one lesson by default unless `--all` or `--limit=N` is also passed.

## Topic and Limit Selection

Run one topic in dry-run mode:

```bash
npm run db:generate:2bac-math -- --topic=derivation --limit=1
```

Run all catalog lessons in dry-run mode:

```bash
npm run db:generate:2bac-math -- --all
```

Do not use `--all --apply` until several one-lesson pilots have passed QA and human review.

## Stop Conditions

The script must not write if any of these are true:

- `--apply` is missing.
- QA score is below 80.
- Placeholder text is detected.
- BAC section is missing.
- French terminology is missing.
- Exercises lack answers or corrections.
- The lesson is not usable by Leila or Lesson Helper.

## Phase 58 QA Minimums

The generator enforces these minimums:

- Content length: at least 3500 characters.
- Guided examples: at least 3.
- Solved exercises: at least 3.
- Progressive exercises: at least 8.
- Challenge exercises: at least 2.
- Common mistakes: at least 3.
- BAC-style exercise: at least 1.
- French terminology: required.
- Summary: required.
- Leila prompts: required.
- Lesson Helper prompts: required.
- Research prompts: required.
- Remediation and weak-point hints: required.

## Artifact Rule

Every generated lesson is saved to:

```text
.generated-lessons/
```

The artifact includes:

- Lesson slug.
- Topic slug.
- Timestamp.
- Full generated JSON.
- QA result.
- Apply mode.
- DB write result if applied.

Artifacts are for review and traceability. They are not database writes.

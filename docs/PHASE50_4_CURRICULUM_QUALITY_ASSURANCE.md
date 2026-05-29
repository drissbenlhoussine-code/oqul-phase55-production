# Oqul Phase50.4 — Curriculum Quality Assurance

This phase checks the quality of curriculum after Phase50.3 injection.

## What it adds

- Curriculum quality engine
- Quality audit script
- Quality report API
- Dashboard page

## Commands

```powershell
node scripts/audit-curriculum-quality.mjs
```

Then open:

```txt
/dashboard/curriculum-quality
/api/curriculum/quality-report
```

## What it detects

- missing content
- too short lessons
- placeholder text
- missing examples
- missing exercises
- missing common mistakes
- missing remediation
- missing summary
- missing Leila hooks

## Safety

No writes to DB.
No auth changes.
No deletion.
Only reads DB and creates report.
# Oqul Phase54 — Official Alignment + Exam Intelligence

Adds:
- source registry
- competency matrix
- alignment audit
- exam intelligence
- remediation append script
- APIs and dashboards

Commands:

```powershell
node scripts/audit-phase54-official-alignment.mjs
node scripts/apply-phase54-alignment-remediation.mjs
node scripts/apply-phase54-alignment-remediation.mjs --apply
```

Dashboards:
- /dashboard/official-alignment
- /dashboard/exam-intelligence

Safety:
- Audit reads only
- Apply appends alignment blocks only
- No deletion

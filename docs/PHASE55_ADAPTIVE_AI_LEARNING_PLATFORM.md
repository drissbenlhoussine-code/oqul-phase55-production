# Oqul Phase55 — Adaptive AI Learning Platform

Adds:
- Dynamic lesson generation engine
- Personalized learning path engine
- Exam prediction engine
- Intelligence report script
- APIs
- Dashboards

Commands:

```powershell
node scripts/generate-phase55-intelligence-report.mjs
```

APIs:
- POST /api/phase55/dynamic-lesson
- POST /api/phase55/learning-path
- POST /api/phase55/exam-prediction
- GET /api/phase55/intelligence-report

Dashboards:
- /dashboard/phase55
- /dashboard/learning-paths
- /dashboard/exam-prediction

Safety:
- Report script reads only.
- No database mutation.
- No auth changes.

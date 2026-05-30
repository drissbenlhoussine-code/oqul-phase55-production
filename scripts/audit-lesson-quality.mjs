import fs from "node:fs";
import path from "node:path";
import { fetchLessons, parseArgs, scoreLessonQuality, withDb } from "./lib/lesson-quality-tools.mjs";

const args = parseArgs();
const limit = Number(args.limit ?? 100);
const writeReport = Boolean(args["write-report"]);

await withDb(async (client) => {
  const lessons = await fetchLessons(client, {
    grade: args.grade,
    subject: args.subject,
    unit: args.unit,
    title: args.title,
    lessonId: args["lesson-id"],
    limit,
  });

  const rows = lessons.map((lesson) => {
    const quality = scoreLessonQuality(lesson);
    return {
      id: lesson.lesson_id,
      title: lesson.lesson_title,
      grade: lesson.grade_slug ?? lesson.grade_title,
      subject: lesson.subject_slug ?? lesson.subject_title,
      unit: lesson.unit_slug ?? lesson.unit_title,
      exercises: lesson.exercise_count,
      score: quality.score,
      status: quality.status,
      issues: quality.issues,
    };
  });

  const byStatus = rows.reduce((acc, row) => {
    acc[row.status] = (acc[row.status] ?? 0) + 1;
    return acc;
  }, {});

  const report = {
    generatedAt: new Date().toISOString(),
    filters: {
      grade: args.grade ?? null,
      subject: args.subject ?? null,
      unit: args.unit ?? null,
      title: args.title ?? null,
      lessonId: args["lesson-id"] ?? null,
      limit,
    },
    totalLessons: rows.length,
    averageScore: Math.round(rows.reduce((sum, row) => sum + row.score, 0) / Math.max(1, rows.length)),
    byStatus,
    weakestLessons: [...rows].sort((a, b) => a.score - b.score).slice(0, Math.min(25, rows.length)),
    rows,
  };

  console.log("Lesson quality audit");
  console.log({
    totalLessons: report.totalLessons,
    averageScore: report.averageScore,
    byStatus,
  });
  console.table(
    report.weakestLessons.map((row) => ({
      id: row.id,
      title: row.title,
      grade: row.grade,
      subject: row.subject,
      unit: row.unit,
      score: row.score,
      status: row.status,
      issues: row.issues.slice(0, 4).join(", "),
    }))
  );

  if (writeReport) {
    const reportsDir = path.join(process.cwd(), "reports");
    fs.mkdirSync(reportsDir, { recursive: true });
    const reportPath = path.join(reportsDir, "lesson-quality-audit.json");
    fs.writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
    console.log("Report written:", reportPath);
  }
});

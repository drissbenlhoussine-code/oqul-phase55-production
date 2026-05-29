import fs from "node:fs";
import path from "node:path";
import pg from "pg";
import dotenv from "dotenv";

dotenv.config({ path: ".env" });
dotenv.config({ path: ".env.local" });

const { Client } = pg;

if (!process.env.DATABASE_URL) {
  console.error("Missing DATABASE_URL");
  process.exit(1);
}

function evaluate(input) {
  const issues = [];
  const content = input.content ?? "";
  const normalized = content.toLowerCase();

  if (!content.trim()) issues.push("missing_content");
  if (content.trim().length < 900) issues.push("too_short");

  const markers = [
    "يحتاج مطابقة",
    "تمرين 1 سهل",
    "جواب نموذجي مختصر",
    "درس أصلي من oqul مبني على عنوان المنهج فقط",
    "مثال بسيط لفهم"
  ];

  if (markers.some((m) => normalized.includes(m.toLowerCase()))) issues.push("placeholder_text");
  if (!content.includes("## أمثلة") && !content.includes("مثال")) issues.push("missing_examples");
  if ((input.exercisesCount ?? 0) < 6) issues.push("missing_exercises");
  if (!content.includes("أخطاء شائعة")) issues.push("missing_common_mistakes");
  if (!content.includes("العلاج") && !content.includes("Remediation")) issues.push("missing_remediation");
  if (!content.includes("ملخص")) issues.push("missing_summary");
  if (!content.includes("ليلى") && !content.includes("تلميح")) issues.push("missing_leila_hooks");

  const score = Math.max(0, 100 - issues.length * 10);
  let status = "weak";
  if (score >= 90) status = "excellent";
  else if (score >= 75) status = "good";
  else if (score >= 50) status = "needs_review";

  return { score, status, issues };
}

const client = new Client({ connectionString: process.env.DATABASE_URL });
await client.connect();

const lessons = await client.query(`
  select
    l.id,
    l.title,
    g.name as grade,
    s.name as subject,
    u.title as unit,
    lc.content,
    coalesce(ex.exercise_count, 0)::int as exercises_count
  from lessons l
  left join units u on u.id = l.unit_id
  left join subjects s on s.id = u.subject_id
  left join grades g on g.id = s.grade_id
  left join lesson_contents lc on lc.lesson_id = l.id
  left join (
    select lesson_id, count(*) as exercise_count
    from exercises
    group by lesson_id
  ) ex on ex.lesson_id = l.id
  order by g.name, s.name, u.title, l.title
`);

const rows = lessons.rows.map((row) => ({
  id: row.id,
  title: row.title,
  grade: row.grade,
  subject: row.subject,
  unit: row.unit,
  exercisesCount: row.exercises_count,
  ...evaluate({
    title: row.title,
    content: row.content,
    exercisesCount: row.exercises_count,
  }),
}));

const byStatus = {};
const byGrade = {};
const bySubject = {};

for (const row of rows) {
  byStatus[row.status] = (byStatus[row.status] ?? 0) + 1;
  byGrade[row.grade ?? "unknown"] ??= { total: 0, average: 0, scores: [] };
  byGrade[row.grade ?? "unknown"].total++;
  byGrade[row.grade ?? "unknown"].scores.push(row.score);

  bySubject[row.subject ?? "unknown"] ??= { total: 0, average: 0, scores: [] };
  bySubject[row.subject ?? "unknown"].total++;
  bySubject[row.subject ?? "unknown"].scores.push(row.score);
}

for (const bucket of Object.values(byGrade)) {
  bucket.average = Math.round(bucket.scores.reduce((a, b) => a + b, 0) / Math.max(1, bucket.scores.length));
  delete bucket.scores;
}

for (const bucket of Object.values(bySubject)) {
  bucket.average = Math.round(bucket.scores.reduce((a, b) => a + b, 0) / Math.max(1, bucket.scores.length));
  delete bucket.scores;
}

const report = {
  generatedAt: new Date().toISOString(),
  totalLessons: rows.length,
  averageScore: Math.round(rows.reduce((a, b) => a + b.score, 0) / Math.max(1, rows.length)),
  byStatus,
  byGrade,
  bySubject,
  weakestLessons: rows
    .filter((r) => r.status === "weak" || r.status === "needs_review")
    .sort((a, b) => a.score - b.score)
    .slice(0, 100),
  rows,
};

fs.mkdirSync(path.join(process.cwd(), "reports"), { recursive: true });
fs.writeFileSync(path.join(process.cwd(), "reports", "phase50-4-curriculum-quality-report.json"), JSON.stringify(report, null, 2), "utf8");

console.log("✅ Phase50.4 curriculum quality audit completed.");
console.table(byStatus);
console.log("Average score:", report.averageScore);
console.log("Total lessons:", report.totalLessons);
console.log("Report:", "reports/phase50-4-curriculum-quality-report.json");

await client.end();
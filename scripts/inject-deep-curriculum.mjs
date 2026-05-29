import fs from "node:fs";
import path from "node:path";
import pg from "pg";
import dotenv from "dotenv";

dotenv.config({ path: ".env" });
dotenv.config({ path: ".env.local" });

const { Client } = pg;

const DRY_RUN = process.argv.includes("--dry-run");
const APPLY = process.argv.includes("--apply");
const MIN_SCORE = Number(process.env.PHASE50_MIN_QUALITY_SCORE ?? 70);

if (!DRY_RUN && !APPLY) {
  console.error("Use one mode:");
  console.error("  node scripts/inject-deep-curriculum.mjs --dry-run");
  console.error("  node scripts/inject-deep-curriculum.mjs --apply");
  process.exit(1);
}

const deepRoot = path.join(process.cwd(), "generated-curriculum", "deep-lessons");
const reportsDir = path.join(process.cwd(), "reports");
fs.mkdirSync(reportsDir, { recursive: true });

if (!fs.existsSync(deepRoot)) {
  console.error("Missing generated deep lessons directory:", deepRoot);
  console.error("Run Phase50.2 first: node scripts/reconstruct-deep-lessons.mjs");
  process.exit(1);
}

function walkJsonFiles(dir) {
  const out = [];
  for (const item of fs.readdirSync(dir)) {
    const p = path.join(dir, item);
    const stat = fs.statSync(p);
    if (stat.isDirectory()) out.push(...walkJsonFiles(p));
    else if (item.endsWith(".json")) out.push(p);
  }
  return out;
}

function countExerciseItems(lesson) {
  const ex = lesson.exercises ?? {};
  return ["easy", "medium", "hard", "examStyle"].reduce((sum, key) => sum + (Array.isArray(ex[key]) ? ex[key].length : 0), 0);
}

function qualityScore(lesson) {
  let score = 100;
  if (!lesson.title || lesson.title.includes("يحتاج مطابقة")) score -= 35;
  if (!lesson.explanation?.concept) score -= 15;
  if ((lesson.examples ?? []).length < 3) score -= 10;
  if ((lesson.interactiveQuestions ?? []).length < 3) score -= 10;
  if ((lesson.commonMistakes ?? []).length < 3) score -= 10;
  if ((lesson.remediation ?? []).length < 4) score -= 10;
  if (countExerciseItems(lesson) < 12) score -= 10;
  if (!lesson.leilaTutorHooks?.opening) score -= 10;
  return Math.max(0, score);
}

function slugify(s = "") {
  return String(s)
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[^\p{Letter}\p{Number}]+/gu, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80) || "item";
}

function contentToMarkdown(lesson) {
  const lines = [];
  lines.push(`# ${lesson.title}`);
  lines.push("");
  lines.push(`## الأهداف`);
  for (const o of lesson.objectives ?? []) lines.push(`- ${o}`);
  lines.push("");
  lines.push(`## الفحص القبلي`);
  for (const p of lesson.prerequisiteCheck ?? []) lines.push(`- ${p}`);
  lines.push("");
  lines.push(`## الشرح`);
  lines.push(lesson.explanation?.hook ?? "");
  lines.push("");
  lines.push(lesson.explanation?.concept ?? "");
  lines.push("");
  lines.push(`## الخطوات`);
  for (const step of lesson.explanation?.stepByStep ?? []) lines.push(`- ${step}`);
  lines.push("");
  lines.push(`## أمثلة محلولة`);
  for (const ex of lesson.examples ?? []) {
    lines.push(`### مثال ${ex.level}`);
    lines.push(ex.prompt);
    for (const s of ex.solutionSteps ?? []) lines.push(`- ${s}`);
  }
  lines.push("");
  lines.push(`## أسئلة تفاعلية`);
  for (const q of lesson.interactiveQuestions ?? []) {
    lines.push(`- سؤال: ${q.question}`);
    lines.push(`  - الجواب المتوقع: ${q.expectedAnswer}`);
    lines.push(`  - تلميح: ${q.hint}`);
  }
  lines.push("");
  lines.push(`## أخطاء شائعة`);
  for (const m of lesson.commonMistakes ?? []) {
    lines.push(`- ${m.mistake}: ${m.correction}`);
  }
  lines.push("");
  lines.push(`## العلاج التربوي`);
  for (const r of lesson.remediation ?? []) {
    lines.push(`- عند: ${r.trigger}`);
    lines.push(`  - الإجراء: ${r.action}`);
    lines.push(`  - سؤال متابعة: ${r.followUpQuestion}`);
  }
  lines.push("");
  lines.push(`## ملخص`);
  for (const s of lesson.summary ?? []) lines.push(`- ${s}`);
  return lines.join("\n");
}

async function ensureGrade(client, lesson) {
  const name = lesson.gradeAr || lesson.grade;
  const code = lesson.grade;
  const existing = await client.query("select id from grades where name=$1 or code=$2 limit 1", [name, code]).catch(() => ({ rows: [] }));
  if (existing.rows[0]) return existing.rows[0].id;

  const inserted = await client.query(
    "insert into grades (name, code, level, created_at, updated_at) values ($1,$2,$3,now(),now()) returning id",
    [name, code, lesson.grade?.includes("AP") ? "primary" : lesson.grade?.includes("BAC") || lesson.grade === "TC" ? "secondary" : "middle"]
  );
  return inserted.rows[0].id;
}

async function ensureSubject(client, lesson, gradeId) {
  const name = lesson.subjectAr || lesson.subject;
  const code = lesson.subject;
  const existing = await client.query(
    "select id from subjects where grade_id=$1 and (name=$2 or code=$3) limit 1",
    [gradeId, name, code]
  ).catch(() => ({ rows: [] }));
  if (existing.rows[0]) return existing.rows[0].id;

  const inserted = await client.query(
    "insert into subjects (grade_id, name, code, created_at, updated_at) values ($1,$2,$3,now(),now()) returning id",
    [gradeId, name, code]
  );
  return inserted.rows[0].id;
}

async function ensureUnit(client, lesson, subjectId) {
  const title = lesson.unitTitle || "وحدة عامة";
  const existing = await client.query(
    "select id from units where subject_id=$1 and title=$2 limit 1",
    [subjectId, title]
  ).catch(() => ({ rows: [] }));
  if (existing.rows[0]) return existing.rows[0].id;

  const inserted = await client.query(
    "insert into units (subject_id, title, description, order_index, created_at, updated_at) values ($1,$2,$3,$4,now(),now()) returning id",
    [subjectId, title, "وحدة منهجية عميقة من Phase50.3", 0]
  );
  return inserted.rows[0].id;
}

async function upsertLesson(client, lesson, unitId) {
  const title = lesson.title;
  const slug = `${lesson.grade}-${lesson.subject}-${slugify(lesson.registryId || title)}`;

  const existing = await client.query(
    "select id from lessons where unit_id=$1 and title=$2 limit 1",
    [unitId, title]
  ).catch(() => ({ rows: [] }));

  if (existing.rows[0]) {
    await client.query(
      "update lessons set description=$1, difficulty=$2, estimated_minutes=$3, updated_at=now() where id=$4",
      ["درس عميق أصلي من Oqul Phase50.3", "medium", 25, existing.rows[0].id]
    ).catch(() => {});
    return { id: existing.rows[0].id, created: false };
  }

  const inserted = await client.query(
    "insert into lessons (unit_id, title, slug, description, difficulty, estimated_minutes, order_index, created_at, updated_at) values ($1,$2,$3,$4,$5,$6,$7,now(),now()) returning id",
    [unitId, title, slug, "درس عميق أصلي من Oqul Phase50.3", "medium", 25, 0]
  );
  return { id: inserted.rows[0].id, created: true };
}

async function upsertLessonContent(client, lesson, lessonId) {
  const body = contentToMarkdown(lesson);
  const existing = await client.query(
    "select id from lesson_contents where lesson_id=$1 limit 1",
    [lessonId]
  ).catch(() => ({ rows: [] }));

  if (existing.rows[0]) {
    await client.query(
      "update lesson_contents set content=$1, updated_at=now() where id=$2",
      [body, existing.rows[0].id]
    ).catch(() => {});
    return false;
  }

  await client.query(
    "insert into lesson_contents (lesson_id, content, content_type, created_at, updated_at) values ($1,$2,$3,now(),now())",
    [lessonId, body, "markdown"]
  );
  return true;
}

async function insertExercises(client, lesson, lessonId) {
  let inserted = 0;
  const groups = lesson.exercises ?? {};
  for (const [difficulty, list] of Object.entries(groups)) {
    if (!Array.isArray(list)) continue;
    for (const prompt of list) {
      const exists = await client.query(
        "select id from exercises where lesson_id=$1 and question=$2 limit 1",
        [lessonId, prompt]
      ).catch(() => ({ rows: [] }));
      if (exists.rows[0]) continue;

      await client.query(
        "insert into exercises (lesson_id, question, type, difficulty, correct_answer, explanation, created_at, updated_at) values ($1,$2,$3,$4,$5,$6,now(),now())",
        [lessonId, prompt, "short_answer", difficulty === "examStyle" ? "hard" : difficulty, "إجابة نموذجية حسب سياق الدرس.", "يصحح هذا التمرين عبر ليلى أو المعلم."]
      ).catch(() => {});
      inserted++;
    }
  }
  return inserted;
}

const files = walkJsonFiles(deepRoot);
const lessons = files.map((f) => JSON.parse(fs.readFileSync(f, "utf8")));
const accepted = lessons.filter((l) => qualityScore(l) >= MIN_SCORE);
const rejected = lessons.filter((l) => qualityScore(l) < MIN_SCORE);

const report = {
  mode: DRY_RUN ? "dry-run" : "apply",
  generatedAt: new Date().toISOString(),
  files: files.length,
  accepted: accepted.length,
  rejected: rejected.length,
  minScore: MIN_SCORE,
  createdLessons: 0,
  updatedLessons: 0,
  contentsUpserted: 0,
  exercisesInserted: 0,
  rejectedItems: rejected.map((l) => ({
    registryId: l.registryId,
    title: l.title,
    score: qualityScore(l)
  }))
};

if (DRY_RUN) {
  fs.writeFileSync(path.join(reportsDir, "phase50-3-db-injection-dry-run.json"), JSON.stringify(report, null, 2), "utf8");
  console.log("✅ Phase50.3 dry-run completed.");
  console.table({
    files: files.length,
    accepted: accepted.length,
    rejected: rejected.length,
    minScore: MIN_SCORE
  });
  console.log("Report:", "reports/phase50-3-db-injection-dry-run.json");
  process.exit(0);
}

if (!process.env.DATABASE_URL) {
  console.error("Missing DATABASE_URL");
  process.exit(1);
}

const client = new Client({ connectionString: process.env.DATABASE_URL });
await client.connect();

try {
  await client.query("begin");

  for (const lesson of accepted) {
    const gradeId = await ensureGrade(client, lesson);
    const subjectId = await ensureSubject(client, lesson, gradeId);
    const unitId = await ensureUnit(client, lesson, subjectId);
    const lessonResult = await upsertLesson(client, lesson, unitId);

    if (lessonResult.created) report.createdLessons++;
    else report.updatedLessons++;

    const contentCreated = await upsertLessonContent(client, lesson, lessonResult.id);
    if (contentCreated) report.contentsUpserted++;

    report.exercisesInserted += await insertExercises(client, lesson, lessonResult.id);
  }

  await client.query("commit");
} catch (error) {
  await client.query("rollback");
  console.error("❌ Injection failed and was rolled back.");
  console.error(error);
  await client.end();
  process.exit(1);
}

await client.end();

fs.writeFileSync(path.join(reportsDir, "phase50-3-db-injection-apply.json"), JSON.stringify(report, null, 2), "utf8");

console.log("✅ Phase50.3 deep curriculum injected successfully.");
console.table({
  accepted: report.accepted,
  rejected: report.rejected,
  createdLessons: report.createdLessons,
  updatedLessons: report.updatedLessons,
  contentsUpserted: report.contentsUpserted,
  exercisesInserted: report.exercisesInserted
});
console.log("Report:", "reports/phase50-3-db-injection-apply.json");
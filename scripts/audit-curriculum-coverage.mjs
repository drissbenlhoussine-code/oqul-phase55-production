import fs from "node:fs";
import path from "node:path";
import pg from "pg";
import dotenv from "dotenv";

dotenv.config({ path: ".env" });
dotenv.config({ path: ".env.local" });

const { Client } = pg;

const registryPath = path.join(process.cwd(), "curriculum-registry", "official-curriculum-registry.scaffold.json");

if (!fs.existsSync(registryPath)) {
  console.error("Missing registry:", registryPath);
  process.exit(1);
}

const registry = JSON.parse(fs.readFileSync(registryPath, "utf8"));

function normalize(s = "") {
  return String(s)
    .toLowerCase()
    .replace(/[أإآ]/g, "ا")
    .replace(/[ة]/g, "ه")
    .replace(/[ى]/g, "ي")
    .replace(/\s+/g, " ")
    .trim();
}

const client = new Client({ connectionString: process.env.DATABASE_URL });

await client.connect();

const lessonsRes = await client.query(`
  select
    l.id,
    l.title as lesson_title,
    g.name as grade_name,
    s.name as subject_name,
    u.title as unit_title
  from lessons l
  left join units u on u.id = l.unit_id
  left join subjects s on s.id = u.subject_id
  left join grades g on g.id = s.grade_id
`);

const dbLessons = lessonsRes.rows;

const coverage = [];
let matched = 0;

for (const item of registry) {
  const gradeNeedle = normalize(item.gradeAr + " " + item.grade);
  const subjectNeedle = normalize(item.subjectAr + " " + item.subject);
  const titleNeedle = normalize(item.lessonTitle);

  const found = dbLessons.find((l) => {
    const hay = normalize(`${l.grade_name ?? ""} ${l.subject_name ?? ""} ${l.unit_title ?? ""} ${l.lesson_title ?? ""}`);
    const gradeOk = hay.includes(normalize(item.gradeAr)) || hay.includes(normalize(item.grade));
    const subjectOk = hay.includes(normalize(item.subjectAr)) || hay.includes(normalize(item.subject));
    const titleOk = item.verificationStatus === "verified" ? hay.includes(titleNeedle) : false;
    return gradeOk && subjectOk && titleOk;
  });

  if (found) matched++;

  coverage.push({
    registryId: item.registryId,
    stage: item.stage,
    grade: item.grade,
    gradeAr: item.gradeAr,
    subject: item.subject,
    subjectAr: item.subjectAr,
    lessonTitle: item.lessonTitle,
    verificationStatus: item.verificationStatus,
    existsInDb: Boolean(found),
    dbLessonId: found?.id ?? null
  });
}

const byStage = {};
for (const row of coverage) {
  byStage[row.stage] ??= { total: 0, existsInDb: 0, missing: 0 };
  byStage[row.stage].total++;
  if (row.existsInDb) byStage[row.stage].existsInDb++;
  else byStage[row.stage].missing++;
}

const report = {
  generatedAt: new Date().toISOString(),
  registryItems: registry.length,
  databaseLessons: dbLessons.length,
  matched,
  byStage,
  warning: "This is Phase50.1 mapping scaffold. Items marked needs_official_title_verification must be replaced by verified TelmidTICE titles before deep lesson generation.",
  nextStep: "Run scripts/import-official-curriculum-titles.mjs after filling curriculum-registry/verified-official-curriculum.json"
};

fs.mkdirSync(path.join(process.cwd(), "reports"), { recursive: true });
fs.writeFileSync(path.join(process.cwd(), "reports", "phase50-curriculum-coverage.json"), JSON.stringify({ report, coverage }, null, 2), "utf8");

console.log("✅ Phase50.1 curriculum coverage audit completed.");
console.table(byStage);
console.log("Registry items:", registry.length);
console.log("DB lessons:", dbLessons.length);
console.log("Report:", "reports/phase50-curriculum-coverage.json");

await client.end();
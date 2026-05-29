/**
 * OQUL Safe Seed — idempotent Moroccan curriculum seed.
 * Runs safely after partial/failed seeds and fills lessons so the app is usable.
 */
import fs from "node:fs";
import path from "node:path";
import postgres from "postgres";
import { hashSync } from "bcryptjs";

function loadEnvFile(file: string) {
  const full = path.resolve(process.cwd(), file);
  if (!fs.existsSync(full)) return;
  for (const line of fs.readFileSync(full, "utf8").split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#") || !trimmed.includes("=")) continue;
    const [key, ...rest] = trimmed.split("=");
    if (!process.env[key]) {
      process.env[key] = rest.join("=").trim().replace(/^['\"]|['\"]$/g, "");
    }
  }
}

loadEnvFile(".env.local");
loadEnvFile(".env");

const url = process.env.DATABASE_URL;
if (!url) throw new Error("DATABASE_URL required");

const sql = postgres(url, { ssl: url.includes("localhost") ? false : "require" });

type Row = { id: string };

async function one<T = Row>(rows: T[]): Promise<T> {
  if (!rows[0]) throw new Error("Seed query returned no rows");
  return rows[0];
}

async function upsertCycle(slug: "primary" | "middle" | "high", titleAr: string, titleFr: string, orderIndex: number) {
  return one(await sql<Row[]>`
    insert into cycles (slug, title_ar, title_fr, order_index, is_active)
    values (${slug}, ${titleAr}, ${titleFr}, ${orderIndex}, true)
    on conflict (slug) do update set title_ar=excluded.title_ar, title_fr=excluded.title_fr, order_index=excluded.order_index, is_active=true
    returning id
  `);
}

async function upsertGrade(cycleId: string, slug: string, titleAr: string, orderIndex: number, ageMin: number, ageMax: number, color: string) {
  return one(await sql<Row[]>`
    insert into grades (cycle_id, slug, title_ar, order_index, age_min, age_max, color, is_active)
    values (${cycleId}, ${slug}, ${titleAr}, ${orderIndex}, ${ageMin}, ${ageMax}, ${color}, true)
    on conflict (slug) do update set title_ar=excluded.title_ar, order_index=excluded.order_index, age_min=excluded.age_min, age_max=excluded.age_max, color=excluded.color, is_active=true
    returning id
  `);
}

async function upsertSubject(gradeId: string, slug: string, titleAr: string, icon: string, color: string, orderIndex: number) {
  return one(await sql<Row[]>`
    insert into subjects (grade_id, slug, title_ar, icon, color, order_index, is_active)
    values (${gradeId}, ${slug}, ${titleAr}, ${icon}, ${color}, ${orderIndex}, true)
    on conflict (grade_id, slug) do update set title_ar=excluded.title_ar, icon=excluded.icon, color=excluded.color, order_index=excluded.order_index, is_active=true
    returning id
  `);
}

async function upsertUnit(subjectId: string, slug: string, titleAr: string, orderIndex: number) {
  return one(await sql<Row[]>`
    insert into units (subject_id, slug, title_ar, order_index, is_published)
    values (${subjectId}, ${slug}, ${titleAr}, ${orderIndex}, true)
    on conflict (subject_id, slug) do update set title_ar=excluded.title_ar, order_index=excluded.order_index, is_published=true
    returning id
  `);
}

async function upsertLesson(unitId: string, slug: string, titleAr: string, objectives: string[], difficulty: "easy" | "medium" | "hard", orderIndex: number) {
  return one(await sql<Row[]>`
    insert into lessons (unit_id, slug, title_ar, objectives, difficulty, estimated_duration_minutes, order_index, is_published)
    values (${unitId}, ${slug}, ${titleAr}, ${JSON.stringify(objectives)}::jsonb, ${difficulty}, 20, ${orderIndex}, true)
    on conflict (unit_id, slug) do update set title_ar=excluded.title_ar, objectives=excluded.objectives, difficulty=excluded.difficulty, order_index=excluded.order_index, is_published=true
    returning id
  `);
}

async function upsertContent(lessonId: string, explanation: string, summary: string) {
  await sql`
    insert into lesson_contents (lesson_id, explanation, vocabulary, examples, summary)
    values (
      ${lessonId},
      ${explanation},
      ${JSON.stringify([{ word: "فكرة", definition: "المعلومة الأساسية في الدرس" }])}::jsonb,
      ${JSON.stringify([{ text: "مثال من الحياة اليومية المغربية", note: "ليلى تستعمل أمثلة قريبة من الطفل" }])}::jsonb,
      ${summary}
    )
    on conflict (lesson_id) do update set explanation=excluded.explanation, vocabulary=excluded.vocabulary, examples=excluded.examples, summary=excluded.summary
  `;
}

async function resetExercises(lessonId: string, titleAr: string) {
  await sql`delete from exercises where lesson_id = ${lessonId}`;
  await sql`
    insert into exercises (lesson_id, type, question, options, correct_answer, explanation, order_index, points)
    values
      (${lessonId}, 'mcq', ${`ما الفكرة الأساسية في درس ${titleAr}؟`}, ${JSON.stringify(["فهم القاعدة", "حفظ الاسم فقط", "تخمين الجواب", "ترك الدرس"])}::jsonb, 'فهم القاعدة', 'الهدف هو الفهم والتطبيق، وليس الحفظ فقط.', 1, 10),
      (${lessonId}, 'true_false', ${`يمكن تطبيق درس ${titleAr} بأمثلة من الحياة اليومية.`}, ${JSON.stringify(["صحيح", "خطأ"])}::jsonb, 'صحيح', 'ليلى تقرّب الدروس بأمثلة من البيت والمدرسة والسوق.', 2, 10)
  `;
}

async function seedSubjectLesson(gradeId: string, subject: { slug: string; title: string; icon: string; color: string; order: number }, gradeLabel: string) {
  const subjectRow = await upsertSubject(gradeId, subject.slug, subject.title, subject.icon, subject.color, subject.order);
  const unit = await upsertUnit(subjectRow.id, "starter", `مدخل إلى ${subject.title}`, 1);
  const lessonTitle = `${subject.title} — درس البداية (${gradeLabel})`;
  const lesson = await upsertLesson(unit.id, "starter-lesson", lessonTitle, ["فهم الفكرة الأساسية", "حل تدريب بسيط", "ربط الدرس بالحياة اليومية"], "easy", 1);
  await upsertContent(
    lesson.id,
    `هذا درس تمهيدي في ${subject.title} مخصص لـ ${gradeLabel}.\n\nليلى تشرح الدرس بخطوات قصيرة وبالدارجة المغربية، ثم تعطي مثالاً قريباً من الطفل، ثم تدريباً صغيراً للتأكد من الفهم.\n\nمثال: نأخذ موقفاً من البيت أو المدرسة ونربطه بالمعلومة حتى يصبح الدرس واضحاً وسهل التطبيق.`,
    `خلاصة ${lessonTitle}: نفهم الفكرة، نرى مثالاً، ثم نطبق بتدريب قصير.`
  );
  await resetExercises(lesson.id, lessonTitle);
}

async function main() {
  console.log("🌱 Seeding OQUL database safely...");

  const primary = await upsertCycle("primary", "التعليم الابتدائي", "Primaire", 1);
  const middle = await upsertCycle("middle", "التعليم الإعدادي", "Collège", 2);
  const high = await upsertCycle("high", "التعليم الثانوي", "Lycée", 3);

  const primaryGrades = [
    ["1ap", "السنة الأولى ابتدائي", 1, 6, 7, "#10b981"],
    ["2ap", "السنة الثانية ابتدائي", 2, 7, 8, "#059669"],
    ["3ap", "السنة الثالثة ابتدائي", 3, 8, 9, "#047857"],
    ["4ap", "السنة الرابعة ابتدائي", 4, 9, 10, "#065f46"],
    ["5ap", "السنة الخامسة ابتدائي", 5, 10, 11, "#064e3b"],
    ["6ap", "السنة السادسة ابتدائي", 6, 11, 12, "#022c22"],
  ] as const;

  const subjects = [
    { slug: "arabic", title: "اللغة العربية", icon: "BookOpen", color: "#059669", order: 1 },
    { slug: "math", title: "الرياضيات", icon: "Calculator", color: "#2563eb", order: 2 },
    { slug: "french", title: "اللغة الفرنسية", icon: "Globe", color: "#7c3aed", order: 3 },
    { slug: "science", title: "النشاط العلمي", icon: "Microscope", color: "#0891b2", order: 4 },
    { slug: "islamic", title: "التربية الإسلامية", icon: "Star", color: "#d97706", order: 5 },
    { slug: "social", title: "التربية المدنية", icon: "Users", color: "#db2777", order: 6 },
  ];

  let firstGradeId = "";
  for (const [slug, title, order, ageMin, ageMax, color] of primaryGrades) {
    const grade = await upsertGrade(primary.id, slug, title, order, ageMin, ageMax, color);
    if (slug === "1ap") firstGradeId = grade.id;
    for (const subject of subjects) {
      await seedSubjectLesson(grade.id, subject, title);
    }
  }

  // Keep higher cycles visible in the app, with basic grades ready for expansion.
  await upsertGrade(middle.id, "1ac", "السنة الأولى إعدادي", 1, 12, 13, "#2563eb");
  await upsertGrade(middle.id, "2ac", "السنة الثانية إعدادي", 2, 13, 14, "#1d4ed8");
  await upsertGrade(middle.id, "3ac", "السنة الثالثة إعدادي", 3, 14, 15, "#1e40af");
  await upsertGrade(high.id, "tc", "الجذع المشترك", 1, 15, 16, "#7c3aed");
  await upsertGrade(high.id, "bac1", "أولى باكالوريا", 2, 16, 17, "#6d28d9");
  await upsertGrade(high.id, "bac2", "ثانية باكالوريا", 3, 17, 18, "#5b21b6");

  await sql`
    insert into badges (slug, title_ar, description, icon, xp_reward, condition)
    values
      ('first-lesson','أول درس','أكمل أول درس','🌟',50,'complete_first_lesson'),
      ('perfect-quiz','علامة كاملة','احصل على نتيجة كاملة','💯',100,'quiz_score_100'),
      ('streak-3','3 أيام متتالية','ادرس 3 أيام متتالية','🔥',75,'streak_3'),
      ('leila-friend','صديق ليلى','أول محادثة مع ليلى','🤖',50,'first_ai_chat')
    on conflict (slug) do update set title_ar=excluded.title_ar, description=excluded.description, icon=excluded.icon, xp_reward=excluded.xp_reward, condition=excluded.condition
  `;

  const passwordHash = hashSync("demo1234", 10);
  const demoUser = await one(await sql<Row[]>`
    insert into users (full_name, email, password_hash, plan, locale, email_verified, terms_accepted_at, trial_ends_at)
    values ('سارة المغربية', 'demo@oqul.ma', ${passwordHash}, 'free', 'ar-MA', true, now(), now() + interval '7 days')
    on conflict (email) do update set full_name=excluded.full_name, password_hash=excluded.password_hash, email_verified=true, updated_at=now()
    returning id
  `);

  await sql`
    insert into children (user_id, name, grade_id, xp, streak)
    values (${demoUser.id}, 'يوسف', ${firstGradeId}, 420, 7)
    on conflict do nothing
  `;

  const counts = await sql<{ table_name: string; count: string }[]>`
    select 'grades' as table_name, count(*)::text from grades
    union all select 'subjects', count(*)::text from subjects
    union all select 'lessons', count(*)::text from lessons
    union all select 'lesson_contents', count(*)::text from lesson_contents
    union all select 'exercises', count(*)::text from exercises
  `;
  console.table(counts);
  console.log("✅ OQUL database seeded successfully.");
}

main()
  .catch((error) => {
    console.error("❌ Seed failed:", error);
    process.exitCode = 1;
  })
  .finally(async () => {
    await sql.end();
  });

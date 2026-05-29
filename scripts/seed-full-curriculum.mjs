import fs from "node:fs";
import path from "node:path";
import postgres from "postgres";

function loadEnvFile(file) {
  const full = path.resolve(process.cwd(), file);
  if (!fs.existsSync(full)) return;
  for (const line of fs.readFileSync(full, "utf8").split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#") || !trimmed.includes("=")) continue;
    const [key, ...rest] = trimmed.split("=");
    if (!process.env[key]) process.env[key] = rest.join("=").trim().replace(/^[ '\"]|[ '\"]$/g, "");
  }
}

loadEnvFile(".env.local");
loadEnvFile(".env");

const url = process.env.DATABASE_URL;
if (!url) throw new Error("DATABASE_URL is required in .env or .env.local");

const sql = postgres(url, { ssl: url.includes("localhost") ? false : "require" });

async function one(rows, label = "query") {
  if (!rows?.[0]) throw new Error(`${label} returned no rows`);
  return rows[0];
}

function slugify(input) {
  return String(input)
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 110) || "item";
}

async function upsertCycle(slug, titleAr, titleFr, orderIndex) {
  return one(await sql`
    insert into cycles (slug, title_ar, title_fr, order_index, is_active)
    values (${slug}, ${titleAr}, ${titleFr}, ${orderIndex}, true)
    on conflict (slug) do update set
      title_ar=excluded.title_ar,
      title_fr=excluded.title_fr,
      order_index=excluded.order_index,
      is_active=true
    returning id
  `, "cycle");
}

async function upsertGrade(cycleId, slug, titleAr, orderIndex, ageMin, ageMax, color) {
  return one(await sql`
    insert into grades (cycle_id, slug, title_ar, order_index, age_min, age_max, color, is_active)
    values (${cycleId}, ${slug}, ${titleAr}, ${orderIndex}, ${ageMin}, ${ageMax}, ${color}, true)
    on conflict (slug) do update set
      cycle_id=excluded.cycle_id,
      title_ar=excluded.title_ar,
      order_index=excluded.order_index,
      age_min=excluded.age_min,
      age_max=excluded.age_max,
      color=excluded.color,
      is_active=true
    returning id
  `, "grade");
}

async function upsertSubject(gradeId, slug, titleAr, icon, color, orderIndex) {
  return one(await sql`
    insert into subjects (grade_id, slug, title_ar, icon, color, order_index, is_active)
    values (${gradeId}, ${slug}, ${titleAr}, ${icon}, ${color}, ${orderIndex}, true)
    on conflict (grade_id, slug) do update set
      title_ar=excluded.title_ar,
      icon=excluded.icon,
      color=excluded.color,
      order_index=excluded.order_index,
      is_active=true
    returning id
  `, "subject");
}

async function upsertUnit(subjectId, slug, titleAr, orderIndex) {
  return one(await sql`
    insert into units (subject_id, slug, title_ar, order_index, is_published)
    values (${subjectId}, ${slug}, ${titleAr}, ${orderIndex}, true)
    on conflict (subject_id, slug) do update set
      title_ar=excluded.title_ar,
      order_index=excluded.order_index,
      is_published=true
    returning id
  `, "unit");
}

async function upsertLesson(unitId, slug, titleAr, objectives, difficulty, minutes, orderIndex) {
  return one(await sql`
    insert into lessons (unit_id, slug, title_ar, objectives, difficulty, estimated_duration_minutes, order_index, is_published)
    values (${unitId}, ${slug}, ${titleAr}, ${JSON.stringify(objectives)}::jsonb, ${difficulty}, ${minutes}, ${orderIndex}, true)
    on conflict (unit_id, slug) do update set
      title_ar=excluded.title_ar,
      objectives=excluded.objectives,
      difficulty=excluded.difficulty,
      estimated_duration_minutes=excluded.estimated_duration_minutes,
      order_index=excluded.order_index,
      is_published=true
    returning id
  `, "lesson");
}

async function upsertContent(lessonId, explanation, examples, summary) {
  await sql`
    insert into lesson_contents (lesson_id, explanation, vocabulary, examples, summary)
    values (
      ${lessonId},
      ${explanation},
      ${JSON.stringify([
        { word: "الكفاية", definition: "قدرة المتعلم على استعمال ما تعلّمه في وضعية جديدة" },
        { word: "التطبيق", definition: "استعمال القاعدة في تمرين أو موقف" }
      ])}::jsonb,
      ${JSON.stringify(examples)}::jsonb,
      ${summary}
    )
    on conflict (lesson_id) do update set
      explanation=excluded.explanation,
      vocabulary=excluded.vocabulary,
      examples=excluded.examples,
      summary=excluded.summary
  `;
}

async function resetExercises(lessonId, titleAr, layer) {
  await sql`delete from exercises where lesson_id = ${lessonId}`;
  const prefix = layer === "primary" ? "اختر الجواب المناسب" : layer === "high" ? "حلل السؤال ثم اختر" : "فكر ثم أجب";
  await sql`
    insert into exercises (lesson_id, type, question, options, correct_answer, explanation, order_index, points)
    values
      (${lessonId}, 'mcq', ${`${prefix}: ما الهدف الأساسي من درس ${titleAr}؟`}, ${JSON.stringify(["الفهم والتطبيق", "حفظ العنوان فقط", "تخمين الجواب", "تجاوز الدرس"])}::jsonb, 'الفهم والتطبيق', 'الدرس يهدف إلى الفهم ثم التطبيق التدريجي.', 1, 10),
      (${lessonId}, 'true_false', ${`في درس ${titleAr} يجب تبرير الجواب وليس اختيار النتيجة فقط.`}, ${JSON.stringify(["صحيح", "خطأ"])}::jsonb, 'صحيح', 'التبرير يساعد ليلى على معرفة طريقة تفكير المتعلم.', 2, 10),
      (${lessonId}, 'short_answer', ${`اكتب خطوة واحدة تساعدك على فهم ${titleAr}.`}, null, 'شرح الفكرة أو إعطاء مثال أو حل تمرين قصير', 'أي إجابة توضّح الفهم أو المثال أو التطبيق تعتبر بداية صحيحة.', 3, 10)
  `;
}

const primarySubjects = [
  { slug: "arabic", title: "اللغة العربية", icon: "BookOpen", color: "#059669", units: ["القراءة", "التراكيب", "الصرف والتحويل", "الإملاء", "التعبير الكتابي", "الاستماع والتحدث"] },
  { slug: "math", title: "الرياضيات", icon: "Calculator", color: "#2563eb", units: ["الأعداد", "العمليات", "الهندسة", "القياس", "المسائل", "تنظيم البيانات"] },
  { slug: "french", title: "اللغة الفرنسية", icon: "Globe", color: "#7c3aed", units: ["lecture", "grammaire", "conjugaison", "orthographe", "vocabulaire", "production"] },
  { slug: "science", title: "النشاط العلمي", icon: "Microscope", color: "#0891b2", units: ["الجسم والصحة", "النبات والحيوان", "المادة", "الطاقة", "البيئة", "الأرض والفضاء"] },
  { slug: "islamic", title: "التربية الإسلامية", icon: "Star", color: "#d97706", units: ["القرآن الكريم", "العقيدة", "العبادات", "السيرة", "الأخلاق", "الآداب"] },
  { slug: "social", title: "التربية المدنية", icon: "Users", color: "#db2777", units: ["الأسرة والمدرسة", "الحقوق والواجبات", "المواطنة", "السلامة", "البيئة", "التعاون"] }
];

const middleSubjects = [
  { slug: "math", title: "الرياضيات", icon: "Calculator", color: "#2563eb", units: ["الأعداد والعمليات", "الكسور", "المعادلات", "الهندسة", "التناسبية", "الإحصاء"] },
  { slug: "physics", title: "الفيزياء والكيمياء", icon: "Atom", color: "#dc2626", units: ["المادة", "الكهرباء", "الحركة", "القوى", "الضوء", "التفاعلات"] },
  { slug: "svt", title: "علوم الحياة والأرض", icon: "Leaf", color: "#16a34a", units: ["الخلية", "التغذية", "التنفس", "البيئة", "الجيولوجيا", "جسم الإنسان"] },
  { slug: "arabic", title: "اللغة العربية", icon: "BookOpen", color: "#059669", units: ["النصوص", "القواعد", "الصرف", "التعبير", "البلاغة", "القراءة المنهجية"] },
  { slug: "french", title: "اللغة الفرنسية", icon: "Globe", color: "#7c3aed", units: ["lecture", "grammaire", "conjugaison", "communication", "production", "vocabulaire"] },
  { slug: "social", title: "الاجتماعيات", icon: "Map", color: "#f97316", units: ["التاريخ", "الجغرافيا", "التربية على المواطنة", "المجال المغربي", "السكان", "الموارد"] }
];

const highSubjects = [
  { slug: "advanced-math", title: "الرياضيات", icon: "Calculator", color: "#2563eb", units: ["المجموعات والمنطق", "المعادلات", "الدوال", "النهايات", "الاشتقاق", "المتتاليات", "الهندسة", "الاحتمالات"] },
  { slug: "physics-chemistry", title: "الفيزياء والكيمياء", icon: "Atom", color: "#dc2626", units: ["الحركة", "القوى", "الطاقة", "الكهرباء", "الموجات", "البنية المادية", "التفاعلات", "الكيمياء العضوية"] },
  { slug: "svt", title: "علوم الحياة والأرض", icon: "Leaf", color: "#16a34a", units: ["الوراثة", "المناعة", "التوالد", "الجهاز العصبي", "الجيولوجيا", "التطور", "البيئة", "الاستقلاب"] },
  { slug: "arabic", title: "اللغة العربية", icon: "BookOpen", color: "#059669", units: ["النصوص", "اللغة", "البلاغة", "المؤلفات", "التعبير", "النقد", "المنهجية", "الكتابة"] },
  { slug: "french", title: "اللغة الفرنسية", icon: "Globe", color: "#7c3aed", units: ["lecture", "grammaire", "conjugaison", "argumentation", "roman", "theatre", "poesie", "production"] },
  { slug: "philosophy", title: "الفلسفة", icon: "Brain", color: "#9333ea", units: ["الشخص", "الغير", "الحقيقة", "الحرية", "الواجب", "العدالة", "الدولة", "الأخلاق"] },
  { slug: "english", title: "اللغة الإنجليزية", icon: "Languages", color: "#0ea5e9", units: ["reading", "grammar", "vocabulary", "writing", "communication", "functions", "exam practice", "projects"] },
  { slug: "islamic", title: "التربية الإسلامية", icon: "Star", color: "#d97706", units: ["القرآن والحديث", "الإيمان", "العبادات", "الأخلاق", "الأسرة", "المعاملات", "المجتمع", "القيم"] },
  { slug: "history-geography", title: "التاريخ والجغرافيا", icon: "Map", color: "#f97316", units: ["تاريخ المغرب", "العالم المعاصر", "المجال", "السكان", "التنمية", "الموارد", "العولمة", "المخاطر"] }
];

async function seedLayer({ cycleSlug, cycleTitle, cycleFr, cycleOrder, grades, subjects, layer }) {
  const cycle = await upsertCycle(cycleSlug, cycleTitle, cycleFr, cycleOrder);
  let count = 0;

  for (const grade of grades) {
    const gradeRow = await upsertGrade(cycle.id, grade.slug, grade.title, grade.order, grade.ageMin, grade.ageMax, grade.color);

    for (let s = 0; s < subjects.length; s++) {
      const subject = subjects[s];
      const subjectRow = await upsertSubject(gradeRow.id, subject.slug, subject.title, subject.icon, subject.color, s + 1);

      for (let u = 0; u < subject.units.length; u++) {
        const unitTitle = subject.units[u];
        const unitRow = await upsertUnit(subjectRow.id, slugify(unitTitle), unitTitle, u + 1);

        const lessonParts = layer === "primary"
          ? ["أفهم", "أتمرن", "أطبق", "أراجع"]
          : layer === "high"
            ? ["المفهوم", "مثال محلول", "تطبيق موجه", "سؤال امتحاني"]
            : ["شرح", "مثال", "تمرين", "تثبيت"];

        for (let l = 0; l < lessonParts.length; l++) {
          const lessonTitle = `${unitTitle} — ${lessonParts[l]} (${grade.title})`;
          const lesson = await upsertLesson(
            unitRow.id,
            `${slugify(unitTitle)}-${l + 1}`,
            lessonTitle,
            [
              `فهم ${unitTitle}`,
              `تطبيق ${unitTitle} في وضعية مناسبة`,
              layer === "high" ? "الاستعداد لسؤال امتحاني" : "حل تمرين قصير مع ليلى"
            ],
            l < 2 ? "easy" : l === 2 ? "medium" : "hard",
            layer === "primary" ? 12 : layer === "high" ? 30 : 20,
            l + 1
          );

          await upsertContent(
            lesson.id,
            `هذا درس في ${subject.title} لمستوى ${grade.title}.\n\nالمحور: ${unitTitle}.\n\nتشرح ليلى الفكرة خطوة بخطوة، ثم تقدم مثالًا واضحًا، ثم تمرينًا قصيرًا. إذا أخطأ المتعلم، لا تعطيه الجواب مباشرة، بل تعطي تلميحًا وتعود إلى الفكرة الأساسية.`,
            [
              { text: `مثال مبسط حول ${unitTitle}`, note: "يستعمل لتقريب الفكرة" },
              { text: layer === "high" ? "مثال بأسلوب فرض أو امتحان" : "مثال من الحياة اليومية", note: "يربط الدرس بالتطبيق" }
            ],
            `خلاصة الدرس: نفهم ${unitTitle}، نرى مثالًا، ثم نطبقه بتدرج حتى نصل إلى الإتقان.`
          );

          await resetExercises(lesson.id, lessonTitle, layer);
          count++;
        }
      }
    }
  }

  return count;
}

async function main() {
  console.log("🌱 Seeding full Oqul curriculum into database...");

  const primaryCount = await seedLayer({
    cycleSlug: "primary",
    cycleTitle: "التعليم الابتدائي",
    cycleFr: "Primaire",
    cycleOrder: 1,
    layer: "primary",
    grades: [
      { slug: "1ap", title: "السنة الأولى ابتدائي", order: 1, ageMin: 6, ageMax: 7, color: "#10b981" },
      { slug: "2ap", title: "السنة الثانية ابتدائي", order: 2, ageMin: 7, ageMax: 8, color: "#059669" },
      { slug: "3ap", title: "السنة الثالثة ابتدائي", order: 3, ageMin: 8, ageMax: 9, color: "#047857" },
      { slug: "4ap", title: "السنة الرابعة ابتدائي", order: 4, ageMin: 9, ageMax: 10, color: "#065f46" },
      { slug: "5ap", title: "السنة الخامسة ابتدائي", order: 5, ageMin: 10, ageMax: 11, color: "#064e3b" },
      { slug: "6ap", title: "السنة السادسة ابتدائي", order: 6, ageMin: 11, ageMax: 12, color: "#022c22" }
    ],
    subjects: primarySubjects
  });

  const middleCount = await seedLayer({
    cycleSlug: "middle",
    cycleTitle: "التعليم الإعدادي",
    cycleFr: "Collège",
    cycleOrder: 2,
    layer: "middle",
    grades: [
      { slug: "1ac", title: "السنة الأولى إعدادي", order: 1, ageMin: 12, ageMax: 13, color: "#2563eb" },
      { slug: "2ac", title: "السنة الثانية إعدادي", order: 2, ageMin: 13, ageMax: 14, color: "#1d4ed8" },
      { slug: "3ac", title: "السنة الثالثة إعدادي", order: 3, ageMin: 14, ageMax: 15, color: "#1e40af" }
    ],
    subjects: middleSubjects
  });

  const highCount = await seedLayer({
    cycleSlug: "high",
    cycleTitle: "التعليم الثانوي",
    cycleFr: "Lycée",
    cycleOrder: 3,
    layer: "high",
    grades: [
      { slug: "tc", title: "الجذع المشترك", order: 1, ageMin: 15, ageMax: 16, color: "#7c3aed" },
      { slug: "bac1", title: "الأولى باكالوريا", order: 2, ageMin: 16, ageMax: 17, color: "#6d28d9" },
      { slug: "bac2", title: "الثانية باكالوريا", order: 3, ageMin: 17, ageMax: 18, color: "#5b21b6" }
    ],
    subjects: highSubjects
  });

  const totals = await sql`
    select 'grades' as table_name, count(*)::text from grades
    union all select 'subjects', count(*)::text from subjects
    union all select 'units', count(*)::text from units
    union all select 'lessons', count(*)::text from lessons
    union all select 'lesson_contents', count(*)::text from lesson_contents
    union all select 'exercises', count(*)::text from exercises
  `;

  console.log("✅ Full curriculum seeded successfully.");
  console.log({ primaryLessonsAddedOrUpdated: primaryCount, middleLessonsAddedOrUpdated: middleCount, highLessonsAddedOrUpdated: highCount });
  console.table(totals);
}

main()
  .catch((error) => {
    console.error("❌ Full curriculum seed failed:", error);
    process.exitCode = 1;
  })
  .finally(async () => {
    await sql.end({ timeout: 5 });
  });

import fs from "node:fs";
import path from "node:path";
import pg from "pg";
import dotenv from "dotenv";

dotenv.config({ path: ".env" });
dotenv.config({ path: ".env.local" });

const { Client } = pg;
const APPLY = process.argv.includes("--apply");
const LIMIT_ARG = process.argv.find((a) => a.startsWith("--limit="));
const LIMIT = LIMIT_ARG ? Number(LIMIT_ARG.split("=")[1]) : 100;

if (!process.env.DATABASE_URL) {
  console.error("Missing DATABASE_URL");
  process.exit(1);
}

function stageFromGrade(grade = "") {
  const g = `${grade}`.toLowerCase();
  if (g.includes("ابتدائي") || g.includes("ap")) return "primary";
  if (g.includes("باك") || g.includes("bac") || g.includes("الجذع")) return "secondary";
  return "middle";
}

function policy(stage) {
  if (stage === "primary") return "فصحى بسيطة مع أمثلة بصرية وقريبة من الطفل.";
  if (stage === "secondary") return "فصحى دقيقة ومنهجية مع توجيه للامتحان.";
  return "فصحى سلسة وتفاعلية مناسبة للإعدادي.";
}

function isWeak(row) {
  const c = row.content ?? "";
  if (!c.trim()) return true;
  if (c.length < 900) return true;
  return ["يحتاج مطابقة", "تمرين 1 سهل", "جواب نموذجي مختصر", "مثال بسيط لفهم", "درس أصلي من oqul مبني على عنوان المنهج فقط"]
    .some((m) => c.toLowerCase().includes(m.toLowerCase()));
}

function enhance(row) {
  const stage = stageFromGrade(row.grade);
  const title = row.title;
  return [
    `# ${title}`,
    "",
    "## معلومات الدرس",
    `- المستوى: ${row.grade ?? "غير محدد"}`,
    `- المادة: ${row.subject ?? "غير محددة"}`,
    `- الوحدة: ${row.unit ?? "غير محددة"}`,
    `- الأسلوب: ${policy(stage)}`,
    "",
    "## أهداف الدرس",
    `1. فهم الفكرة الأساسية في "${title}".`,
    "2. تطبيق المفهوم في أمثلة تدريجية.",
    "3. التعرف على الأخطاء الشائعة وتصحيحها.",
    "4. حل تمارين متنوعة باستقلالية.",
    "",
    "## تمهيد",
    stage === "primary"
      ? "نبدأ بمثال قريب من حياة الطفل: البيت، المدرسة، اللعب أو الأشياء اليومية."
      : stage === "secondary"
        ? "نبدأ بربط الدرس بالفرض أو الامتحان: لماذا هذا الدرس مهم؟ وكيف يظهر في التمارين؟"
        : "نبدأ بسؤال قصير يربط الدرس بما يعرفه التلميذ سابقًا.",
    "",
    "## الشرح الأساسي",
    `الفكرة الأساسية في "${title}" هي أن نفهم المعنى قبل استعمال القاعدة. لا نبدأ بالحفظ فقط، بل نسأل: ماذا يعني هذا؟ ومتى نحتاجه؟`,
    "",
    "خطوات الفهم:",
    "1. نقرأ عنوان الدرس ونحدد الكلمات المهمة.",
    "2. نربط الدرس بمكتسب سابق.",
    "3. نقدم مثالًا بسيطًا.",
    "4. نقدم مثالًا متوسطًا.",
    "5. نطلب من المتعلم محاولة قصيرة.",
    "6. عند الخطأ نعطي تلميحًا لا جوابًا مباشرًا.",
    "",
    "## مثال محلول 1 — بسيط",
    `السؤال: أعط مثالًا بسيطًا يوضح فكرة "${title}".`,
    "الحل: نحدد المعطيات، ثم المطلوب، ثم نطبق الفكرة الأساسية، ثم نتحقق من النتيجة.",
    "",
    "## مثال محلول 2 — متوسط",
    "السؤال: طبّق نفس الفكرة في وضعية مختلفة.",
    "الحل: نقارن الوضعية بالمثال الأول، نحدد الفرق، نختار الطريقة المناسبة، ونبرر الجواب.",
    "",
    "## مثال محلول 3 — متقدم",
    "السؤال: حل وضعية مركبة تحتاج أكثر من خطوة.",
    "الحل: نقسم المسألة إلى أجزاء، نحل كل جزء، نربط النتائج، ثم نتحقق من منطقية الجواب.",
    "",
    "## أسئلة تفاعلية لليلى",
    `1. ما الفكرة الأساسية في "${title}"؟`,
    "2. هل تستطيع إعطاء مثال من عندك؟",
    "3. أين يمكن أن يقع التلميذ في الخطأ؟",
    "4. ما أول خطوة في الحل؟",
    "",
    "## أخطاء شائعة",
    "1. حفظ القاعدة دون فهم.",
    "   - التصحيح: الرجوع إلى مثال بسيط.",
    "2. استعمال المفهوم في غير موضعه.",
    "   - التصحيح: مقارنة الوضعية بالمثال الأصلي.",
    "3. القفز إلى الجواب دون تبرير.",
    "   - التصحيح: كتابة خطوة وسيطة واحدة على الأقل.",
    "",
    "## العلاج التربوي",
    "- عند الخطأ الأول: أعط تلميحًا قصيرًا.",
    "- عند تكرار الخطأ: ارجع إلى prerequisite.",
    "- عند الارتباك: استعمل مثالًا أسهل.",
    "- عند النجاح السريع: أعط تمرينًا أصعب.",
    "",
    "## تمارين",
    "### سهلة",
    `1. تمرين مباشر حول ${title}.`,
    "2. تمرين اختيار من متعدد.",
    "3. تمرين إكمال.",
    "",
    "### متوسطة",
    "1. تمرين يحتاج خطوتين.",
    "2. تمرين يطلب تفسير الجواب.",
    "3. تمرين يربط الدرس بدرس سابق.",
    "",
    "### صعبة",
    "1. تمرين مركب.",
    "2. تمرين لتحليل خطأ.",
    "",
    "### بأسلوب الفرض",
    "1. وضعية إدماجية قصيرة.",
    "2. سؤال يتطلب تبريرًا.",
    "",
    "## ملخص",
    `- درس "${title}" يركز على الفهم قبل الحفظ.`,
    "- طبقنا الفكرة في أمثلة متدرجة.",
    "- تعرفنا على الأخطاء الشائعة.",
    "- تدربنا بتمارين متنوعة.",
    "",
    "## تعليمات ليلى",
    "- ابدئي بسؤال بسيط.",
    "- لا تعطي الجواب مباشرة.",
    "- استعملي تلميحًا عند الخطأ.",
    "- امدحي المحاولة.",
    "- اختمي بسؤال تحقق."
  ].join("\\n");
}

const client = new Client({ connectionString: process.env.DATABASE_URL });
await client.connect();

const res = await client.query(`
  select
    l.id,
    l.title,
    g.name as grade,
    s.name as subject,
    u.title as unit,
    lc.id as content_id,
    lc.content
  from lessons l
  left join units u on u.id = l.unit_id
  left join subjects s on s.id = u.subject_id
  left join grades g on g.id = s.grade_id
  left join lesson_contents lc on lc.lesson_id = l.id
  order by l.created_at desc
`);

const weak = res.rows.filter(isWeak).slice(0, LIMIT);
const drafts = weak.map((row) => ({
  lessonId: row.id,
  title: row.title,
  grade: row.grade,
  subject: row.subject,
  unit: row.unit,
  enhancedContent: enhance(row)
}));

fs.mkdirSync(path.join(process.cwd(), "generated-curriculum", "enhanced-drafts"), { recursive: true });
fs.mkdirSync(path.join(process.cwd(), "reports"), { recursive: true });

fs.writeFileSync(
  path.join(process.cwd(), "generated-curriculum", "enhanced-drafts", "phase50-5-enhanced-drafts.json"),
  JSON.stringify(drafts, null, 2),
  "utf8"
);

const report = {
  generatedAt: new Date().toISOString(),
  mode: APPLY ? "apply" : "draft",
  scannedLessons: res.rows.length,
  weakSelected: weak.length,
  limit: LIMIT,
  updated: 0
};

if (APPLY) {
  await client.query("begin");
  try {
    for (const draft of drafts) {
      const row = weak.find((w) => w.id === draft.lessonId);
      if (row?.content_id) {
        await client.query("update lesson_contents set content=$1, updated_at=now() where id=$2", [draft.enhancedContent, row.content_id]);
      } else {
        await client.query("insert into lesson_contents (lesson_id, content, content_type, created_at, updated_at) values ($1,$2,$3,now(),now())", [draft.lessonId, draft.enhancedContent, "markdown"]);
      }
      report.updated++;
    }
    await client.query("commit");
  } catch (e) {
    await client.query("rollback");
    console.error("Failed. Rolled back.");
    console.error(e);
    process.exit(1);
  }
}

fs.writeFileSync(path.join(process.cwd(), "reports", "phase50-5-deep-content-enhancer-report.json"), JSON.stringify(report, null, 2), "utf8");

console.log("✅ Phase50.5 deep content enhancer completed.");
console.table(report);
console.log("Drafts:", "generated-curriculum/enhanced-drafts/phase50-5-enhanced-drafts.json");
console.log("Report:", "reports/phase50-5-deep-content-enhancer-report.json");

await client.end();
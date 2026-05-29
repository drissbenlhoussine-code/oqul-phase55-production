
import fs from "node:fs";
import path from "node:path";
import pg from "pg";
import dotenv from "dotenv";

dotenv.config({ path: ".env" });
dotenv.config({ path: ".env.local" });

const { Client } = pg;
const APPLY = process.argv.includes("--apply");
const registryPath = path.join(process.cwd(), "curriculum-registry", "phase51-middle-school-full-curriculum.json");

if (!fs.existsSync(registryPath)) {
  console.error("Missing registry file:", registryPath);
  process.exit(1);
}

const items = JSON.parse(fs.readFileSync(registryPath, "utf8")).items ?? [];

function slugify(s = "") {
  return String(s).toLowerCase().normalize("NFKD").replace(/[^\p{Letter}\p{Number}]+/gu, "-").replace(/^-+|-+$/g, "").slice(0, 80) || "lesson";
}

function content(item) {
  const title = item.lessonTitle;
  return [
    `# ${title}`,"",
    "## معلومات الدرس",
    `- المستوى: ${item.gradeAr}`,
    `- المادة: ${item.subjectAr}`,
    `- الوحدة: ${item.unitTitle}`,
    "- اللغة: العربية الفصحى السلسة، مع إمكانية التبسيط بالدارجة عند الطلب.","",
    "## أهداف الدرس",
    `1. فهم الفكرة الأساسية في \"${title}\".`,
    "2. ربط الدرس بالمكتسبات السابقة.",
    "3. تطبيق المفهوم في أمثلة متدرجة.",
    "4. التعرف على الأخطاء الشائعة وتصحيحها.",
    "5. حل تمارين سهلة ومتوسطة وصعبة.","",
    "## تمهيد",
    `قبل أن نبدأ درس \"${title}\" نسأل: ماذا يعرف التلميذ مسبقًا؟ وما الفكرة الجديدة التي سنبنيها؟ الهدف هو الفهم قبل الحفظ.`,"",
    "## الشرح الأساسي",
    `يدور هذا الدرس حول \"${title}\". نبدأ بتحديد المصطلحات المهمة، ثم نشرح المفهوم خطوة بخطوة، ثم نستعمل أمثلة بسيطة ومتوسطة ومتقدمة.`,
    "طريقة التعلم:",
    "1. قراءة عنوان الدرس وفهم المصطلحات.",
    "2. استحضار درس سابق مرتبط.",
    "3. تقديم مثال بسيط.",
    "4. حل مثال موجه.",
    "5. طرح سؤال تفاعلي.",
    "6. تصحيح الخطأ بتلميح تدريجي.","",
    "## مثال محلول 1 — بسيط",
    `السؤال: أعط مثالًا بسيطًا يوضح فكرة \"${title}\".`,
    "الحل: نحدد المعطيات، ثم المطلوب، ثم نستعمل الفكرة الأساسية، ثم نتحقق من الجواب.","",
    "## مثال محلول 2 — متوسط",
    `السؤال: طبّق فكرة \"${title}\" في وضعية جديدة.`,
    "الحل: نقرأ الوضعية، نحدد العلاقة بينها وبين المثال الأول، نطبق الخطوات المناسبة، ونكتب الجواب مع تفسير.","",
    "## مثال محلول 3 — متقدم",
    "السؤال: حل وضعية مركبة تحتاج أكثر من خطوة.",
    "الحل: نقسم المسألة إلى أجزاء، نحل كل جزء، نربط النتائج، ثم نتحقق من منطقية الجواب.","",
    "## أسئلة تفاعلية لليلى",
    `1. ما الفكرة الأساسية في \"${title}\"؟`,
    "2. ما أول خطوة يجب أن نقوم بها؟",
    "3. هل تستطيع إعطاء مثال من عندك؟",
    "4. أين يمكن أن يقع التلميذ في الخطأ؟",
    "5. هل تريد شرحًا أبسط أم تمرينًا آخر؟","",
    "## أخطاء شائعة",
    "1. حفظ القاعدة دون فهم معناها.",
    "   - التصحيح: الرجوع إلى مثال محسوس أو بسيط.",
    "2. الخلط بين هذا الدرس ودرس سابق.",
    "   - التصحيح: المقارنة بين الدرسين وإبراز الفرق.",
    "3. القفز مباشرة إلى الجواب دون خطوات.",
    "   - التصحيح: كتابة خطوة وسيطة واحدة على الأقل.","",
    "## العلاج التربوي",
    "- إذا أخطأ المتعلم أول مرة: أعطه تلميحًا قصيرًا.",
    "- إذا كرر الخطأ: ارجع إلى prerequisite أبسط.",
    "- إذا كان مترددًا: أعطه مثالًا محلولًا جزئيًا.",
    "- إذا أجاب بسرعة: قدم له تحديًا أصعب.","",
    "## تمارين",
    "### سهلة",
    `1. تمرين مباشر حول ${title}.`,
    `2. سؤال اختيار من متعدد حول ${title}.`,
    "3. تمرين إكمال فراغ.",
    "4. سؤال فهم قصير.","",
    "### متوسطة",
    "1. تمرين يحتاج خطوتين.",
    "2. تمرين يطلب تفسير الجواب.",
    "3. تمرين يربط الدرس بدرس سابق.",
    "4. تمرين تطبيقي في وضعية جديدة.","",
    "### صعبة",
    "1. تمرين مركب.",
    "2. تمرين لتحليل خطأ.",
    "3. وضعية تتطلب تبريرًا.","",
    "### بأسلوب الفرض",
    "1. وضعية إدماجية قصيرة.",
    "2. سؤال يتطلب تنظيم الجواب.","",
    "## ملخص",
    `- درس \"${title}\" يعتمد على الفهم قبل الحفظ.`,
    "- تعلمنا الفكرة الأساسية.",
    "- طبقناها في أمثلة متدرجة.",
    "- تعرفنا على الأخطاء الشائعة.",
    "- تدربنا بتمارين متنوعة.","",
    "## تعليمات ليلى",
    "- ابدئي بسؤال بسيط قبل الشرح.",
    "- اشرحي بالفصحى السلسة.",
    "- لا تعطي الجواب مباشرة عند الخطأ.",
    "- استعملي تلميحًا ثم مثالًا أبسط.",
    "- اختمي بسؤال تحقق قصير."
  ].join("\n");
}

async function ensureGrade(client, item) {
  const r = await client.query("select id from grades where code=$1 or name=$2 limit 1", [item.grade, item.gradeAr]);
  if (r.rows[0]) return r.rows[0].id;
  const n = await client.query("insert into grades (name, code, level, created_at, updated_at) values ($1,$2,$3,now(),now()) returning id", [item.gradeAr, item.grade, "middle"]);
  return n.rows[0].id;
}
async function ensureSubject(client, item, gradeId) {
  const r = await client.query("select id from subjects where grade_id=$1 and (code=$2 or name=$3) limit 1", [gradeId,item.subject,item.subjectAr]);
  if (r.rows[0]) return r.rows[0].id;
  const n = await client.query("insert into subjects (grade_id,name,code,created_at,updated_at) values ($1,$2,$3,now(),now()) returning id", [gradeId,item.subjectAr,item.subject]);
  return n.rows[0].id;
}
async function ensureUnit(client, item, subjectId) {
  const r = await client.query("select id from units where subject_id=$1 and title=$2 limit 1", [subjectId,item.unitTitle]);
  if (r.rows[0]) return r.rows[0].id;
  const n = await client.query("insert into units (subject_id,title,description,order_index,created_at,updated_at) values ($1,$2,$3,$4,now(),now()) returning id", [subjectId,item.unitTitle,"وحدة من منهج الإعدادي الموسع Phase51",item.unitOrder]);
  return n.rows[0].id;
}
async function upsertLesson(client,item,unitId){
  const r=await client.query("select id from lessons where unit_id=$1 and title=$2 limit 1",[unitId,item.lessonTitle]);
  if(r.rows[0]) return {id:r.rows[0].id,created:false};
  const n=await client.query("insert into lessons (unit_id,title,slug,description,difficulty,estimated_minutes,order_index,created_at,updated_at) values ($1,$2,$3,$4,$5,$6,$7,now(),now()) returning id",[unitId,item.lessonTitle,`${item.grade}-${item.subject}-${slugify(item.lessonTitle)}`,"درس إعدادي عميق من Phase51","medium",30,item.lessonOrder]);
  return {id:n.rows[0].id,created:true};
}
async function upsertContent(client,lessonId,body){
  const r=await client.query("select id from lesson_contents where lesson_id=$1 limit 1",[lessonId]);
  if(r.rows[0]){await client.query("update lesson_contents set content=$1,updated_at=now() where id=$2",[body,r.rows[0].id]); return false;}
  await client.query("insert into lesson_contents (lesson_id,content,content_type,created_at,updated_at) values ($1,$2,$3,now(),now())",[lessonId,body,"markdown"]);
  return true;
}
async function exercises(client,item,lessonId){
  const qs=[["سؤال مباشر","easy"],["اختيار من متعدد","easy"],["إكمال فراغ","easy"],["سؤال فهم","easy"],["تمرين خطوتين","medium"],["تفسير جواب","medium"],["ربط بدرس سابق","medium"],["وضعية تطبيقية","medium"],["تمرين مركب","hard"],["تحليل خطأ","hard"],["سؤال فرض","hard"],["وضعية إدماجية","hard"]];
  let added=0;
  for(const [q,d] of qs){
    const question=`${q} حول ${item.lessonTitle}`;
    const e=await client.query("select id from exercises where lesson_id=$1 and question=$2 limit 1",[lessonId,question]);
    if(e.rows[0]) continue;
    await client.query("insert into exercises (lesson_id,question,type,difficulty,correct_answer,explanation,created_at,updated_at) values ($1,$2,$3,$4,$5,$6,now(),now())",[lessonId,question,"short_answer",d,"إجابة نموذجية حسب الدرس.","يتم التصحيح عبر ليلى خطوة بخطوة."]);
    added++;
  }
  return added;
}

const summary={mode:APPLY?"apply":"dry-run", registryItems:items.length, createdLessons:0, updatedLessons:0, contentCreated:0, exercisesAdded:0, byGrade:{}};
for(const item of items){summary.byGrade[item.grade]=(summary.byGrade[item.grade]??0)+1;}
if(!APPLY){console.log("✅ Phase51 dry-run"); console.table(summary.byGrade); console.log("Registry lessons:",items.length); console.log("Run with --apply"); process.exit(0);}

if(!process.env.DATABASE_URL){console.error("Missing DATABASE_URL"); process.exit(1);}
const client=new Client({connectionString:process.env.DATABASE_URL});
await client.connect();
try{
  await client.query("begin");
  for(const item of items){
    const gradeId=await ensureGrade(client,item);
    const subjectId=await ensureSubject(client,item,gradeId);
    const unitId=await ensureUnit(client,item,subjectId);
    const lesson=await upsertLesson(client,item,unitId);
    if(lesson.created) summary.createdLessons++; else summary.updatedLessons++;
    if(await upsertContent(client,lesson.id,content(item))) summary.contentCreated++;
    summary.exercisesAdded += await exercises(client,item,lesson.id);
  }
  await client.query("commit");
}catch(e){await client.query("rollback"); console.error("❌ Failed and rolled back"); console.error(e); process.exit(1);}
await client.end();
fs.mkdirSync(path.join(process.cwd(),"reports"),{recursive:true});
fs.writeFileSync(path.join(process.cwd(),"reports","phase51-full-middle-school-curriculum-report.json"),JSON.stringify(summary,null,2),"utf8");
console.log("✅ Phase51 full middle school curriculum injected.");
console.table(summary);

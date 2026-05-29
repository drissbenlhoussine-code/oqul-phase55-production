import fs from "node:fs";
import path from "node:path";
import pg from "pg";
import dotenv from "dotenv";
dotenv.config({path:".env"}); dotenv.config({path:".env.local"});
const {Client}=pg; const APPLY=process.argv.includes("--apply");
const reportPath=path.join(process.cwd(),"reports","phase54-official-alignment-report.json");
if(!fs.existsSync(reportPath)){console.error("Run node scripts/audit-phase54-official-alignment.mjs first");process.exit(1);}
const report=JSON.parse(fs.readFileSync(reportPath,"utf8"));
const targets=(report.priorityFixes??[]).slice(0,Number(process.env.PHASE54_FIX_LIMIT??200));
function block(r){return ["","---","","## Phase54 — المطابقة الرسمية والمنهجية","- يجب التحقق من عنوان وترتيب هذا الدرس مع TelmidTICE، مع مطابقة Moutamadris وAlloSchool عند الحاجة.","- الشرح داخل Oqul أصلي ولا ينسخ من أي مصدر.","","## كفايات الدرس",`- فهم ${r.title}.`,`- تطبيق ${r.title} في وضعيات مدرسية.`,"- تحليل الأخطاء الشائعة.","- الاستعداد لأسئلة الفرض أو الامتحان.","","## منهجية الامتحان","1. قراءة السؤال وتحديد المطلوب.","2. استخراج المعطيات.","3. اختيار الطريقة المناسبة.","4. تبرير الخطوات.","5. التحقق من الجواب.","","## سلم تنقيط مبسط","- فهم المطلوب: 2 نقاط.","- اختيار الطريقة: 2 نقاط.","- سلامة الخطوات: 3 نقاط.","- صحة الجواب: 2 نقاط.","- التنظيم والتبرير: 1 نقطة.","","## ربط بليلى","- إذا أخطأ المتعلم، اسأليه عن المعطيات أولًا.","- إذا لم يعرف الطريقة، أعطيه تلميحًا لا الجواب.","- إذا نجح، قدمي سؤالًا امتحانيًا أصعب."].join("\n");}
if(!APPLY){console.log("✅ Phase54 remediation dry-run."); console.log("Targets:",targets.length); console.log("Run with --apply"); process.exit(0);}
if(!process.env.DATABASE_URL){console.error("Missing DATABASE_URL");process.exit(1);}
const c=new Client({connectionString:process.env.DATABASE_URL}); await c.connect(); let updated=0;
try{await c.query("begin"); for(const r of targets){const cr=await c.query("select id,content from lesson_contents where lesson_id=$1 limit 1",[r.id]); const b=block(r); if(cr.rows[0]){const current=cr.rows[0].content??""; if(current.includes("Phase54 — المطابقة الرسمية والمنهجية"))continue; await c.query("update lesson_contents set content=$1,updated_at=now() where id=$2",[current+"\n"+b,cr.rows[0].id]);}else{await c.query("insert into lesson_contents(lesson_id,content,content_type,created_at,updated_at) values($1,$2,$3,now(),now())",[r.id,b,"markdown"]);} updated++;} await c.query("commit");}catch(e){await c.query("rollback");console.error("❌ Rolled back");console.error(e);process.exit(1);}
await c.end(); fs.writeFileSync(path.join(process.cwd(),"reports","phase54-remediation-apply-report.json"),JSON.stringify({generatedAt:new Date().toISOString(),updated,targetCount:targets.length},null,2),"utf8"); console.log("✅ Phase54 remediation applied."); console.log("Updated:",updated);
import fs from "node:fs";
import path from "node:path";
import pg from "pg";
import dotenv from "dotenv";
dotenv.config({path:".env"}); dotenv.config({path:".env.local"});
const {Client}=pg;
if(!process.env.DATABASE_URL){console.error("Missing DATABASE_URL");process.exit(1);}

function examRisk(row){
 const c=row.content??""; const risks=[];
 if((row.exercises_count??0)<8)risks.push("تمارين قليلة");
 if(!c.includes("امتحان")&&!c.includes("فرض")&&!c.includes("باك"))risks.push("غياب الربط بالامتحان");
 if(!c.includes("أخطاء شائعة"))risks.push("غياب الأخطاء الشائعة");
 if(!c.includes("العلاج التربوي"))risks.push("غياب العلاج التربوي");
 const severity=risks.length>=3?"high":risks.length>=1?"medium":"low";
 return {severity,risks};
}
function pathPlan(row){
 const risk=examRisk(row).severity;
 return {
   pace:risk==="high"?"slow_guided":risk==="medium"?"balanced":"accelerated",
   actions:[
     "تشخيص سريع قبل الدرس",
     "شرح موجه مع ليلى",
     "تمارين سهلة ثم متوسطة",
     "تصحيح الأخطاء الشائعة",
     "اختبار قصير وتوصية"
   ]
 };
}
const c=new Client({connectionString:process.env.DATABASE_URL}); await c.connect();
const res=await c.query(`
 select l.id,l.title,g.name as grade,g.code as grade_code,s.name as subject,s.code as subject_code,u.title as unit,lc.content,coalesce(ex.exercise_count,0)::int as exercises_count
 from lessons l
 left join units u on u.id=l.unit_id
 left join subjects s on s.id=u.subject_id
 left join grades g on g.id=s.grade_id
 left join lesson_contents lc on lc.lesson_id=l.id
 left join (select lesson_id,count(*) as exercise_count from exercises group by lesson_id) ex on ex.lesson_id=l.id
 order by g.name,s.name,u.title,l.title`);
const rows=res.rows.map(r=>({id:r.id,title:r.title,grade:r.grade,gradeCode:r.grade_code,subject:r.subject,subjectCode:r.subject_code,unit:r.unit,exercisesCount:r.exercises_count,examRisk:examRisk(r),learningPath:pathPlan(r)}));
const byRisk={high:0,medium:0,low:0};
for(const r of rows)byRisk[r.examRisk.severity]=(byRisk[r.examRisk.severity]??0)+1;
const report={phase:"Phase55",generatedAt:new Date().toISOString(),totalLessons:rows.length,byRisk,highPriority:rows.filter(r=>r.examRisk.severity==="high").slice(0,200),rows};
fs.mkdirSync(path.join(process.cwd(),"reports"),{recursive:true});
fs.writeFileSync(path.join(process.cwd(),"reports","phase55-intelligence-report.json"),JSON.stringify(report,null,2),"utf8");
console.log("✅ Phase55 intelligence report generated."); console.table(byRisk); console.log("Total:",rows.length);
await c.end();
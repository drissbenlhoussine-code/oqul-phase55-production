import fs from "node:fs";
import path from "node:path";
import pg from "pg";
import dotenv from "dotenv";
dotenv.config({path:".env"}); dotenv.config({path:".env.local"});
const {Client}=pg;
if(!process.env.DATABASE_URL){console.error("Missing DATABASE_URL");process.exit(1);}
function align(row){
 const issues=[]; const c=row.content??""; const title=row.title??"";
 if(!row.grade)issues.push("missing_grade");
 if(!row.subject)issues.push("missing_subject");
 if(!row.unit)issues.push("missing_unit");
 if(!title.trim())issues.push("missing_title");
 if(title.includes("يحتاج مطابقة"))issues.push("unverified_title");
 if(c.length<1200)issues.push("content_too_short");
 if((row.exercises_count??0)<8)issues.push("insufficient_exercises");
 if(!c.includes("أهداف الدرس"))issues.push("missing_objectives");
 if(!c.includes("أخطاء شائعة"))issues.push("missing_common_mistakes");
 if(!c.includes("العلاج التربوي"))issues.push("missing_remediation");
 if(!c.includes("تعليمات ليلى"))issues.push("missing_leila_hooks");
 const score=Math.max(0,100-issues.length*9);
 const status=score>=92?"officially_aligned":score>=82?"cross_checked":score>=70?"mapped":score<45?"unverified":"needs_review";
 return {alignmentScore:score,status,issues};
}
function exam(row){
 const grade=row.grade??""; const c=row.content??"";
 const isBac=grade.includes("باك")||grade.includes("BAC")||grade.includes("2BAC");
 const isRegional=grade.includes("الثالثة")||grade.includes("3AC")||grade.includes("الأولى باكالوريا")||grade.includes("1BAC");
 const risks=[];
 if((row.exercises_count??0)<8)risks.push("تمارين قليلة");
 if(!c.includes("امتحان")&&!c.includes("باك")&&!c.includes("فرض"))risks.push("ضعف الربط بالامتحانات");
 if(!c.includes("أخطاء شائعة"))risks.push("لا توجد أخطاء شائعة كافية");
 if(!c.includes("منهجية"))risks.push("المنهجية غير واضحة");
 return {examType:isBac?"bac":isRegional?"regional_or_local_exam":"continuous_assessment",priority:isBac?"very_high":isRegional?"high":"medium",risks};
}
const client=new Client({connectionString:process.env.DATABASE_URL}); await client.connect();
const res=await client.query(`
 select l.id,l.title,g.name as grade,g.code as grade_code,s.name as subject,s.code as subject_code,u.title as unit,lc.content,coalesce(ex.exercise_count,0)::int as exercises_count
 from lessons l
 left join units u on u.id=l.unit_id
 left join subjects s on s.id=u.subject_id
 left join grades g on g.id=s.grade_id
 left join lesson_contents lc on lc.lesson_id=l.id
 left join (select lesson_id,count(*) as exercise_count from exercises group by lesson_id) ex on ex.lesson_id=l.id
 order by g.name,s.name,u.title,l.title`);
const rows=res.rows.map(r=>({id:r.id,title:r.title,grade:r.grade,gradeCode:r.grade_code,subject:r.subject,subjectCode:r.subject_code,unit:r.unit,exercisesCount:r.exercises_count,...align(r),examIntelligence:exam(r)}));
const byStatus={},byGrade={},bySubject={},examRisk=[];
for(const r of rows){
 byStatus[r.status]=(byStatus[r.status]??0)+1;
 byGrade[r.grade??"unknown"]??={total:0,avg:0,scores:[]}; byGrade[r.grade??"unknown"].total++; byGrade[r.grade??"unknown"].scores.push(r.alignmentScore);
 bySubject[r.subject??"unknown"]??={total:0,avg:0,scores:[]}; bySubject[r.subject??"unknown"].total++; bySubject[r.subject??"unknown"].scores.push(r.alignmentScore);
 if(r.examIntelligence.risks.length)examRisk.push(r);
}
for(const b of Object.values(byGrade)){b.avg=Math.round(b.scores.reduce((a,b)=>a+b,0)/Math.max(1,b.scores.length)); delete b.scores;}
for(const b of Object.values(bySubject)){b.avg=Math.round(b.scores.reduce((a,b)=>a+b,0)/Math.max(1,b.scores.length)); delete b.scores;}
const report={phase:"Phase54",generatedAt:new Date().toISOString(),totalLessons:rows.length,averageAlignmentScore:Math.round(rows.reduce((s,r)=>s+r.alignmentScore,0)/Math.max(1,rows.length)),byStatus,byGrade,bySubject,priorityFixes:rows.filter(r=>r.status==="unverified"||r.status==="needs_review").sort((a,b)=>a.alignmentScore-b.alignmentScore).slice(0,200),examRisk:examRisk.slice(0,200),rows};
fs.mkdirSync(path.join(process.cwd(),"reports"),{recursive:true});
fs.writeFileSync(path.join(process.cwd(),"reports","phase54-official-alignment-report.json"),JSON.stringify(report,null,2),"utf8");
console.log("✅ Phase54 official alignment audit completed."); console.table(byStatus); console.log("Average alignment:",report.averageAlignmentScore); console.log("Total lessons:",report.totalLessons);
await client.end();
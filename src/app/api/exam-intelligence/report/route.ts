import { NextResponse } from "next/server";
import fs from "node:fs";
import path from "node:path";
export async function GET(){const p=path.join(process.cwd(),"reports","phase54-official-alignment-report.json");if(!fs.existsSync(p))return NextResponse.json({ok:false,error:"missing_report",message:"Run node scripts/audit-phase54-official-alignment.mjs"},{status:404});const r=JSON.parse(fs.readFileSync(p,"utf8"));return NextResponse.json({ok:true,examIntelligence:{generatedAt:r.generatedAt,totalLessons:r.totalLessons,examRisk:r.examRisk??[],priorityFixes:r.priorityFixes??[]}});}

import { NextResponse } from "next/server";
import fs from "node:fs";
import path from "node:path";
export async function GET(){const p=path.join(process.cwd(),"reports","phase54-official-alignment-report.json");if(!fs.existsSync(p))return NextResponse.json({ok:false,error:"missing_report",message:"Run node scripts/audit-phase54-official-alignment.mjs"},{status:404});return NextResponse.json({ok:true,report:JSON.parse(fs.readFileSync(p,"utf8"))});}

import { NextResponse } from "next/server";
import { getSession } from "@/server/auth/session";
import fs from "node:fs";
import path from "node:path";

export async function GET(){
 const session = await getSession();
 if (!session) return NextResponse.json({ok:false,error:"unauthorized",message:"يجب تسجيل الدخول"},{status:401});
 const p=path.join(process.cwd(),"reports","phase55-intelligence-report.json");
 if(!fs.existsSync(p)) return NextResponse.json({ok:false,error:"missing_report",message:"Run node scripts/generate-phase55-intelligence-report.mjs"},{status:404});
 return NextResponse.json({ok:true,report:JSON.parse(fs.readFileSync(p,"utf8"))});
}

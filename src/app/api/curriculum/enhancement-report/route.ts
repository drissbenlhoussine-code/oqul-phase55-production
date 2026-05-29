import { NextResponse } from "next/server";
import fs from "node:fs";
import path from "node:path";

export async function GET() {
  const reportPath = path.join(process.cwd(), "reports", "phase50-5-deep-content-enhancer-report.json");
  if (!fs.existsSync(reportPath)) {
    return NextResponse.json({ ok: false, error: "report_missing", message: "Run: node scripts/enhance-weak-lessons.mjs --limit=100" }, { status: 404 });
  }
  return NextResponse.json({ ok: true, report: JSON.parse(fs.readFileSync(reportPath, "utf8")) });
}
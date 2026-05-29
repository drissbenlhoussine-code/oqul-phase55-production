import { NextResponse } from "next/server";
import fs from "node:fs";
import path from "node:path";

export async function GET() {
  const reportPath = path.join(process.cwd(), "reports", "phase50-4-curriculum-quality-report.json");

  if (!fs.existsSync(reportPath)) {
    return NextResponse.json(
      {
        ok: false,
        error: "quality_report_missing",
        message: "Run: node scripts/audit-curriculum-quality.mjs",
      },
      { status: 404 }
    );
  }

  const report = JSON.parse(fs.readFileSync(reportPath, "utf8"));
  return NextResponse.json({ ok: true, report });
}
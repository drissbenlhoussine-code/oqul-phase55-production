import { NextRequest, NextResponse } from "next/server";
import { getSecondaryLessons, getSecondarySummary } from "@/features/secondary/lib/secondary-curriculum";
import { createBacExamPlan } from "@/features/secondary/lib/bac-exam-engine";
import { buildSecondaryReasoningFlow } from "@/features/secondary/lib/reasoning-tutor";

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const grade = searchParams.get("grade") ?? undefined;
  const subject = searchParams.get("subject") ?? undefined;

  if (searchParams.get("summary") === "true") {
    return NextResponse.json({ ok: true, layer: "secondary", summary: getSecondarySummary() });
  }

  return NextResponse.json({ ok: true, layer: "secondary", lessons: getSecondaryLessons(grade, subject) });
}

export async function POST(req: NextRequest) {
  const body = await req.json().catch(() => ({}));
  const grade = body.grade ?? "2BAC";
  const subject = body.subject ?? "advanced_math";
  const unit = body.unit ?? "functions";

  return NextResponse.json({
    ok: true,
    layer: "secondary",
    reasoningFlow: buildSecondaryReasoningFlow(subject, unit),
    examPlan: createBacExamPlan({
      grade,
      subject,
      weakCompetencies: body.weakCompetencies ?? [],
      daysAvailable: body.daysAvailable ?? 14,
    }),
  });
}
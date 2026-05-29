import { NextResponse } from "next/server";
import {
  getMoroccoCompanionGrade,
  moroccoSchoolCompanionCurriculum,
  type MoroccoCompanionGrade,
} from "@/db/curriculum/morocco";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const grade = url.searchParams.get("grade");

  if (grade) {
    const parsed = Number(grade) as MoroccoCompanionGrade;

    if (![1, 2, 3, 4, 5, 6].includes(parsed)) {
      return NextResponse.json(
        { ok: false, error: "grade must be between 1 and 6." },
        { status: 400 }
      );
    }

    return NextResponse.json({
      ok: true,
      curriculum: getMoroccoCompanionGrade(parsed),
    });
  }

  return NextResponse.json({
    ok: true,
    curriculum: moroccoSchoolCompanionCurriculum,
  });
}

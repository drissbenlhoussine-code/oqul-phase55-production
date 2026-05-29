import { NextResponse } from "next/server";
import { z } from "zod";
import { generateDailyChallenge } from "@/server/daily-challenges/challenge-generator";

function assertPreviewEnabled() {
  if (process.env.NODE_ENV === "production" && process.env.ENABLE_PREVIEW_APIS !== "true") {
    return Response.json({ ok: false, error: "Preview API disabled in production." }, { status: 404 });
  }
  return null;
}


const schema = z.object({
  grade: z.number().int().min(1).max(6),
  subject: z.enum(["math", "arabic", "french", "science"]).optional(),
  weakSkillId: z.string().optional(),
});

export async function POST(request: Request) {
  const previewGuard = assertPreviewEnabled();
  if (previewGuard) return previewGuard;
  const body = schema.parse(await request.json());
  return NextResponse.json({ ok: true, challenge: generateDailyChallenge(body) });
}

import { NextResponse } from "next/server";
import { z } from "zod";
import { buildLeilaNoticedNote } from "@/server/leila-notes/leila-noticed-engine";

function assertPreviewEnabled() {
  if (process.env.NODE_ENV === "production" && process.env.ENABLE_PREVIEW_APIS !== "true") {
    return Response.json({ ok: false, error: "Preview API disabled in production." }, { status: 404 });
  }
  return null;
}


const schema = z.object({
  childName: z.string().optional(),
  strengths: z.array(z.string()).optional(),
  weaknesses: z.array(z.string()).optional(),
  emotion: z.enum(["confident", "frustrated", "tired", "curious", "neutral"]).optional(),
});

export async function POST(request: Request) {
  const previewGuard = assertPreviewEnabled();
  if (previewGuard) return previewGuard;
  const body = schema.parse(await request.json());
  return NextResponse.json({ ok: true, note: buildLeilaNoticedNote(body) });
}

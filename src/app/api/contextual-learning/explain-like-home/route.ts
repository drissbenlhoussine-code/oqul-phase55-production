import { NextResponse } from "next/server";
import { z } from "zod";
import { explainLikeHome } from "@/server/contextual-learning/moroccan-context-examples";

function assertPreviewEnabled() {
  if (process.env.NODE_ENV === "production" && process.env.ENABLE_PREVIEW_APIS !== "true") {
    return Response.json({ ok: false, error: "Preview API disabled in production." }, { status: 404 });
  }
  return null;
}


const schema = z.object({
  topic: z.string().min(1),
  childName: z.string().optional(),
});

export async function POST(request: Request) {
  const previewGuard = assertPreviewEnabled();
  if (previewGuard) return previewGuard;
  const body = schema.parse(await request.json());
  return NextResponse.json({ ok: true, explanation: explainLikeHome(body) });
}

/**
 * Admin-only endpoint for AI-assisted curriculum content generation.
 * Allows generating lessons at scale without manual writing.
 *
 * POST /api/admin/generate-lesson
 * Body: { subject, grade, topic, objectives, difficulty }
 * Returns: Generated lesson content ready to insert into DB
 */
import { z } from "zod";
import { generateLesson } from "@/server/ai/content-generator";
import { NextRequest } from "next/server";
import { requireAuth } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";
import { AppError } from "@/server/errors";

const schema = z.object({
  subject:    z.string().min(1),
  grade:      z.number().int().min(1).max(12),
  topic:      z.string().min(2),
  objectives: z.array(z.string()).min(1).max(5),
  difficulty: z.enum(["easy", "medium", "hard"]),
});

export async function POST(request: NextRequest) {
  try {
    const session = await requireAuth();
    if (session.role !== "admin") {
      throw new AppError("Ù„ÙŠØ³ Ù„Ø¯ÙŠÙƒ ØµÙ„Ø§Ø­ÙŠØ© Ù„Ù„ÙˆØµÙˆÙ„", "FORBIDDEN", 403);
    }
    const body = schema.parse(await request.json());
    const lesson = await generateLesson(body);
    return ok(lesson);
  } catch (e) {
    return errorResponse(e);
  }
}

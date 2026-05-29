import { NextRequest } from "next/server";
import { z } from "zod";
import { requireAuth } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";
import { assertOwnsChild } from "@/server/auth/ownership";
import { progressService } from "@/server/services/progress-service";

const schema = z.object({
  childId: z.string().uuid(),
  lessonId: z.string().uuid(),
  score: z.number().min(0).max(100).optional(),
});

export async function POST(request: NextRequest) {
  try {
    const session = await requireAuth();
    const body = schema.parse(await request.json());
    await assertOwnsChild(session.sub, body.childId);
    const result = await progressService.completeLesson(body.childId, body.lessonId, body.score);
    return ok(result);
  } catch (e) {
    return errorResponse(e);
  }
}

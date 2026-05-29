import { NextRequest } from "next/server";
import { z } from "zod";
import { requireAuth } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";
import { assertOwnsChild } from "@/server/auth/ownership";
import { learningService } from "@/server/services/learning-service";

const schema = z.object({
  childId: z.string().uuid(),
  exerciseId: z.string().uuid(),
  lessonId: z.string().uuid(),
  answer: z.string().min(1),
});

export async function POST(request: NextRequest) {
  try {
    const session = await requireAuth();
    const body = schema.parse(await request.json());
    await assertOwnsChild(session.sub, body.childId);
    const result = await learningService.submitExercise(body);
    return ok(result);
  } catch (e) {
    return errorResponse(e);
  }
}

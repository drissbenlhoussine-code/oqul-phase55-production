import { z } from "zod";
import { withAuth } from "@/server/http/with-auth";
import { progressRepo } from "@/server/repositories/progress";
import { assertOwnsChild } from "@/server/auth/ownership";
import { AppError } from "@/server/errors";

const updateSchema = z.object({
  childId:       z.string().uuid(),
  lessonId:      z.string().uuid(),
  status:        z.enum(["in_progress", "completed", "needs_review"]),
  score:         z.number().min(0).max(100).optional(),
  timeSpentSecs: z.number().int().min(0).optional(),
});

export const GET = withAuth(async ({ session, request }) => {
  const childId = request.nextUrl.searchParams.get("childId");
  if (!childId) throw new AppError("childId مطلوب", "VALIDATION_ERROR", 422);
  await assertOwnsChild(session.sub, childId);
  return progressRepo.getChildProgress(childId);
});

export const POST = withAuth(async ({ session, request }) => {
  const body = updateSchema.parse(await request.json());
  await assertOwnsChild(session.sub, body.childId);
  return progressRepo.upsertLessonProgress(body);
});

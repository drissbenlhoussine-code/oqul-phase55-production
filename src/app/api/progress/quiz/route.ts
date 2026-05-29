import { z } from "zod";
import { withAuth } from "@/server/http/with-auth";
import { assertOwnsChild } from "@/server/auth/ownership";
import { progressRepo } from "@/server/repositories/progress";
import { curriculumRepo } from "@/server/repositories/curriculum";
import { gamificationService, getLevelInfo } from "@/server/services/gamification-service";
import { masteryService } from "@/server/services/mastery-service";
import { AppError } from "@/server/errors";

const quizSchema = z.object({
  childId:  z.string().uuid(),
  lessonId: z.string().uuid(),
  answers:  z.record(z.string()),
});

export const POST = withAuth(async ({ session, request }) => {
  const body = quizSchema.parse(await request.json());
  await assertOwnsChild(session.sub, body.childId);

  const lesson = await curriculumRepo.getLessonWithContent(body.lessonId);
  if (!lesson) throw new AppError("الدرس غير موجود", "NOT_FOUND", 404);

  // ── Score the quiz ──────────────────────────────────────────────────────────
  let earnedPoints = 0;
  const totalPoints = lesson.exercises.reduce((s, e) => s + e.points, 0);

  const feedback = lesson.exercises.map((ex) => {
    const given   = body.answers[ex.id]?.trim().toLowerCase() ?? "";
    const correct = given === ex.correctAnswer.trim().toLowerCase();
    if (correct) earnedPoints += ex.points;
    return { exerciseId: ex.id, correct, yourAnswer: body.answers[ex.id] ?? "", correctAnswer: ex.correctAnswer, explanation: ex.explanation ?? null, points: ex.points };
  });

  const score  = totalPoints > 0 ? (earnedPoints / totalPoints) * 100 : 0;
  const passed = score >= 60;
  const isPerfect = score === 100;

  // ── Persist ─────────────────────────────────────────────────────────────────
  const attempt = await progressRepo.saveQuizAttempt({ childId: body.childId, lessonId: body.lessonId, score, totalPoints, earnedPoints, answers: body.answers });
  await progressRepo.upsertLessonProgress({ childId: body.childId, lessonId: body.lessonId, status: passed ? "completed" : "needs_review", score });

  // ── Gamification ─────────────────────────────────────────────────────────────
  let gamification = null;
  if (passed) {
    const xpAmount = isPerfect ? 50 : Math.round(earnedPoints * 0.5);
    const source   = isPerfect ? "perfect_score" : "quiz_pass";
    const [{ streak }, xpResult] = await Promise.all([
      gamificationService.updateStreak(body.childId),
      gamificationService.awardXP({ childId: body.childId, source, xpAmount }),
    ]);
    gamification = { xpEarned: xpAmount, newXP: xpResult.newXP, levelInfo: xpResult.levelInfo, newBadges: xpResult.newBadges, streak };
  }

  // Update mastery / weak points
  if (lesson.unit?.subject?.id) {
    await masteryService.updateAfterQuiz({
      childId:   body.childId,
      subjectId: lesson.unit.subject.id,
      topic:     lesson.titleAr,
      score,
    }).catch(console.error);
  }

  return { attempt, score: Math.round(score), earnedPoints, totalPoints, passed, feedback, gamification };
});

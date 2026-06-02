import { z } from "zod";
import { withAuth } from "@/server/http/with-auth";
import { assertOwnsChild } from "@/server/auth/ownership";
import { progressRepo } from "@/server/repositories/progress";
import { curriculumRepo } from "@/server/repositories/curriculum";
import { gamificationService, getLevelInfo } from "@/server/services/gamification-service";
import { masteryService } from "@/server/services/mastery-service";
import { AppError } from "@/server/errors";

// Normalize Arabic text for fill_blank comparison:
// - strip diacritics (حركات) so missing tashkeel is never penalised
// - unify hamza forms (أإآ → ا) since placement is a keyboard concern, not a Grade 2 skill
// - ة is kept strict because الإملاء exercises explicitly test ة vs ه
function normalizeAnswer(s: string): string {
  return s
    .trim()
    .replace(/[ً-ْ]/g, "")   // remove diacritics
    .replace(/[أإآٱ]/g, "ا")            // normalise hamza variants
    .replace(/\s+/g, " ");              // collapse multiple spaces
}

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
    const given   = normalizeAnswer(body.answers[ex.id] ?? "");
    const correct = given === normalizeAnswer(ex.correctAnswer);
    if (correct) earnedPoints += ex.points;
    return { exerciseId: ex.id, correct, yourAnswer: body.answers[ex.id] ?? "", correctAnswer: ex.correctAnswer, explanation: ex.explanation ?? null, points: ex.points };
  });

  const score  = totalPoints > 0 ? (earnedPoints / totalPoints) * 100 : 0;
  const passed = score >= 60;
  const isPerfect = score === 100;

  // ── Persist ─────────────────────────────────────────────────────────────────
  // Check before writing: if lesson already completed, skip gamification (idempotency)
  const existingProgress = await progressRepo.getLessonProgress(body.childId, body.lessonId);
  const alreadyCompleted = existingProgress?.status === "completed";

  const attempt = await progressRepo.saveQuizAttempt({ childId: body.childId, lessonId: body.lessonId, score, totalPoints, earnedPoints, answers: body.answers });
  await progressRepo.upsertLessonProgress({ childId: body.childId, lessonId: body.lessonId, status: passed ? "completed" : "needs_review", score });

  // ── Gamification ─────────────────────────────────────────────────────────────
  // XP is awarded exactly once: skip if lesson was already completed before this attempt
  let gamification = null;
  if (passed && !alreadyCompleted) {
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

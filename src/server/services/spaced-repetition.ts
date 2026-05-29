/**
 * Spaced Repetition Scheduler (SRS)
 * Based on SM-2 algorithm — the proven science of remembering things permanently.
 *
 * Principle: Review a lesson at increasing intervals based on how well you knew it:
 * - Score 100%: review in 7 days
 * - Score 80%+: review in 4 days
 * - Score 60%+: review in 2 days
 * - Score <60%: review tomorrow
 *
 * This is what makes flashcard apps like Anki so effective.
 */

export interface SRSResult {
  lessonId:          string;
  nextReviewDate:    Date;
  intervalDays:      number;
  repetitions:       number;
  easeFactor:        number;
}

/**
 * Calculate next review date based on score (SM-2 inspired)
 */
export function calculateNextReview(params: {
  lessonId:   string;
  score:      number;      // 0-100
  repetitions: number;     // times reviewed before
  easeFactor:  number;     // starts at 2.5
}): SRSResult {
  const { lessonId, score, repetitions, easeFactor } = params;

  // Convert score to quality rating (0-5 scale like SM-2)
  const quality = score >= 90 ? 5 : score >= 80 ? 4 : score >= 70 ? 3 : score >= 60 ? 2 : score >= 40 ? 1 : 0;

  // Calculate new ease factor (prevents too-easy intervals)
  const newEase = Math.max(
    1.3,
    easeFactor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
  );

  // Calculate interval
  let intervalDays: number;
  if (quality < 2) {
    // Failed — review tomorrow
    intervalDays = 1;
  } else if (repetitions === 0) {
    intervalDays = 1;
  } else if (repetitions === 1) {
    intervalDays = 3;
  } else {
    // Growing interval: multiply by ease factor
    intervalDays = Math.round((repetitions <= 1 ? 3 : 6) * Math.pow(newEase, repetitions - 1));
    intervalDays = Math.min(intervalDays, 30); // cap at 30 days
  }

  const nextReviewDate = new Date();
  nextReviewDate.setDate(nextReviewDate.getDate() + intervalDays);
  nextReviewDate.setHours(9, 0, 0, 0); // 9 AM next review day

  return {
    lessonId,
    nextReviewDate,
    intervalDays,
    repetitions: quality >= 2 ? repetitions + 1 : 0, // reset if failed
    easeFactor:  newEase,
  };
}

/**
 * Get lessons due for review today
 * Returns lessonIds sorted by urgency (overdue first)
 */
export function getDueForReview(
  lessonProgress: Array<{
    lessonId:     string;
    score?:       number;
    completedAt?: Date | null;
    status:       string;
  }>,
  today = new Date()
): string[] {
  const completed = lessonProgress.filter(
    (p) => p.status === "completed" && p.completedAt
  );

  const due = completed.filter((p) => {
    if (!p.completedAt) return false;
    const daysSince = (today.getTime() - new Date(p.completedAt).getTime()) / 86400000;
    const score     = p.score ?? 0;

    // Determine if due based on score
    const reviewInterval = score >= 90 ? 7 : score >= 80 ? 4 : score >= 60 ? 2 : 1;
    return daysSince >= reviewInterval;
  });

  // Sort: lowest score (needs most review) first
  return due
    .sort((a, b) => (a.score ?? 0) - (b.score ?? 0))
    .map((p) => p.lessonId);
}

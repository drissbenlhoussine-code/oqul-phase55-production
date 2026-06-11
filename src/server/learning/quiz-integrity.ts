export interface QuizExerciseForScoring {
  id: string;
  correctAnswer: string;
  explanation?: string | null;
  points: number;
}

export interface QuizFeedbackItem {
  exerciseId: string;
  correct: boolean;
  yourAnswer: string;
  correctAnswer: string;
  explanation: string | null;
  points: number;
}

export function normalizeAnswer(value: string): string {
  return value
    .normalize("NFKC")
    .replace(/[\u064B-\u065F\u0670]/g, "")
    .replace(/[أإآٱ]/g, "ا")
    .replace(/ؤ/g, "و")
    .replace(/ئ/g, "ي")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}

export function scoreQuizAnswers(
  exercises: QuizExerciseForScoring[],
  answers: Record<string, string>
) {
  let earnedPoints = 0;
  const totalPoints = exercises.reduce((sum, exercise) => sum + exercise.points, 0);

  const feedback: QuizFeedbackItem[] = exercises.map((exercise) => {
    const yourAnswer = answers[exercise.id] ?? "";
    const correct = normalizeAnswer(yourAnswer) === normalizeAnswer(exercise.correctAnswer);
    if (correct) earnedPoints += exercise.points;
    return {
      exerciseId: exercise.id,
      correct,
      yourAnswer,
      correctAnswer: exercise.correctAnswer,
      explanation: exercise.explanation ?? null,
      points: exercise.points,
    };
  });

  const score = totalPoints > 0 ? (earnedPoints / totalPoints) * 100 : 0;
  return {
    score,
    roundedScore: Math.round(score),
    earnedPoints,
    totalPoints,
    passed: score >= 60,
    isPerfect: score === 100,
    feedback,
  };
}

export function calculateQuizXp(earnedPoints: number, isPerfect: boolean): {
  source: "quiz_pass" | "perfect_score";
  xpAmount: number;
} {
  return {
    source: isPerfect ? "perfect_score" : "quiz_pass",
    xpAmount: isPerfect ? 50 : Math.round(earnedPoints * 0.5),
  };
}

export function shouldPreserveCompletedProgress(
  existingStatus: string | undefined,
  nextStatus: "in_progress" | "completed" | "needs_review"
): boolean {
  return existingStatus === "completed" && nextStatus !== "completed";
}

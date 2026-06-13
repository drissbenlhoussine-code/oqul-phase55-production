export interface StudentKnowledgeProfile {
  childId: string;
  strengths: string[];
  weaknesses: string[];
  masteredConcepts: string[];
  strugglingConcepts: string[];
  recentLessons: string[];
  recommendedReview: string[];
  confidenceLevel: "high" | "medium" | "low";
  readinessScore: number;
  riskLevel: "low" | "medium" | "high";
  nextBestActions: string[];
  evidence: {
    completedLessons: number;
    quizAttempts: number;
    weakPoints: number;
    averageScore: number | null;
  };
}

type UnknownRecord = Record<string, unknown>;

function isRecord(value: unknown): value is UnknownRecord {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function asArray(value: unknown): unknown[] {
  return Array.isArray(value) ? value : [];
}

function getString(record: unknown, key: string): string | null {
  if (!isRecord(record)) return null;
  const value = record[key];
  return typeof value === "string" && value.trim().length > 0 ? value.trim() : null;
}

function getNumber(record: unknown, key: string): number | null {
  if (!isRecord(record)) return null;
  const value = record[key];
  if (typeof value === "number" && Number.isFinite(value)) return value;
  if (typeof value === "string" && value.trim() !== "") {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? parsed : null;
  }
  return null;
}

function getNested(record: unknown, key: string): unknown {
  return isRecord(record) ? record[key] : undefined;
}

function lessonTitle(item: unknown): string | null {
  return (
    getString(item, "lessonTitle") ??
    getString(item, "title") ??
    getString(getNested(item, "lesson"), "titleAr") ??
    getString(getNested(item, "lesson"), "title") ??
    getString(item, "lessonId")
  );
}

function conceptFromWeakPoint(item: unknown): string | null {
  return getString(item, "topic") ?? getString(item, "concept") ?? getString(item, "title");
}

function scoreFrom(item: unknown): number | null {
  const raw = getNumber(item, "score") ?? getNumber(item, "percentage") ?? getNumber(item, "averageScore");
  if (raw == null) return null;
  return clamp(raw, 0, 100);
}

function severityFrom(item: unknown): number {
  return clamp(getNumber(item, "severity") ?? 1, 1, 5);
}

function unique(values: Array<string | null | undefined>): string[] {
  return [...new Set(values.filter((value): value is string => Boolean(value && value.trim())))];
}

function average(values: number[]): number | null {
  if (!values.length) return null;
  return values.reduce((sum, value) => sum + value, 0) / values.length;
}

function clamp(value: number, min: number, max: number): number {
  return Math.max(min, Math.min(max, value));
}

function confidenceLevel(readinessScore: number): StudentKnowledgeProfile["confidenceLevel"] {
  if (readinessScore >= 75) return "high";
  if (readinessScore >= 45) return "medium";
  return "low";
}

function riskLevel(readinessScore: number, weakPointCount: number, severeWeakPoints: number): StudentKnowledgeProfile["riskLevel"] {
  if (readinessScore < 45 || weakPointCount >= 5 || severeWeakPoints >= 2) return "high";
  if (readinessScore < 70 || weakPointCount >= 2) return "medium";
  return "low";
}

function sortByRecency(items: unknown[]): unknown[] {
  return [...items].sort((a, b) => {
    const aDate = Date.parse(getString(a, "completedAt") ?? getString(a, "updatedAt") ?? "");
    const bDate = Date.parse(getString(b, "completedAt") ?? getString(b, "updatedAt") ?? "");
    return (Number.isFinite(bDate) ? bDate : 0) - (Number.isFinite(aDate) ? aDate : 0);
  });
}

export function buildStudentKnowledgeProfile(input: {
  childId: string;
  lessonProgress: unknown[];
  quizAttempts: unknown[];
  weakPoints: unknown[];
  learningProfile?: unknown | null;
}): StudentKnowledgeProfile {
  const lessonProgress = asArray(input.lessonProgress);
  const quizAttempts = asArray(input.quizAttempts);
  const weakPoints = asArray(input.weakPoints);

  const completedProgress = lessonProgress.filter((item) => getString(item, "status") === "completed");
  const needsReviewProgress = lessonProgress.filter((item) => getString(item, "status") === "needs_review");
  const progressScores = completedProgress.map(scoreFrom).filter((value): value is number => value != null);
  const quizScores = quizAttempts.map(scoreFrom).filter((value): value is number => value != null);
  const allScores = [...progressScores, ...quizScores];
  const averageScore = average(allScores);

  const weakPointTopics = unique(weakPoints.map(conceptFromWeakPoint));
  const severeWeakPoints = weakPoints.filter((item) => severityFrom(item) >= 3).length;
  const lowQuizAttempts = quizAttempts.filter((item) => (scoreFrom(item) ?? 100) < 60);
  const highQuizAttempts = quizAttempts.filter((item) => (scoreFrom(item) ?? 0) >= 80);

  const completionBonus = Math.min(25, completedProgress.length * 5);
  const scoreBonus = averageScore == null ? 0 : averageScore * 0.35;
  const weakPenalty = Math.min(35, weakPoints.reduce<number>((sum, item) => sum + severityFrom(item) * 5, 0));
  const lowScorePenalty = Math.min(20, lowQuizAttempts.length * 6 + needsReviewProgress.length * 5);
  const profileConfidence = getNumber(input.learningProfile, "confidenceScore");
  const profileAdjustment = profileConfidence == null ? 0 : (clamp(profileConfidence, 0, 100) - 50) * 0.1;

  const readinessScore = Math.round(clamp(
    30 + completionBonus + scoreBonus + profileAdjustment - weakPenalty - lowScorePenalty,
    0,
    100,
  ));

  const masteredConcepts = unique([
    ...completedProgress.map(lessonTitle),
    ...highQuizAttempts.map(lessonTitle),
  ]).slice(0, 8);

  const strugglingConcepts = unique([
    ...weakPointTopics,
    ...needsReviewProgress.map(lessonTitle),
    ...lowQuizAttempts.map(lessonTitle),
  ]).slice(0, 8);

  const strengths = unique([
    ...masteredConcepts.slice(0, 4),
    averageScore != null && averageScore >= 80 ? "Consistent quiz performance" : null,
  ]);

  const weaknesses = strugglingConcepts;
  const recentLessons = unique(sortByRecency(lessonProgress).map(lessonTitle)).slice(0, 5);

  const recommendedReview = unique([
    ...weakPointTopics.slice(0, 5),
    ...needsReviewProgress.map(lessonTitle).slice(0, 3),
    ...lowQuizAttempts.map(lessonTitle).slice(0, 3),
  ]);

  const nextBestActions: string[] = [];
  if (recommendedReview.length > 0) {
    nextBestActions.push(`Review: ${recommendedReview.slice(0, 3).join(", ")}`);
  }
  if (lowQuizAttempts.length > 0 || (averageScore != null && averageScore < 60)) {
    nextBestActions.push("Practice easier exercises before moving forward");
  }
  if (readinessScore >= 75 && weakPoints.length === 0) {
    nextBestActions.push("Try challenge or exam-style exercises");
  }
  if (nextBestActions.length === 0) {
    nextBestActions.push("Complete the next lesson and take a short quiz");
  }

  return {
    childId: input.childId,
    strengths,
    weaknesses,
    masteredConcepts,
    strugglingConcepts,
    recentLessons,
    recommendedReview,
    confidenceLevel: confidenceLevel(readinessScore),
    readinessScore,
    riskLevel: riskLevel(readinessScore, weakPoints.length, severeWeakPoints),
    nextBestActions,
    evidence: {
      completedLessons: completedProgress.length,
      quizAttempts: quizAttempts.length,
      weakPoints: weakPoints.length,
      averageScore: averageScore == null ? null : Math.round(averageScore),
    },
  };
}

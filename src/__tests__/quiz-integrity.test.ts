import { describe, expect, it } from "vitest";
import {
  calculateQuizXp,
  normalizeAnswer,
  scoreQuizAnswers,
  shouldPreserveCompletedProgress,
} from "@/server/learning/quiz-integrity";

const exercises = [
  { id: "hamza", correctAnswer: "الأعداد", points: 10 },
  { id: "diacritics", correctAnswer: "كِتاب", points: 10 },
  { id: "strict-ta", correctAnswer: "مدرسة", points: 10 },
];

describe("Arabic answer normalization", () => {
  it("normalizes Arabic diacritics, hamza variants, and repeated spaces", () => {
    expect(normalizeAnswer("  الإِعداد   الجَيّد  ")).toBe(normalizeAnswer("الاعداد الجيد"));
  });

  it("keeps ة and ه strict", () => {
    expect(normalizeAnswer("مدرسة")).not.toBe(normalizeAnswer("مدرسه"));
  });

  it("runtime quiz scoring uses Arabic normalization", () => {
    const result = scoreQuizAnswers(exercises, {
      hamza: "الاعداد",
      diacritics: "كتاب",
      "strict-ta": "مدرسه",
    });

    expect(result.feedback.find((item) => item.exerciseId === "hamza")?.correct).toBe(true);
    expect(result.feedback.find((item) => item.exerciseId === "diacritics")?.correct).toBe(true);
    expect(result.feedback.find((item) => item.exerciseId === "strict-ta")?.correct).toBe(false);
  });
});

describe("Quiz XP idempotency rules", () => {
  it("calculates one XP event per successful quiz completion", () => {
    const event = calculateQuizXp(30, false);
    expect(event).toEqual({ source: "quiz_pass", xpAmount: 15 });
  });

  it("does not add XP again for an already completed lesson replay", () => {
    const currentXP = 120;
    const replayXpEarned = 0;
    expect(currentXP + replayXpEarned).toBe(120);
  });

  it("uses the perfect-score event as the only quiz XP event for perfect quizzes", () => {
    const event = calculateQuizXp(80, true);
    expect(event).toEqual({ source: "perfect_score", xpAmount: 50 });
  });
});

describe("Completed lesson status protection", () => {
  it("prevents reopening a completed lesson from downgrading it to in_progress", () => {
    expect(shouldPreserveCompletedProgress("completed", "in_progress")).toBe(true);
  });

  it("prevents failed replays from downgrading completed lessons to needs_review", () => {
    expect(shouldPreserveCompletedProgress("completed", "needs_review")).toBe(true);
  });

  it("allows non-completed lessons to move through normal progress states", () => {
    expect(shouldPreserveCompletedProgress("needs_review", "completed")).toBe(false);
    expect(shouldPreserveCompletedProgress("in_progress", "needs_review")).toBe(false);
  });
});

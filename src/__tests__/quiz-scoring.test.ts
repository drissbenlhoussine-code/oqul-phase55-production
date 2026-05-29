import { describe, it, expect } from "vitest";

interface Exercise { id: string; correctAnswer: string; points: number; }

function scoreQuiz(exercises: Exercise[], answers: Record<string, string>) {
  const totalPoints = exercises.reduce((s, e) => s + e.points, 0);
  let earnedPoints = 0;
  const feedback = exercises.map((ex) => {
    const given = answers[ex.id]?.trim().toLowerCase() ?? "";
    const correct = given === ex.correctAnswer.trim().toLowerCase();
    if (correct) earnedPoints += ex.points;
    return { exerciseId: ex.id, correct, points: ex.points };
  });
  const score = totalPoints > 0 ? (earnedPoints / totalPoints) * 100 : 0;
  return { score, earnedPoints, totalPoints, passed: score >= 60, feedback };
}

const exercises: Exercise[] = [
  { id: "e1", correctAnswer: "الألف", points: 10 },
  { id: "e2", correctAnswer: "صحيح",  points: 10 },
  { id: "e3", correctAnswer: "3",     points: 15 },
  { id: "e4", correctAnswer: "باب",   points: 15 },
];

describe("Quiz Scoring", () => {
  it("scores 100% for all correct", () => {
    const r = scoreQuiz(exercises, { e1: "الألف", e2: "صحيح", e3: "3", e4: "باب" });
    expect(r.score).toBe(100);
    expect(r.passed).toBe(true);
    expect(r.earnedPoints).toBe(50);
  });

  it("scores 0 for all wrong", () => {
    const r = scoreQuiz(exercises, { e1: "الباء", e2: "خطأ", e3: "5", e4: "بيت" });
    expect(r.score).toBe(0);
    expect(r.passed).toBe(false);
  });

  it("passes at 60%", () => {
    // e1(10) + e2(10) + e3(15) = 35/50 = 70% ✓
    const r = scoreQuiz(exercises, { e1: "الألف", e2: "صحيح", e3: "3", e4: "غلط" });
    expect(r.score).toBe(70);
    expect(r.passed).toBe(true);
  });

  it("fails below 60%", () => {
    // e1(10) = 20%
    const r = scoreQuiz(exercises, { e1: "الألف" });
    expect(r.score).toBe(20);
    expect(r.passed).toBe(false);
  });

  it("is case-insensitive and trims whitespace", () => {
    const r = scoreQuiz(exercises, { e1: "  الألف  ", e2: "  صحيح  ", e3: " 3 ", e4: "  باب  " });
    expect(r.score).toBe(100);
  });

  it("handles completely missing answers", () => {
    const r = scoreQuiz(exercises, {});
    expect(r.score).toBe(0);
    expect(r.earnedPoints).toBe(0);
  });

  it("handles empty exercises", () => {
    const r = scoreQuiz([], { e1: "anything" });
    expect(r.score).toBe(0);
    expect(r.passed).toBe(false);
    expect(r.feedback).toHaveLength(0);
  });

  it("feedback has correct structure", () => {
    const r = scoreQuiz(exercises, { e1: "الألف", e2: "غلط" });
    expect(r.feedback[0].correct).toBe(true);
    expect(r.feedback[1].correct).toBe(false);
    expect(r.feedback[0].exerciseId).toBe("e1");
  });
});

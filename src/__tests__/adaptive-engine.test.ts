/**
 * Adaptive Engine tests — prioritized learning actions
 */
import { describe, it, expect } from "vitest";

type ProgressItem = {
  status: string;
  score?: number;
  lessonId: string;
  lesson?: { titleAr: string };
};

function analyzeActions(
  progress: ProgressItem[],
  weakPoints: string[],
  streak: number
) {
  const actions: { type: string; priority: number; reason: string }[] = [];

  const needsReview = progress.filter((p) => p.status === "needs_review");
  const inProgress  = progress.filter((p) => p.status === "in_progress");
  const completed   = progress.filter((p) => p.status === "completed");

  // 1. Critical: review failing lessons
  for (const item of needsReview.slice(0, 2)) {
    const score = item.score ?? 0;
    actions.push({ type: "review_lesson", priority: score < 40 ? 1 : 2, reason: `score ${score}%` });
  }

  // 2. Continue in-progress
  for (const item of inProgress.slice(0, 1)) {
    actions.push({ type: "next_lesson", priority: 3, reason: "في المنتصف" });
  }

  // 3. Weak points → ask Leila
  if (weakPoints.length > 0 && actions.length < 3) {
    actions.push({ type: "ask_leila", priority: 4, reason: weakPoints[0] });
  }

  return actions.sort((a, b) => a.priority - b.priority);
}

describe("Adaptive Engine", () => {
  it("prioritizes critical failures first", () => {
    const progress: ProgressItem[] = [
      { status: "needs_review", score: 20, lessonId: "1" },
      { status: "needs_review", score: 65, lessonId: "2" },
    ];
    const actions = analyzeActions(progress, [], 3);
    expect(actions[0].type).toBe("review_lesson");
    expect(actions[0].priority).toBe(1); // score < 40 = critical
  });

  it("continues in-progress before suggesting new lessons", () => {
    const progress: ProgressItem[] = [
      { status: "in_progress", lessonId: "1" },
    ];
    const actions = analyzeActions(progress, [], 1);
    expect(actions[0].type).toBe("next_lesson");
  });

  it("suggests Leila for weak points when no urgent actions", () => {
    const actions = analyzeActions([], ["الكسور"], 5);
    expect(actions[0].type).toBe("ask_leila");
    expect(actions[0].reason).toBe("الكسور");
  });

  it("handles empty state gracefully", () => {
    const actions = analyzeActions([], [], 0);
    expect(actions).toHaveLength(0);
  });

  it("limits to max 4 actions", () => {
    const progress: ProgressItem[] = Array.from({ length: 10 }, (_, i) => ({
      status: "needs_review", score: 30, lessonId: String(i),
    }));
    const actions = analyzeActions(progress, ["topic1", "topic2"], 2);
    expect(actions.length).toBeLessThanOrEqual(4);
  });
});

describe("Engagement Score", () => {
  function engagementScore(streak: number, completed: number, avgScore: number): number {
    return Math.min(100, streak * 15 + Math.min(completed * 5, 50) + (avgScore > 70 ? 20 : 0));
  }

  it("zero engagement for new user", () => {
    expect(engagementScore(0, 0, 0)).toBe(0);
  });

  it("streak contributes 15 points per day", () => {
    expect(engagementScore(3, 0, 0)).toBe(45);
  });

  it("caps at 100", () => {
    expect(engagementScore(10, 20, 85)).toBe(100);
  });

  it("high avg score adds 20 points", () => {
    expect(engagementScore(0, 0, 75)).toBe(20);
    expect(engagementScore(0, 0, 70)).toBe(0);
  });
});

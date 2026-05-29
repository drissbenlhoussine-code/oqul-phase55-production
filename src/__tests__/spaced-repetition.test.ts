/**
 * Spaced Repetition tests — the science of remembering
 */
import { describe, it, expect } from "vitest";
import { calculateNextReview, getDueForReview } from "@/server/services/spaced-repetition";

describe("calculateNextReview (SM-2 based)", () => {
  it("perfect score (100%) schedules review in 7 days", () => {
    const result = calculateNextReview({ lessonId: "l1", score: 100, repetitions: 1, easeFactor: 2.5 });
    expect(result.intervalDays).toBeGreaterThanOrEqual(3);
  });

  it("failing score (<60%) schedules review tomorrow", () => {
    const result = calculateNextReview({ lessonId: "l1", score: 40, repetitions: 0, easeFactor: 2.5 });
    expect(result.intervalDays).toBe(1);
  });

  it("first repetition always 1 day", () => {
    const result = calculateNextReview({ lessonId: "l1", score: 80, repetitions: 0, easeFactor: 2.5 });
    expect(result.intervalDays).toBe(1);
  });

  it("intervals grow with successful repetitions", () => {
    const r1 = calculateNextReview({ lessonId: "l1", score: 85, repetitions: 1, easeFactor: 2.5 });
    const r2 = calculateNextReview({ lessonId: "l1", score: 85, repetitions: 2, easeFactor: r1.easeFactor });
    const r3 = calculateNextReview({ lessonId: "l1", score: 85, repetitions: 3, easeFactor: r2.easeFactor });
    expect(r2.intervalDays).toBeGreaterThan(r1.intervalDays);
    expect(r3.intervalDays).toBeGreaterThan(r2.intervalDays);
  });

  it("caps maximum interval at 30 days", () => {
    const result = calculateNextReview({ lessonId: "l1", score: 100, repetitions: 10, easeFactor: 3.0 });
    expect(result.intervalDays).toBeLessThanOrEqual(30);
  });

  it("failed review resets repetition count to 0", () => {
    const result = calculateNextReview({ lessonId: "l1", score: 30, repetitions: 5, easeFactor: 2.5 });
    expect(result.repetitions).toBe(0);
  });

  it("ease factor decreases after failure (lesson gets shorter intervals)", () => {
    const good = calculateNextReview({ lessonId: "l1", score: 100, repetitions: 1, easeFactor: 2.5 });
    const bad  = calculateNextReview({ lessonId: "l1", score: 40,  repetitions: 1, easeFactor: 2.5 });
    expect(bad.easeFactor).toBeLessThan(good.easeFactor);
  });

  it("ease factor never drops below 1.3", () => {
    const result = calculateNextReview({ lessonId: "l1", score: 0, repetitions: 5, easeFactor: 1.3 });
    expect(result.easeFactor).toBeGreaterThanOrEqual(1.3);
  });
});

describe("getDueForReview", () => {
  const yesterday = new Date(Date.now() - 86400000 * 2);
  const lastWeek  = new Date(Date.now() - 86400000 * 8);
  const today     = new Date();

  it("returns lessons completed long ago with low scores as due", () => {
    const progress = [
      { lessonId: "l1", score: 50, completedAt: lastWeek, status: "completed" },
    ];
    const due = getDueForReview(progress);
    expect(due).toContain("l1");
  });

  it("does not return recently completed high-score lessons", () => {
    const progress = [
      { lessonId: "l1", score: 95, completedAt: yesterday, status: "completed" },
    ];
    const due = getDueForReview(progress);
    expect(due).not.toContain("l1");
  });

  it("sorts by lowest score first (worst knowledge = highest urgency)", () => {
    const progress = [
      { lessonId: "l1", score: 80, completedAt: lastWeek, status: "completed" },
      { lessonId: "l2", score: 55, completedAt: lastWeek, status: "completed" },
    ];
    const due = getDueForReview(progress);
    expect(due[0]).toBe("l2"); // lowest score first
  });

  it("ignores in-progress and not-started lessons", () => {
    const progress = [
      { lessonId: "l1", score: undefined, completedAt: null, status: "in_progress" },
      { lessonId: "l2", score: undefined, completedAt: null, status: "not_started" },
    ];
    expect(getDueForReview(progress)).toHaveLength(0);
  });

  it("score 90%+ needs review after 7 days (not before)", () => {
    const fiveDaysAgo = new Date(Date.now() - 86400000 * 5);
    const progress = [{ lessonId: "l1", score: 95, completedAt: fiveDaysAgo, status: "completed" }];
    expect(getDueForReview(progress)).not.toContain("l1");
  });
});

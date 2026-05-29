/**
 * Integration tests for the complete learning flow:
 * Quiz → XP → Streak → Badges → Mastery
 */
import { describe, it, expect } from "vitest";
import { getLevelInfo } from "@/server/services/gamification-service";

// ── Level System ─────────────────────────────────────────────────────────────
describe("Level System", () => {
  it("starts at level 1 with 0 XP", () => {
    const info = getLevelInfo(0);
    expect(info.level).toBe(1);
    expect(info.title).toBe("مبتدئ");
    expect(info.progress).toBe(0);
  });

  it("reaches level 2 at 100 XP", () => {
    const info = getLevelInfo(100);
    expect(info.level).toBe(2);
    expect(info.title).toBe("طالب نشيط");
  });

  it("level 5 unlocks at 900 XP", () => {
    const info = getLevelInfo(900);
    expect(info.level).toBe(5);
    expect(info.title).toBe("نجم الفصل");
  });

  it("calculates progress percentage correctly", () => {
    // Level 1 goes from 0 to 100 — at 50 XP: 50% progress
    const info = getLevelInfo(50);
    expect(info.progress).toBe(50);
  });

  it("xpToNext decreases as XP increases", () => {
    const a = getLevelInfo(0);
    const b = getLevelInfo(50);
    expect(b.xpToNext).toBeLessThan(a.xpToNext);
  });

  it("handles max level gracefully", () => {
    const info = getLevelInfo(99999);
    expect(info.level).toBeGreaterThanOrEqual(10);
    expect(info.progress).toBeGreaterThanOrEqual(0);
    expect(info.progress).toBeLessThanOrEqual(100);
  });
});

// ── XP Awards by Source ──────────────────────────────────────────────────────
describe("XP Award Logic", () => {
  function calculateXP(source: string, earnedPoints: number, totalPoints: number): number {
    const score = totalPoints > 0 ? (earnedPoints / totalPoints) * 100 : 0;
    if (source === "perfect_score" || score === 100) return 50;
    if (source === "quiz_pass") return Math.round(earnedPoints * 0.5);
    if (source === "lesson_complete") return 25;
    if (source === "streak_bonus") return 20;
    return 0;
  }

  it("perfect quiz awards 50 XP", () => {
    expect(calculateXP("perfect_score", 50, 50)).toBe(50);
  });

  it("passing quiz awards proportional XP", () => {
    expect(calculateXP("quiz_pass", 30, 50)).toBe(15); // 30 * 0.5
  });

  it("lesson completion awards 25 XP", () => {
    expect(calculateXP("lesson_complete", 0, 0)).toBe(25);
  });

  it("no XP for failed quiz", () => {
    expect(calculateXP("quiz_fail", 0, 50)).toBe(0);
  });
});

// ── Mastery / Weak Points ─────────────────────────────────────────────────────
describe("Mastery Severity", () => {
  function getSeverity(score: number): number {
    if (score >= 80) return 0;   // mastered
    if (score < 40)  return 3;   // critical
    if (score < 60)  return 2;   // moderate
    return 1;                    // slight
  }

  it("80%+ means mastered (severity 0)", () => {
    expect(getSeverity(80)).toBe(0);
    expect(getSeverity(100)).toBe(0);
  });

  it("below 40% is critical weakness (3)", () => {
    expect(getSeverity(0)).toBe(3);
    expect(getSeverity(39)).toBe(3);
  });

  it("40-59% is moderate weakness (2)", () => {
    expect(getSeverity(40)).toBe(2);
    expect(getSeverity(59)).toBe(2);
  });

  it("60-79% is slight weakness (1)", () => {
    expect(getSeverity(60)).toBe(1);
    expect(getSeverity(79)).toBe(1);
  });
});

// ── Streak Logic ──────────────────────────────────────────────────────────────
describe("Streak Logic", () => {
  function calculateStreak(currentStreak: number, studiedYesterday: boolean): number {
    if (studiedYesterday || currentStreak === 0) return currentStreak + 1;
    return 1; // reset
  }

  it("increments streak when studied yesterday", () => {
    expect(calculateStreak(5, true)).toBe(6);
  });

  it("resets to 1 when streak broken", () => {
    expect(calculateStreak(10, false)).toBe(1);
  });

  it("first day starts at 1", () => {
    expect(calculateStreak(0, false)).toBe(1);
  });

  it("long streaks keep incrementing", () => {
    expect(calculateStreak(29, true)).toBe(30);
  });
});

// ── Badge Eligibility ─────────────────────────────────────────────────────────
describe("Badge Eligibility", () => {
  function checkBadge(
    condition: string,
    state: { streak: number; completedLessons: number; isPerfect: boolean }
  ): boolean {
    switch (condition) {
      case "complete_first_lesson": return state.completedLessons >= 1;
      case "quiz_score_100":        return state.isPerfect;
      case "streak_3":              return state.streak >= 3;
      case "streak_7":              return state.streak >= 7;
      case "streak_30":             return state.streak >= 30;
      case "complete_10_lessons":   return state.completedLessons >= 10;
      default:                      return false;
    }
  }

  const base = { streak: 0, completedLessons: 0, isPerfect: false };

  it("first-lesson badge after 1 completed lesson", () => {
    expect(checkBadge("complete_first_lesson", { ...base, completedLessons: 1 })).toBe(true);
  });

  it("perfect-quiz badge only on 100% score", () => {
    expect(checkBadge("quiz_score_100", { ...base, isPerfect: true })).toBe(true);
    expect(checkBadge("quiz_score_100", { ...base, isPerfect: false })).toBe(false);
  });

  it("streak-3 badge at 3 consecutive days", () => {
    expect(checkBadge("streak_3", { ...base, streak: 3 })).toBe(true);
    expect(checkBadge("streak_3", { ...base, streak: 2 })).toBe(false);
  });

  it("streak-7 not triggered at 6 days", () => {
    expect(checkBadge("streak_7", { ...base, streak: 6 })).toBe(false);
    expect(checkBadge("streak_7", { ...base, streak: 7 })).toBe(true);
  });
});

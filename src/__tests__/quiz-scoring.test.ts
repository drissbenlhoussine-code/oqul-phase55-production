import { describe, it, expect } from "vitest";

// ── normalizeAnswer (mirrors src/app/api/progress/quiz/route.ts) ──────────────
function normalizeAnswer(s: string): string {
  return s
    .trim()
    .replace(/[ً-ْ]/g, "")  // strip diacritics
    .replace(/[أإآٱ]/g, "ا")           // unify hamza variants
    .replace(/\s+/g, " ");             // collapse spaces
}

interface Exercise { id: string; correctAnswer: string; points: number; }

function scoreQuiz(exercises: Exercise[], answers: Record<string, string>) {
  const totalPoints = exercises.reduce((s, e) => s + e.points, 0);
  let earnedPoints = 0;
  const feedback = exercises.map((ex) => {
    const given   = normalizeAnswer(answers[ex.id] ?? "");
    const correct = given === normalizeAnswer(ex.correctAnswer);
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

// ── Basic scoring ─────────────────────────────────────────────────────────────
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
    const r = scoreQuiz(exercises, { e1: "الألف", e2: "صحيح", e3: "3", e4: "غلط" });
    expect(r.score).toBe(70);
    expect(r.passed).toBe(true);
  });

  it("fails below 60%", () => {
    const r = scoreQuiz(exercises, { e1: "الألف" });
    expect(r.score).toBe(20);
    expect(r.passed).toBe(false);
  });

  it("trims whitespace", () => {
    const r = scoreQuiz(exercises, { e1: "  الألف  ", e2: "  صحيح  ", e3: " 3 ", e4: "  باب  " });
    expect(r.score).toBe(100);
  });

  it("handles missing answers", () => {
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

// ── Arabic normalization ───────────────────────────────────────────────────────
describe("normalizeAnswer — Arabic normalization", () => {
  it("strips diacritics (tashkeel)", () => {
    expect(normalizeAnswer("مَدرسة")).toBe(normalizeAnswer("مدرسة"));
    expect(normalizeAnswer("كِتَابٌ")).toBe(normalizeAnswer("كتاب"));
  });

  it("unifies hamza variants (أإآٱ → ا)", () => {
    expect(normalizeAnswer("إسلام")).toBe(normalizeAnswer("اسلام"));
    expect(normalizeAnswer("أحمد")).toBe(normalizeAnswer("احمد"));
    expect(normalizeAnswer("آمن")).toBe(normalizeAnswer("امن"));
  });

  it("collapses multiple spaces", () => {
    expect(normalizeAnswer("كلمة  واحدة")).toBe("كلمة واحدة");
  });

  it("student with tashkeel scores correctly against answer without", () => {
    const ex: Exercise[] = [{ id: "x", correctAnswer: "مدرسة", points: 10 }];
    const r = scoreQuiz(ex, { x: "مَدرسة" });
    expect(r.feedback[0].correct).toBe(true);
  });

  it("student using ا scores correctly when answer uses أ", () => {
    const ex: Exercise[] = [{ id: "x", correctAnswer: "أستاذ", points: 10 }];
    const r = scoreQuiz(ex, { x: "استاذ" });
    expect(r.feedback[0].correct).toBe(true);
  });

  it("ة vs ه stays strict — wrong letter is still wrong", () => {
    const ex: Exercise[] = [{ id: "x", correctAnswer: "مدرسة", points: 10 }];
    const r = scoreQuiz(ex, { x: "مدرسه" });
    expect(r.feedback[0].correct).toBe(false);
  });

  it("ة vs ت stays strict — taa maftouha is still wrong for taa marbuta", () => {
    const ex: Exercise[] = [{ id: "x", correctAnswer: "معلمة", points: 10 }];
    const r = scoreQuiz(ex, { x: "معلمت" });
    expect(r.feedback[0].correct).toBe(false);
  });
});

// ── Duplicate XP / idempotency logic ─────────────────────────────────────────
describe("XP idempotency (unit-level logic)", () => {
  it("alreadyCompleted=true prevents gamification", () => {
    // Simulates quiz route logic: if alreadyCompleted, gamification is null
    const alreadyCompleted = true;
    const passed = true;
    let gamification = null;
    if (passed && !alreadyCompleted) {
      gamification = { xpEarned: 50 };
    }
    expect(gamification).toBeNull();
  });

  it("alreadyCompleted=false allows gamification on first pass", () => {
    const alreadyCompleted = false;
    const passed = true;
    let gamification = null;
    if (passed && !alreadyCompleted) {
      gamification = { xpEarned: 50 };
    }
    expect(gamification).not.toBeNull();
    expect(gamification!.xpEarned).toBe(50);
  });

  it("failed quiz never triggers gamification regardless of alreadyCompleted", () => {
    for (const alreadyCompleted of [true, false]) {
      const passed = false;
      let gamification = null;
      if (passed && !alreadyCompleted) {
        gamification = { xpEarned: 10 };
      }
      expect(gamification).toBeNull();
    }
  });
});

// ── Completed lesson status protection ────────────────────────────────────────
describe("upsertLessonProgress — no downgrade from completed", () => {
  function simulateUpsert(
    existingStatus: string | null,
    newStatus: string
  ): string {
    if (existingStatus === "completed" && newStatus !== "completed") {
      return existingStatus; // guard: do not downgrade
    }
    return newStatus;
  }

  it("completed lesson stays completed when resubmitted as needs_review", () => {
    expect(simulateUpsert("completed", "needs_review")).toBe("completed");
  });

  it("completed lesson stays completed when resubmitted as in_progress", () => {
    expect(simulateUpsert("completed", "in_progress")).toBe("completed");
  });

  it("needs_review can be upgraded to completed", () => {
    expect(simulateUpsert("needs_review", "completed")).toBe("completed");
  });

  it("in_progress can be set to needs_review", () => {
    expect(simulateUpsert("in_progress", "needs_review")).toBe("needs_review");
  });

  it("new lesson (no existing) gets the provided status", () => {
    expect(simulateUpsert(null, "completed")).toBe("completed");
    expect(simulateUpsert(null, "needs_review")).toBe("needs_review");
  });
});

// ── Streak idempotency ────────────────────────────────────────────────────────
describe("Streak idempotency — once per day", () => {
  function simulateStreak(alreadyHadToday: boolean, currentStreak: number, hadYesterday: boolean): number {
    if (alreadyHadToday) return currentStreak; // idempotent: no increment
    return (hadYesterday || currentStreak === 0) ? currentStreak + 1 : 1;
  }

  it("does not increment streak when called twice on same day", () => {
    const afterFirst  = simulateStreak(false, 3, true); // 4
    const afterSecond = simulateStreak(true,  4, true); // still 4
    expect(afterFirst).toBe(4);
    expect(afterSecond).toBe(4);
  });

  it("increments on first call of the day", () => {
    expect(simulateStreak(false, 5, true)).toBe(6);
  });

  it("resets to 1 when streak is broken", () => {
    expect(simulateStreak(false, 5, false)).toBe(1);
  });

  it("starts at 1 for new child (currentStreak = 0)", () => {
    expect(simulateStreak(false, 0, false)).toBe(1);
  });
});

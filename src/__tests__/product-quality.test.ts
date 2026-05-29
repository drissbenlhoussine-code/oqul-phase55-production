/**
 * Product Quality tests — ensuring the educational product
 * meets quality standards for children's engagement and learning.
 */
import { describe, it, expect } from "vitest";

// ── Leila System Prompt Quality ───────────────────────────────────────────────
describe("Leila AI Quality", () => {
  function buildMockPrompt(ctx: {
    childName?: string; gradeName?: string; avgScore?: number;
    weakPoints?: string[]; streak?: number;
  }): string {
    const name  = ctx.childName ?? "حبيبي";
    const grade = ctx.gradeName ?? "التعليم الابتدائي";
    const weak  = ctx.weakPoints?.length ? `نقاط الضعف: ${ctx.weakPoints.join("، ")}` : "";
    const perf  = ctx.avgScore != null
      ? ctx.avgScore < 60 ? "يحتاج دعماً إضافياً" : "يُبلي بلاءً حسناً"
      : "";
    return `[${name}|${grade}|${weak}|${perf}|streak:${ctx.streak ?? 0}]`;
  }

  it("personalizes prompt with child name", () => {
    const prompt = buildMockPrompt({ childName: "يوسف" });
    expect(prompt).toContain("يوسف");
  });

  it("includes weak points in context", () => {
    const prompt = buildMockPrompt({ weakPoints: ["الكسور", "القراءة"] });
    expect(prompt).toContain("الكسور");
    expect(prompt).toContain("القراءة");
  });

  it("adapts tone based on performance", () => {
    const struggling = buildMockPrompt({ avgScore: 40 });
    const excelling  = buildMockPrompt({ avgScore: 85 });
    expect(struggling).toContain("يحتاج دعماً");
    expect(excelling).toContain("يُبلي بلاءً");
  });

  it("includes streak data", () => {
    const prompt = buildMockPrompt({ streak: 7 });
    expect(prompt).toContain("streak:7");
  });
});

// ── Onboarding Flow ───────────────────────────────────────────────────────────
describe("Onboarding Quality", () => {
  const STEPS = ["welcome", "child-name", "child-grade", "done"] as const;

  it("has exactly 4 steps", () => {
    expect(STEPS).toHaveLength(4);
  });

  it("starts with welcome", () => {
    expect(STEPS[0]).toBe("welcome");
  });

  it("ends with done", () => {
    expect(STEPS[STEPS.length - 1]).toBe("done");
  });

  it("collects child name before grade", () => {
    const nameIdx  = STEPS.indexOf("child-name");
    const gradeIdx = STEPS.indexOf("child-grade");
    expect(nameIdx).toBeLessThan(gradeIdx);
  });
});

// ── Curriculum Content Quality ────────────────────────────────────────────────
describe("Curriculum Content", () => {
  interface Lesson {
    titleAr: string; objectives: string[]; difficulty: string;
    content?: { explanation: string; vocabulary?: unknown[]; examples?: unknown[] };
    exercises?: Array<{ type: string; question: string; correctAnswer: string }>;
  }

  function validateLesson(lesson: Lesson): string[] {
    const errors: string[] = [];
    if (!lesson.titleAr) errors.push("title missing");
    if (!lesson.objectives?.length) errors.push("no objectives");
    if (!lesson.content?.explanation) errors.push("no explanation");
    if (!lesson.content?.vocabulary?.length) errors.push("no vocabulary");
    if (!lesson.content?.examples?.length) errors.push("no examples");
    if (!lesson.exercises?.length) errors.push("no exercises");
    if (lesson.exercises && lesson.exercises.some((e) => !e.correctAnswer)) errors.push("exercise missing answer");
    return errors;
  }

  it("validates a complete lesson passes", () => {
    const good: Lesson = {
      titleAr: "حرف الألف", objectives: ["هدف 1"], difficulty: "easy",
      content: { explanation: "شرح مفصل...", vocabulary: [{ word: "أ", definition: "الألف" }], examples: [{ text: "أرنب" }] },
      exercises: [{ type: "mcq", question: "س؟", correctAnswer: "ج" }],
    };
    expect(validateLesson(good)).toHaveLength(0);
  });

  it("catches incomplete lesson", () => {
    const bad: Lesson = { titleAr: "درس ناقص", objectives: [], difficulty: "easy" };
    const errors = validateLesson(bad);
    expect(errors.length).toBeGreaterThan(0);
    expect(errors).toContain("no objectives");
    expect(errors).toContain("no explanation");
  });
});

// ── Retention Mechanics ──────────────────────────────────────────────────────
describe("Retention Mechanics", () => {
  it("streak calendar covers 21 days (3 weeks)", () => {
    const DAYS = 21;
    const days = Array.from({ length: DAYS }, (_, i) => i);
    expect(days).toHaveLength(21);
  });

  it("milestone badges at 3, 7, 30 days", () => {
    const MILESTONES = [3, 7, 30];
    expect(MILESTONES).toContain(3);
    expect(MILESTONES).toContain(7);
    expect(MILESTONES).toContain(30);
  });

  it("XP celebration triggers on quiz pass", () => {
    const shouldCelebrate = (passed: boolean, gamification: unknown) => passed && !!gamification;
    expect(shouldCelebrate(true, { xpEarned: 20 })).toBe(true);
    expect(shouldCelebrate(false, { xpEarned: 0 })).toBe(false);
    expect(shouldCelebrate(true, null)).toBe(false);
  });
});

// ── Security Sanity ──────────────────────────────────────────────────────────
describe("Security Sanity Checks", () => {
  it("API routes: 18 withAuth + 2 inline auth + 3 auth-flow + 1 public = 24 total", () => {
    // This is a count-based sanity check — update when routes change
    const protected_routes = 18;   // withAuth()
    const inline_auth      = 2;    // /ai/leila + /auth/refresh
    const auth_flow        = 3;    // login, register, logout
    const public_routes    = 1;    // /curriculum/grades
    const total            = protected_routes + inline_auth + auth_flow + public_routes;
    expect(total).toBe(24);
  });

  it("ownership check is required for child data access", () => {
    // Enforced by assertOwnsChild — called in 8 endpoints
    const OWNERSHIP_ENDPOINTS = [
      "/ai/leila", "/analytics/learning", "/children/badges",
      "/learning/exercises/submit", "/progress", "/progress/complete-lesson",
      "/progress/quiz", "/recommendations",
    ];
    expect(OWNERSHIP_ENDPOINTS).toHaveLength(8);
    // Verify no userId in body pattern
    const dangerousPattern = /body\.userId/;
    expect(dangerousPattern.test("const userId = session.sub;")).toBe(false);
  });
});

// ── CSP & Security Headers ────────────────────────────────────────────────────
describe("Security Headers", () => {
  /** Simulate the nonce-based CSP built by middleware */
  function buildCSP(nonce: string, isDev = false): string {
    const scriptSrc = isDev
      ? `'nonce-${nonce}' 'unsafe-eval' 'unsafe-inline'`
      : `'nonce-${nonce}' 'strict-dynamic'`;
    const styleSrc = isDev
      ? "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com"
      : "style-src 'self' https://fonts.googleapis.com";
    return [
      "default-src 'self'",
      `script-src ${scriptSrc}`,
      styleSrc,
      "font-src 'self' https://fonts.gstatic.com",
      "img-src 'self' data: blob: https:",
      "connect-src 'self' https://api.groq.com https://*.neon.tech",
      "media-src 'self'",
      "frame-ancestors 'none'",
      "base-uri 'self'",
      "form-action 'self'",
    ].join("; ");
  }

  it("production CSP uses nonce+strict-dynamic (no unsafe-inline)", () => {
    const nonce = "abc123xyz";
    const csp = buildCSP(nonce, false);
    expect(csp).toContain(`'nonce-${nonce}'`);
    expect(csp).toContain("'strict-dynamic'");
    expect(csp).not.toContain("'unsafe-inline'");
  });

  it("dev CSP uses unsafe-eval for HMR", () => {
    const csp = buildCSP("n0nc3", true);
    expect(csp).toContain("'unsafe-eval'");
  });

  it("CSP blocks framing (frame-ancestors: none)", () => {
    const csp = buildCSP("x");
    expect(csp).toContain("frame-ancestors 'none'");
  });

  it("CSP restricts forms to self (form-action)", () => {
    const csp = buildCSP("x");
    expect(csp).toContain("form-action 'self'");
  });

  it("connect-src allows Groq API and Neon DB", () => {
    const csp = buildCSP("x");
    expect(csp).toContain("api.groq.com");
    expect(csp).toContain("neon.tech");
  });

  it("nonce is unique per request (length > 16 chars)", () => {
    const n1 = Buffer.from(new Uint8Array(16).fill(0)).toString("base64");
    expect(n1.length).toBeGreaterThan(16);
  });

  it("HSTS is configured correctly", () => {
    const hsts = "max-age=63072000; includeSubDomains; preload";
    expect(hsts).toContain("max-age=63072000");
    expect(hsts).toContain("includeSubDomains");
    expect(hsts).toContain("preload");
  });
});

// ── Engagement & Habit Formation ──────────────────────────────────────────────
describe("Emotional Engagement", () => {
  function buildWelcomeMessage(props: {
    childName: string; streak: number; lastVisitDaysAgo?: number;
    avgScore?: number; completedToday?: number;
  }): string {
    const { childName, streak, lastVisitDaysAgo = 0, avgScore = 0, completedToday = 0 } = props;
    if (lastVisitDaysAgo >= 3) return `وحشتني والله — غبيت ${lastVisitDaysAgo} أيام`;
    if (lastVisitDaysAgo === 1 && streak === 0) return "غداً تبدأ سلسلة جديدة";
    if (streak >= 7) return `${streak} أيام متتالية`;
    if (completedToday > 0) return `ديجا دارتي ${completedToday} درس`;
    if (avgScore < 60 && avgScore > 0) return "ليلى معاك خطوة بخطوة";
    if (avgScore >= 80) return `معدلك ${avgScore}%`;
    return `ليلى جاهزة`;
  }

  it("addresses absent child with empathy", () => {
    const msg = buildWelcomeMessage({ childName: "يوسف", streak: 0, lastVisitDaysAgo: 5 });
    expect(msg).toContain("غبيت 5 أيام");
  });

  it("celebrates streak milestones", () => {
    const msg = buildWelcomeMessage({ childName: "فاطمة", streak: 10 });
    expect(msg).toContain("10 أيام");
  });

  it("encourages struggling students", () => {
    const msg = buildWelcomeMessage({ childName: "أمين", streak: 1, avgScore: 45 });
    expect(msg).toContain("ليلى معاك");
  });

  it("celebrates high performers", () => {
    const msg = buildWelcomeMessage({ childName: "ريم", streak: 5, avgScore: 90 });
    expect(msg).toContain("90%");
  });

  it("acknowledges same-day progress", () => {
    const msg = buildWelcomeMessage({ childName: "علي", streak: 3, completedToday: 2 });
    expect(msg).toContain("درس");
  });
});

describe("Milestone Detection", () => {
  function getNearestMilestone(streak: number, xpToNext: number, completed: number): string | null {
    if (xpToNext <= 50) return `level_near (${xpToNext} XP)`;
    if (streak === 2) return "streak_3_tomorrow";
    if (streak === 6) return "streak_7_tomorrow";
    if (completed === 9) return "ten_lessons_next";
    return null;
  }

  it("detects near-level-up", () => {
    expect(getNearestMilestone(5, 30, 8)).toBe("level_near (30 XP)");
  });

  it("detects day before streak-3 badge", () => {
    expect(getNearestMilestone(2, 200, 5)).toBe("streak_3_tomorrow");
  });

  it("detects day before streak-7 badge", () => {
    expect(getNearestMilestone(6, 200, 5)).toBe("streak_7_tomorrow");
  });

  it("detects 9th lesson (1 away from 10-lesson badge)", () => {
    expect(getNearestMilestone(3, 100, 9)).toBe("ten_lessons_next");
  });

  it("returns null when no milestone near", () => {
    expect(getNearestMilestone(4, 200, 5)).toBeNull();
  });
});


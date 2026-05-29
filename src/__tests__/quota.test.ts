import { describe, it, expect } from "vitest";

type Plan = "free" | "basic" | "advanced";
type Feature = "leila_text" | "leila_voice" | "quiz" | "lesson";

const LIMITS: Record<Plan, Record<Feature, number>> = {
  free:     { leila_text: 30, leila_voice: 0,  quiz: 50,  lesson: 200 },
  basic:    { leila_text: 100, leila_voice: 20, quiz: 200, lesson: 2000 },
  advanced: { leila_text: 200, leila_voice: 50, quiz: 500, lesson: 10000 },
};

function checkQuota(plan: Plan, feature: Feature, used: number) {
  const limit = LIMITS[plan][feature];
  if (limit === 0) return { allowed: false, reason: "not_in_plan", remaining: 0 };
  if (used >= limit) return { allowed: false, reason: "limit_reached", remaining: 0 };
  return { allowed: true, reason: null, remaining: limit - used };
}

describe("Quota Enforcement", () => {
  it("free plan: allows leila_text within limit", () => {
    expect(checkQuota("free", "leila_text", 0).allowed).toBe(true);
    expect(checkQuota("free", "leila_text", 29).allowed).toBe(true);
  });

  it("free plan: blocks at exact limit", () => {
    const r = checkQuota("free", "leila_text", 30);
    expect(r.allowed).toBe(false);
    expect(r.reason).toBe("limit_reached");
    expect(r.remaining).toBe(0);
  });

  it("free plan: voice is never allowed", () => {
    const r = checkQuota("free", "leila_voice", 0);
    expect(r.allowed).toBe(false);
    expect(r.reason).toBe("not_in_plan");
  });

  it("advanced plan: higher limits", () => {
    expect(checkQuota("advanced", "leila_text", 150).allowed).toBe(true);
    expect(checkQuota("advanced", "leila_text", 200).allowed).toBe(false);
  });

  it("calculates remaining correctly", () => {
    expect(checkQuota("free", "leila_text", 20).remaining).toBe(10);
    expect(checkQuota("advanced", "leila_text", 50).remaining).toBe(150);
  });
});

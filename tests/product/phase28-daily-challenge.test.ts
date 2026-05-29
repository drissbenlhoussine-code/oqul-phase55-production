import { describe, expect, it } from "vitest";
import { generateDailyChallenge } from "@/server/daily-challenges/challenge-generator";

describe("Phase 28 daily challenge", () => {
  it("creates a short habit-forming challenge", () => {
    const challenge = generateDailyChallenge({ grade: 1, subject: "math" });

    expect(challenge.estimatedMinutes).toBeLessThanOrEqual(5);
    expect(challenge.prompt.length).toBeGreaterThan(10);
    expect(challenge.rewardPoints).toBeGreaterThan(0);
  });
});

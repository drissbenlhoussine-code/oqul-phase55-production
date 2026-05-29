import { describe, expect, it } from "vitest";
import {
  buildEmotionAwareTeachingHint,
  chooseExampleContext,
  mergeEmotionalPreferences,
} from "@/server/leila-memory/emotional-memory-engine";

describe("Phase 28 emotional memory", () => {
  it("uses child preferences for explanation context", () => {
    expect(chooseExampleContext({ preferredExamples: ["football"] })).toBe("football");
  });

  it("builds gentle hint for frustration", () => {
    const hint = buildEmotionAwareTeachingHint({
      childName: "يوسف",
      preferredExamples: ["football"],
      recentEmotion: "frustrated",
    });

    expect(hint).toContain("يوسف");
    expect(hint).toContain("نرجعو خطوة");
  });

  it("merges emotional preferences safely", () => {
    const merged = mergeEmotionalPreferences({
      currentPreferredExamples: ["football"],
      newPreferredExample: "food",
    });

    expect(merged).toContain("football");
    expect(merged).toContain("food");
  });
});

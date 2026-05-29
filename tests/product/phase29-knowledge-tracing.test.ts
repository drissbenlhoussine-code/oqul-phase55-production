import { describe, expect, it } from "vitest";
import { KnowledgeTracingEngine } from "../../src/server/adaptive-learning/knowledge-tracing-engine";

describe("phase29 knowledge tracing", () => {
  it("improves mastery after successful answers", () => {
    const engine = new KnowledgeTracingEngine();

    const result = engine.update(
      {
        skillId: "fractions",
        mastery: 0.4,
        confidence: 0.5,
        misconceptionRisk: 0.3,
      },
      true,
    );

    expect(result.mastery).toBeGreaterThan(0.4);
  });
});

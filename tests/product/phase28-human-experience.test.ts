import { describe, expect, it } from "vitest";
import { buildLeilaNoticedNote } from "@/server/leila-notes/leila-noticed-engine";
import { explainLikeHome } from "@/server/contextual-learning/moroccan-context-examples";
import { buildParentJournalSummary } from "@/server/parent/parent-journal-engine";
import { createAdventureNode, buildAdventureReward } from "@/server/adventure-map/adventure-map-engine";

describe("Phase 28 human learning experience", () => {
  it("creates personal Leila noticed notes", () => {
    const note = buildLeilaNoticedNote({
      childName: "يوسف",
      weaknesses: ["الطرح مع الاحتفاظ"],
    });

    expect(note).toContain("يوسف");
    expect(note).toContain("الطرح مع الاحتفاظ");
  });

  it("uses Moroccan everyday examples", () => {
    expect(explainLikeHome({ topic: "money", childName: "آدم" })).toContain("آدم");
  });

  it("summarizes parent journal simply", () => {
    const summary = buildParentJournalSummary({
      learnedToday: ["الجمع"],
      struggledWith: ["الطرح"],
    });

    expect(summary.leilaSuggestion).toContain("5 دقائق");
  });

  it("creates adventure map nodes", () => {
    const node = createAdventureNode({ grade: 1, subject: "math", title: "الجمع", order: 1 });
    expect(node.world).toBeTruthy();
    expect(buildAdventureReward({ completed: true, stars: 3 })).toContain("3 نجوم");
  });
});

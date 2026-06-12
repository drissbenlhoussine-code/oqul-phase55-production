import { describe, expect, it } from "vitest";
import { buildExamIntelligence } from "@/server/curriculum/exam-intelligence";
import type { CurriculumKnowledge } from "@/server/curriculum/knowledge-engine";

function highKnowledge(overrides: Partial<CurriculumKnowledge> = {}): CurriculumKnowledge {
  return {
    lessonId: "lesson-exam-1",
    title: "Les déterminants",
    cycle: "الإعدادي",
    grade: "الأولى إعدادي",
    subject: "Français",
    unit: "Langue et grammaire",
    objectives: ["Identifier les déterminants", "Justifier le choix du déterminant"],
    prerequisites: ["Reconnaître le nom"],
    definitions: [{ term: "déterminant", definition: "mot placé devant le nom" }],
    rules: ["La règle: le déterminant s'accorde avec le nom."],
    examples: [{ text: "Le cahier", note: "Le est un article défini." }],
    methodology: ["Méthode: lire le groupe nominal puis identifier le nom."],
    commonMistakes: ["Attention: ne confonds pas déterminant et pronom."],
    vocabulary: [{ word: "article défini", definition: "le, la, les" }],
    summary: "Les déterminants accompagnent le nom.",
    exercises: [
      {
        question: "Souligne le déterminant: le livre.",
        type: "short_answer",
        correctAnswer: "le",
        explanation: "Le est placé devant le nom livre.",
        points: 2,
      },
      {
        question: "Choisis: ___ fille lit.",
        type: "fill_blank",
        correctAnswer: "La",
        explanation: "Fille est féminin singulier.",
        points: 3,
      },
    ],
    examHints: ["Dans un فرض, justifie ton choix avec la règle."],
    nextSteps: ["Revoir le groupe nominal."],
    confidence: "high",
    gaps: [],
    ...overrides,
  };
}

describe("runtime exam intelligence engine", () => {
  it("builds common questions from exercises, definitions, rules, and examples", () => {
    const intelligence = buildExamIntelligence(highKnowledge());

    expect(intelligence.lessonId).toBe("lesson-exam-1");
    expect(intelligence.title).toBe("Les déterminants");
    expect(intelligence.commonQuestions).toContain("Souligne le déterminant: le livre.");
    expect(intelligence.commonQuestions.some((question) => question.includes("Define: déterminant"))).toBe(true);
    expect(intelligence.commonQuestions.some((question) => question.includes("Use the rule"))).toBe(true);
  });

  it("builds methodology, common mistakes, examiner expectations, and scoring rules", () => {
    const intelligence = buildExamIntelligence(highKnowledge());

    expect(intelligence.methodology.some((item) => item.includes("Méthode"))).toBe(true);
    expect(intelligence.commonMistakes.some((item) => item.includes("déterminant et pronom"))).toBe(true);
    expect(intelligence.examinerExpectations.some((item) => item.includes("Identifier les déterminants"))).toBe(true);
    expect(intelligence.scoringRules).toContain("2 pts: Souligne le déterminant: le livre.");
    expect(intelligence.scoringRules.some((item) => item.includes("correct rule application"))).toBe(true);
  });

  it("builds revision checklist and exam keywords", () => {
    const intelligence = buildExamIntelligence(highKnowledge());

    expect(intelligence.revisionChecklist.some((item) => item.includes("Review objective"))).toBe(true);
    expect(intelligence.revisionChecklist.some((item) => item.includes("Redo exercise"))).toBe(true);
    expect(intelligence.examKeywords).toContain("déterminant");
    expect(intelligence.examKeywords).toContain("Français");
  });

  it("infers difficulty from exam signals and content depth", () => {
    expect(buildExamIntelligence(highKnowledge()).difficulty).toBe("medium");
    expect(buildExamIntelligence(highKnowledge({
      title: "BAC national - fonction dérivée",
      examHints: ["BAC national: justifier chaque étape."],
      rules: Array.from({ length: 12 }, (_, index) => `Rule ${index}`),
    })).difficulty).toBe("hard");
    expect(buildExamIntelligence(highKnowledge({
      confidence: "low",
      rules: [],
      methodology: [],
      definitions: [],
      exercises: [],
      examHints: [],
    })).difficulty).toBe("easy");
  });

  it("computes readiness score from available exam intelligence signals", () => {
    const strong = buildExamIntelligence(highKnowledge());
    const weak = buildExamIntelligence(highKnowledge({
      confidence: "low",
      objectives: [],
      definitions: [],
      rules: [],
      examples: [],
      methodology: [],
      commonMistakes: [],
      vocabulary: [],
      exercises: [],
      examHints: [],
      nextSteps: [],
    }));

    expect(strong.readinessScore).toBeGreaterThanOrEqual(80);
    expect(weak.readinessScore).toBeLessThan(strong.readinessScore);
    expect(weak.readinessScore).toBeGreaterThanOrEqual(0);
    expect(weak.readinessScore).toBeLessThanOrEqual(100);
  });

  it("does not mutate curriculum knowledge input", () => {
    const knowledge = highKnowledge();
    const before = JSON.stringify(knowledge);

    buildExamIntelligence(knowledge);

    expect(JSON.stringify(knowledge)).toBe(before);
  });
});

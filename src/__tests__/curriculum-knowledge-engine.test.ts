import { describe, expect, it } from "vitest";
import { buildCurriculumKnowledge } from "@/server/curriculum/knowledge-engine";

function fullLesson() {
  return {
    id: "lesson-1",
    titleAr: "Les déterminants",
    objectives: ["Identifier les déterminants", "Utiliser les articles correctement"],
    unit: {
      titleAr: "Langue et grammaire",
      subject: {
        titleAr: "اللغة الفرنسية",
        titleFr: "Français",
        grade: {
          titleAr: "الأولى إعدادي",
          cycle: { titleAr: "الإعدادي" },
        },
      },
    },
    content: {
      explanation: [
        "Les déterminants sont des mots placés devant le nom.",
        "La règle: le déterminant s'accorde avec le nom.",
        "Méthode: lire le groupe nominal puis identifier le nom.",
        "Attention: لا تخلط بين déterminant و pronom.",
        "في الفرض، يجب تبرير الاختيار مع مثال.",
      ].join("\n"),
      vocabulary: [{ word: "déterminant", definition: "mot placé devant le nom" }],
      examples: [{ text: "Le cahier", note: "Le est un article défini." }],
      summary: "Les déterminants accompagnent le nom.",
    },
    exercises: [
      {
        type: "short_answer",
        question: "Souligne le déterminant: le livre.",
        correctAnswer: "le",
        explanation: "Le est placé devant le nom livre.",
        points: 2,
      },
    ],
  };
}

describe("curriculum knowledge engine", () => {
  it("builds knowledge from a lesson with content, examples, vocabulary, and exercises", () => {
    const knowledge = buildCurriculumKnowledge(fullLesson());

    expect(knowledge.lessonId).toBe("lesson-1");
    expect(knowledge.title).toBe("Les déterminants");
    expect(knowledge.cycle).toBe("الإعدادي");
    expect(knowledge.grade).toBe("الأولى إعدادي");
    expect(knowledge.subject).toBe("اللغة الفرنسية");
    expect(knowledge.unit).toBe("Langue et grammaire");
    expect(knowledge.objectives).toHaveLength(2);
    expect(knowledge.vocabulary[0]).toEqual({ word: "déterminant", definition: "mot placé devant le nom" });
    expect(knowledge.examples[0]).toEqual({ text: "Le cahier", note: "Le est un article défini." });
    expect(knowledge.exercises[0]).toMatchObject({ question: "Souligne le déterminant: le livre.", correctAnswer: "le", points: 2 });
    expect(knowledge.summary).toBe("Les déterminants accompagnent le nom.");
  });

  it("detects gaps when content is missing", () => {
    const knowledge = buildCurriculumKnowledge({ id: "empty", titleAr: "درس فارغ" });

    expect(knowledge.confidence).toBe("low");
    expect(knowledge.gaps).toContain("missing_objectives");
    expect(knowledge.gaps).toContain("missing_explanation");
    expect(knowledge.gaps).toContain("missing_vocabulary");
    expect(knowledge.gaps).toContain("missing_examples");
    expect(knowledge.gaps).toContain("missing_exercises");
    expect(knowledge.gaps).toContain("missing_summary");
  });

  it("extracts definitions, rules, methodology, common mistakes, and exam hints from explanation text", () => {
    const knowledge = buildCurriculumKnowledge(fullLesson());

    expect(knowledge.definitions.some((item) => item.term.includes("Les déterminants"))).toBe(true);
    expect(knowledge.rules.some((line) => /règle|قاعدة/i.test(line))).toBe(true);
    expect(knowledge.methodology.some((line) => /Méthode|منهجية/i.test(line))).toBe(true);
    expect(knowledge.commonMistakes.some((line) => /Attention|لا تخلط/i.test(line))).toBe(true);
    expect(knowledge.examHints.some((line) => /فرض|barème|BAC/i.test(line))).toBe(true);
  });

  it("computes high, medium, and low confidence", () => {
    expect(buildCurriculumKnowledge(fullLesson()).confidence).toBe("high");
    expect(buildCurriculumKnowledge({
      id: "medium",
      titleAr: "Medium",
      objectives: ["هدف"],
      content: { explanation: "العدد هو رمز للكمية.", examples: [{ text: "1 + 1 = 2" }] },
      exercises: [],
    }).confidence).toBe("medium");
    expect(buildCurriculumKnowledge({ id: "low", titleAr: "Low" }).confidence).toBe("low");
  });

  it("does not mutate input", () => {
    const lesson = fullLesson();
    const before = JSON.stringify(lesson);

    buildCurriculumKnowledge(lesson);

    expect(JSON.stringify(lesson)).toBe(before);
  });
});

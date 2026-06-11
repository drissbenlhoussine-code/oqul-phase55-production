import { describe, expect, it } from "vitest";
import {
  buildWeakGrounding,
  classifySubject,
  guardAgentOutput,
  hasMojibake,
} from "@/server/ai/pipeline/quality";

describe("pipeline curriculum quality guards", () => {
  it("classifies French grammar and rejects Arabic grammar/economic drift", () => {
    const input = "اشرح لي درس: grammaire niveau collège";
    const grounding = buildWeakGrounding(input);

    expect(classifySubject(input)).toBe("french");

    const result = guardAgentOutput({
      agentId: "researcher",
      input,
      grounding,
      output: "هذا تحليل اقتصادي واجتماعي ثم نشرح النحو العربي والمبتدأ والخبر.",
    });

    expect(result.ok).toBe(false);
    expect(result.issues).toContain("off_subject_content");
  });

  it("rejects math output that drifts into social/economic dimensions", () => {
    const input = "اشرح درس الدوال في الرياضيات";
    const grounding = buildWeakGrounding(input);
    const result = guardAgentOutput({
      agentId: "analyst",
      input,
      grounding,
      output: "الدوال موضوع اجتماعي اقتصادي يرتبط بالسياسة العمومية وتحليل اقتصادي واسع.",
    });

    expect(result.ok).toBe(false);
    expect(result.issues).toContain("off_subject_content");
  });

  it("rejects philosophy output that generates math equations", () => {
    const input = "حلل مفهوم الحرية في الفلسفة";
    const grounding = buildWeakGrounding(input);
    const result = guardAgentOutput({
      agentId: "analyst",
      input,
      grounding,
      output: "نحلل الحرية عبر المعادلة f(x)=x^2 ثم نحسب اشتقاق الدالة.",
    });

    expect(result.ok).toBe(false);
    expect(result.issues).toContain("off_subject_content");
  });

  it("rejects mojibake output", () => {
    expect(hasMojibake("Ø£Ù†Øª")).toBe(true);

    const input = "اشرح درس الدوال";
    const result = guardAgentOutput({
      agentId: "researcher",
      input,
      grounding: buildWeakGrounding(input),
      output: "Ø£Ù†Øª نص مكسور الترميز",
    });

    expect(result.ok).toBe(false);
    expect(result.issues).toContain("mojibake_output");
  });

  it("rejects placeholder output", () => {
    const input = "اشرح درس الدوال";
    const result = guardAgentOutput({
      agentId: "researcher",
      input,
      grounding: buildWeakGrounding(input),
      output: "هذا شرح مؤقت. [أدخل الحل هنا]",
    });

    expect(result.ok).toBe(false);
    expect(result.issues).toContain("placeholder_output");
  });

  it("requires corrections and point allocation from exercise generator", () => {
    const input = "اشرح grammaire مع تمارين";
    const grounding = buildWeakGrounding(input);
    const weak = guardAgentOutput({
      agentId: "exercise_gen",
      input,
      grounding,
      output: "Exercice: choisissez la bonne réponse.",
    });

    expect(weak.ok).toBe(false);
    expect(weak.issues).toContain("missing_corrections");
    expect(weak.issues).toContain("missing_point_allocation");

    const strong = guardAgentOutput({
      agentId: "exercise_gen",
      input,
      grounding,
      output: [
        "Grammaire française: accord du participe passé.",
        "Exercice progressif: Choisissez la bonne forme.",
        "Correction: La réponse correcte est choisie car le participe s'accorde avec le sujet.",
        "Barème: 2 points pour la règle, 2 points pour l'application.",
        "انتظارات المصحح: ذكر القاعدة وتطبيقها على الجملة.",
      ].join("\n"),
    });

    expect(strong.ok).toBe(true);
  });
});

import { describe, expect, it } from "vitest";
import {
  buildWeakGrounding,
  classifySubject,
  type CurriculumGrounding,
  guardAgentOutput,
  hasMojibake,
  inferIntent,
  isClarificationNeeded,
} from "@/server/ai/pipeline/quality";

function strongGrounding(input: string): CurriculumGrounding {
  return {
    mode: "grounded",
    languageOfInstruction: "french",
    intent: inferIntent(input),
    confidence: "high",
    missingDbLesson: false,
    cycle: "الإعدادي",
    grade: "الأولى إعدادي",
    subject: classifySubject(input),
    unit: "Langue et grammaire",
    lesson: "Grammaire française: nature et fonction des mots",
    topic: "grammaire",
    examContext: "فرض محروس للأولى إعدادي مع barème و critères d'évaluation.",
    strength: "strong",
    warnings: [],
    matches: [
      {
        lessonId: "lesson-grammar",
        title: "Grammaire française: nature et fonction des mots",
        cycle: "الإعدادي",
        grade: "الأولى إعدادي",
        subject: "اللغة الفرنسية / français",
        unit: "Langue et grammaire",
        objectives: ["Identifier la nature des mots", "Distinguer les fonctions grammaticales"],
        contentSnippet: "Nature des mots, groupe nominal, verbe, sujet, complément, accords.",
        exerciseCount: 6,
      },
    ],
  };
}

function validFrenchGrammarOutput() {
  return [
    "لم أجد هذا الدرس محفوظًا بعد داخل قاعدة OQUL، لذلك سأقدمه كدرس جديد متوافق مع توقعات المنهاج المغربي.",
    "Grammaire française: définition, nature des mots, fonction grammaticale, phrase simple, groupe nominal, verbe, sujet, complément et accords.",
    "الأولى إعدادي - Langue et grammaire - grammaire.",
    "Devoir surveillé: Analysez les phrases et indiquez la nature des mots et la fonction grammaticale.",
    "Exercice 1: Dans la phrase 'Le petit élève lit une histoire', trouvez le sujet, le verbe et le complément.",
    "Correction: Le sujet est 'Le petit élève', le verbe est 'lit', et le complément est 'une histoire'. La réponse est correcte car chaque groupe a une fonction grammaticale précise.",
    "Barème: 2 points pour la nature des mots, 2 points pour la fonction grammaticale, 1 point pour la justification.",
    "انتظارات المصحح: تحديد القاعدة، استعمال المصطلحات الفرنسية، ثم تطبيقها على الجملة.",
    "أخطاء شائعة: الخلط بين nature و fonction، نسيان accord، وتحليل groupe nominal كفعل.",
  ].join("\n");
}

describe("pipeline curriculum quality guards", () => {
  it("uses aligned fallback for clear French grammar requests when no DB lesson is grounded", () => {
    const input = "اشرح لي درس grammaire";
    const grounding = buildWeakGrounding(input);

    expect(classifySubject(input)).toBe("french");
    expect(grounding.mode).toBe("aligned_fallback");
    expect(grounding.missingDbLesson).toBe(true);
    expect(grounding.languageOfInstruction).toBe("french");
    expect(grounding.studentFacingNotice).toContain("لم أجد هذا الدرس محفوظًا");

    const result = guardAgentOutput({
      agentId: "exercise_gen",
      input,
      grounding,
      final: true,
      output: validFrenchGrammarOutput(),
    });

    expect(result.ok).toBe(true);
    expect(result.issues).not.toContain("no_lesson_grounding");
    expect(result.issues).not.toContain("off_subject_content");
  });

  it("asks clarification only for vague requests", () => {
    const input = "بغيت نراجع";
    const grounding = buildWeakGrounding(input);

    expect(isClarificationNeeded(input)).toBe(true);
    expect(grounding.mode).toBe("clarification_needed");
    expect(grounding.studentFacingNotice).toBe("ما المستوى والمادة؟");
  });

  it("does not ask clarification when subject and topic can be inferred", () => {
    const input = "اشرح لي درس grammaire";
    expect(isClarificationNeeded(input)).toBe(false);
    expect(buildWeakGrounding(input).mode).toBe("aligned_fallback");
  });

  it("separates lesson, exam, and research intents", () => {
    expect(inferIntent("اشرح لي grammaire")).toBe("lesson");
    expect(inferIntent("فرض محروس في grammaire مع barème")).toBe("exam");
    expect(inferIntent("قارن بين مفهومين في الفلسفة")).toBe("research");
  });

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

  it("requires French grammar output to stay in French subject language", () => {
    const input = "اشرح لي درس: grammaire";
    const grounding = buildWeakGrounding(input);
    const result = guardAgentOutput({
      agentId: "exercise_gen",
      input,
      grounding,
      final: true,
      output: [
        "grammaire",
        "هذا تعريف عام للنحو فقط دون مصطلحات فرنسية.",
        "تصحيح: جواب عام.",
        "Barème: 4 points.",
        "انتظارات المصحح: تعريف القاعدة.",
        "أخطاء شائعة: الخلط في القاعدة.",
        "فرض محروس.",
      ].join("\n"),
    });

    expect(result.ok).toBe(false);
    expect(result.issues).toContain("missing_french_grammar_concepts");
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

  it("allows formulas for math and rejects grammar-only math answers", () => {
    const input = "اشرح لي معادلة في الرياضيات";
    const grounding = buildWeakGrounding(input);
    const result = guardAgentOutput({
      agentId: "exercise_gen",
      input,
      grounding,
      final: true,
      output: [
        "رياضيات - معادلة: نحل خطوة بخطوة x + 3 = 7 إذن x = 4.",
        "فرض محروس: حل المعادلة.",
        "تصحيح: نطرح 3 من الطرفين.",
        "Barème: 2 points للطريقة و2 points للنتيجة.",
        "انتظارات المصحح: احترام خطوات الحل وكتابة النتيجة.",
        "أخطاء شائعة: نسيان تغيير الطرفين بنفس العملية.",
      ].join("\n"),
    });

    expect(result.ok).toBe(true);
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

  it("rejects mojibake output while accepting normal Arabic", () => {
    expect(hasMojibake("Ø£Ù†Øª")).toBe(true);
    expect(hasMojibake("أنت تلميذ مجتهد")).toBe(false);

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

  it("allows lesson mode without exam-only barème requirements", () => {
    const input = "اشرح grammaire مع تمارين";
    const grounding = strongGrounding(input);
    const result = guardAgentOutput({
      agentId: "exercise_gen",
      input,
      grounding,
      final: true,
      output: [
        "Grammaire française: définition, nature des mots, fonction grammaticale, phrase simple, groupe nominal, verbe, sujet et complément.",
        "Exercice: Soulignez le verbe dans la phrase: Le garçon lit un livre.",
        "Correction: Le verbe est 'lit'. Il indique l'action dans la phrase.",
        "أخطاء شائعة: الخلط بين verbe و sujet، ونسيان accord.",
      ].join("\n"),
    });

    expect(result.ok).toBe(true);
  });

  it("requires corrections, barème, examiner expectations, and common mistakes in exam mode", () => {
    const input = "اشرح grammaire مع تمارين";
    const grounding = { ...strongGrounding("فرض محروس في grammaire"), intent: "exam" as const };
    const weak = guardAgentOutput({
      agentId: "exercise_gen",
      input,
      grounding,
      output: "Exercice: choisissez la bonne réponse.",
    });

    expect(weak.ok).toBe(false);
    expect(weak.issues).toContain("missing_corrections");
    expect(weak.issues).toContain("missing_point_allocation");
    expect(weak.issues).toContain("missing_examiner_expectations");
    expect(weak.issues).toContain("missing_common_mistakes");

    const strong = guardAgentOutput({
      agentId: "exercise_gen",
      input,
      grounding,
      final: true,
      output: validFrenchGrammarOutput(),
    });

    expect(strong.ok).toBe(true);
  });
});

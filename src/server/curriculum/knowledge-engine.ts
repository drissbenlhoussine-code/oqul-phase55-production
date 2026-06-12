export interface CurriculumKnowledge {
  lessonId: string;
  title: string;
  cycle?: string | null;
  grade?: string | null;
  subject?: string | null;
  unit?: string | null;

  objectives: string[];
  prerequisites: string[];
  definitions: Array<{ term: string; definition: string }>;
  rules: string[];
  examples: Array<{ text: string; note?: string }>;
  methodology: string[];
  commonMistakes: string[];
  vocabulary: Array<{ word: string; definition: string }>;
  summary: string | null;
  exercises: Array<{
    question: string;
    type: string;
    correctAnswer: string;
    explanation?: string | null;
    points: number;
  }>;

  examHints: string[];
  nextSteps: string[];
  confidence: "high" | "medium" | "low";
  gaps: string[];
}

type AnyRecord = Record<string, unknown>;

export function buildCurriculumKnowledge(lesson: unknown): CurriculumKnowledge {
  const source = asRecord(lesson);
  const content = asRecord(source.content);
  const explanation = asString(content.explanation);
  const lines = splitMeaningfulLines(explanation);
  const objectives = toStringArray(source.objectives);
  const vocabulary = normalizeVocabulary(content.vocabulary);
  const examples = normalizeExamples(content.examples);
  const exercises = normalizeExercises(source.exercises);
  const unit = asRecord(source.unit);
  const subject = asRecord(unit.subject);
  const grade = asRecord(subject.grade);
  const cycle = asRecord(grade.cycle);

  const knowledge: CurriculumKnowledge = {
    lessonId: asString(source.id) || asString(source.lessonId),
    title: asString(source.titleAr) || asString(source.title) || "Untitled lesson",
    cycle: relationTitle(cycle),
    grade: relationTitle(grade),
    subject: relationTitle(subject),
    unit: relationTitle(unit),
    objectives,
    prerequisites: extractTaggedLines(lines, [/متطلب|مكتسبات|pr[ée]requis/i]),
    definitions: extractDefinitions(lines),
    rules: extractTaggedLines(lines, [/قاعدة|خاصية|يجب|on doit|r[èe]gle/i]),
    examples,
    methodology: extractTaggedLines(lines, [/الطريقة|منهجية|خطوات|m[ée]thode|[ée]tapes/i]),
    commonMistakes: extractTaggedLines(lines, [/خطأ شائع|لا تخلط|انتبه|erreur fr[ée]quente|attention/i]),
    vocabulary,
    summary: asString(content.summary) || null,
    exercises,
    examHints: extractTaggedLines(lines, [/امتحان|فرض|BAC|جهوي|إقليمي|bar[èe]me/i]),
    nextSteps: extractTaggedLines(lines, [/بعد ذلك|الخطوة الموالية|للمراجعة|next/i]),
    confidence: "low",
    gaps: [],
  };

  knowledge.gaps = computeGaps({ explanation, knowledge });
  knowledge.confidence = computeConfidence({ explanation, knowledge });

  return knowledge;
}

function asRecord(value: unknown): AnyRecord {
  return value && typeof value === "object" && !Array.isArray(value) ? value as AnyRecord : {};
}

function asString(value: unknown): string {
  return typeof value === "string" ? value.trim() : "";
}

function relationTitle(value: AnyRecord): string | null {
  return asString(value.titleAr) || asString(value.titleFr) || asString(value.title) || asString(value.slug) || null;
}

function toStringArray(value: unknown): string[] {
  if (!Array.isArray(value)) return [];
  return value.map((item) => asString(item)).filter(Boolean);
}

function splitMeaningfulLines(text: string): string[] {
  return text
    .split(/\r?\n|[•*-]\s+/)
    .map((line) => line.trim())
    .filter((line) => line.length >= 3);
}

function normalizeVocabulary(value: unknown): Array<{ word: string; definition: string }> {
  if (!Array.isArray(value)) return [];
  return value.flatMap((item) => {
    if (typeof item === "string") {
      const [word, definition = ""] = item.split(/[:：-]/).map((part) => part.trim());
      return word ? [{ word, definition }] : [];
    }
    const record = asRecord(item);
    const word = asString(record.word) || asString(record.term);
    const definition = asString(record.definition) || asString(record.meaning);
    return word ? [{ word, definition }] : [];
  });
}

function normalizeExamples(value: unknown): Array<{ text: string; note?: string }> {
  if (!Array.isArray(value)) return [];
  return value.flatMap((item) => {
    if (typeof item === "string") return item.trim() ? [{ text: item.trim() }] : [];
    const record = asRecord(item);
    const text = asString(record.text) || asString(record.example);
    const note = asString(record.note);
    return text ? [{ text, ...(note ? { note } : {}) }] : [];
  });
}

function normalizeExercises(value: unknown): CurriculumKnowledge["exercises"] {
  if (!Array.isArray(value)) return [];
  return value.flatMap((item) => {
    const record = asRecord(item);
    const question = asString(record.question);
    const type = asString(record.type) || "unknown";
    const correctAnswer = asString(record.correctAnswer) || asString(record.correct_answer);
    const explanation = asString(record.explanation) || null;
    const points = typeof record.points === "number" ? record.points : Number(record.points ?? 0) || 0;
    return question ? [{ question, type, correctAnswer, explanation, points }] : [];
  });
}

function extractDefinitions(lines: string[]): Array<{ term: string; definition: string }> {
  const definitions: Array<{ term: string; definition: string }> = [];
  for (const line of lines) {
    const arabic = line.match(/^(.{2,60}?)\s+(?:هو|هي)\s+(.{4,})$/);
    if (arabic) {
      definitions.push({ term: cleanTerm(arabic[1]), definition: arabic[2].trim() });
      continue;
    }

    const frenchCall = line.match(/on appelle\s+(.{2,60}?)\s+(.{4,})$/i);
    if (frenchCall) {
      definitions.push({ term: cleanTerm(frenchCall[1]), definition: frenchCall[2].trim() });
      continue;
    }

    const frenchEst = line.match(/^(.{2,60}?)\s+(?:est|sont)\s+(.{4,})$/i);
    if (frenchEst) {
      definitions.push({ term: cleanTerm(frenchEst[1]), definition: frenchEst[2].trim() });
    }
  }
  return definitions;
}

function extractTaggedLines(lines: string[], patterns: RegExp[]): string[] {
  return unique(lines.filter((line) => patterns.some((pattern) => pattern.test(line))));
}

function cleanTerm(value: string): string {
  return value.replace(/^[-–—:\s]+|[-–—:\s]+$/g, "").trim();
}

function unique(values: string[]): string[] {
  return [...new Set(values.map((value) => value.trim()).filter(Boolean))];
}

function computeGaps(params: { explanation: string; knowledge: CurriculumKnowledge }): string[] {
  const { explanation, knowledge } = params;
  const gaps: string[] = [];
  if (!knowledge.objectives.length) gaps.push("missing_objectives");
  if (!explanation) gaps.push("missing_explanation");
  if (!knowledge.vocabulary.length) gaps.push("missing_vocabulary");
  if (!knowledge.examples.length) gaps.push("missing_examples");
  if (!knowledge.exercises.length) gaps.push("missing_exercises");
  if (!knowledge.summary) gaps.push("missing_summary");
  if (!knowledge.methodology.length) gaps.push("missing_methodology");
  if (!knowledge.commonMistakes.length) gaps.push("missing_common_mistakes");
  if (!knowledge.examHints.length) gaps.push("missing_exam_hints");
  return gaps;
}

function computeConfidence(params: { explanation: string; knowledge: CurriculumKnowledge }): CurriculumKnowledge["confidence"] {
  const { explanation, knowledge } = params;
  const hasObjectives = knowledge.objectives.length > 0;
  const hasExamples = knowledge.examples.length > 0;
  const hasExercises = knowledge.exercises.length > 0;
  if (explanation && hasObjectives && hasExamples && hasExercises) return "high";
  const supportingFields = [hasObjectives, hasExamples, hasExercises].filter(Boolean).length;
  if (explanation && supportingFields >= 2) return "medium";
  return "low";
}

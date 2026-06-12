import type { CurriculumKnowledge } from "@/server/curriculum/knowledge-engine";

export interface ExamIntelligence {
  lessonId: string;
  title: string;
  commonQuestions: string[];
  methodology: string[];
  commonMistakes: string[];
  examinerExpectations: string[];
  scoringRules: string[];
  revisionChecklist: string[];
  examKeywords: string[];
  difficulty: "easy" | "medium" | "hard";
  readinessScore: number;
}

export function buildExamIntelligence(knowledge: CurriculumKnowledge): ExamIntelligence {
  const methodology = unique([
    ...knowledge.methodology,
    ...knowledge.rules.map((rule) => `Apply rule: ${rule}`),
    ...fallbackMethodology(knowledge),
  ]);
  const commonQuestions = unique([
    ...knowledge.exercises.map((exercise) => exercise.question),
    ...knowledge.definitions.map((definition) => `Define: ${definition.term}`),
    ...knowledge.rules.map((rule) => `Use the rule: ${shorten(rule)}`),
    ...knowledge.examples.map((example) => `Explain the example: ${shorten(example.text)}`),
  ]).slice(0, 10);
  const commonMistakes = unique([
    ...knowledge.commonMistakes,
    ...knowledge.exercises
      .map((exercise) => exercise.explanation)
      .filter((value): value is string => Boolean(value))
      .filter((value) => /mistake|erreur|attention|wrong|خطأ|انتبه|لا تخلط/i.test(value)),
    ...fallbackMistakes(knowledge),
  ]);
  const examinerExpectations = unique([
    ...knowledge.examHints,
    ...knowledge.objectives.map((objective) => `Show mastery of: ${objective}`),
    ...knowledge.definitions.map((definition) => `Use the definition of ${definition.term} correctly.`),
    ...knowledge.rules.map((rule) => `Justify answers using: ${shorten(rule)}`),
  ]);
  const scoringRules = unique([
    ...knowledge.exercises.map((exercise) => `${exercise.points} pts: ${shorten(exercise.question)}`),
    ...knowledge.rules.map((rule) => `Award points for correct rule application: ${shorten(rule)}`),
    ...knowledge.methodology.map((step) => `Award method points for: ${shorten(step)}`),
  ]);
  const examKeywords = extractKeywords(knowledge);
  const revisionChecklist = unique([
    ...knowledge.objectives.map((objective) => `Review objective: ${objective}`),
    ...knowledge.definitions.map((definition) => `Memorize definition: ${definition.term}`),
    ...knowledge.rules.map((rule) => `Practice rule: ${shorten(rule)}`),
    ...knowledge.examples.map((example) => `Rework example: ${shorten(example.text)}`),
    ...knowledge.exercises.map((exercise) => `Redo exercise: ${shorten(exercise.question)}`),
    ...knowledge.nextSteps,
  ]);

  return {
    lessonId: knowledge.lessonId,
    title: knowledge.title,
    commonQuestions,
    methodology,
    commonMistakes,
    examinerExpectations,
    scoringRules,
    revisionChecklist,
    examKeywords,
    difficulty: inferDifficulty(knowledge),
    readinessScore: computeReadinessScore({
      knowledge,
      commonQuestions,
      methodology,
      commonMistakes,
      examinerExpectations,
      scoringRules,
      revisionChecklist,
      examKeywords,
    }),
  };
}

function fallbackMethodology(knowledge: CurriculumKnowledge): string[] {
  const steps: string[] = [];
  if (knowledge.definitions.length) steps.push("Start by recalling the key definitions.");
  if (knowledge.rules.length) steps.push("Identify the rule required by the question.");
  if (knowledge.examples.length) steps.push("Compare the question with a solved example.");
  if (knowledge.exercises.length) steps.push("Write the answer, then verify it using the correction method.");
  return steps;
}

function fallbackMistakes(knowledge: CurriculumKnowledge): string[] {
  const mistakes: string[] = [];
  if (knowledge.definitions.length) mistakes.push("Confusing the definition with an example.");
  if (knowledge.rules.length) mistakes.push("Applying the rule without checking the condition.");
  if (knowledge.exercises.length) mistakes.push("Giving the final answer without justification.");
  return mistakes;
}

function extractKeywords(knowledge: CurriculumKnowledge): string[] {
  return unique([
    ...wordsFrom(knowledge.title),
    ...wordsFrom(knowledge.cycle),
    ...wordsFrom(knowledge.grade),
    ...wordsFrom(knowledge.subject),
    ...wordsFrom(knowledge.unit),
    ...knowledge.objectives.flatMap(wordsFrom),
    ...knowledge.definitions.flatMap((definition) => [definition.term, ...wordsFrom(definition.definition)]),
    ...knowledge.vocabulary.flatMap((item) => [item.word, ...wordsFrom(item.definition)]),
    ...knowledge.rules.flatMap(wordsFrom),
    ...knowledge.examHints.flatMap(wordsFrom),
  ])
    .filter((word) => word.length >= 3)
    .slice(0, 20);
}

function inferDifficulty(knowledge: CurriculumKnowledge): ExamIntelligence["difficulty"] {
  const signalCount = knowledge.rules.length
    + knowledge.methodology.length
    + knowledge.definitions.length
    + knowledge.exercises.length;
  const text = [
    knowledge.title,
    knowledge.unit,
    knowledge.subject,
    ...knowledge.rules,
    ...knowledge.examHints,
  ].filter(Boolean).join(" ");
  if (/BAC|national|جهوي|وطني|hard|complex|proof|démontrer|برهن/i.test(text) || signalCount >= 12) return "hard";
  if (/فرض|exam|contr[oô]le|medium|application|طبق/i.test(text) || signalCount >= 6) return "medium";
  return "easy";
}

function computeReadinessScore(params: {
  knowledge: CurriculumKnowledge;
  commonQuestions: string[];
  methodology: string[];
  commonMistakes: string[];
  examinerExpectations: string[];
  scoringRules: string[];
  revisionChecklist: string[];
  examKeywords: string[];
}): number {
  let score = 0;
  if (params.knowledge.confidence === "high") score += 25;
  else if (params.knowledge.confidence === "medium") score += 15;
  else score += 5;

  if (params.commonQuestions.length >= 3) score += 15;
  else if (params.commonQuestions.length) score += 8;
  if (params.methodology.length >= 2) score += 15;
  else if (params.methodology.length) score += 8;
  if (params.commonMistakes.length >= 2) score += 10;
  else if (params.commonMistakes.length) score += 5;
  if (params.examinerExpectations.length >= 2) score += 15;
  else if (params.examinerExpectations.length) score += 8;
  if (params.scoringRules.length >= 2) score += 10;
  else if (params.scoringRules.length) score += 5;
  if (params.revisionChecklist.length >= 3) score += 5;
  if (params.examKeywords.length >= 5) score += 5;

  return clamp(score, 0, 100);
}

function wordsFrom(text: string | null | undefined): string[] {
  if (!text) return [];
  return text
    .split(/[^\p{L}\p{N}_+-]+/u)
    .map((word) => word.trim())
    .filter(Boolean);
}

function shorten(text: string, max = 120): string {
  return text.length > max ? `${text.slice(0, max - 1)}…` : text;
}

function unique(values: string[]): string[] {
  return [...new Set(values.map((value) => value.trim()).filter(Boolean))];
}

function clamp(value: number, min: number, max: number): number {
  return Math.min(max, Math.max(min, value));
}

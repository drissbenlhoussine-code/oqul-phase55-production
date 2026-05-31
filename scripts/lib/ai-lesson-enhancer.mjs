import Groq from "groq-sdk";
import fs from "node:fs/promises";
import path from "node:path";
import { scoreLessonQuality } from "./lesson-quality-tools.mjs";

const MIN_TARGET_SCORE = 85;
const MIN_ACCEPTABLE_SCORE = 75;
const MIN_CONTENT_CHARS = 2000;
const MIN_WORKED_EXAMPLES = 3;
const MIN_GUIDED_PRACTICE = 3;
const MIN_EXERCISES = 8;
const MIN_COMMON_MISTAKES = 3;
const MIN_EXAM_QUESTIONS = 2;
const GENERATED_LESSONS_DIR = ".generated-lessons";

export function requireGroqApiKey() {
  if (!process.env.GROQ_API_KEY) {
    throw new Error("GROQ_API_KEY is required for AI lesson enhancement. Dry-run audits do not need it.");
  }
  return process.env.GROQ_API_KEY;
}

function isPrimaryMathLesson(lesson) {
  const grade = String(lesson.grade_slug ?? lesson.grade_title ?? "").toLowerCase();
  const subject = String(lesson.subject_slug ?? lesson.subject_title ?? "").toLowerCase();
  return /^(1ap|2ap|3ap|4ap|5ap|6ap)$/.test(grade) && (subject.includes("math") || subject.includes("رياض"));
}

function buildPrompt(lesson, feedback = [], options = {}) {
  const compact = Boolean(options.compact);
  const primaryMath = isPrimaryMathLesson(lesson);
  const feedbackBlock = feedback.length
    ? `
The previous generation failed quality checks. Fix these failures explicitly:
${feedback.map((item) => `- ${item}`).join("\n")}
`
    : "";
  const compactBlock = compact
    ? `
Compact mode is ON.
- Target 2500-3500 Arabic characters in the combined lesson body.
- Keep prose short and avoid repeated paragraphs.
- Still include objectives, short explanation, 3 solved examples, 8 exercises, hints, answers, structured explanations, common mistakes, guided practice, and Leila instructions.
- Use concise Grade 1/Grade 2 language for primary math.
${primaryMath ? "- Do not mention الجذع المشترك, الباكالوريا, or secondary-school exams for primary lessons." : ""}
`
    : "";

  return `
You are Leila, OQUL's Moroccan curriculum tutor and lesson designer.

Create one rich, original, Moroccan curriculum-aligned lesson. Do not copy textbooks word-for-word.
Use official curriculum style only for order, competencies, concepts, and exam expectations.
Return strict valid JSON only. Do not use Markdown fences. Do not add text before or after JSON.
Write ONLY in Arabic and standard math notation. Never use Chinese/CJK characters such as 概念.

Lesson metadata:
- Grade: ${lesson.grade_title ?? lesson.grade_slug ?? "unknown"}
- Subject: ${lesson.subject_title ?? lesson.subject_slug ?? "unknown"}
- Unit: ${lesson.unit_title ?? lesson.unit_slug ?? "unknown"}
- Lesson title: ${lesson.lesson_title}
- Existing objectives: ${JSON.stringify(lesson.objectives ?? [])}

Hard quality requirements. These are exact counts, not suggestions:
- Write clear Modern Arabic suitable for Moroccan students.
- Mention Moroccan context explicitly: المغرب, المنهاج المغربي, الجذع المشترك, الفرض, الامتحان.
- Include Leila tutoring instructions explicitly using the word ليلى.
- Content must be detailed: at least 2200 Arabic characters in the combined lesson body.
- Exactly 3 or more key concepts.
- Exactly 3 or more key definitions.
- Exactly 3 worked examples, each with at least 4 numbered steps and answer.
- Exactly 3 guided practice activities, each with hint and expected answer.
- Exactly 8 exercises: exercises 1-3 easy, exercises 4-6 medium, exercises 7-8 hard.
- Every exercise must include question, difficulty, answer, detailed explanation, hint, and skillTag.
- Every exercise detailedExplanation must be child-friendly and must include four parts: Reasoning, Calculation, Answer, and Explanation.
- Do not use one short generic explanation such as "لأننا جمعنا العددين" or "اقرأ الأعداد بعناية".
- For Grade 1 and Grade 2 math, make the calculation concrete and simple. Example:
  Reasoning: We count all objects first.
  Calculation: 40 + 20 = 60
  Answer: There are 60 objects.
  Explanation: Because 40 and 20 together make 60.
- Exactly 3 common mistakes with correction.
- Exactly 2 exam preparation questions.
- Include key concepts, key definitions, prerequisites, introduction, detailed explanation, summary.
- Do not repeat the same answer or the same problem pattern across all exercises.
- For probability, use concrete contexts such as نرد, قطعة نقدية, كرات في كيس, بطاقات, قرعة داخل القسم.
- Do not write vague phrases like "طرح رقمين". Say exactly what the random experiment is.
- Avoid non-Arabic artifacts or Chinese/CJK characters.
- Use varied answers: fractions like 1/2, 1/3, 2/5, 3/8, 1/6, 5/12, 0, 1 depending on the context.
- Make every worked example and exercise mathematically coherent.

Use these exact Arabic section ideas naturally in the content so automated quality gates can verify it:
تعريف، مفهوم، مثال محلول، خطوة، نحسب، الحل، تمرين، تطبيق، تدريب، أجب، احسب،
الجواب، شرح، خطأ شائع، أخطاء شائعة، تصحيح، تلميح، العلاج، فرض، امتحان، وضعية، استعداد، ملخص، خلاصة، ليلى.

${compactBlock}
${feedbackBlock}

Return exactly this JSON shape:
{
  "title": "عنوان الدرس",
  "objectives": ["objective 1", "objective 2", "objective 3", "objective 4"],
  "prerequisites": ["prerequisite 1", "prerequisite 2", "prerequisite 3"],
  "introduction": "intro paragraph",
  "detailedExplanation": "long detailed explanation",
  "keyConcepts": [
    {"name": "concept 1", "explanation": "explanation"},
    {"name": "concept 2", "explanation": "explanation"},
    {"name": "concept 3", "explanation": "explanation"}
  ],
  "keyDefinitions": [
    {"term": "term 1", "definition": "definition"},
    {"term": "term 2", "definition": "definition"},
    {"term": "term 3", "definition": "definition"}
  ],
  "workedExamples": [
    {"title": "نرد متوازن", "problem": "probability problem", "steps": ["step 1", "step 2", "step 3", "step 4"], "answer": "answer"},
    {"title": "كرات في كيس", "problem": "probability problem", "steps": ["step 1", "step 2", "step 3", "step 4"], "answer": "answer"},
    {"title": "بطاقات مرقمة", "problem": "probability problem", "steps": ["step 1", "step 2", "step 3", "step 4"], "answer": "answer"}
  ],
  "guidedPractice": [
    {"prompt": "activity 1", "hint": "hint", "expectedAnswer": "expected answer"},
    {"prompt": "activity 2", "hint": "hint", "expectedAnswer": "expected answer"},
    {"prompt": "activity 3", "hint": "hint", "expectedAnswer": "expected answer"}
  ],
  "commonMistakes": [
    {"mistake": "mistake 1", "correction": "correction"},
    {"mistake": "mistake 2", "correction": "correction"},
    {"mistake": "mistake 3", "correction": "correction"}
  ],
  "examPreparation": [
    {"question": "exam-style question 1", "answer": "answer", "method": "method"},
    {"question": "exam-style question 2", "answer": "answer", "method": "method"}
  ],
  "leilaInstructions": ["how Leila should tutor this lesson"],
  "summary": "short recap",
  "vocabulary": [{"word": "word", "definition": "definition"}],
  "examples": [{"text": "short example text", "note": "teaching note"}],
  "exercises": [
    {"type": "short_answer", "difficulty": "easy", "question": "exercise 1", "hint": "hint", "answer": "answer", "detailedExplanation": "Reasoning: explain how to think. Calculation: show the operation. Answer: give the final answer. Explanation: explain why the answer is correct in child-friendly words.", "skillTag": "skill tag", "points": 10},
    {"type": "short_answer", "difficulty": "easy", "question": "exercise 2", "hint": "hint", "answer": "answer", "detailedExplanation": "Reasoning: explain how to think. Calculation: show the operation. Answer: give the final answer. Explanation: explain why the answer is correct in child-friendly words.", "skillTag": "skill tag", "points": 10},
    {"type": "short_answer", "difficulty": "easy", "question": "exercise 3", "hint": "hint", "answer": "answer", "detailedExplanation": "Reasoning: explain how to think. Calculation: show the operation. Answer: give the final answer. Explanation: explain why the answer is correct in child-friendly words.", "skillTag": "skill tag", "points": 10},
    {"type": "short_answer", "difficulty": "medium", "question": "exercise 4", "hint": "hint", "answer": "answer", "detailedExplanation": "Reasoning: explain how to think. Calculation: show the operation. Answer: give the final answer. Explanation: explain why the answer is correct in child-friendly words.", "skillTag": "skill tag", "points": 15},
    {"type": "short_answer", "difficulty": "medium", "question": "exercise 5", "hint": "hint", "answer": "answer", "detailedExplanation": "Reasoning: explain how to think. Calculation: show the operation. Answer: give the final answer. Explanation: explain why the answer is correct in child-friendly words.", "skillTag": "skill tag", "points": 15},
    {"type": "short_answer", "difficulty": "medium", "question": "exercise 6", "hint": "hint", "answer": "answer", "detailedExplanation": "Reasoning: explain how to think. Calculation: show the operation. Answer: give the final answer. Explanation: explain why the answer is correct in child-friendly words.", "skillTag": "skill tag", "points": 15},
    {"type": "short_answer", "difficulty": "hard", "question": "exercise 7", "hint": "hint", "answer": "answer", "detailedExplanation": "Reasoning: explain how to think. Calculation: show the operation. Answer: give the final answer. Explanation: explain why the answer is correct in child-friendly words.", "skillTag": "skill tag", "points": 20},
    {"type": "short_answer", "difficulty": "hard", "question": "exercise 8", "hint": "hint", "answer": "answer", "detailedExplanation": "Reasoning: explain how to think. Calculation: show the operation. Answer: give the final answer. Explanation: explain why the answer is correct in child-friendly words.", "skillTag": "skill tag", "points": 20}
  ]
}
`;
}

export function estimateLessonGenerationTokens(lesson, options = {}) {
  const prompt = buildPrompt(lesson, [], options);
  const estimatedInputTokens = Math.ceil(prompt.length / 3.6);
  const estimatedExpectedOutputTokens = options.compact ? 1800 : 3400;
  return {
    mode: options.compact ? "compact" : "standard",
    inputPromptChars: prompt.length,
    estimatedInputTokens,
    estimatedExpectedOutputTokens,
    estimatedTotalTokens: estimatedInputTokens + estimatedExpectedOutputTokens,
  };
}

function stripJsonFences(text) {
  return String(text)
    .trim()
    .replace(/^```(?:json)?\s*/i, "")
    .replace(/\s*```$/i, "")
    .trim();
}

function parseGeneratedJson(text) {
  const cleaned = stripJsonFences(text);
  try {
    return JSON.parse(cleaned);
  } catch {
    const start = cleaned.indexOf("{");
    const end = cleaned.lastIndexOf("}");
    if (start >= 0 && end > start) return JSON.parse(cleaned.slice(start, end + 1));
    throw new Error(`Generated lesson is not valid JSON: ${cleaned.slice(0, 240)}`);
  }
}

function asArray(value) {
  return Array.isArray(value) ? value : [];
}

function asText(value) {
  if (typeof value !== "string") return "";
  return value.replaceAll("概念", "مفهوم").replace(/[\u3400-\u9fff]/g, "").trim();
}

function sanitizeDeep(value) {
  if (typeof value === "string") return asText(value);
  if (Array.isArray(value)) return value.map(sanitizeDeep);
  if (value && typeof value === "object") {
    return Object.fromEntries(Object.entries(value).map(([key, item]) => [key, sanitizeDeep(item)]));
  }
  return value;
}

function bulletList(items, formatter) {
  return items.map((item, index) => `${index + 1}. ${formatter(item, index)}`).join("\n");
}

function composeExplanation(parsed) {
  const objectives = asArray(parsed.objectives);
  const prerequisites = asArray(parsed.prerequisites);
  const keyConcepts = asArray(parsed.keyConcepts);
  const keyDefinitions = asArray(parsed.keyDefinitions);
  const workedExamples = asArray(parsed.workedExamples);
  const guidedPractice = asArray(parsed.guidedPractice);
  const commonMistakes = asArray(parsed.commonMistakes);
  const examPreparation = asArray(parsed.examPreparation);
  const leilaInstructions = asArray(parsed.leilaInstructions);
  const exercises = asArray(parsed.exercises);

  return [
    `مقدمة: ${asText(parsed.introduction)}`,
    `أهداف التعلم:\n${bulletList(objectives, (item) => asText(item))}`,
    `المكتسبات القبلية:\n${bulletList(prerequisites, (item) => asText(item))}`,
    `شرح مفصل وفق المنهاج المغربي والجذع المشترك:\n${asText(parsed.detailedExplanation)}`,
    `مفاهيم أساسية:\n${bulletList(keyConcepts, (item) => `${asText(item.name)}: ${asText(item.explanation)}`)}`,
    `تعريفات دقيقة:\n${bulletList(keyDefinitions, (item) => `${asText(item.term)}: ${asText(item.definition)}`)}`,
    `أمثلة محلولة خطوة بخطوة:\n${bulletList(
      workedExamples,
      (item) =>
        `مثال محلول: ${asText(item.title)}\nالمسألة: ${asText(item.problem)}\nالخطوات:\n${bulletList(asArray(item.steps), (step) => asText(step))}\nالحل والجواب: ${asText(item.answer)}`
    )}`,
    `تطبيقات وتدريب موجه:\n${bulletList(
      guidedPractice,
      (item) => `تطبيق: ${asText(item.prompt)}\nتلميح: ${asText(item.hint)}\nالجواب المنتظر: ${asText(item.expectedAnswer)}`
    )}`,
    `أخطاء شائعة وطريقة التصحيح:\n${bulletList(
      commonMistakes,
      (item) => `خطأ شائع: ${asText(item.mistake)}\nتصحيح وعلاج: ${asText(item.correction)}`
    )}`,
    `استعداد للفرض والامتحان:\n${bulletList(
      examPreparation,
      (item) => `وضعية امتحانية: ${asText(item.question)}\nطريقة الحل: ${asText(item.method)}\nالجواب: ${asText(item.answer)}`
    )}`,
    `تمارين إضافية مع الأجوبة والشروح:\n${bulletList(
      exercises,
      (item) =>
        `تمرين (${asText(item.difficulty)}): ${asText(item.question)}\nتلميح: ${asText(item.hint)}\nالجواب: ${asText(item.answer)}\nشرح التصحيح: ${asText(item.detailedExplanation)}`
    )}`,
    `تعليمات ليلى:\n${bulletList(leilaInstructions, (item) => `ليلى: ${asText(item)}`)}`,
    `ملخص وخلاصة:\n${asText(parsed.summary)}`,
  ]
    .filter((section) => section.replace(/[\s:.\n0-9]/g, "").length > 0)
    .join("\n\n");
}

function normalizeExercise(exercise, index) {
  const difficulty = ["easy", "medium", "hard"].includes(exercise?.difficulty) ? exercise.difficulty : index < 3 ? "easy" : index < 6 ? "medium" : "hard";
  return {
    type: ["mcq", "true_false", "fill_blank", "short_answer"].includes(exercise?.type) ? exercise.type : "short_answer",
    difficulty,
    question: asText(exercise?.question),
    options: Array.isArray(exercise?.options) ? exercise.options : undefined,
    correctAnswer: asText(exercise?.correctAnswer ?? exercise?.answer),
    explanation: asText(exercise?.detailedExplanation ?? exercise?.explanation),
    hint: asText(exercise?.hint),
    skillTag: asText(exercise?.skillTag),
    points: Number(exercise?.points ?? (difficulty === "easy" ? 10 : difficulty === "medium" ? 15 : 20)),
    orderIndex: index + 1,
  };
}

function normalizeGeneratedLesson(rawParsed) {
  const parsed = sanitizeDeep(rawParsed);
  const exercises = asArray(parsed.exercises).map(normalizeExercise);
  const vocabulary = asArray(parsed.vocabulary).length
    ? asArray(parsed.vocabulary)
    : asArray(parsed.keyDefinitions).map((item) => ({ word: asText(item.term), definition: asText(item.definition) }));
  const examples = asArray(parsed.examples).length
    ? asArray(parsed.examples)
    : asArray(parsed.workedExamples).map((item) => ({ text: `${asText(item.problem)} ${asText(item.answer)}`, note: asText(item.title) }));

  return {
    title: asText(parsed.title),
    objectives: asArray(parsed.objectives).map(asText).filter(Boolean),
    prerequisites: asArray(parsed.prerequisites),
    introduction: asText(parsed.introduction),
    detailedExplanation: asText(parsed.detailedExplanation),
    keyConcepts: asArray(parsed.keyConcepts),
    keyDefinitions: asArray(parsed.keyDefinitions),
    workedExamples: asArray(parsed.workedExamples),
    guidedPractice: asArray(parsed.guidedPractice),
    commonMistakes: asArray(parsed.commonMistakes),
    examPreparation: asArray(parsed.examPreparation),
    leilaInstructions: asArray(parsed.leilaInstructions),
    summary: asText(parsed.summary),
    vocabulary,
    examples,
    exercises,
    explanation: composeExplanation(parsed),
  };
}

export function buildQualityReport(payload, baseLesson = {}) {
  const quality = scoreLessonQuality({
    ...baseLesson,
    ...payload,
    exercise_count: payload.exercises?.length ?? 0,
  });

  const report = {
    length: String(payload.explanation ?? "").length,
    workedExamples: payload.workedExamples?.length ?? 0,
    exercises: payload.exercises?.length ?? 0,
    commonMistakes: payload.commonMistakes?.length ?? 0,
    examQuestions: payload.examPreparation?.length ?? 0,
    guidedPractice: payload.guidedPractice?.length ?? 0,
    hints: payload.exercises?.filter((exercise) => exercise.hint).length ?? 0,
    qualityScore: quality.score,
    status: quality.status,
    issues: quality.issues,
    deductions: quality.issues.map((issue) => ({ issue, points: 8 })),
  };

  const validationFailures = validateGeneratedLesson(payload);
  const weakSections = findWeakSections(payload);
  return { ...report, validationFailures, weakSections };
}

export function formatQualityReport(report) {
  return [
    "QUALITY REPORT",
    "--------------",
    `Length: ${report.length}`,
    `Worked examples: ${report.workedExamples}`,
    `Exercises: ${report.exercises}`,
    `Common mistakes: ${report.commonMistakes}`,
    `Exam questions: ${report.examQuestions}`,
    `Guided practice: ${report.guidedPractice}`,
    `Hints: ${report.hints}`,
    `Quality score: ${report.qualityScore}`,
    `Issues: ${report.issues.length ? report.issues.join(", ") : "none"}`,
    `Validation failures: ${report.validationFailures.length ? report.validationFailures.join(", ") : "none"}`,
    `Weak sections: ${report.weakSections.length ? report.weakSections.join(", ") : "none"}`,
    `Deductions: ${report.deductions.length ? report.deductions.map((item) => `${item.issue} -${item.points}`).join("; ") : "none"}`,
  ].join("\n");
}

function isSafeToApply(report, minimumScore, targetScore) {
  return (
    !report.validationFailures.length &&
    !report.weakSections.length &&
    report.qualityScore >= minimumScore &&
    report.qualityScore >= targetScore
  );
}

function safeFilePart(value) {
  return String(value ?? "")
    .trim()
    .replace(/[^\p{L}\p{N}-]+/gu, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80);
}

export function isGroqRateLimitError(error) {
  return error?.status === 429 || error?.error?.error?.code === "rate_limit_exceeded" || String(error?.message ?? "").includes("rate_limit");
}

function meaningfulSentenceCount(text) {
  return String(text ?? "")
    .split(/[.!؟?\n]+/)
    .map((sentence) => sentence.trim())
    .filter((sentence) => sentence.length >= 14).length;
}

function hasCalculationStep(text) {
  const value = String(text ?? "");
  return /[0-9٠-٩]+\s*[+\-×x*/=<>]\s*[0-9٠-٩]+/.test(value) || /[0-9٠-٩]+\s*=\s*[0-9٠-٩]/.test(value);
}

function hasExplanationSentence(text) {
  const value = String(text ?? "").toLowerCase();
  return /(لأن|بما أن|إذن|لذلك|معا|معًا|نقارن|نحسب|نعد|نضيف|نطرح|يساوي|أكبر|أصغر)/.test(value);
}

export function isWeakExerciseExplanation(explanation) {
  const text = String(explanation ?? "").trim();
  if (!text) return true;

  const genericOneLiners = [
    "لأننا جمعنا العددين",
    "اقرأ الأعداد بعناية",
    "قارن الأعداد بعناية",
    "انظر إلى الآحاد والعشرات",
  ];
  if (genericOneLiners.some((line) => text === line || text.includes(line))) return true;

  const hasRequiredStructure =
    /(reasoning|التفكير|السبب|الاستدلال)/i.test(text) &&
    /(calculation|الحساب|العملية)/i.test(text) &&
    /(answer|الجواب|الإجابة)/i.test(text) &&
    /(explanation|الشرح|التفسير)/i.test(text);
  const hasEnoughSentences = meaningfulSentenceCount(text) >= 2;
  const hasCalculationAndExplanation = hasCalculationStep(text) && hasExplanationSentence(text);

  return text.length < 80 || !(hasRequiredStructure || hasEnoughSentences || hasCalculationAndExplanation);
}

export async function saveGeneratedLessonArtifact(lesson, payload, report, metadata = {}) {
  if (!payload || !report) return null;

  await fs.mkdir(GENERATED_LESSONS_DIR, { recursive: true });
  const timestamp = new Date().toISOString();
  const lessonId = lesson.lesson_id ?? lesson.id ?? "unknown-lesson";
  const title = lesson.lesson_title ?? lesson.title ?? payload.title ?? "untitled";
  const filename = `${timestamp.replace(/[:.]/g, "-")}_${lessonId}_${safeFilePart(title)}.json`;
  const artifactPath = path.join(GENERATED_LESSONS_DIR, filename);
  const artifact = {
    timestamp,
    lesson: {
      id: lessonId,
      title,
      grade: lesson.grade_slug ?? lesson.grade_title,
      subject: lesson.subject_slug ?? lesson.subject_title,
      unit: lesson.unit_slug ?? lesson.unit_title,
    },
    generated: payload,
    qualityReport: report,
    weakSections: report.weakSections,
    safeToApply: Boolean(metadata.safeToApply),
    status: metadata.status ?? (metadata.safeToApply ? "safe_to_apply" : "generated_not_safe"),
    message: metadata.message ?? null,
    resumeCommand: `node scripts/test-lesson-generation.mjs --lesson-id=${lessonId} --resume-from-local`,
  };

  await fs.writeFile(artifactPath, JSON.stringify(artifact, null, 2), "utf8");
  return artifactPath;
}

export async function loadLatestGeneratedLessonArtifact(lessonId) {
  const entries = await fs.readdir(GENERATED_LESSONS_DIR).catch((error) => {
    if (error?.code === "ENOENT") return [];
    throw error;
  });
  const matches = entries
    .filter((entry) => entry.endsWith(".json") && entry.includes(String(lessonId)))
    .sort()
    .reverse();

  if (!matches.length) {
    throw new Error(`No local generated lesson artifact found for lesson ${lessonId}.`);
  }

  const artifactPath = path.join(GENERATED_LESSONS_DIR, matches[0]);
  const artifact = JSON.parse(await fs.readFile(artifactPath, "utf8"));
  return { artifactPath, artifact };
}

export function validateGeneratedLesson(payload) {
  const failures = [];
  if (!payload.title) failures.push("missing title");
  if (!payload.introduction) failures.push("missing introduction");
  if (!payload.detailedExplanation) failures.push("missing detailed explanation");
  if ((payload.workedExamples?.length ?? 0) < MIN_WORKED_EXAMPLES) failures.push("fewer than 3 worked examples");
  if ((payload.guidedPractice?.length ?? 0) < MIN_GUIDED_PRACTICE) failures.push("fewer than 3 guided practice activities");
  if ((payload.exercises?.length ?? 0) < MIN_EXERCISES) failures.push("fewer than 8 exercises");
  if ((payload.commonMistakes?.length ?? 0) < MIN_COMMON_MISTAKES) failures.push("missing common mistakes");
  if ((payload.examPreparation?.length ?? 0) < MIN_EXAM_QUESTIONS) failures.push("missing exam preparation");
  if ((payload.exercises?.filter((exercise) => exercise.hint).length ?? 0) < MIN_EXERCISES) failures.push("missing hints on exercises");
  if (String(payload.explanation ?? "").length < MIN_CONTENT_CHARS) failures.push("content length below 2000 characters");
  if (payload.exercises?.some((exercise) => !exercise.correctAnswer || !exercise.explanation)) {
    failures.push("one or more exercises missing answers or explanations");
  }
  if (payload.exercises?.some((exercise) => isWeakExerciseExplanation(exercise.explanation))) {
    failures.push("one or more exercise explanations are too short or missing reasoning/calculation");
  }
  if (/[\u3400-\u9fff]/.test(JSON.stringify(payload))) failures.push("contains non-Arabic CJK characters");
  if (/طرح رقمين|طرح ثلاثة أرقام|طرح أربعة أرقام/.test(JSON.stringify(payload))) {
    failures.push("uses vague probability experiment wording");
  }
  const uniqueQuestions = new Set((payload.exercises ?? []).map((exercise) => String(exercise.question ?? "").trim()));
  if (uniqueQuestions.size < MIN_EXERCISES) failures.push("exercise questions are not unique");
  const uniqueAnswers = new Set((payload.exercises ?? []).map((exercise) => String(exercise.correctAnswer ?? "").trim()));
  if (uniqueAnswers.size < Math.ceil(MIN_EXERCISES / 2)) failures.push("exercise answers are too repetitive");
  return failures;
}

export function findWeakSections(payload) {
  const weak = [];
  if ((payload.objectives?.length ?? 0) < 3) weak.push("fewer than 3 learning objectives");
  if ((payload.prerequisites?.length ?? 0) < 3) weak.push("fewer than 3 prerequisites");
  if ((payload.keyConcepts?.length ?? 0) < 3) weak.push("fewer than 3 key concepts");
  if ((payload.keyDefinitions?.length ?? 0) < 3) weak.push("fewer than 3 key definitions");
  if (payload.workedExamples?.some((example) => (example.steps?.length ?? 0) < 4)) {
    weak.push("one or more worked examples has fewer than 4 steps");
  }
  if (payload.exercises?.some((exercise) => isWeakExerciseExplanation(exercise.explanation))) {
    weak.push("one or more exercise explanations are short or missing reasoning/calculation");
  }
  return weak;
}

async function callGroq(prompt, options = {}) {
  const groq = new Groq({ apiKey: requireGroqApiKey() });
  const completion = await groq.chat.completions.create({
    model: process.env.GROQ_MODEL ?? "llama-3.3-70b-versatile",
    messages: [{ role: "user", content: prompt }],
    temperature: 0.25,
    max_tokens: Number(process.env.GROQ_MAX_TOKENS ?? (options.compact ? 3000 : 4500)),
    stream: false,
  });
  return completion.choices[0]?.message?.content ?? "{}";
}

async function generateOnce(lesson, feedback = [], options = {}) {
  const text = await callGroq(buildPrompt(lesson, feedback, options), options);
  return normalizeGeneratedLesson(parseGeneratedJson(text));
}

export async function generateEnhancedLessonWithReport(lesson, options = {}) {
  const minimumScore = Number(options.minimumScore ?? MIN_ACCEPTABLE_SCORE);
  const targetScore = Number(options.targetScore ?? MIN_TARGET_SCORE);
  const maxAttempts = Number(options.noRetry ? 1 : options.maxAttempts ?? 4);
  const saveArtifact = Boolean(options.saveArtifact);
  const skipIfRateLimited = Boolean(options.skipIfRateLimited);
  let payload;
  let report;
  let feedback = [];
  let artifactPath = null;

  for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
    try {
      payload = await generateOnce(lesson, feedback, options);
    } catch (error) {
      if (isGroqRateLimitError(error) && (skipIfRateLimited || payload || report)) {
        const message = "Generation incomplete because retry was rate-limited.";
        artifactPath = saveArtifact
          ? await saveGeneratedLessonArtifact(lesson, payload, report, {
              safeToApply: false,
              status: "blocked_by_rate_limit",
              message,
            })
          : null;
        return {
          payload,
          report,
          artifactPath,
          safeToApply: false,
          status: "blocked_by_rate_limit",
          message,
          resumeCommand: `node scripts/test-lesson-generation.mjs --lesson-id=${lesson.lesson_id ?? lesson.id} --resume-from-local`,
          error,
        };
      }
      throw error;
    }

    report = buildQualityReport(payload, lesson);
    console.log(formatQualityReport(report));

    const passed = isSafeToApply(report, minimumScore, targetScore);
    if (saveArtifact) {
      artifactPath = await saveGeneratedLessonArtifact(lesson, payload, report, {
        safeToApply: passed,
        status: passed ? "safe_to_apply" : "generated_not_safe",
        message: passed ? "Generated lesson passed all quality gates." : "Generated lesson has quality issues and is not safe to apply.",
      });
      console.log(`Saved local review artifact: ${artifactPath}`);
    }

    if (passed) break;

    if (attempt < maxAttempts) {
      feedback = [
        ...report.validationFailures,
        ...report.weakSections.map((section) => `weak section: ${section}`),
        ...report.issues.map((issue) => `quality issue: ${issue}`),
        `Target quality score is ${targetScore}; previous score was ${report.qualityScore}.`,
        "Regenerate the full lesson, not only the missing fields.",
        "Make every missing or weak section explicit with Arabic headings and enough detail.",
        "If prerequisites are weak, provide at least 3 concrete prerequisites such as fractions, set notation, counting cases, percentages.",
        "For every exercise explanation, include reasoning, calculation, final answer, and a child-friendly explanation. Do not use one-sentence generic explanations.",
      ];
      console.log(`\nRegenerating with quality feedback (${attempt + 1}/${maxAttempts})...`);
    }
  }

  if (report.validationFailures.length) {
    return {
      payload,
      report,
      artifactPath,
      safeToApply: false,
      status: "generated_not_safe",
      message: `Generated lesson failed validation: ${report.validationFailures.join(", ")}`,
    };
  }
  if (report.qualityScore < minimumScore) {
    return {
      payload,
      report,
      artifactPath,
      safeToApply: false,
      status: "generated_not_safe",
      message: `Generated lesson scored ${report.qualityScore}, below threshold ${minimumScore}. Issues: ${report.issues.join(", ")}`,
    };
  }
  if (report.qualityScore < targetScore) {
    return {
      payload,
      report,
      artifactPath,
      safeToApply: false,
      status: "generated_not_safe",
      message: `Generated lesson scored ${report.qualityScore}, below target ${targetScore}. Issues: ${report.issues.join(", ")}`,
    };
  }
  if (report.weakSections.length) {
    return {
      payload,
      report,
      artifactPath,
      safeToApply: false,
      status: "generated_not_safe",
      message: `Generated lesson still has weak sections: ${report.weakSections.join(", ")}`,
    };
  }

  return {
    payload,
    report,
    artifactPath,
    safeToApply: true,
    status: "safe_to_apply",
    message: "Generated lesson passed all quality gates.",
  };
}

export async function generateEnhancedLesson(lesson, options = {}) {
  const result = await generateEnhancedLessonWithReport(lesson, options);
  if (!result.safeToApply) {
    throw new Error(result.message);
  }
  return result.payload;
}

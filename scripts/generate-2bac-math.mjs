#!/usr/bin/env node
/**
 * Phase 58A - 2BAC Mathematics Content Generator
 *
 * Safe by default:
 * - Dry-run unless --apply is passed.
 * - One pilot lesson unless --all or --limit is passed.
 * - --skip-ai performs static catalog checks without Groq or DB access.
 */

import fs from "node:fs";
import path from "node:path";

const GENERATED_DIR = ".generated-lessons";
const REPORTS_DIR = "reports";
const MODEL = "llama-3.3-70b-versatile";
const GRADE_SLUG = "bac2";
const SUBJECT_SLUG = "advanced-math";
const SUBJECT_TITLE = "الرياضيات - الثانية باكالوريا";

function loadEnv(file) {
  const full = path.resolve(process.cwd(), file);
  if (!fs.existsSync(full)) return;

  for (const line of fs.readFileSync(full, "utf8").split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#") || !trimmed.includes("=")) continue;
    const [key, ...rest] = trimmed.split("=");
    if (!process.env[key]) {
      process.env[key] = rest.join("=").trim().replace(/^["']|["']$/g, "");
    }
  }
}

function parseArgs(argv) {
  const flags = {
    apply: false,
    all: false,
    limit: undefined,
    topic: undefined,
    lesson: undefined,
    skipAi: false,
  };

  for (const arg of argv) {
    if (arg === "--apply") flags.apply = true;
    else if (arg === "--all") flags.all = true;
    else if (arg === "--skip-ai") flags.skipAi = true;
    else if (arg.startsWith("--limit=")) {
      const value = Number.parseInt(arg.slice("--limit=".length), 10);
      if (!Number.isFinite(value) || value < 1) throw new Error("--limit must be a positive integer");
      flags.limit = value;
    } else if (arg.startsWith("--topic=")) {
      flags.topic = arg.slice("--topic=".length).trim();
    } else if (arg.startsWith("--lesson=")) {
      flags.lesson = arg.slice("--lesson=".length).trim();
    } else {
      throw new Error(`Unknown flag: ${arg}`);
    }
  }

  return flags;
}

const TOPICS = [
  {
    unitSlug: "limites",
    unitTitle: "النهايات (Limites)",
    order: 1,
    lessons: [
      ["definition-limite", "مفهوم النهاية وتعريفها", "التعريف الرياضي للنهاية، التعويض المباشر، حالة 0/0، النهايات الجانبية، والتمييز بين f(a) و lim f(x)."],
      ["calcul-limites", "تقنيات حساب النهايات", "قواعد العمليات على النهايات، رفع الإبهام بالتبسيط والتحليل والعبارة المرافقة، والنهايات المرجعية الأساسية."],
      ["limites-infini", "النهايات عند اللانهاية والمقاربات", "الحدود المسيطرة، المقاربات الأفقية والعمودية والمائلة، وكيفية توظيفها في دراسة دالة."],
      ["continuite", "الاستمرارية وعلاقتها بالنهايات", "الاستمرارية عند نقطة وعلى فترة، نظرية القيم الوسطية TVI، واستعمالها لإثبات وجود حل لمعادلة."],
    ],
  },
  {
    unitSlug: "derivation",
    unitTitle: "الاشتقاق (Derivation)",
    order: 2,
    lessons: [
      ["definition-derivee", "تعريف المشتق والتأويل الهندسي", "تعريف المشتق بالنهاية f'(a)=lim (f(a+h)-f(a))/h، الحساب من التعريف، معنى ميل المماس، ومعادلة المماس."],
      ["regles-derivation", "قواعد الاشتقاق", "مشتق الثابت والقوى والجذر والدوال المثلثية و ln و exp، وقواعد الجداء والخارج والسلسلة."],
      ["etude-variation", "تطبيق المشتق في دراسة التغير والتطرف", "علاقة إشارة f'(x) بالتزايد والتناقص، القيم الحرجة، القيم القصوى، وجدول التغيرات كما يطلب في الباكالوريا."],
      ["tangente-applications", "معادلة المماس وتطبيقات المشتق", "معادلة المماس y=f(a)+f'(a)(x-a)، تطبيقات في الفيزياء والاقتصاد، وتحليل وضعيات باكالوريا."],
    ],
  },
  {
    unitSlug: "integration",
    unitTitle: "التكامل (Integration)",
    order: 3,
    lessons: [
      ["integrale-indefinie", "التكامل غير المحدود", "مفهوم primitive، جدول التكاملات الأساسية، خطية التكامل، وتكامل الدوال المركبة من نوع u'/u و u^n u'."],
      ["integrale-definie", "التكامل المحدود ونظرية التكامل الأساسية", "تعريف التكامل المحدود، نظرية نيوتن لايبنيز F(b)-F(a)، الخصائص الأساسية، ومتباينة الوسط التكاملية."],
      ["calcul-aires", "حساب المساحات بالتكامل", "المساحة بين المنحنى ومحور السينات، المساحة بين منحنيين، تحديد نقاط التقاطع وتجزيء الفترة حسب الإشارة."],
      ["equations-differentielles", "المعادلات التفاضلية البسيطة", "حل y'=ay و y'=ay+b، الحل العام والخاص، تحديد الثابت بالشرط الابتدائي، وتطبيقات النمو والتناقص الأسي."],
    ],
  },
  {
    unitSlug: "fonctions",
    unitTitle: "الدوال (Fonctions)",
    order: 4,
    lessons: [
      ["fonction-logarithme", "الدالة اللوغاريتمية", "الدالة اللوغاريتمية الطبيعية ln: المجال، النهايات، المشتق، قواعد اللوغاريتم، ودراسة دوال تتضمن ln."],
      ["fonction-exponentielle", "الدالة الأسية", "الدالة الأسية exp: الخصائص الأساسية، العلاقة مع ln، النهايات والمشتق، وتطبيقات النمو الأسي."],
      ["etude-fonction-complete", "دراسة دالة كاملة", "المجال، النهايات، المقاربات، الاشتقاق، جدول التغيرات، التمثيل المبياني، وقراءة النتائج."],
      ["fonctions-applications-bac", "تطبيقات الدوال في مسائل الباكالوريا", "الجمع بين النهايات والاشتقاق والتكامل، تحليل وضعيات مركبة، وتنظيم الحل للحصول على كامل النقط."],
    ],
  },
  {
    unitSlug: "suites",
    unitTitle: "المتتاليات (Suites)",
    order: 5,
    lessons: [
      ["suites-arithmetiques-geometriques", "المتتاليات الحسابية والهندسية", "التعريف، الحد العام، مجموع الحدود، التمثيل، والتطبيقات البسيطة في مسائل باكالوريا."],
      ["limites-suites", "نهايات المتتاليات", "النهايات المرجعية، المقارنة، الحصر، الرتابة والتقارب، وربط النهاية بسلوك الحدود."],
      ["raisonnement-recurrence", "الاستقراء الرياضي", "التحقق الأولي، فرضية الاستقراء، خطوة الانتقال، تطبيقات على الصيغ والمتباينات وقابلية القسمة."],
      ["suites-recurrentes", "المتتاليات المعرفة بالتكرار", "الحد الثابت، دراسة الاتجاه بإشارة u(n+1)-u(n)، استعمال الرسم التكراري، والتقارب نحو حل f(x)=x."],
    ],
  },
].map((topic) => ({
  ...topic,
  lessons: topic.lessons.map(([slug, title, topicDescription], index) => ({
    slug,
    title,
    topic: topicDescription,
    order: index + 1,
    objectives: [
      `فهم المفهوم الأساسي في درس ${title}`,
      "تطبيق الطريقة المنهجية في تمارين متدرجة",
      "حل تمرين باكالوريا باستعمال خطوات واضحة",
    ],
  })),
}));

function flattenCatalog() {
  return TOPICS.flatMap((topic) => topic.lessons.map((lesson) => ({ topic, lesson })));
}

function selectLessons(flags) {
  let selected = flattenCatalog();

  if (flags.topic) selected = selected.filter(({ topic }) => topic.unitSlug === flags.topic);
  if (flags.lesson) selected = selected.filter(({ lesson }) => lesson.slug === flags.lesson);
  if (flags.topic && !TOPICS.some((topic) => topic.unitSlug === flags.topic)) {
    throw new Error(`No topic found for --topic=${flags.topic}`);
  }
  if (flags.lesson && selected.length === 0) {
    throw new Error(`No lesson found for --lesson=${flags.lesson}`);
  }

  const effectiveLimit = flags.limit ?? (flags.all ? selected.length : 1);
  return selected.slice(0, effectiveLimit);
}

function printBanner(flags, selected) {
  console.log("\nPhase 58A - 2BAC Mathematics Generator");
  console.log("=".repeat(56));
  console.log(`mode: ${flags.apply ? "apply" : "dry-run"}`);
  console.log(`selected topic: ${flags.topic ?? "not specified"}`);
  console.log(`selected lesson: ${flags.lesson ?? "not specified"}`);
  console.log(`limit: ${flags.limit ?? (flags.all ? "all selected" : "1 pilot lesson")}`);
  console.log(`DB write enabled: ${flags.apply ? "yes" : "no"}`);
  console.log(`AI enabled: ${flags.skipAi ? "no" : "yes"}`);
  console.log(`planned lessons: ${selected.length}`);
  if (flags.apply) {
    console.log("\nWARNING: --apply enables database writes after QA passes.");
    console.log("Use --all only after pilot lessons pass QA and human review.");
  }
  console.log("=".repeat(56));
}

function staticCatalogCheck(selected) {
  const issues = [];
  const seen = new Set();

  for (const { topic, lesson } of selected) {
    const key = `${topic.unitSlug}/${lesson.slug}`;
    if (seen.has(key)) issues.push(`duplicate lesson slug: ${key}`);
    seen.add(key);
    if (!topic.unitSlug || !topic.unitTitle) issues.push(`topic metadata missing for ${lesson.slug}`);
    if (!lesson.slug || !lesson.title || !lesson.topic) issues.push(`lesson metadata missing in ${key}`);
    if (!Array.isArray(lesson.objectives) || lesson.objectives.length < 2) issues.push(`lesson objectives too weak: ${key}`);
  }

  return issues;
}

function buildPrompt(lesson, topic) {
  return `أنت خبير تربوي متخصص في منهاج الرياضيات المغربي للسنة الثانية باكالوريا.

المطلوب: أنشئ درساً كاملاً عالي الجودة مطابقاً لمعيار OQUL Phase 58.

الوحدة: ${topic.unitTitle}
عنوان الدرس: ${lesson.title}
وصف الدرس: ${lesson.topic}
الأهداف: ${lesson.objectives.join("؛ ")}

قواعد صارمة:
- أعد JSON صالحاً فقط، دون Markdown ودون code fences ودون نص خارج JSON.
- يجب أن تكون اللغة عربية أكاديمية واضحة مع مصطلحات فرنسية دقيقة.
- يجب أن يرتبط الدرس بمنهاج الباكالوريا المغربية وبطريقة التصحيح المتوقعة.
- لا تستعمل نصوصاً عامة أو placeholders.
- يجب أن يكون المحتوى قابلاً لاستعمال ليلى، Lesson Helper، Research، Exam Prep، و Learning Path.
- يجب أن يتضمن BAC layer واضحاً وليس نصائح عامة.

أعد البنية التالية حرفياً مع ملء كل الحقول:
{
  "coreLearning": {
    "objectives": [],
    "prerequisites": [],
    "keyConcepts": [],
    "keyDefinitions": [],
    "frenchTerminology": [],
    "explanation": "",
    "moroccanExamples": [],
    "summary": ""
  },
  "practice": {
    "guidedExamples": [],
    "solvedExercises": [],
    "progressiveExercises": [],
    "challengeExercises": []
  },
  "bac": {
    "bacStyleExercise": "",
    "methodology": "",
    "commonMistakes": [],
    "pointAllocation": [],
    "examinerExpectations": [],
    "timeManagementAdvice": "",
    "recognitionPattern": ""
  },
  "ai": {
    "leilaPrompts": [],
    "lessonHelperPrompts": [],
    "researchPrompts": [],
    "learningPathLinks": [],
    "remediationGuidance": [],
    "weakPointDetectionHints": []
  }
}

الحدود الدنيا:
- المحتوى المدمج لا يقل عن 3500 حرف.
- 3 guidedExamples على الأقل.
- 3 solvedExercises على الأقل.
- 8 progressiveExercises على الأقل.
- 2 challengeExercises على الأقل.
- 3 commonMistakes على الأقل.
- BAC-style exercise واحد على الأقل.
- كل تمرين يجب أن يتضمن جواباً وتصحيحاً أو شرحاً.
- frenchTerminology مطلوبة ولا تقل عن 5 عناصر.
- summary مطلوبة.
- leilaPrompts و lessonHelperPrompts و researchPrompts مطلوبة.
- remediationGuidance و weakPointDetectionHints مطلوبة.`;
}

function stripCodeFence(text) {
  return text.replace(/^```(?:json)?\s*/i, "").replace(/\s*```$/i, "").trim();
}

function parseGeneratedJson(rawText) {
  const stripped = stripCodeFence(rawText);
  try {
    return JSON.parse(stripped);
  } catch (error) {
    const debugDir = path.join(GENERATED_DIR, "debug");
    fs.mkdirSync(debugDir, { recursive: true });
    const debugPath = path.join(debugDir, `malformed-json-${new Date().toISOString().replace(/[:.]/g, "-")}.txt`);
    fs.writeFileSync(debugPath, rawText, "utf8");
    throw new Error(`AI returned malformed JSON. Raw response saved to ${debugPath}. ${error.message}`);
  }
}

async function createGroqClient() {
  if (!process.env.GROQ_API_KEY) throw new Error("GROQ_API_KEY is required unless --skip-ai is used");
  const { default: Groq } = await import("groq-sdk");
  return new Groq({ apiKey: process.env.GROQ_API_KEY });
}

async function generateLesson(groq, topic, lesson) {
  const completion = await groq.chat.completions.create({
    model: MODEL,
    messages: [{ role: "user", content: buildPrompt(lesson, topic) }],
    max_tokens: 6000,
    temperature: 0.25,
    stream: false,
    response_format: { type: "json_object" },
  });
  return parseGeneratedJson(completion.choices[0]?.message?.content ?? "{}");
}

function asArray(value) {
  return Array.isArray(value) ? value : [];
}

function stringifyItem(value) {
  if (typeof value === "string") return value;
  if (value && typeof value === "object") return JSON.stringify(value, null, 2);
  return "";
}

function combinedContent(generated) {
  return [
    generated.coreLearning?.explanation,
    generated.coreLearning?.summary,
    ...asArray(generated.coreLearning?.objectives),
    ...asArray(generated.coreLearning?.keyConcepts),
    ...asArray(generated.coreLearning?.keyDefinitions).map(stringifyItem),
    ...asArray(generated.coreLearning?.frenchTerminology).map(stringifyItem),
    ...asArray(generated.coreLearning?.moroccanExamples).map(stringifyItem),
    ...asArray(generated.practice?.guidedExamples).map(stringifyItem),
    ...asArray(generated.practice?.solvedExercises).map(stringifyItem),
    ...asArray(generated.practice?.progressiveExercises).map(stringifyItem),
    ...asArray(generated.practice?.challengeExercises).map(stringifyItem),
    generated.bac?.bacStyleExercise,
    generated.bac?.methodology,
    ...asArray(generated.bac?.commonMistakes).map(stringifyItem),
    ...asArray(generated.bac?.examinerExpectations).map(stringifyItem),
    generated.bac?.timeManagementAdvice,
    generated.bac?.recognitionPattern,
    ...asArray(generated.ai?.leilaPrompts),
    ...asArray(generated.ai?.lessonHelperPrompts),
    ...asArray(generated.ai?.researchPrompts),
    ...asArray(generated.ai?.remediationGuidance),
    ...asArray(generated.ai?.weakPointDetectionHints),
  ].filter(Boolean).join("\n\n");
}

function hasAnswerAndCorrection(exercise) {
  if (typeof exercise === "string") return /جواب|الحل|تصحيح|answer|solution/i.test(exercise);
  if (!exercise || typeof exercise !== "object") return false;
  const answer = exercise.answer ?? exercise.correctAnswer ?? exercise.correct_answer;
  const explanation = exercise.explanation ?? exercise.correction ?? exercise.solution ?? exercise.detailedExplanation;
  return Boolean(String(answer ?? "").trim()) && Boolean(String(explanation ?? "").trim());
}

function detectPlaceholders(text) {
  const placeholders = [
    "placeholder",
    "lorem ipsum",
    "TODO",
    "مثال بسيط",
    "جواب نموذجي مختصر",
    "هذا درس في الرياضيات",
    "درس أصلي من oqul",
    "يحتاج مطابقة",
  ];
  return placeholders.filter((placeholder) => text.toLowerCase().includes(placeholder.toLowerCase()));
}

function scoreStatus(score) {
  if (score >= 90) return "production_ready";
  if (score >= 80) return "light_review";
  if (score >= 70) return "needs_revision";
  return "reject";
}

function qaCheck(generated, title) {
  const issues = [];
  const hardStops = [];
  const content = combinedContent(generated);
  const placeholders = detectPlaceholders(content);
  const guidedExamples = asArray(generated.practice?.guidedExamples);
  const solvedExercises = asArray(generated.practice?.solvedExercises);
  const progressiveExercises = asArray(generated.practice?.progressiveExercises);
  const challengeExercises = asArray(generated.practice?.challengeExercises);
  const allExercises = [...solvedExercises, ...progressiveExercises, ...challengeExercises];
  const commonMistakes = asArray(generated.bac?.commonMistakes);
  const frenchTerminology = asArray(generated.coreLearning?.frenchTerminology);
  const leilaPrompts = asArray(generated.ai?.leilaPrompts);
  const lessonHelperPrompts = asArray(generated.ai?.lessonHelperPrompts);
  const researchPrompts = asArray(generated.ai?.researchPrompts);
  const remediation = asArray(generated.ai?.remediationGuidance);
  const weakHints = asArray(generated.ai?.weakPointDetectionHints);
  const exercisesWithAnswers = allExercises.filter(hasAnswerAndCorrection).length;

  if (content.length < 3500) issues.push("content_below_3500_chars");
  if (guidedExamples.length < 3) issues.push("guided_examples_below_3");
  if (solvedExercises.length < 3) issues.push("solved_exercises_below_3");
  if (progressiveExercises.length < 8) issues.push("progressive_exercises_below_8");
  if (challengeExercises.length < 2) issues.push("challenge_exercises_below_2");
  if (commonMistakes.length < 3) issues.push("common_mistakes_below_3");
  if (!String(generated.bac?.bacStyleExercise ?? "").trim()) issues.push("missing_bac_style_exercise");
  if (!String(generated.bac?.methodology ?? "").trim()) issues.push("missing_bac_methodology");
  if (frenchTerminology.length < 5) issues.push("missing_or_weak_french_terminology");
  if (!String(generated.coreLearning?.summary ?? "").trim()) issues.push("missing_summary");
  if (leilaPrompts.length < 1) issues.push("missing_leila_prompts");
  if (lessonHelperPrompts.length < 1) issues.push("missing_lesson_helper_prompts");
  if (researchPrompts.length < 1) issues.push("missing_research_prompts");
  if (remediation.length < 1) issues.push("missing_remediation_guidance");
  if (weakHints.length < 1) issues.push("missing_weak_point_detection_hints");
  if (exercisesWithAnswers < allExercises.length) issues.push("exercise_answers_or_corrections_missing");
  if (placeholders.length > 0) issues.push(`placeholder_text:${placeholders.join("|")}`);

  if (placeholders.length > 0) hardStops.push("placeholders_detected");
  if (!String(generated.bac?.bacStyleExercise ?? "").trim()) hardStops.push("bac_section_missing");
  if (frenchTerminology.length < 5) hardStops.push("french_terminology_missing");
  if (exercisesWithAnswers < allExercises.length) hardStops.push("exercises_lack_answers_or_corrections");
  if (leilaPrompts.length < 1 || lessonHelperPrompts.length < 1) hardStops.push("not_usable_by_leila_or_lesson_helper");

  const score = Math.max(0, 100 - issues.length * 8 - hardStops.length * 10);
  return {
    title,
    score,
    status: scoreStatus(score),
    safeToWrite: score >= 80 && hardStops.length === 0,
    issues,
    hardStops,
    metrics: {
      contentLength: content.length,
      guidedExamples: guidedExamples.length,
      solvedExercises: solvedExercises.length,
      progressiveExercises: progressiveExercises.length,
      challengeExercises: challengeExercises.length,
      commonMistakes: commonMistakes.length,
      frenchTerminology: frenchTerminology.length,
      leilaPrompts: leilaPrompts.length,
      lessonHelperPrompts: lessonHelperPrompts.length,
      researchPrompts: researchPrompts.length,
      remediationGuidance: remediation.length,
      weakPointDetectionHints: weakHints.length,
      exercisesWithAnswers,
      totalPracticeExercises: allExercises.length,
    },
  };
}

function normalizeExercise(exercise, index) {
  if (typeof exercise === "string") {
    return {
      type: "open_ended",
      question: exercise,
      correctAnswer: "انظر التصحيح المرفق.",
      explanation: "يجب اتباع خطوات الحل المنهجي للوصول إلى الجواب.",
      points: index < 8 ? 10 : 20,
    };
  }
  return {
    type: exercise.type ?? "open_ended",
    question: exercise.question ?? exercise.prompt ?? stringifyItem(exercise),
    options: exercise.options,
    correctAnswer: exercise.correctAnswer ?? exercise.correct_answer ?? exercise.answer ?? "انظر التصحيح المرفق.",
    explanation: exercise.explanation ?? exercise.correction ?? exercise.solution ?? exercise.detailedExplanation ?? "تصحيح منهجي مطلوب.",
    points: exercise.points ?? (index < 8 ? 10 : 20),
  };
}

function mapToDbContent(generated) {
  const vocabulary = [
    ...asArray(generated.coreLearning?.keyDefinitions),
    ...asArray(generated.coreLearning?.frenchTerminology),
  ];
  const examples = [
    ...asArray(generated.practice?.guidedExamples),
    ...asArray(generated.practice?.solvedExercises),
  ].map((example) => ({ text: stringifyItem(example), note: "Phase 58 guided/solved example" }));
  const explanation = [
    generated.coreLearning?.explanation,
    generated.bac?.methodology ? `منهجية الباكالوريا:\n${generated.bac.methodology}` : "",
    asArray(generated.bac?.examinerExpectations).length
      ? `انتظارات المصحح:\n${asArray(generated.bac.examinerExpectations).map(stringifyItem).join("\n")}`
      : "",
  ].filter(Boolean).join("\n\n");
  const exercises = [
    ...asArray(generated.practice?.progressiveExercises),
    ...asArray(generated.practice?.challengeExercises),
    generated.bac?.bacStyleExercise
      ? {
          type: "open_ended",
          question: stringifyItem(generated.bac.bacStyleExercise),
          correctAnswer: "انظر التصحيح والمنهجية المرفقة.",
          explanation: generated.bac.methodology ?? "تصحيح منهجي بأسلوب الباكالوريا.",
          points: 20,
        }
      : null,
  ].filter(Boolean).map((exercise, index) => normalizeExercise(exercise, index));
  return { explanation, vocabulary, examples, summary: generated.coreLearning?.summary ?? "", exercises };
}

function saveArtifact({ topic, lesson, generated, qa, flags, dbWriteResult }) {
  fs.mkdirSync(GENERATED_DIR, { recursive: true });
  const stamp = new Date().toISOString().replace(/[:.]/g, "-");
  const filePath = path.join(GENERATED_DIR, `${topic.unitSlug}-${lesson.slug}-${stamp}.json`);
  fs.writeFileSync(filePath, JSON.stringify({
    lessonSlug: lesson.slug,
    topicSlug: topic.unitSlug,
    timestamp: new Date().toISOString(),
    generatedContent: generated,
    qaResult: qa,
    applyMode: flags.apply,
    dbWriteResult: dbWriteResult ?? null,
  }, null, 2), "utf8");
  return filePath;
}

async function createDbClient() {
  if (!process.env.DATABASE_URL) throw new Error("DATABASE_URL is required only when --apply is used");
  const { neon } = await import("@neondatabase/serverless");
  return neon(process.env.DATABASE_URL);
}

async function writeLessonToDb(sql, topic, lesson, generated, qa) {
  if (!qa.safeToWrite) throw new Error(`QA hard stop: ${qa.issues.join(", ") || "unknown issue"}`);
  const gradeRows = await sql`select id from grades where slug = ${GRADE_SLUG} limit 1`;
  if (!gradeRows[0]) throw new Error(`Grade '${GRADE_SLUG}' not found in DB`);
  const gradeId = gradeRows[0].id;
  const subjectRows = await sql`
    insert into subjects (grade_id, slug, title_ar, icon, color, order_index, is_active)
    values (${gradeId}, ${SUBJECT_SLUG}, ${SUBJECT_TITLE}, 'Calculator', '#7c3aed', 1, true)
    on conflict (grade_id, slug) do update set title_ar = excluded.title_ar, is_active = true
    returning id
  `;
  const subjectId = subjectRows[0].id;
  const unitRows = await sql`
    insert into units (subject_id, slug, title_ar, order_index, is_published)
    values (${subjectId}, ${topic.unitSlug}, ${topic.unitTitle}, ${topic.order}, true)
    on conflict (subject_id, slug) do update set title_ar = excluded.title_ar, order_index = excluded.order_index
    returning id
  `;
  const unitId = unitRows[0].id;
  const lessonRows = await sql`
    insert into lessons (unit_id, slug, title_ar, objectives, difficulty, estimated_duration_minutes, order_index, is_published)
    values (${unitId}, ${lesson.slug}, ${lesson.title}, ${JSON.stringify(lesson.objectives)}::jsonb, 'hard', 40, ${lesson.order}, true)
    on conflict (unit_id, slug) do update
      set title_ar = excluded.title_ar, objectives = excluded.objectives, difficulty = 'hard', is_published = true
    returning id
  `;
  const lessonId = lessonRows[0].id;
  const mapped = mapToDbContent(generated);
  console.log(`DB target: grade=${gradeId} subject=${subjectId} unit=${unitId} lesson=${lessonId}`);
  await sql`
    insert into lesson_contents (lesson_id, explanation, vocabulary, examples, summary)
    values (${lessonId}, ${mapped.explanation}, ${JSON.stringify(mapped.vocabulary)}::jsonb, ${JSON.stringify(mapped.examples)}::jsonb, ${mapped.summary})
    on conflict (lesson_id) do update
      set explanation = excluded.explanation, vocabulary = excluded.vocabulary, examples = excluded.examples, summary = excluded.summary
  `;
  await sql`delete from exercises where lesson_id = ${lessonId}`;
  for (let index = 0; index < mapped.exercises.length; index++) {
    const exercise = mapped.exercises[index];
    const options = exercise.options ? JSON.stringify(exercise.options) : null;
    await sql`
      insert into exercises (lesson_id, type, question, options, correct_answer, explanation, order_index, points)
      values (${lessonId}, ${exercise.type}, ${exercise.question}, ${options}::jsonb, ${exercise.correctAnswer}, ${exercise.explanation}, ${index + 1}, ${exercise.points})
    `;
  }
  return { gradeId, subjectId, unitId, lessonId, contentWritten: true, exercisesReplaced: mapped.exercises.length };
}

function printQaReport(qa) {
  console.log("\nQA REPORT");
  console.log("-".repeat(56));
  console.log(`Score: ${qa.score}/100`);
  console.log(`Status: ${qa.status}`);
  console.log(`Safe to write: ${qa.safeToWrite ? "yes" : "no"}`);
  console.log(`Content length: ${qa.metrics.contentLength}`);
  console.log(`Guided examples: ${qa.metrics.guidedExamples}`);
  console.log(`Solved exercises: ${qa.metrics.solvedExercises}`);
  console.log(`Progressive exercises: ${qa.metrics.progressiveExercises}`);
  console.log(`Challenge exercises: ${qa.metrics.challengeExercises}`);
  console.log(`Common mistakes: ${qa.metrics.commonMistakes}`);
  console.log(`French terminology: ${qa.metrics.frenchTerminology}`);
  console.log(`Leila prompts: ${qa.metrics.leilaPrompts}`);
  console.log(`Lesson Helper prompts: ${qa.metrics.lessonHelperPrompts}`);
  console.log(`Research prompts: ${qa.metrics.researchPrompts}`);
  console.log(`Issues: ${qa.issues.length ? qa.issues.join(", ") : "none"}`);
  console.log(`Hard stops: ${qa.hardStops.length ? qa.hardStops.join(", ") : "none"}`);
}

async function main() {
  loadEnv(".env.local");
  loadEnv(".env");
  const flags = parseArgs(process.argv.slice(2));
  const selected = selectLessons(flags);
  printBanner(flags, selected);

  const catalogIssues = staticCatalogCheck(selected);
  if (catalogIssues.length) {
    console.error("Static catalog check failed:");
    for (const issue of catalogIssues) console.error(`- ${issue}`);
    process.exitCode = 1;
    return;
  }

  console.log("\nPlanned lessons:");
  for (const { topic, lesson } of selected) console.log(`- ${topic.unitSlug}/${lesson.slug}: ${lesson.title}`);

  if (flags.skipAi) {
    console.log("\n--skip-ai enabled. Static checks passed. No Groq call. No DB access. No DB writes.");
    return;
  }

  const groq = await createGroqClient();
  const sql = flags.apply ? await createDbClient() : null;
  const report = [];

  for (const { topic, lesson } of selected) {
    console.log(`\nGenerating: ${topic.unitSlug}/${lesson.slug} - ${lesson.title}`);
    const generated = await generateLesson(groq, topic, lesson);
    const qa = qaCheck(generated, lesson.title);
    printQaReport(qa);

    let dbWriteResult = null;
    if (flags.apply) {
      if (!qa.safeToWrite) {
        console.log("DB write skipped: QA did not pass Phase 58 hard gates.");
      } else {
        dbWriteResult = await writeLessonToDb(sql, topic, lesson, generated, qa);
        console.log(`DB write complete: lessonId=${dbWriteResult.lessonId}, exercises=${dbWriteResult.exercisesReplaced}`);
      }
    } else {
      console.log("Dry-run: no upsertContent, no replaceExercises, no lesson insert/update.");
    }

    const artifact = saveArtifact({ topic, lesson, generated, qa, flags, dbWriteResult });
    console.log(`Artifact saved: ${artifact}`);
    report.push({ topic: topic.unitSlug, lesson: lesson.slug, qa, artifact, dbWriteResult });
  }

  fs.mkdirSync(REPORTS_DIR, { recursive: true });
  const reportPath = path.join(REPORTS_DIR, `phase58a-2bac-math-${new Date().toISOString().replace(/[:.]/g, "-")}.json`);
  fs.writeFileSync(reportPath, JSON.stringify({ flags, report, timestamp: new Date().toISOString() }, null, 2), "utf8");
  console.log("\nFINAL REPORT");
  console.log("-".repeat(56));
  console.log(`Processed: ${report.length}`);
  console.log(`DB writes: ${report.filter((entry) => entry.dbWriteResult).length}`);
  console.log(`Report saved: ${reportPath}`);
}

main().catch((error) => {
  console.error("\nScript failed:", error.message);
  process.exitCode = 1;
});

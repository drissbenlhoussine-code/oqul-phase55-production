import type { AgentId } from "./config";
import type { CurriculumKnowledge } from "@/server/curriculum/knowledge-engine";

export type PipelineSubject =
  | "french"
  | "arabic"
  | "math"
  | "physics"
  | "svt"
  | "philosophy"
  | "unknown";

export type GroundingMode = "grounded" | "aligned_fallback" | "clarification_needed";
export type LanguageOfInstruction = "arabic" | "french" | "bilingual" | "math_symbols";
export type GroundingConfidence = "high" | "medium" | "low";
export type PipelineIntent = "lesson" | "exam" | "research";

export interface CurriculumMatch {
  lessonId: string;
  title: string;
  cycle?: string | null;
  grade?: string | null;
  subject?: string | null;
  unit?: string | null;
  objectives?: string[];
  contentSnippet?: string | null;
  exerciseCount?: number;
}

export interface CurriculumGrounding {
  mode: GroundingMode;
  languageOfInstruction: LanguageOfInstruction;
  intent: PipelineIntent;
  confidence: GroundingConfidence;
  missingDbLesson: boolean;
  studentFacingNotice?: string;
  cycle?: string | null;
  grade?: string | null;
  subject: PipelineSubject;
  unit?: string | null;
  lesson?: string | null;
  topic?: string | null;
  knowledge?: CurriculumKnowledge | null;
  examContext: string;
  strength: "strong" | "weak";
  matches: CurriculumMatch[];
  warnings: string[];
}

export interface OutputGuardResult {
  ok: boolean;
  issues: string[];
}

const MOJIBAKE_MARKERS = ["Ø", "Ù", "Ã", "â", "�"];
const PLACEHOLDER_MARKERS = ["[أدخل", "[نص", "placeholder", "lorem ipsum", "TODO", "à compléter", "أدخل الحل هنا"];

const SUBJECT_PATTERNS: Array<{ subject: PipelineSubject; patterns: RegExp[] }> = [
  { subject: "french", patterns: [/fran[cç]ais/i, /\bgrammaire\b/i, /\bconjugaison\b/i, /\borthographe\b/i, /\bvocabulaire\b/i, /compr[ée]hension/i, /production [ée]crite/i, /\bphrase simple\b/i, /\bgroupe nominal\b/i, /\bd[ée]terminants?\b/i, /\badjectifs? qualificatifs?\b/i, /\bpronoms?\b/i, /\bfonctions? grammaticales?\b/i, /الفرنسية|لغة فرنسية|قواعد فرنسية/] },
  { subject: "arabic", patterns: [/العربية|اللغة العربية|النحو العربي|الصرف|الإملاء|البلاغة|النصوص القرائية/] },
  { subject: "math", patterns: [/math|math[ée]matiques|رياضيات|الدوال|الأعداد|الهندسة|الجبر|الاشتقاق|التكامل|النهايات|معادلة|احسب/] },
  { subject: "physics", patterns: [/physique|فيزياء|الكهرباء|الميكانيك|الموجات|النووي|الحركة|الكيمياء|تفاعل كيميائي|حمض|قاعدة/] },
  { subject: "svt", patterns: [/svt|علوم الحياة|الأرض|البيولوجيا|الوراثة|التغذية|التنفس|خلية|جيولوجيا/] },
  { subject: "philosophy", patterns: [/philo|philosophie|فلسفة|الشخص|الغير|الحقيقة|الدولة|الحرية|الواجب|السعادة|مجزوءة|إشكال/] },
];

const OFF_SUBJECT_PATTERNS: Record<PipelineSubject, RegExp[]> = {
  french: [/النحو العربي|تعريف النحو|علم يدرس بناء الجمل|الإعراب|المبتدأ|الخبر|السياسة|الاقتصاد|العرض والطلب|معادلة\s*\d|احسب\s*\d/],
  arabic: [/\b[ée]quation\b|\bfonction\b|\bd[ée]riv[ée]e\b|\bint[ée]grale\b|x\s*[+=]|\bSVT\b|\bcellule\b/i],
  math: [/تحليل اقتصادي|أبعاد اجتماعية|سياسة عمومية|نص فلسفي|الشخص والغير|cellule|photosynth[èe]se|النحو العربي|الإعراب/i],
  physics: [/photosynth[èe]se|ADN|خلية نباتية|إعراب|مبتدأ|خبر|نص فلسفي/i],
  svt: [/قانون أوم|توتر كهربائي|شدة التيار|حركة مستقيمة|إعراب|مبتدأ|خبر/i],
  philosophy: [/\b\d+\s*[+\-*/=]\s*\d+|f\(x\)|x\^2|معادلة|اشتقاق|تكامل|قانون أوم/],
  unknown: [],
};

const CLARIFICATION_PATTERNS = [
  /^اشرح لي هذا\.?$/i,
  /^هذا$/i,
  /^عندي امتحان\.?$/i,
  /^بغيت نراجع\.?$/i,
  /^درس صعب\.?$/i,
  /^ساعدني\.?$/i,
];

const BROAD_FRENCH_GRAMMAR_TOPICS = ["grammaire", "قواعد", "القواعد", "قواعد الفرنسية", "قواعد اللغة الفرنسية"];

export function hasMojibake(text: string): boolean {
  return MOJIBAKE_MARKERS.some((marker) => text.includes(marker));
}

export function classifySubject(input: string): PipelineSubject {
  for (const candidate of SUBJECT_PATTERNS) {
    if (candidate.patterns.some((pattern) => pattern.test(input))) return candidate.subject;
  }
  return "unknown";
}

export function extractRequestedTopic(input: string): string | null {
  const normalized = input.trim();
  const explicit = normalized.match(/(?:درس|محور|موضوع|leçon|lesson)\s*[:：-]?\s*([^\n،.]+)/i);
  if (explicit?.[1]) return explicit[1].trim();
  const explain = normalized.match(/^(?:اشرح(?:\s+لي)?|شرح|فسر(?:\s+لي)?)\s+(?:درس\s+)?(.+)$/i);
  if (explain?.[1] && explain[1].trim().split(/\s+/).length >= 1) return explain[1].trim();
  const grammar = normalized.match(/\b(grammaire|conjugaison|orthographe|vocabulaire|compr[ée]hension|production [ée]crite)\b/i);
  if (grammar?.[1]) return grammar[1].trim();
  const quoted = normalized.match(/["“”']([^"“”']+)["“”']/);
  if (quoted?.[1]) return quoted[1].trim();
  const words = normalized.split(/\s+/).filter(Boolean);
  if (words.length <= 2) return null;
  return words.slice(-4).join(" ") || null;
}

export function inferGrade(input: string): string | null {
  const lower = input.toLowerCase();
  if (/2bac|الثانية باك|الثانية باكالوريا|باك/.test(lower)) return "2BAC";
  if (/1bac|الأولى باك|الأولى باكالوريا|جهوي/.test(lower)) return "1BAC";
  if (/جذع|tronc commun|tc/.test(lower)) return "الجذع المشترك";
  if (/الأولى إعدادي|اولى اعدادي|1ac|coll[eè]ge|إعدادي|اعدادي|middle/.test(lower)) return "الإعدادي";
  if (/ابتدائي|primary|primaire/.test(lower)) return "الابتدائي";
  return null;
}

export function languageForSubject(subject: PipelineSubject): LanguageOfInstruction {
  if (subject === "french") return "french";
  if (subject === "math") return "math_symbols";
  return "arabic";
}

export function inferIntent(input: string): PipelineIntent {
  if (/فرض|امتحان|اختبار|bac|باك|جهوي|إقليمي|موحد|مراجعة|استعد|استعداد|devoir|examen|contr[oô]le|bar[eè]me/i.test(input)) {
    return "exam";
  }
  if (/قارن|حلل|ابحث|بحث|ناقش|analyse|compare|recherche/i.test(input)) {
    return "research";
  }
  return "lesson";
}

export function isClarificationNeeded(input: string, subject = classifySubject(input), topic = extractRequestedTopic(input)): boolean {
  const normalized = input.trim();
  if (CLARIFICATION_PATTERNS.some((pattern) => pattern.test(normalized))) return true;
  if (subject === "french" && isBroadFrenchGrammarTopic(topic)) return true;
  return subject === "unknown" && !topic;
}

export function examContextFor(input: string, subject: PipelineSubject): string {
  const grade = inferGrade(input);
  if (grade === "2BAC") return "أسلوب الامتحان الوطني للباكالوريا مع تصحيح مفصل، barème، وانتظارات المصحح.";
  if (grade === "1BAC") return "أسلوب الامتحان الجهوي عند الملاءمة مع تصحيح منهجي ومعايير تقييم واضحة.";
  if (grade === "الجذع المشترك") return "أسلوب فرض محروس أو امتحان محلي مناسب للجذع المشترك.";
  if (grade === "الإعدادي") return "أسلوب فرض محروس أو موحد محلي/إقليمي مناسب للإعدادي.";
  if (grade === "الابتدائي") return "تمارين صفية بسيطة ومتدرجة مناسبة للابتدائي.";
  if (subject === "french") return "تمارين لغة فرنسية مدرسية مع correction و barème مناسبين للمستوى.";
  return "سياق مدرسي مغربي مع تمارين متدرجة وتصحيح واضح.";
}

export function buildWeakGrounding(input: string): CurriculumGrounding {
  const subject = classifySubject(input);
  const topic = extractRequestedTopic(input);
  const clarification = isClarificationNeeded(input, subject, topic);
  return {
    mode: clarification ? "clarification_needed" : "aligned_fallback",
    languageOfInstruction: languageForSubject(subject),
    intent: inferIntent(input),
    confidence: clarification ? "low" : subject === "unknown" ? "low" : "medium",
    missingDbLesson: true,
    studentFacingNotice: clarification
      ? clarificationMessage(input)
      : "لم أجد هذا الدرس محفوظًا بعد داخل قاعدة OQUL، لذلك سأقدمه كدرس جديد متوافق مع توقعات المنهاج المغربي حسب المستوى والمادة المحددين.",
    grade: inferGrade(input),
    subject,
    topic,
    examContext: examContextFor(input, subject),
    strength: "weak",
    matches: [],
    warnings: clarification
      ? ["الطلب عام جدًا ويحتاج تحديد المستوى والمادة قبل توليد جواب آمن."]
      : ["لم يتم العثور على درس مطابق مؤكد في قاعدة البيانات. سيتم استعمال وضع fallback متوافق مع توقعات المنهاج المغربي دون الادعاء بأنه مأخوذ من وثيقة رسمية."],
  };
}

export function clarificationMessage(input?: string): string {
  const subject = input ? classifySubject(input) : "unknown";
  const topic = input ? extractRequestedTopic(input) : null;
  if (subject === "french" && isBroadFrenchGrammarTopic(topic)) {
    return [
      "كلمة grammaire واسعة جدًا. أي درس تريد؟",
      "- La phrase simple",
      "- Le groupe nominal",
      "- Les déterminants",
      "- Les adjectifs qualificatifs",
      "- Les pronoms",
      "- Les fonctions grammaticales",
    ].join("\n");
  }
  return "ما المستوى والمادة؟";
}

export function missingLessonMessage(): string {
  return "لم أجد هذا الدرس محفوظًا بعد داخل قاعدة OQUL، لذلك سأقدمه كدرس جديد متوافق مع توقعات المنهاج المغربي حسب المستوى والمادة المحددين.";
}

export function guardAgentOutput(params: {
  agentId: AgentId;
  output: string;
  input: string;
  grounding: CurriculumGrounding;
  final?: boolean;
}): OutputGuardResult {
  const issues: string[] = [];
  const subject = params.grounding.subject;
  const output = params.output;
  const topic = params.grounding.topic;

  if (params.grounding.mode === "clarification_needed") issues.push("clarification_required");
  if (hasMojibake(output)) issues.push("mojibake_output");
  if (PLACEHOLDER_MARKERS.some((marker) => output.includes(marker))) issues.push("placeholder_output");
  if (topic && !containsRequestedTopic(output, topic) && params.final) issues.push("missing_requested_topic");
  if (subject !== "unknown" && !mentionsSubject(output, subject) && params.final) issues.push("missing_selected_subject");

  const offSubject = OFF_SUBJECT_PATTERNS[subject]?.some((pattern) => pattern.test(output)) ?? false;
  if (offSubject) issues.push("off_subject_content");
  if (subject === "french" && params.final && !containsFrenchGrammarSignal(output, topic)) {
    issues.push("missing_french_grammar_concepts");
  }
  if (subject === "french" && params.final && !containsFrenchLanguageSignals(output)) {
    issues.push("wrong_language_for_subject");
  }
  if (subject === "math" && params.final && !containsMathSignal(output)) {
    issues.push("missing_math_method");
  }
  if (subject === "philosophy" && /\b\d+\s*[+\-*/=]\s*\d+|f\(x\)|x\^2/.test(output)) {
    issues.push("wrong_language_for_subject");
  }
  if (params.final && isGenericExplanation(output, params.grounding)) {
    issues.push("generic_explanation");
  }

  const needsExerciseCorrection = params.agentId === "exercise_gen" || params.final;
  const needsExamStructure = params.grounding.intent === "exam";

  if (needsExerciseCorrection) {
    if (!/تصحيح|الحل|correction|solution/i.test(output)) issues.push("missing_corrections");
    if (!/أخطاء شائعة|pi[eè]ges fr[eé]quents|erreurs? fr[eé]quentes?/i.test(output)) issues.push("missing_common_mistakes");
  }

  if (needsExamStructure) {
    if (!/نقط|نقطة|bar[eè]me|point/i.test(output)) issues.push("missing_point_allocation");
    if (!/انتظارات|المصحح|examinateur|professeur|crit[eè]res d'[ée]valuation/i.test(output)) issues.push("missing_examiner_expectations");
    if (!/فرض|موحد|جهوي|وطني|امتحان|examen|contr[oô]le|devoir|évaluation/i.test(output)) issues.push("missing_moroccan_exam_style");
  }

  return { ok: issues.length === 0, issues };
}

function containsRequestedTopic(output: string, topic: string): boolean {
  const text = output.toLowerCase();
  const normalizedText = text.replace(/\bال/g, "");
  const normalizedTopic = topic.toLowerCase();
  if (text.includes(normalizedTopic)) return true;
  const stopWords = new Set(["في", "لي", "درس", "ال", "من", "عن", "مع", "the", "a", "an"]);
  const tokens = normalizedTopic
    .split(/[\s،:؛.\-_/]+/)
    .map((token) => token.trim().replace(/^ال/, ""))
    .filter((token) => token.length >= 3 && !stopWords.has(token));
  if (!tokens.length) return false;
  const hits = tokens.filter((token) => text.includes(token) || normalizedText.includes(token)).length;
  return hits >= Math.min(tokens.length, 2);
}

function isBroadFrenchGrammarTopic(topic?: string | null): boolean {
  if (!topic) return false;
  const normalized = topic.trim().toLowerCase();
  return BROAD_FRENCH_GRAMMAR_TOPICS.some((candidate) => normalized === candidate);
}

function mentionsSubject(output: string, subject: PipelineSubject): boolean {
  if (subject === "unknown") return true;
  return SUBJECT_PATTERNS.find((item) => item.subject === subject)?.patterns.some((pattern) => pattern.test(output)) ?? true;
}

function containsFrenchGrammarSignal(output: string, topic?: string | null): boolean {
  if (topic && !/grammaire|conjugaison|orthographe|vocabulaire|compr[ée]hension|production [ée]crite/i.test(topic)) return true;
  const markers = [
    /\bnature des mots\b/i,
    /\bfonction grammaticale\b/i,
    /\bgroupe nominal\b/i,
    /\bconjugaison\b/i,
    /\baccords?\b/i,
    /\bcompl[eé]ment\b/i,
    /\bverbe\b/i,
    /\bsujet\b/i,
    /\bphrase simple\b/i,
  ];
  return markers.some((marker) => marker.test(output));
}

function containsFrenchLanguageSignals(output: string): boolean {
  return /\b(le|la|les|un|une|des|verbe|sujet|phrase|nom|adjectif|compl[eé]ment|accord|correction|bar[eè]me)\b/i.test(output);
}

function containsMathSignal(output: string): boolean {
  return /\d|=|\+|-|×|÷|f\(|x|حساب|معادلة|صيغة|طريقة|خطوة/.test(output);
}

function isGenericExplanation(output: string, grounding: CurriculumGrounding): boolean {
  const text = output.toLowerCase();
  const lesson = grounding.matches[0];
  if (
    grounding.intent === "lesson"
    && grounding.topic
    && containsRequestedTopic(output, grounding.topic)
    && /définition|definition|exercice|example|exemple|correction|شرح|مثال|تمرين|تصحيح|خطوة/i.test(output)
  ) {
    return false;
  }
  const curriculumSignals = [
    grounding.grade,
    grounding.unit,
    grounding.lesson,
    grounding.topic,
    lesson?.title,
    lesson?.unit,
    lesson?.grade,
    grounding.mode === "aligned_fallback" ? "متوافق مع توقعات المنهاج المغربي" : null,
    "barème",
    "تصحيح",
    "انتظارات المصحح",
    "فرض",
    "امتحان",
    "devoir",
  ].filter(Boolean).map((item) => String(item).toLowerCase());
  const signalHits = curriculumSignals.filter((signal) => text.includes(signal)).length;
  return signalHits < 2;
}






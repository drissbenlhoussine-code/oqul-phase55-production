import type { AgentId } from "./config";

export type PipelineSubject =
  | "french"
  | "arabic"
  | "math"
  | "physics"
  | "svt"
  | "philosophy"
  | "unknown";

export interface CurriculumMatch {
  lessonId: string;
  title: string;
  grade?: string | null;
  subject?: string | null;
  unit?: string | null;
  objectives?: string[];
  contentSnippet?: string | null;
  exerciseCount?: number;
}

export interface CurriculumGrounding {
  grade?: string | null;
  subject: PipelineSubject;
  topic?: string | null;
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
const PLACEHOLDER_MARKERS = ["[أدخل", "[نص", "placeholder", "lorem ipsum", "TODO"];

const SUBJECT_PATTERNS: Array<{ subject: PipelineSubject; patterns: RegExp[] }> = [
  { subject: "french", patterns: [/fran[cç]ais/i, /\bgrammaire\b/i, /\bconjugaison\b/i, /\borthographe\b/i, /الفرنسية|لغة فرنسية/] },
  { subject: "arabic", patterns: [/العربية|اللغة العربية|النحو العربي|الصرف|الإملاء|البلاغة/] },
  { subject: "math", patterns: [/math|mathématiques|رياضيات|الدوال|الأعداد|الهندسة|الجبر|الاشتقاق|التكامل|النهايات/] },
  { subject: "physics", patterns: [/physique|فيزياء|الكهرباء|الميكانيك|الموجات|النووي|الحركة/] },
  { subject: "svt", patterns: [/svt|علوم الحياة|الأرض|البيولوجيا|الوراثة|التغذية|التنفس/] },
  { subject: "philosophy", patterns: [/philo|philosophie|فلسفة|الشخص|الغير|الحقيقة|الدولة|الحرية|الواجب|السعادة/] },
];

const OFF_SUBJECT_PATTERNS: Record<PipelineSubject, RegExp[]> = {
  french: [/النحو العربي|الإعراب|المبتدأ|الخبر|السياسة|الاقتصاد|العرض والطلب|معادلة\s*\d|احسب\s*\d/],
  arabic: [/équation|fonction|dérivée|integrale|x\s*[+=]|SVT|cellule/i],
  math: [/تحليل اقتصادي|أبعاد اجتماعية|سياسة عمومية|نص فلسفي|الشخص والغير|cellule|photosynthèse/i],
  physics: [/photosynthèse|ADN|خلية نباتية|إعراب|مبتدأ|خبر|نص فلسفي/i],
  svt: [/قانون أوم|توتر كهربائي|شدة التيار|حركة مستقيمة|إعراب|مبتدأ|خبر/i],
  philosophy: [/\b\d+\s*[+\-*/=]\s*\d+|f\(x\)|x\^2|معادلة|اشتقاق|تكامل|قانون أوم/],
  unknown: [],
};

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
  const explicit = normalized.match(/(?:درس|محور|موضوع|leçon|lesson)\s*[:：-]\s*([^\n،.]+)/i);
  if (explicit?.[1]) return explicit[1].trim();
  const grammar = normalized.match(/\b(grammaire|conjugaison|orthographe|vocabulaire)\b/i);
  if (grammar?.[1]) return grammar[1].trim();
  const quoted = normalized.match(/["“”']([^"“”']+)["“”']/);
  if (quoted?.[1]) return quoted[1].trim();
  return normalized.split(/\s+/).slice(-4).join(" ") || null;
}

export function inferGrade(input: string): string | null {
  const lower = input.toLowerCase();
  if (/2bac|الثانية باك|الثانية باكالوريا|باك/.test(lower)) return "2BAC";
  if (/1bac|الأولى باك|الأولى باكالوريا|جهوي/.test(lower)) return "1BAC";
  if (/جذع|tronc commun|tc/.test(lower)) return "الجذع المشترك";
  if (/إعدادي|اعدادي|collège|middle/.test(lower)) return "الإعدادي";
  if (/ابتدائي|primary|primaire/.test(lower)) return "الابتدائي";
  return null;
}

export function examContextFor(input: string, subject: PipelineSubject): string {
  const grade = inferGrade(input);
  if (grade === "2BAC") return "أسلوب الامتحان الوطني للباكالوريا مع توزيع النقط وانتظارات المصحح.";
  if (grade === "1BAC") return "أسلوب الامتحان الجهوي عند الملاءمة مع تصحيح منهجي.";
  if (grade === "الجذع المشترك") return "أسلوب فرض أو امتحان محلي مناسب للجذع المشترك.";
  if (grade === "الإعدادي") return "أسلوب فرض محروس أو موحد إقليمي مناسب للإعدادي.";
  if (subject === "french") return "تمارين لغة فرنسية مدرسية مع correction و barème مناسبين للمستوى.";
  return "سياق مدرسي مغربي مع تمارين متدرجة وتصحيح واضح.";
}

export function buildWeakGrounding(input: string): CurriculumGrounding {
  const subject = classifySubject(input);
  return {
    grade: inferGrade(input),
    subject,
    topic: extractRequestedTopic(input),
    examContext: examContextFor(input, subject),
    strength: "weak",
    matches: [],
    warnings: ["لم يتم العثور على درس مطابق مؤكد في قاعدة البيانات. يجب الالتزام بالموضوع المطلوب وطلب توضيح المستوى إذا لزم."],
  };
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

  if (hasMojibake(output)) issues.push("mojibake_output");
  if (PLACEHOLDER_MARKERS.some((marker) => output.includes(marker))) issues.push("placeholder_output");
  if (topic && !output.toLowerCase().includes(topic.toLowerCase()) && params.final) issues.push("missing_requested_topic");
  if (subject !== "unknown" && !mentionsSubject(output, subject) && params.final) issues.push("missing_selected_subject");

  const offSubject = OFF_SUBJECT_PATTERNS[subject]?.some((pattern) => pattern.test(output)) ?? false;
  if (offSubject) issues.push("off_subject_content");

  if (params.agentId === "exercise_gen" || params.final) {
    if (!/تصحيح|الحل|correction|solution/i.test(output)) issues.push("missing_corrections");
    if (!/نقط|نقطة|bar[eè]me|point/i.test(output)) issues.push("missing_point_allocation");
    if (!/انتظارات|المصحح|examinateur|professeur/i.test(output)) issues.push("missing_examiner_expectations");
  }

  return { ok: issues.length === 0, issues };
}

function mentionsSubject(output: string, subject: PipelineSubject): boolean {
  if (subject === "unknown") return true;
  return SUBJECT_PATTERNS.find((item) => item.subject === subject)?.patterns.some((pattern) => pattern.test(output)) ?? true;
}

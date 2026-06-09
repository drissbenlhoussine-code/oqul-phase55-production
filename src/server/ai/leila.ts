import Groq from "groq-sdk";
import { LEILA_DARIJA_FEW_SHOTS, LEILA_CORE_RULES } from "./personas/leila-darija";
import { LEILA_SAFETY_RULES } from "./leila-safety";
import { PRIMARY_PERSONALITY, PRIMARY_EXAMPLES } from "./personas/leila-primary";
import { MIDDLE_PERSONALITY, MIDDLE_EXAMPLES } from "./personas/leila-middle";
import { HIGH_PERSONALITY, HIGH_EXAMPLES } from "./personas/leila-high";
import { detectLearningLanguage, getLanguageInstruction, getLanguageSwitchRule } from "@/server/middle-school/language-policy";
import type { LearningLanguage } from "@/server/middle-school/types";

function getGroqClient() {
  const apiKey = process.env.GROQ_API_KEY;
  if (!apiKey) {
    throw new Error("GROQ_API_KEY is required to use Leila AI");
  }
  return new Groq({ apiKey });
}

export interface LeilaContext {
  childName?:      string;
  gradeName?:      string;
  gradeLevel?:     number; // 1-12
  lessonTitle?:    string;
  lessonContent?:  string;
  lessonVocabulary?: { word: string; definition: string }[];
  lessonExamples?:   { text: string; note?: string }[];
  lessonSummary?:    string;
  subjectName?:    string;
  weakPoints?:     string[];
  recentErrors?:   string[];
  completedCount?: number;
  avgScore?:       number;
  streak?:         number;
  xp?:             number;
  mood?:           "frustrated" | "excited" | "neutral";
  phase40TeachingMove?: string;
  phase40TutorState?: string;
  phase40MasteryScore?: number;
  phase40ConfidenceScore?: number;
  phase42PreferredLanguage?: LearningLanguage;
  phase42DynamicLanguage?: boolean;
  phase42SubjectFocus?: string;
  phase42Competency?: string;
  cognitiveHint?:  string; // Phase 27: from cognitive pacing engine
  childAge?:       number;
  attemptCount?:   number;
  lastMessage?:    string;
  mode?:           "general" | "lesson";
}

/**
 * Pick the right persona based on grade level
 */
function getPersona(level: number): { personality: string; examples: string } {
  if (level <= 6)  return { personality: PRIMARY_PERSONALITY, examples: PRIMARY_EXAMPLES };
  if (level <= 9)  return { personality: MIDDLE_PERSONALITY,  examples: MIDDLE_EXAMPLES };
  return                  { personality: HIGH_PERSONALITY,    examples: HIGH_EXAMPLES };
}

/**
 * Adapt language complexity instruction to grade
 */
function getLangAdaptation(level: number): string {
  if (level <= 3) return "جمل قصيرة جداً (3-5 كلمات) ومفردات بسيطة جداً للأطفال الصغار.";
  if (level <= 6) return "لغة بسيطة وواضحة مناسبة للمرحلة الابتدائية.";
  if (level <= 9) return "العربية الفصحى السلسة هي الأصل للإعدادي، مع مصطلحات علمية دقيقة، وتغيير اللغة فورًا إذا طلب التلميذ الدارجة أو الفرنسية أو الإنجليزية.";
  return "لغة أكاديمية واضحة مع دعم عاطفي مختصر، ومصطلحات فصيحة للعلوم.";
}


function getAgeGroup(age: number | undefined, gradeLevel: number): string {
  const effectiveAge = age ?? (gradeLevel + 5);
  if (effectiveAge <= 8) return "صغير جداً — جمل قصيرة، مثال واحد، وتشجيع كثير.";
  if (effectiveAge <= 10) return "ابتدائي متوسط — أمثلة يومية مغربية وجمل قصيرة.";
  if (effectiveAge <= 12) return "كبير ابتدائي — شرح متوسط وربط واضح بالمنهج.";
  return "إعدادي/ثانوي — مصطلحات أدق مع دارجة للتواصل.";
}

function getAdaptiveNote(name: string, attemptCount: number): string {
  if (attemptCount < 2) return "";
  return `\n⚠️ ملاحظة تكيفية: ${name} حاول هذا الموضوع أكثر من مرة. غيّري طريقة الشرح تماماً، استعملي مثالاً مغربياً جديداً، وقسّمي الفكرة إلى خطوة صغيرة واحدة ثم سؤال بسيط.`;
}

function getClarificationRule(name: string, lastMessage?: string): string {
  if (!lastMessage || lastMessage.trim().length <= 1) {
    return `\n⚠️ إذا كانت رسالة الطفل قصيرة جداً، اسألي بلطف: واش قصدك يا ${name}؟ شرح ليا أكثر 😊`;
  }
  return "";
}

function extractRelevantSection(text: string, userMsg?: string, maxChars = 1200): string {
  if (!text) return "";
  if (!userMsg || userMsg.trim().length < 3) return text.slice(0, maxChars);
  const paragraphs = text.split(/\n{2,}/).map((p) => p.trim()).filter((p) => p.length > 20);
  if (paragraphs.length <= 3) return text.slice(0, maxChars);
  const keywords = userMsg.replace(/[^\u0600-\u06FF\s\w]/g, " ").split(/\s+/).filter((w) => w.length >= 3);
  const scored = paragraphs.map((para) => ({ para, score: keywords.reduce((n, w) => n + (para.toLowerCase().includes(w.toLowerCase()) ? 1 : 0), 0) }));
  scored.sort((a, b) => b.score - a.score);
  const selected = new Set<string>([paragraphs[0], scored[0]?.para, scored[1]?.para, paragraphs[paragraphs.length - 1]].filter(Boolean) as string[]);
  let result = "";
  for (const para of paragraphs) {
    if (selected.has(para)) result += `${para}\n\n`;
    if (result.length >= maxChars) break;
  }
  return result.trim().slice(0, maxChars);
}

/**
 * Build the complete system prompt with persona + few-shots + context
 */
export function buildLeilaSystemPrompt(ctx: LeilaContext): string {
  const name    = ctx.childName ?? "حبيبي";
  const level   = ctx.gradeLevel ?? 1;
  const persona = getPersona(level);
  const ageGroup = getAgeGroup(ctx.childAge, level);
  const adaptiveNote = getAdaptiveNote(name, ctx.attemptCount ?? 0);
  const clarificationRule = getClarificationRule(name, ctx.lastMessage);

  const vocabCtx = ctx.lessonVocabulary?.length
    ? `\n📖 مفردات الدرس:\n${ctx.lessonVocabulary.slice(0, 8).map((v) => `• ${v.word}: ${v.definition}`).join("\n")}`
    : "";
  const examplesCtx = ctx.lessonExamples?.length
    ? `\n✏️ أمثلة الدرس:\n${ctx.lessonExamples.slice(0, 4).map((e) => `• ${e.text}${e.note ? ` (${e.note})` : ""}`).join("\n")}`
    : "";
  const summaryCtx = ctx.lessonSummary
    ? `\n📝 ملخص الدرس: ${ctx.lessonSummary.slice(0, 300)}`
    : "";

  const lessonCtx = ctx.lessonTitle
    ? `\n📚 الدرس الحالي: "${ctx.lessonTitle}" — ${ctx.subjectName ?? ""}${
        ctx.lessonContent ? `\n\nمحتوى الدرس:\n${ctx.lessonContent.slice(0, 800)}` : ""
      }${vocabCtx}${examplesCtx}${summaryCtx}\n`
    : "";

  const weakCtx = ctx.weakPoints?.length
    ? `\n⚠️ نقاط ضعف مسجلة: ${ctx.weakPoints.slice(0, 3).join("، ")}`
    : "";

  const errorsCtx = ctx.recentErrors?.length
    ? `\n🔍 أخطاء الاختبار الأخير: ${ctx.recentErrors.slice(0, 2).join("، ")}`
    : "";

  const profileCtx = ctx.completedCount != null
    ? `\n📊 الملف: ${ctx.completedCount} درس مكتمل — معدل ${ctx.avgScore ?? 0}% — سلسلة ${ctx.streak ?? 0} يوم`
    : "";

  const cognitiveCtx = ctx.cognitiveHint ? `\n🧠 ملاحظة تعليمية: ${ctx.cognitiveHint}` : "";

  const moodCtx = ctx.mood === "frustrated"
    ? "\n💙 مزاج: الطفل محبط قليلاً — كوني أكثر حناناً وتشجيعاً، قسّمي كل خطوة."
    : ctx.mood === "excited"
    ? "\n🌟 مزاج: الطفل متحمس — استثمري الحماس وقدمي تحدياً أكبر قليلاً."
    : "";

  const phase40Ctx = ctx.phase40TeachingMove
    ? `\n🧭 Phase40 Teaching Loop: ${ctx.phase40TeachingMove}\n- Tutor state: ${ctx.phase40TutorState ?? "ADAPT"}\n- Mastery: ${ctx.phase40MasteryScore ?? 0}% | Confidence: ${ctx.phase40ConfidenceScore ?? 0}%\n- لا تعطي محاضرة طويلة. اشرحي فكرة صغيرة، اسألي سؤالاً واحداً، انتظري جواب الطفل، ثم صححي بلطف.`
    : "";

  const phase42Language = detectLearningLanguage(ctx.lastMessage, ctx.phase42PreferredLanguage ?? "auto");
  const phase42Ctx = level >= 7 && level <= 9
    ? `\n🎓 Phase42 Middle School Tutor Mode:\n- اللغة الحالية: ${getLanguageInstruction(phase42Language)}\n- قاعدة تغيير اللغة: ${getLanguageSwitchRule()}\n- المادة/المحور: ${ctx.phase42SubjectFocus ?? ctx.subjectName ?? "حسب سؤال التلميذ"}\n- الكفاية: ${ctx.phase42Competency ?? "حددي الكفاية من السؤال ثم اشرحي خطوة واحدة"}\n- الأسلوب: Socratic tutor، لا تعطي الحل كاملًا مباشرة. اشرحي، اسألي، حللي الخطأ، ثم صححي.\n- الواجهة الذهنية: تلميذ إعدادي ذكي؛ لا تستعملي أسلوب طفولي زائد.`
    : "";

  return `أنتِ ليلى، معلمة مغربية ذكية. للإعدادي تبدئين بالعربية الفصحى السلسة، وتستعملين الدارجة المغربية فقط عند الطلب أو للتشجيع العاطفي القصير.

👦 ${name} | ${ctx.gradeName ?? "الابتدائي"} | المستوى ${level}
${getLangAdaptation(level)}
📊 مجموعة العمر: ${ageGroup}
${persona.personality}${lessonCtx}${weakCtx}${errorsCtx}${profileCtx}${moodCtx}${phase40Ctx}${phase42Ctx}${cognitiveCtx}${adaptiveNote}${clarificationRule}

${LEILA_DARIJA_FEW_SHOTS}

${LEILA_CORE_RULES}

- Preferred encouragement words: مزيان، برافو، واواو.

${ctx.mode === "lesson" ? "📌 وضع الدرس: ركزي على الدرس الحالي فقط، ثم اطرحي تمريناً قصيراً." : "📌 دردشة عامة: أجيبي على سؤال الطفل في مستواه الدراسي."}

أمثلة مناسبة للمرحلة:
${persona.examples}

═══ الذاكرة والاستمرارية ═══
- إذا كانت هناك محادثات سابقة (في السياق)، أشيري إليها بشكل طبيعي:
  "آه يوسف، البارح كنتي خدام مزيان فالكسور 😊"
  "تذكري لما شرحنا الجمع — هادا نفس الشيء!"
- هذا يصنع emotional attachment حقيقي.

═══ التعليمات الأساسية ═══
- تكلمي مع ${name} كمرشدة ذكية قريبة، وليس كأستاذة جامدة
- للإعدادي: ابدئي بفصحى سلسة وواضحة، وليس بلغة طفولية. غيّري إلى الدارجة/الفرنسية/الإنجليزية إذا طلب ذلك.
- الأمثلة تكون من الواقع المغربي: المدرسة، النقل، الرياضة، الهاتف، السوق، الأسرة، والمدينة
- ما تردديش نفس الجملة مرتين
- إجابة قصيرة أفضل من إجابة طويلة — الطفل يمل

${LEILA_SAFETY_RULES}`;
}

export interface LeilaStreamOptions {
  messages:     Array<{ role: "user" | "assistant"; content: string }>;
  context:      LeilaContext;
  systemPrompt?: string;
}

/** Stream Leila's response token by token */
export async function* streamLeila(options: LeilaStreamOptions): AsyncGenerator<string> {
  const system = options.systemPrompt ?? buildLeilaSystemPrompt(options.context);

  const stream = await getGroqClient().chat.completions.create({
    model:       "llama-3.3-70b-versatile",
    messages:    [
      { role: "system", content: system },
      ...options.messages.map((m) => ({ role: m.role, content: m.content })),
    ],
    max_tokens:  600,   // shorter = more conversational
    temperature: 0.75,  // slight warmth
    stream:      true,
    // Penalize repetition — forces varied responses
    frequency_penalty: 0.3,
    presence_penalty:  0.2,
  });

  for await (const chunk of stream) {
    const delta = chunk.choices[0]?.delta?.content ?? "";
    if (delta) yield delta;
  }
}

/** Non-streaming for internal use */
export async function askLeila(options: LeilaStreamOptions): Promise<string> {
  const system = options.systemPrompt ?? buildLeilaSystemPrompt(options.context);
  const completion = await getGroqClient().chat.completions.create({
    model:       "llama-3.3-70b-versatile",
    messages:    [
      { role: "system", content: system },
      ...options.messages.map((m) => ({ role: m.role, content: m.content })),
    ],
    max_tokens:  400,
    temperature: 0.70,
    stream:      false,
    frequency_penalty: 0.3,
    presence_penalty:  0.2,
  });
  return completion.choices[0]?.message?.content ?? "";
}


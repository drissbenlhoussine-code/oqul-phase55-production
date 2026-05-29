/**
 * Leila Encouragement Engine
 * Generates personalized encouragement messages after quiz completion.
 * Uses real performance data to make messages feel genuine, not generic.
 *
 * Never shows a generic "Good job!" — always references specific performance.
 */
import { askLeila } from "./leila";

export interface QuizEncouragementInput {
  childName:  string;
  lessonTitle: string;
  score:       number;
  passed:      boolean;
  streak:      number;
  isPerfect:   boolean;
  weakTopics?: string[];
}

export async function generateEncouragement(input: QuizEncouragementInput): Promise<string> {
  const { childName, lessonTitle, score, passed, streak, isPerfect, weakTopics } = input;

  // Use Leila for genuine personalized messages
  const prompt = isPerfect
    ? `التلميذ ${childName} حصل على علامة كاملة 100% في درس "${lessonTitle}". اكتبي له رسالة تشجيعية قصيرة جداً (جملتان فقط) بالدارجة المغربية تحتفل بهذا الإنجاز الرائع.`
    : passed
    ? `التلميذ ${childName} نجح في اختبار "${lessonTitle}" بنتيجة ${score}%${streak > 2 ? ` وعنده سلسلة ${streak} أيام` : ""}. اكتبي له رسالة تشجيعية قصيرة جداً (جملتان) بالدارجة تشجعه على الاستمرار.`
    : `التلميذ ${childName} لم ينجح في اختبار "${lessonTitle}" (${score}%)${weakTopics?.length ? ` وعنده صعوبة في ${weakTopics[0]}` : ""}. اكتبي له رسالة تشجيعية لطيفة جداً (جملتان فقط) بالدارجة تشجعه على المحاولة مرة أخرى بدون إحباط.`;

  try {
    const message = await askLeila({
      messages: [{ role: "user", content: prompt }],
      context:  { childName, gradeName: undefined },
    });
    return message.trim();
  } catch {
    // Fallback messages if AI call fails
    if (isPerfect) return `مبروك ${childName}! علامة كاملة ماشي هيّنة 🏆 كمل هكذا!`;
    if (passed)    return `برافو ${childName}! راك تتحسن شوية بشوية 💪 استمر!`;
    return `ما يخصش تيأس ${childName}! كل واحد كيخطئ — المهم نرجعو ونحاولو 🌟`;
  }
}

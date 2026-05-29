import { getPrimaryLessons, normalizePrimaryGrade, primarySubjects } from "./curriculum";
import { buildPrimaryMicroLesson } from "./lesson-engine";
import { detectPrimaryLanguage, getPrimaryLanguageInstruction } from "./language-policy";
import type { PrimaryLanguage, PrimaryStudentProfile, PrimarySubject } from "./types";

type WeakPointLike = { topic?: string | null; severity?: number | null };

type BuildPrimaryInput = {
  childId: string;
  childName?: string;
  gradeLevel?: number | string | null;
  message?: string | null;
  preferredLanguage?: PrimaryLanguage;
  subject?: PrimarySubject;
  weakPoints?: WeakPointLike[];
};

function scoreLesson(title: string, weakPoints: WeakPointLike[]) {
  const lower = title.toLowerCase();
  return weakPoints.reduce((score, point) => {
    const topic = (point.topic ?? "").toLowerCase();
    return score + (topic && (lower.includes(topic) || topic.includes(lower)) ? (point.severity ?? 1) + 2 : 0);
  }, 0);
}

export function buildPhase46PrimaryProfile(input: BuildPrimaryInput): PrimaryStudentProfile {
  const grade = normalizePrimaryGrade(input.gradeLevel);
  const targetLanguage = detectPrimaryLanguage(input.message, input.preferredLanguage ?? "auto");
  const lessons = getPrimaryLessons(grade, input.subject);
  const weakPoints = input.weakPoints ?? [];

  const priorityLessons = [...lessons]
    .sort((a, b) => scoreLesson(b.titleAr, weakPoints) - scoreLesson(a.titleAr, weakPoints))
    .slice(0, 6);

  const mainLesson = priorityLessons[0] ?? lessons[0];

  return {
    childId: input.childId,
    childName: input.childName,
    grade,
    targetLanguage,
    subjects: primarySubjects.map((s) => s.id),
    totalLessons: getPrimaryLessons(grade).length,
    priorityLessons,
    suggestedMicroLesson: mainLesson ? buildPrimaryMicroLesson(mainLesson) : [],
    tutorPolicy: {
      persona: "ليلى للابتدائي: دافئة، صبورة، صوتية، مرحة، وتبني الثقة قبل الصعوبة.",
      defaultLanguage: getPrimaryLanguageInstruction(targetLanguage),
      pacing: [
        "درس قصير من 6 إلى 12 دقيقة",
        "سؤال واحد في كل مرة",
        "تشجيع بعد كل محاولة",
        "انتقال سريع بين شرح ولعبة وتطبيق",
        "توقف قبل التعب الذهني",
      ],
      reinforcement: [
        "نجمة للمحاولة",
        "ملصق للتركيز",
        "مهمة يومية قصيرة",
        "رسالة صغيرة للولي",
      ],
    },
    uxMode: "primary_child_first",
    safetyNote: "Phase46 يضيف طبقة الابتدائي كامتداد آمن فوق Oqul دون تعديل المصادقة أو قاعدة البيانات أو البنية الحساسة.",
  };
}

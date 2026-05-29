import { getMiddleSchoolCompetencies, middleSchoolSubjects, normalizeMiddleSchoolGrade } from "./curriculum";
import { buildStructuredLesson } from "./lesson-engine";
import { detectLearningLanguage, getLanguageInstruction, getLanguageSwitchRule } from "./language-policy";
import type { LearningLanguage, MiddleSchoolSubject, Phase42StudentProfile } from "./types";

type WeakPointLike = { topic?: string | null; severity?: number | null };

type BuildPhase42Input = {
  childId: string;
  childName?: string;
  gradeLevel?: number | string | null;
  message?: string | null;
  preferredLanguage?: LearningLanguage;
  subject?: MiddleSchoolSubject;
  weakPoints?: WeakPointLike[];
};

function scoreCompetency(topic: string, weakPoints: WeakPointLike[]) {
  const lower = topic.toLowerCase();
  return weakPoints.reduce((score, point) => {
    const t = (point.topic ?? "").toLowerCase();
    return score + (t && (lower.includes(t) || t.includes(lower)) ? (point.severity ?? 1) + 2 : 0);
  }, 0);
}

export function buildPhase42MiddleSchoolProfile(input: BuildPhase42Input): Phase42StudentProfile {
  const grade = normalizeMiddleSchoolGrade(input.gradeLevel);
  const language = input.preferredLanguage ?? "auto";
  const targetLanguage = detectLearningLanguage(input.message, language);
  const competencies = getMiddleSchoolCompetencies(grade, input.subject);
  const weakPoints = input.weakPoints ?? [];

  const priorityCompetencies = [...competencies]
    .sort((a, b) => scoreCompetency(b.titleAr, weakPoints) - scoreCompetency(a.titleAr, weakPoints))
    .slice(0, 3);

  const mainCompetency = priorityCompetencies[0] ?? competencies[0];

  return {
    childId: input.childId,
    childName: input.childName,
    grade,
    language,
    targetLanguage,
    subjects: middleSchoolSubjects.map((s) => s.id),
    priorityCompetencies,
    suggestedLesson: buildStructuredLesson(mainCompetency),
    tutorPolicy: {
      tone: "ذكية، محترمة، محفزة، مناسبة لتلميذ إعدادي وليس لطفل صغير.",
      defaultLanguage: getLanguageInstruction(targetLanguage),
      languageSwitchingRule: getLanguageSwitchRule(),
      teachingLoop: [
        "شرح منظم وقصير",
        "مثال قريب من الواقع المغربي",
        "سؤال سقراطي واحد",
        "تحليل نوع الخطأ",
        "تصحيح تكيفي",
        "تقييم مصغر",
        "قرار تقدّم أو مراجعة",
      ],
    },
    uxMode: "middle_school_smart",
    safetyNote: "Phase42 يضيف Curriculum Intelligence وLesson Engine للإعدادي كطبقة آمنة دون تعديل auth أو البنية الحساسة.",
  };
}

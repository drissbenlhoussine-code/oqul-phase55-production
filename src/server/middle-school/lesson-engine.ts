import type { LessonEngineBlock, MiddleSchoolCompetency } from "./types";

export function buildStructuredLesson(competency: MiddleSchoolCompetency): LessonEngineBlock[] {
  const misconception = competency.misconceptions[0] ?? "الخلط بين الفكرة والنتيجة";
  const objective = competency.objectives[0] ?? competency.skill;
  const example = competency.lessonSeeds[0] ?? "مثال من الحياة اليومية";

  return [
    {
      kind: "objective",
      title: "هدف الدرس",
      body: `في نهاية هذه الجلسة يجب أن يستطيع التلميذ: ${objective}.`,
    },
    {
      kind: "explanation",
      title: "شرح قصير",
      body: `${competency.titleAr}: ${competency.skill} نبدأ بفكرة واحدة فقط، ثم ننتقل إلى تطبيق مباشر حتى لا يتحول الدرس إلى حفظ طويل.`,
    },
    {
      kind: "example",
      title: "مثال قريب",
      body: `مثال: ${example}. تستعمل ليلى هذا المثال لتقريب المفهوم قبل استعمال الرموز أو المصطلحات المدرسية.`,
    },
    {
      kind: "interactive_question",
      title: "سؤال تفاعلي",
      body: "ما أول خطوة يجب أن نقوم بها قبل الحل؟",
      expectedAnswer: "تحديد المعطيات والمطلوب أو الفكرة الأساسية.",
      adaptiveHint: "إذا تردد التلميذ، أعطه اختيارين بدل سؤال مفتوح.",
    },
    {
      kind: "remediation",
      title: "تصحيح ذكي",
      body: `إذا ظهر خطأ مثل: ${misconception}، لا تعتبريه فشلًا. أعيدي الشرح بطريقة مختلفة واطلبي جوابًا قصيرًا واحدًا.`,
    },
    {
      kind: "mini_assessment",
      title: "تقييم مصغر",
      body: "سؤال واحد للتأكد من الفهم، ثم قرار: نمر للتحدي، نراجع، أو نشرح بطريقة أخرى.",
    },
    {
      kind: "summary",
      title: "ملخص ذكي",
      body: "خلاصة في ثلاث نقاط: الفكرة، الطريقة، الخطأ الذي يجب تجنبه.",
    },
  ];
}

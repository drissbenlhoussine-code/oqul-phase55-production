import type { EducationLayer } from "./types";

export function buildRemediationPath(params: {
  layer: EducationLayer;
  subject?: string;
  misconception?: string;
  failedCompetency?: string;
}) {
  const base = [
    {
      step: "diagnose",
      goal: "تحديد نوع الخطأ بدقة",
      action: "اطلب من المتعلم شرح تفكيره بجملة قصيرة.",
    },
    {
      step: "simplify",
      goal: "تبسيط المفهوم",
      action: "قدّم مثالًا أبسط مع تقليل المعلومات الجانبية.",
    },
    {
      step: "guided_practice",
      goal: "تمرين موجّه",
      action: "حل مع المتعلم خطوة بخطوة دون إعطاء الجواب كاملًا.",
    },
    {
      step: "independent_retry",
      goal: "إعادة المحاولة باستقلالية",
      action: "أعط سؤالًا مشابهًا وتابع النتيجة.",
    },
  ];

  if (params.layer === "primary") {
    return [
      ...base,
      {
        step: "visual_reinforcement",
        goal: "تثبيت بصري ولعبي",
        action: "استعمل قصة قصيرة أو لعبة مصغرة أو مثال من الحياة اليومية.",
      },
    ];
  }

  if (params.layer === "secondary") {
    return [
      ...base,
      {
        step: "exam_transfer",
        goal: "نقل الفهم إلى سؤال امتحاني",
        action: "حوّل نفس الفكرة إلى تمرين بأسلوب فرض أو باك.",
      },
    ];
  }

  return base;
}
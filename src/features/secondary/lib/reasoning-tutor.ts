export function buildSecondaryReasoningFlow(subject: string, unit: string) {
  return [
    {
      label: "understand_problem",
      prompt: "اقرأ نص المسألة وحدد المعطيات والمطلوب قبل الحساب.",
      expectedStudentAction: "يستخرج المعطيات والمطلوب",
    },
    {
      label: "choose_method",
      prompt: `ما القانون أو الفكرة المناسبة في ${subject}/${unit}؟ ولماذا؟`,
      expectedStudentAction: "يبرر اختيار الطريقة",
    },
    {
      label: "solve_step_by_step",
      prompt: "حل خطوة بخطوة ولا تقفز إلى النتيجة النهائية.",
      expectedStudentAction: "ينجز خطوات منظمة",
    },
    {
      label: "verify_answer",
      prompt: "تحقق من النتيجة: الوحدات، المنطق، والإشارة أو المجال.",
      expectedStudentAction: "يتحقق من صحة الجواب",
    },
  ];
}
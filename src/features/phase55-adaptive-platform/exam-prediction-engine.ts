export type ExamPredictionInput = {
  grade?: string | null;
  subject?: string | null;
  lessonTitle?: string;
  exercisesCount?: number;
  hasExamMethodology?: boolean;
  hasCommonMistakes?: boolean;
  hasRemediation?: boolean;
  averageScore?: number;
};

export function predictExamRisk(input: ExamPredictionInput) {
  const risks: string[] = [];
  const grade = input.grade ?? "";
  const subject = input.subject ?? "";
  const isBac = grade.includes("باك") || grade.includes("BAC") || grade.includes("2BAC");

  if ((input.exercisesCount ?? 0) < 8) risks.push("تمارين غير كافية");
  if (!input.hasExamMethodology) risks.push("غياب منهجية الامتحان");
  if (!input.hasCommonMistakes) risks.push("غياب الأخطاء الشائعة");
  if (!input.hasRemediation) risks.push("غياب العلاج التربوي");
  if ((input.averageScore ?? 60) < 50) risks.push("معدل أداء منخفض");

  const severity = risks.length >= 4 ? "high" : risks.length >= 2 ? "medium" : "low";

  return {
    severity,
    examType: isBac ? "bac" : grade.includes("3AC") || grade.includes("الثالثة") ? "regional" : "continuous",
    subjectFocus: subject,
    predictedQuestionStyles: [
      "سؤال مباشر للتحقق من الفهم",
      "تمرين تطبيقي متوسط",
      "وضعية مركبة",
      isBac ? "سؤال باك بمنهجية منظمة" : "سؤال فرض أو مراقبة مستمرة"
    ],
    risks,
    improvementPlan: [
      "أضف تمرينًا امتحانيًا واحدًا على الأقل.",
      "أضف سلم تنقيط مختصر.",
      "أضف فقرة أخطاء شائعة.",
      "أضف remediation step بعد كل خطأ."
    ]
  };
}
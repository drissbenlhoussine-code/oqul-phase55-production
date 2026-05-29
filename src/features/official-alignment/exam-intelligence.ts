export function buildExamIntelligence(input: {grade?:string|null; subject?:string|null; title:string; content?:string|null; exercisesCount?:number}) {
  const grade = input.grade ?? "";
  const content = input.content ?? "";
  const isBac = grade.includes("باك") || grade.includes("BAC") || grade.includes("2BAC");
  const isRegional = grade.includes("الثالثة") || grade.includes("3AC") || grade.includes("الأولى باكالوريا") || grade.includes("1BAC");
  const risks: string[] = [];
  if ((input.exercisesCount ?? 0) < 8) risks.push("تمارين قليلة");
  if (!content.includes("امتحان") && !content.includes("باك") && !content.includes("فرض")) risks.push("ضعف الربط بالامتحانات");
  if (!content.includes("أخطاء شائعة")) risks.push("لا توجد أخطاء شائعة كافية");
  if (!content.includes("منهجية")) risks.push("المنهجية غير واضحة");
  return { examType: isBac ? "bac" : isRegional ? "regional_or_local_exam" : "continuous_assessment", priority: isBac ? "very_high" : isRegional ? "high" : "medium", risks };
}
export function scoreOfficialAlignment(input: { title:string; grade?:string|null; subject?:string|null; unit?:string|null; content?:string|null; exercisesCount?:number }) {
  const issues: string[] = [];
  const content = input.content ?? "";
  if (!input.grade) issues.push("missing_grade");
  if (!input.subject) issues.push("missing_subject");
  if (!input.unit) issues.push("missing_unit");
  if (!input.title?.trim()) issues.push("missing_title");
  if (input.title?.includes("يحتاج مطابقة")) issues.push("unverified_title");
  if (content.length < 1200) issues.push("content_too_short");
  if ((input.exercisesCount ?? 0) < 8) issues.push("insufficient_exercises");
  if (!content.includes("أهداف الدرس")) issues.push("missing_objectives");
  if (!content.includes("أخطاء شائعة")) issues.push("missing_misconceptions");
  if (!content.includes("العلاج التربوي")) issues.push("missing_remediation");
  if (!content.includes("تعليمات ليلى")) issues.push("missing_leila_hooks");
  const score = Math.max(0, 100 - issues.length * 9);
  const status = score >= 92 ? "officially_aligned" : score >= 82 ? "cross_checked" : score >= 70 ? "mapped" : score < 45 ? "unverified" : "needs_review";
  return { score, status, issues };
}
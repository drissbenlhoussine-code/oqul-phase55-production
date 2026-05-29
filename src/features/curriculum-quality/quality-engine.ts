export type CurriculumQualityIssue =
  | "missing_content"
  | "too_short"
  | "placeholder_text"
  | "missing_examples"
  | "missing_exercises"
  | "missing_common_mistakes"
  | "missing_remediation"
  | "missing_summary"
  | "missing_leila_hooks"
  | "language_quality_risk";

export type CurriculumQualityInput = {
  title: string;
  content?: string | null;
  exercisesCount?: number;
};

export function evaluateCurriculumQuality(input: CurriculumQualityInput) {
  const issues: CurriculumQualityIssue[] = [];
  const content = input.content ?? "";
  const normalized = content.toLowerCase();

  if (!content.trim()) issues.push("missing_content");
  if (content.trim().length < 900) issues.push("too_short");

  const placeholderMarkers = [
    "يحتاج مطابقة",
    "تمرين 1 سهل",
    "جواب نموذجي مختصر",
    "درس أصلي من oqul مبني على عنوان المنهج فقط",
    "مثال بسيط لفهم",
  ];

  if (placeholderMarkers.some((m) => normalized.includes(m.toLowerCase()))) {
    issues.push("placeholder_text");
  }

  if (!content.includes("## أمثلة") && !content.includes("مثال")) issues.push("missing_examples");
  if ((input.exercisesCount ?? 0) < 6) issues.push("missing_exercises");
  if (!content.includes("أخطاء شائعة")) issues.push("missing_common_mistakes");
  if (!content.includes("العلاج") && !content.includes("Remediation")) issues.push("missing_remediation");
  if (!content.includes("ملخص")) issues.push("missing_summary");
  if (!content.includes("ليلى") && !content.includes("تلميح")) issues.push("missing_leila_hooks");

  const score = Math.max(0, 100 - issues.length * 10);

  let status: "excellent" | "good" | "needs_review" | "weak";
  if (score >= 90) status = "excellent";
  else if (score >= 75) status = "good";
  else if (score >= 50) status = "needs_review";
  else status = "weak";

  return {
    score,
    status,
    issues,
    recommendation:
      status === "weak"
        ? "أعد بناء الدرس بعمق تربوي كامل."
        : status === "needs_review"
          ? "حسّن الأمثلة والتمارين والعلاج التربوي."
          : "الدرس قابل للاستخدام مع مراجعة بشرية خفيفة.",
  };
}
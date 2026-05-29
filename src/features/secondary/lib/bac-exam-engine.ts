export type BacExamPlanInput = {
  grade: "TC" | "1BAC" | "2BAC";
  subject: string;
  weakCompetencies: string[];
  daysAvailable?: number;
};

export function createBacExamPlan(input: BacExamPlanInput) {
  const days = input.daysAvailable ?? 14;

  return {
    mode: input.grade === "2BAC" ? "national_exam_readiness" : "progressive_exam_training",
    subject: input.subject,
    days,
    plan: [
      { phase: "diagnostic", goal: "تحديد نقاط الضعف", durationDays: Math.max(1, Math.floor(days * 0.15)) },
      { phase: "remediation", goal: "إصلاح التعثرات", focus: input.weakCompetencies, durationDays: Math.max(2, Math.floor(days * 0.35)) },
      { phase: "exam_practice", goal: "حل تمارين امتحانية", durationDays: Math.max(2, Math.floor(days * 0.35)) },
      { phase: "final_review", goal: "مراجعة مركزة", durationDays: Math.max(1, Math.floor(days * 0.15)) },
    ],
  };
}
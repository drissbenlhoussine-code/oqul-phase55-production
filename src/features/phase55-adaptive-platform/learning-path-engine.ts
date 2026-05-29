export type LearnerSignal = {
  childId?: string;
  grade?: string | null;
  subject?: string | null;
  weakPoints?: string[];
  completedLessons?: number;
  averageScore?: number;
  confidence?: number;
};

export function buildPersonalizedLearningPath(signal: LearnerSignal) {
  const score = signal.averageScore ?? 50;
  const confidence = signal.confidence ?? 3;
  const weakPoints = signal.weakPoints ?? [];

  const risk =
    score < 45 || confidence <= 2 ? "high" :
    score < 65 || weakPoints.length >= 3 ? "medium" :
    "low";

  const pace =
    risk === "high" ? "slow_guided" :
    risk === "medium" ? "balanced" :
    "accelerated";

  return {
    risk,
    pace,
    weeklyPlan: [
      { day: "اليوم 1", action: "تشخيص سريع + مراجعة prerequisite", durationMinutes: 20 },
      { day: "اليوم 2", action: "شرح موجه مع ليلى + مثالين", durationMinutes: 25 },
      { day: "اليوم 3", action: "تمارين سهلة ومتوسطة", durationMinutes: 25 },
      { day: "اليوم 4", action: "علاج الأخطاء الشائعة", durationMinutes: 20 },
      { day: "اليوم 5", action: "اختبار قصير + توصية تلقائية", durationMinutes: 20 },
    ],
    recommendations: [
      risk === "high" ? "ابدأ من أساسيات أبسط ولا تنتقل بسرعة." : "استمر في التدرج مع تمارين متنوعة.",
      "اطلب من ليلى تفسير كل خطأ قبل إعطاء الجواب.",
      "استعمل اختبارًا قصيرًا بعد كل درس.",
      "راجع نقطة ضعف واحدة فقط في كل جلسة."
    ],
    nextActions: weakPoints.length
      ? weakPoints.map((w) => `راجع: ${w}`)
      : ["ابدأ بدرس جديد مع اختبار قبلي قصير"]
  };
}
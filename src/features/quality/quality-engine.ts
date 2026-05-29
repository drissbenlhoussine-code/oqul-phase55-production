import type { QualitySignal, QualityDecision } from "./types";

export function evaluateLearningQuality(signal: QualitySignal): QualityDecision {
  const correct = signal.answerCorrect === true;
  const retryCount = signal.retryCount ?? 0;
  const hintsUsed = signal.hintsUsed ?? 0;
  const responseTime = signal.responseTimeSeconds ?? 0;
  const confidence = signal.confidenceSelfRating ?? 3;

  if (correct && retryCount === 0 && hintsUsed === 0 && confidence >= 4) {
    return {
      masteryDelta: 8,
      confidenceDelta: 5,
      nextAction: responseTime > 0 && responseTime < 20 ? "increase_difficulty" : "celebrate",
      reason: "إجابة صحيحة بثقة عالية وبدون مساعدة.",
      leilaInstruction: "هنّئ المتعلم ثم قدّم تحديًا أعلى قليلًا.",
    };
  }

  if (correct) {
    return {
      masteryDelta: 5,
      confidenceDelta: 3,
      nextAction: "continue",
      reason: "إجابة صحيحة لكن تحتاج تثبيتًا تدريجيًا.",
      leilaInstruction: "اشرح لماذا الجواب صحيح ثم انتقل لتطبيق مشابه.",
    };
  }

  if (!correct && retryCount >= 2) {
    return {
      masteryDelta: -4,
      confidenceDelta: -2,
      nextAction: "review_prerequisite",
      reason: "تكرار الخطأ يدل على نقص في prerequisite.",
      leilaInstruction: "ارجع خطوة إلى الوراء واشرح الأساس بمثال أبسط جدًا.",
    };
  }

  if (!correct && hintsUsed > 0) {
    return {
      masteryDelta: -1,
      confidenceDelta: 0,
      nextAction: "repeat_with_example",
      reason: "المتعلم احتاج مساعدة، الأفضل إعادة الشرح بمثال جديد.",
      leilaInstruction: "أعد الشرح بطريقة مختلفة ثم أعط سؤالًا أسهل.",
    };
  }

  return {
    masteryDelta: -2,
    confidenceDelta: -1,
    nextAction: "give_hint",
    reason: "خطأ أولي يحتاج تلميحًا لا جوابًا مباشرًا.",
    leilaInstruction: "لا تعط الجواب مباشرة. أعط تلميحًا قصيرًا وسؤالًا موجّهًا.",
  };
}
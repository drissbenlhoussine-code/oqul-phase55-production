import { confidenceTutorPolicy } from "@/server/confidence-engine/confidence-engine";
import { recommendCognitivePace } from "@/server/cognitive-pacing/cognitive-pacing-engine";

export type LivingLeilaInput = {
  childName?: string;
  masteryScore: number;
  confidenceScore: number;
  recentMistakes: number;
  emotion?: "confident" | "frustrated" | "tired" | "curious" | "neutral";
};

export function buildLivingLeilaResponse(input: LivingLeilaInput) {
  const policy = confidenceTutorPolicy(input.confidenceScore);
  const pace = recommendCognitivePace({
    masteryScore: input.masteryScore,
    confidenceScore: input.confidenceScore,
    recentMistakes: input.recentMistakes,
    emotion: input.emotion,
  });

  const name = input.childName ? `${input.childName}، ` : "";

  const message =
    input.emotion === "frustrated" || input.confidenceScore < 40
      ? `${name}لا تقلق يا بطل 🌱 سنرجع خطوة صغيرة ونفهمها بطريقة أسهل.`
      : input.masteryScore >= 85
        ? `${name}ممتاز جدًا 👏 أنت جاهز لتحدي صغير مع ليلى.`
        : `${name}نكمل بهدوء وبطريقة جميلة. التقدم ديالك واضح 😊`;

  return {
    message,
    tone: policy.tone,
    pace: pace.recommendedPace,
    challengeLevel: pace.challengeLevel,
    maxSessionMinutes: pace.maxSessionMinutes,
    reason: pace.reason,
  };
}

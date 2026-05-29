export type PacingInput = {
  masteryScore: number;
  confidenceScore: number;
  recentMistakes: number;
  averageResponseSeconds?: number;
  emotion?: "confident" | "frustrated" | "tired" | "curious" | "neutral";
};

export function recommendCognitivePace(input: PacingInput) {
  if (input.emotion === "tired" || input.recentMistakes >= 4) {
    return {
      recommendedPace: "short-and-soft",
      maxSessionMinutes: 8,
      challengeLevel: "easy",
      reason: "الطفل يحتاج جلسة قصيرة لتجنب الإرهاق.",
    };
  }

  if (input.confidenceScore < 40 || input.masteryScore < 40) {
    return {
      recommendedPace: "slow-rebuild",
      maxSessionMinutes: 10,
      challengeLevel: "foundation",
      reason: "الثقة أو الإتقان منخفضان، الأفضل الرجوع للأساسيات.",
    };
  }

  if (input.masteryScore >= 85 && input.confidenceScore >= 75 && input.emotion !== "frustrated") {
    return {
      recommendedPace: "challenge-ready",
      maxSessionMinutes: 18,
      challengeLevel: "slightly-harder",
      reason: "الطفل مستعد لتحدي بسيط.",
    };
  }

  return {
    recommendedPace: "balanced",
    maxSessionMinutes: 12,
    challengeLevel: "normal",
    reason: "المستوى مستقر ويحتاج تقدمًا متوازنًا.",
  };
}

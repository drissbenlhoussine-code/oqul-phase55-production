export type ConfidenceInput = {
  correct: boolean;
  previousConfidence: number;
  attemptsOnSkill: number;
  emotion?: "confident" | "frustrated" | "tired" | "curious" | "neutral";
};

export function calculateConfidence(input: ConfidenceInput) {
  let delta = input.correct ? 6 : -5;

  if (input.emotion === "frustrated") delta -= 4;
  if (input.emotion === "tired") delta -= 2;
  if (input.emotion === "curious") delta += 2;
  if (input.attemptsOnSkill >= 5 && !input.correct) delta -= 3;

  return Math.max(0, Math.min(100, Math.round((input.previousConfidence + delta) * 100) / 100));
}

export function confidenceState(score: number) {
  if (score >= 80) return "confident";
  if (score >= 60) return "steady";
  if (score >= 40) return "fragile";
  return "needs-protection";
}

export function confidenceTutorPolicy(score: number) {
  const state = confidenceState(score);

  if (state === "needs-protection") {
    return {
      pace: "slow",
      challenge: "easy",
      tone: "extra-gentle",
      message: "نبدأ بخطوة صغيرة جدًا حتى نرجع الثقة.",
    };
  }

  if (state === "fragile") {
    return {
      pace: "calm",
      challenge: "normal-light",
      tone: "encouraging",
      message: "نتمرن بهدوء ونقوي الفكرة تدريجيًا.",
    };
  }

  if (state === "confident") {
    return {
      pace: "normal",
      challenge: "slightly-harder",
      tone: "celebratory",
      message: "أنت جاهز لتحدي صغير!",
    };
  }

  return {
    pace: "normal",
    challenge: "normal",
    tone: "warm",
    message: "نكمل بتوازن جميل.",
  };
}

export type LearnerMemorySignal = {
  skillId?: string;
  subject?: string;
  emotion?: "confident" | "frustrated" | "tired" | "curious" | "neutral";
  correct?: boolean;
  masteryScore?: number;
  durationSeconds?: number;
};

export function summarizeLearnerMemory(signals: LearnerMemorySignal[]) {
  const mistakes = signals.filter((signal) => signal.correct === false);
  const wins = signals.filter((signal) => signal.correct === true);
  const frustration = signals.filter((signal) => signal.emotion === "frustrated").length;
  const tired = signals.filter((signal) => signal.emotion === "tired").length;

  const weakSkillIds = Array.from(
    new Set(
      signals
        .filter((signal) => typeof signal.masteryScore === "number" && signal.masteryScore < 50)
        .map((signal) => signal.skillId)
        .filter(Boolean)
    )
  );

  const strongSkillIds = Array.from(
    new Set(
      signals
        .filter((signal) => typeof signal.masteryScore === "number" && signal.masteryScore >= 80)
        .map((signal) => signal.skillId)
        .filter(Boolean)
    )
  );

  const summary =
    mistakes.length > wins.length
      ? "الطفل يحتاج دعمًا هادئًا ومراجعة قصيرة قبل رفع مستوى التحدي."
      : "الطفل يحقق تقدمًا جيدًا ويمكن رفع التحدي تدريجيًا مع الحفاظ على التشجيع.";

  return {
    summary,
    weakSkillIds,
    strongSkillIds,
    emotionalState:
      frustration > 0 ? "needs-reassurance" : tired > 0 ? "needs-short-session" : "stable",
    confidenceHint: wins.length >= mistakes.length ? "rising" : "fragile",
  };
}

export function shouldRefreshLearnerMemory(lastSnapshotMinutesAgo: number) {
  return lastSnapshotMinutesAgo >= 30;
}

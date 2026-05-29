export function buildParentJournalSummary(input: {
  learnedToday: string[];
  struggledWith: string[];
  emotionalState?: "excited" | "stable" | "tired" | "frustrated";
}) {
  const suggestion =
    input.struggledWith.length > 0
      ? `تقترح ليلى مراجعة ${input.struggledWith[0]} لمدة 5 دقائق فقط.`
      : "تقترح ليلى الحفاظ على تحدي يومي قصير للحفاظ على التقدم.";

  return {
    learnedToday: input.learnedToday,
    struggledWith: input.struggledWith,
    leilaSuggestion: suggestion,
    emotionalState: input.emotionalState ?? "stable",
  };
}

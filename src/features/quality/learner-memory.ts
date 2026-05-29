export type LearnerMemoryPatch = {
  masteryChange: number;
  confidenceChange: number;
  misconception?: string;
  preferredExplanationStyle?: "visual" | "step_by_step" | "story" | "formal" | "exam";
  recommendedNextReview?: "today" | "tomorrow" | "this_week";
};

export function createLearnerMemoryPatch(input: {
  correct: boolean;
  repeatedMistake?: boolean;
  layer: "primary" | "middle_school" | "secondary";
}): LearnerMemoryPatch {
  if (input.correct) {
    return {
      masteryChange: 5,
      confidenceChange: 3,
      recommendedNextReview: "this_week",
    };
  }

  if (input.repeatedMistake) {
    return {
      masteryChange: -4,
      confidenceChange: -1,
      misconception: "repeated_pattern_detected",
      preferredExplanationStyle: input.layer === "primary" ? "story" : input.layer === "secondary" ? "step_by_step" : "visual",
      recommendedNextReview: "tomorrow",
    };
  }

  return {
    masteryChange: -2,
    confidenceChange: 0,
    recommendedNextReview: "today",
  };
}
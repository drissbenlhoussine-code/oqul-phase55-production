export const PROMPT_VERSIONS = {
  LEILA_TUTOR_V1: "leila_tutor_v1",
  LEILA_EXPLANATION_V1: "leila_explanation_v1",
  LEILA_RECOMMENDATION_V1: "leila_recommendation_v1",
} as const;

export type PromptVersion =
  (typeof PROMPT_VERSIONS)[keyof typeof PROMPT_VERSIONS];

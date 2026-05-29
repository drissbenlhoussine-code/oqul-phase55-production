export type PoisonJobDecision = {
  shouldEscalate: boolean;
  reason: string;
};

export function classifyPoisonJob(
  attemptsMade: number,
  maxAttempts: number
): PoisonJobDecision {
  if (attemptsMade >= maxAttempts) {
    return {
      shouldEscalate: true,
      reason: "Retry exhaustion reached.",
    };
  }

  return {
    shouldEscalate: false,
    reason: "Job still retryable.",
  };
}

export type RetryDecision = {
  retryable: boolean;
  delayMs: number;
  quarantine: boolean;
  reason: string;
};

export function calculateExternalEffectRetry(input: {
  attempts: number;
  maxAttempts?: number;
  baseDelayMs?: number;
}): RetryDecision {
  const maxAttempts = input.maxAttempts ?? 5;
  const baseDelayMs = input.baseDelayMs ?? 500;

  if (input.attempts >= maxAttempts) {
    return {
      retryable: false,
      delayMs: 0,
      quarantine: true,
      reason: "retry attempts exhausted",
    };
  }

  return {
    retryable: true,
    delayMs: Math.min(baseDelayMs * 2 ** input.attempts, 30_000),
    quarantine: false,
    reason: "retry scheduled",
  };
}

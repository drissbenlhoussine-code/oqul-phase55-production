export type RetryExhaustionInput = {
  attemptsMade: number;
  maxAttempts: number;
};

export function hasExhaustedRetries(input: RetryExhaustionInput) {
  return input.attemptsMade >= input.maxAttempts;
}

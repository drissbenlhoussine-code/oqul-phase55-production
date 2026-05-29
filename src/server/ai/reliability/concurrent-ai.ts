export type AIConcurrencyDecision = {
  allowed: boolean;
  reason: string;
};

export function decideAIConcurrency(
  activeRequests: number,
  maxConcurrentRequests: number
): AIConcurrencyDecision {
  if (activeRequests >= maxConcurrentRequests) {
    return {
      allowed: false,
      reason: "AI concurrency limit reached.",
    };
  }

  return {
    allowed: true,
    reason: "AI request allowed.",
  };
}

export type QuotaDecision = {
  allowed: boolean;
  remaining: number;
};

export function decideQuotaAfterConcurrentUse(
  currentUsage: number,
  requested: number,
  limit: number
): QuotaDecision {
  const nextUsage = currentUsage + requested;

  return {
    allowed: nextUsage <= limit,
    remaining: Math.max(limit - nextUsage, 0),
  };
}

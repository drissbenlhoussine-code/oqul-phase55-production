export type AtomicLimiterState = {
  count: number;
  resetAt: number;
};

const states = new Map<string, AtomicLimiterState>();

export async function simulateAtomicLimit(
  key: string,
  limit: number,
  windowMs: number
) {
  const now = Date.now();
  const existing = states.get(key);

  if (!existing || existing.resetAt <= now) {
    states.set(key, {
      count: 1,
      resetAt: now + windowMs,
    });

    return {
      allowed: true,
      remaining: limit - 1,
    };
  }

  if (existing.count >= limit) {
    return {
      allowed: false,
      remaining: 0,
    };
  }

  existing.count += 1;

  return {
    allowed: true,
    remaining: limit - existing.count,
  };
}

export function resetAtomicLimiterSimulator() {
  states.clear();
}

const memory = new Map<string, number>();

export function rateLimit(
  key: string,
  limit: number
) {
  const current = memory.get(key) || 0;

  if (current >= limit) {
    return false;
  }

  memory.set(key, current + 1);

  return true;
}

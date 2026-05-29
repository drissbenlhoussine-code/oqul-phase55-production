import { getRedisClient } from "./redis-client";

export async function safeRedisOperation<T>(
  operation: () => Promise<T>,
  fallback: T,
  timeoutMs = 1500
): Promise<T> {
  const client = getRedisClient();

  if (!client) {
    return fallback;
  }

  try {
    return await Promise.race([
      operation(),
      new Promise<T>((resolve) => setTimeout(() => resolve(fallback), timeoutMs)),
    ]);
  } catch (error) {
    console.error("[REDIS_DEGRADED_MODE]", {
      error: error instanceof Error ? error.message : error,
    });

    return fallback;
  }
}

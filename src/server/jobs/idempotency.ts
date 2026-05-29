import { redisCache } from "@/server/cache/redis-cache";

export async function hasProcessedJob(key: string) {
  return Boolean(await redisCache.get(`job:idempotency:${key}`));
}

export async function markJobProcessed(key: string, ttlMs = 1000 * 60 * 60 * 24) {
  await redisCache.set(`job:idempotency:${key}`, true, { ttlMs });
}

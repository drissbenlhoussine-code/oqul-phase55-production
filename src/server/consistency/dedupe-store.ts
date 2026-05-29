import { redisCache } from "@/server/cache/redis-cache";

export type DedupeResult = {
  accepted: boolean;
  key: string;
};

export async function acceptOnce(key: string, ttlMs = 1000 * 60 * 60): Promise<DedupeResult> {
  const existing = await redisCache.get<boolean>(`dedupe:${key}`);

  if (existing) {
    return {
      accepted: false,
      key,
    };
  }

  await redisCache.set(`dedupe:${key}`, true, { ttlMs });

  return {
    accepted: true,
    key,
  };
}

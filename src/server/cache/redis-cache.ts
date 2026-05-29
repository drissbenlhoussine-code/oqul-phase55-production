import { getRedisClient } from "./redis-client";
import { safeRedisOperation } from "./resilient-redis";
import type { CacheOptions, CacheStore } from "./cache-types";

export class RedisCacheStore implements CacheStore {
  async get<T>(key: string): Promise<T | null> {
    const client = getRedisClient();

    if (!client) {
      return null;
    }

    return safeRedisOperation(async () => {
      const raw = await client.get(key);
      return raw ? (JSON.parse(raw) as T) : null;
    }, null);
  }

  async set<T>(key: string, value: T, options: CacheOptions): Promise<void> {
    const client = getRedisClient();

    if (!client) {
      return;
    }

    await safeRedisOperation(
      async () => {
        await client.set(key, JSON.stringify(value), "PX", options.ttlMs);
      },
      undefined
    );
  }

  async delete(key: string): Promise<void> {
    const client = getRedisClient();

    if (!client) {
      return;
    }

    await safeRedisOperation(
      async () => {
        await client.del(key);
      },
      undefined
    );
  }
}

export const redisCache = new RedisCacheStore();

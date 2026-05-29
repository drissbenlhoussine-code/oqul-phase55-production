/**
 * Redis Client — resilient singleton for OQUL.
 * Falls back gracefully if Redis unavailable (dev/test).
 * Source of truth: Phase 26 redis-client + resilience patterns.
 */
import Redis from "ioredis";
import type { Redis as RedisType } from "ioredis";

let client: RedisType | null = null;
let initAttempted = false;

export function getRedisClient(): RedisType | null {
  if (initAttempted) return client;
  initAttempted = true;

  const url = process.env.REDIS_URL;
  if (!url) {
    if (process.env.NODE_ENV !== "production") {
      // Dev: silent fallback to in-memory
      return null;
    }
    console.warn("[REDIS] REDIS_URL not set — Redis disabled");
    return null;
  }

  try {
    client = new Redis(url, {
      maxRetriesPerRequest: 3,
      enableReadyCheck: true,
      lazyConnect: true,
      retryStrategy: (times) => Math.min(times * 200, 2000),
    });

    client.on("error", (err) => {
      console.error("[REDIS] Connection error:", err.message);
    });

    client.on("connect", () => {
      console.info("[REDIS] Connected");
    });

    return client;
  } catch {
    console.warn("[REDIS] ioredis not available — Redis disabled");
    return null;
  }
}

export function isRedisAvailable(): boolean {
  return getRedisClient() !== null;
}

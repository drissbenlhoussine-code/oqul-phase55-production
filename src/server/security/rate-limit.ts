/**
 * Unified Rate Limiter — Redis-backed in production, in-memory in dev.
 * Uses Phase 26's Lua-based atomic Redis limiter when Redis is available.
 */
import { getRedisClient, isRedisAvailable } from "@/server/cache/redis-client";

export interface RateLimitResult {
  allowed:   boolean;
  remaining: number;
  resetAt:   number;
}

// ── In-memory fallback (dev / no Redis) ────────────────────────────────────
const memStore = new Map<string, { count: number; resetAt: number }>();

function memoryLimit(key: string, limit: number, windowMs: number): RateLimitResult {
  const now    = Date.now();
  const record = memStore.get(key);

  if (!record || now > record.resetAt) {
    memStore.set(key, { count: 1, resetAt: now + windowMs });
    return { allowed: true, remaining: limit - 1, resetAt: now + windowMs };
  }

  record.count++;
  const remaining = Math.max(0, limit - record.count);
  return { allowed: record.count <= limit, remaining, resetAt: record.resetAt };
}

// ── Redis-backed limiter (Lua atomic fixed-window) ─────────────────────────
const LUA_SCRIPT = `
local current = redis.call("INCR", KEYS[1])
if current == 1 then
  redis.call("PEXPIRE", KEYS[1], ARGV[1])
end
local remaining = math.max(0, tonumber(ARGV[2]) - current)
if current > tonumber(ARGV[2]) then
  return {0, remaining, 0}
end
return {1, remaining, 1}
`;

type RedisEvalClient = {
  eval: (script: string, numKeys: number, ...args: string[]) => Promise<[number, number, number]>;
};

async function redisLimit(key: string, limit: number, windowMs: number): Promise<RateLimitResult> {
  const client = getRedisClient();
  if (!client) return memoryLimit(key, limit, windowMs);

  try {
    const redisEvalClient = client as unknown as RedisEvalClient;
    const result = await redisEvalClient.eval(
      LUA_SCRIPT, 1, `rl:${key}`, String(windowMs), String(limit)
    );

    const allowed    = result[0] === 1;
    const remaining  = Math.max(0, result[1]);
    const resetAt    = Date.now() + windowMs;
    return { allowed, remaining, resetAt };
  } catch {
    // Redis error → fallback
    return memoryLimit(key, limit, windowMs);
  }
}

/** Sync fallback for development-only legacy callers. Prefer rateLimitAsync in routes. */
export function rateLimit(key: string, limit: number, windowMs: number): RateLimitResult {
  if (process.env.NODE_ENV === "production" && isRedisAvailable()) {
    throw new Error("rateLimit() is synchronous and cannot use Redis. Use rateLimitAsync() in production routes.");
  }
  return memoryLimit(key, limit, windowMs);
}

/** Async version — uses Redis when available */
export async function rateLimitAsync(key: string, limit: number, windowMs: number): Promise<RateLimitResult> {
  if (isRedisAvailable()) {
    return redisLimit(key, limit, windowMs);
  }
  return memoryLimit(key, limit, windowMs);
}

// ── Preset limiters ────────────────────────────────────────────────────────
export const loginLimiter    = (ip: string)     => rateLimitAsync(`login:${ip}`,    5,  15 * 60 * 1000);
export const registerLimiter = (ip: string)     => rateLimitAsync(`register:${ip}`, 3,  60 * 60 * 1000);
export const aiChatLimiter   = (userId: string) => rateLimitAsync(`ai:${userId}`,   10, 60 * 1000);
export const refreshLimiter  = (ip: string)     => rateLimitAsync(`refresh:${ip}`,  20, 60 * 1000);

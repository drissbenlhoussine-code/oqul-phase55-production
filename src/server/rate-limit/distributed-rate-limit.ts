import { getRedisClient } from "@/server/cache/redis-client";

export type DistributedRateLimitInput = {
  key: string;
  limit: number;
  windowMs: number;
};

export type DistributedRateLimitResult = {
  allowed: boolean;
  remaining: number;
  resetAt: number;
  algorithm: "redis-fixed-window-lua" | "memory-fallback";
};

const luaScript = `
local current = redis.call("INCR", KEYS[1])
if current == 1 then
  redis.call("PEXPIRE", KEYS[1], ARGV[1])
end
local remaining = tonumber(ARGV[2]) - current
if current > tonumber(ARGV[2]) then
  return {0, 0}
end
return {1, remaining}
`;

const memoryStore = new Map<string, { count: number; resetAt: number }>();

function memoryFallback(input: DistributedRateLimitInput): DistributedRateLimitResult {
  const now = Date.now();
  const current = memoryStore.get(input.key);

  if (!current || current.resetAt < now) {
    memoryStore.set(input.key, {
      count: 1,
      resetAt: now + input.windowMs,
    });

    return {
      allowed: true,
      remaining: input.limit - 1,
      resetAt: now + input.windowMs,
      algorithm: "memory-fallback",
    };
  }

  if (current.count >= input.limit) {
    return {
      allowed: false,
      remaining: 0,
      resetAt: current.resetAt,
      algorithm: "memory-fallback",
    };
  }

  current.count += 1;

  return {
    allowed: true,
    remaining: input.limit - current.count,
    resetAt: current.resetAt,
    algorithm: "memory-fallback",
  };
}

export async function checkDistributedRateLimit(
  input: DistributedRateLimitInput
): Promise<DistributedRateLimitResult> {
  const client = getRedisClient();

  if (!client) {
    return memoryFallback(input);
  }

  try {
    const result = (await client.eval(
      luaScript,
      1,
      input.key,
      input.windowMs,
      input.limit
    )) as [number, number];

    return {
      allowed: result[0] === 1,
      remaining: Number(result[1]),
      resetAt: Date.now() + input.windowMs,
      algorithm: "redis-fixed-window-lua",
    };
  } catch (error) {
    console.error("[RATE_LIMIT_REDIS_FAILURE]", {
      error: error instanceof Error ? error.message : error,
    });

    return memoryFallback(input);
  }
}

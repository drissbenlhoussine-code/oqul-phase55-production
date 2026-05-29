export type RedisRuntimeHealth = {
  connected: boolean;
  degraded: boolean;
  checkedAt: string;
};

export function createRedisRuntimeHealth(
  connected: boolean,
  degraded = false
): RedisRuntimeHealth {
  return {
    connected,
    degraded,
    checkedAt: new Date().toISOString(),
  };
}

import { recordMetric } from "./runtime-metrics";

export function recordRedisReconnect() {
  recordMetric({
    name: "redis.reconnect",
    value: 1,
    timestamp: Date.now(),
  });
}

export function recordRedisDisconnect() {
  recordMetric({
    name: "redis.disconnect",
    value: 1,
    timestamp: Date.now(),
  });
}

export function recordRedisLatency(latencyMs: number) {
  recordMetric({
    name: "redis.latency",
    value: latencyMs,
    timestamp: Date.now(),
  });
}

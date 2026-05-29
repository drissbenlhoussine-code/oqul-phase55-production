import { Counter, Gauge } from "prom-client";

export const redisReconnectCounter = new Counter({
  name: "oqul_redis_reconnect_total",
  help: "Total Redis reconnect attempts",
});

export const queueRecoveryCounter = new Counter({
  name: "oqul_queue_recovery_total",
  help: "Total queue recovery operations",
});

export const runtimeDegradedModeGauge = new Gauge({
  name: "oqul_runtime_degraded_mode",
  help: "Runtime degraded mode status",
});

export const workerLagGauge = new Gauge({
  name: "oqul_worker_lag",
  help: "Queue worker lag estimation",
});

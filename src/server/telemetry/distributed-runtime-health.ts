export type DistributedRuntimeHealth = {
  redis: "healthy" | "degraded";
  queue: "healthy" | "degraded";
  workers: "healthy" | "degraded";
};

export function getDistributedRuntimeHealth(): DistributedRuntimeHealth {
  return {
    redis: "healthy",
    queue: "healthy",
    workers: "healthy",
  };
}
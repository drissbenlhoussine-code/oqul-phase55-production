export type RuntimeHealthSnapshot = {
  redis: "healthy" | "degraded";
  queue: "healthy" | "degraded";
  telemetry: "healthy" | "degraded";
};

export function getRuntimeHealthSnapshot(): RuntimeHealthSnapshot {
  return {
    redis: "healthy",
    queue: "healthy",
    telemetry: "healthy",
  };
}

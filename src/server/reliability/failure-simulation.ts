export type FailureKind =
  | "redis-timeout"
  | "redis-disconnect"
  | "queue-crash"
  | "ai-timeout"
  | "stream-stall"
  | "duplicate-job";

export function simulateFailure(kind: FailureKind) {
  return {
    id: crypto.randomUUID(),
    kind,
    simulatedAt: new Date().toISOString(),
  };
}

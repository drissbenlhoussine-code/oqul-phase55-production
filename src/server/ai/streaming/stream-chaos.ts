export type StreamChaosEvent =
  | "abort"
  | "stall"
  | "long-running"
  | "client-disconnect";

export function simulateStreamChaos(event: StreamChaosEvent) {
  return {
    id: crypto.randomUUID(),
    event,
    occurredAt: new Date().toISOString(),
  };
}

export function shouldCleanupStream(
  lastChunkAt: number,
  now = Date.now(),
  timeoutMs = 15000
) {
  return now - lastChunkAt > timeoutMs;
}

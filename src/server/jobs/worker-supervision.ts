export type WorkerHeartbeat = {
  workerId: string;
  queueName: string;
  lastSeenAt: number;
};

const heartbeats = new Map<string, WorkerHeartbeat>();

export function recordWorkerHeartbeat(workerId: string, queueName: string) {
  heartbeats.set(workerId, {
    workerId,
    queueName,
    lastSeenAt: Date.now(),
  });
}

export function isWorkerStalled(workerId: string, timeoutMs = 30000) {
  const heartbeat = heartbeats.get(workerId);

  if (!heartbeat) {
    return true;
  }

  return Date.now() - heartbeat.lastSeenAt > timeoutMs;
}

export function getWorkerHeartbeats() {
  return Array.from(heartbeats.values());
}

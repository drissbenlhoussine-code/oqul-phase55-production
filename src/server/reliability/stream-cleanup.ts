const activeStreams = new Map<string, number>();

export function markStreamActive(streamId: string) {
  activeStreams.set(streamId, Date.now());
}

export function cleanupInactiveStreams(maxAgeMs = 300000) {
  const now = Date.now();

  for (const [streamId, startedAt] of activeStreams.entries()) {
    if (now - startedAt > maxAgeMs) {
      activeStreams.delete(streamId);
    }
  }
}

export function getActiveStreamCount() {
  return activeStreams.size;
}

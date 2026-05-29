type StreamLifecycle = {
  streamId: string;
  startedAt: number;
  lastChunkAt: number;
  aborted: boolean;
};

const activeStreams = new Map<string, StreamLifecycle>();

export function startStream(streamId: string) {
  activeStreams.set(streamId, {
    streamId,
    startedAt: Date.now(),
    lastChunkAt: Date.now(),
    aborted: false,
  });
}

export function touchStream(streamId: string) {
  const stream = activeStreams.get(streamId);

  if (!stream) {
    return;
  }

  stream.lastChunkAt = Date.now();
}

export function abortStream(streamId: string) {
  const stream = activeStreams.get(streamId);

  if (!stream) {
    return;
  }

  stream.aborted = true;
}

export function cleanupStream(streamId: string) {
  activeStreams.delete(streamId);
}

export function isStreamStalled(streamId: string, timeoutMs = 15000) {
  const stream = activeStreams.get(streamId);

  if (!stream) {
    return false;
  }

  return Date.now() - stream.lastChunkAt > timeoutMs;
}

export function cleanupStalledStreams(timeoutMs = 60000) {
  const now = Date.now();

  for (const [streamId, stream] of activeStreams.entries()) {
    if (stream.aborted || now - stream.lastChunkAt > timeoutMs) {
      activeStreams.delete(streamId);
    }
  }
}

export function getActiveStreamCount() {
  return activeStreams.size;
}

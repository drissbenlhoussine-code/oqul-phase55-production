export type StreamHealthState = {
  startedAt: number;
  lastChunkAt: number;
  chunks: number;
  aborted: boolean;
};

export function createStreamHealth(): StreamHealthState {
  const now = Date.now();
  return {
    startedAt: now,
    lastChunkAt: now,
    chunks: 0,
    aborted: false,
  };
}

export function markChunk(state: StreamHealthState) {
  state.lastChunkAt = Date.now();
  state.chunks += 1;
}

export function markAborted(state: StreamHealthState) {
  state.aborted = true;
}

export function isStreamStalled(state: StreamHealthState, timeoutMs: number) {
  return Date.now() - state.lastChunkAt > timeoutMs;
}

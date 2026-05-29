export type TraceSpan = {
  id: string;
  name: string;
  requestId: string;
  startedAt: number;
  endedAt?: number;
  durationMs?: number;
  attributes?: Record<string, unknown>;
};

export function startSpan(
  name: string,
  requestId: string,
  attributes?: Record<string, unknown>
): TraceSpan {
  return {
    id: crypto.randomUUID(),
    name,
    requestId,
    startedAt: Date.now(),
    attributes,
  };
}

export function endSpan(span: TraceSpan): TraceSpan {
  const endedAt = Date.now();
  return {
    ...span,
    endedAt,
    durationMs: endedAt - span.startedAt,
  };
}

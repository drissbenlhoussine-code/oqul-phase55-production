export type TelemetrySpan = {
  traceId: string;
  spanId: string;
  name: string;
  startedAt: number;
};

export function createTelemetrySpan(name: string): TelemetrySpan {
  return {
    traceId: crypto.randomUUID(),
    spanId: crypto.randomUUID(),
    name,
    startedAt: Date.now(),
  };
}

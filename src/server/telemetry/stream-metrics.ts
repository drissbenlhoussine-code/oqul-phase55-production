import { recordMetric } from "./runtime-metrics";

export function recordStreamAbort() {
  recordMetric({
    name: "stream.abort",
    value: 1,
    timestamp: Date.now(),
  });
}

export function recordStreamPressure(connections: number) {
  recordMetric({
    name: "stream.concurrent",
    value: connections,
    timestamp: Date.now(),
  });
}

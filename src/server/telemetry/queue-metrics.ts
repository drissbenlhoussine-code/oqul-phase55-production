import { recordMetric } from "./runtime-metrics";

export function recordQueueLag(queue: string, lag: number) {
  recordMetric({
    name: "queue.lag",
    value: lag,
    tags: { queue },
    timestamp: Date.now(),
  });
}

export function recordWorkerFailure(queue: string) {
  recordMetric({
    name: "queue.worker.failure",
    value: 1,
    tags: { queue },
    timestamp: Date.now(),
  });
}

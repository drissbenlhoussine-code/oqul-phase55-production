export type RuntimeMetric = {
  name: string;
  value: number;
  tags?: Record<string, string>;
  timestamp: number;
};

const metrics: RuntimeMetric[] = [];

export function recordMetric(metric: RuntimeMetric) {
  metrics.push(metric);
}

export function getMetrics() {
  return metrics;
}

export function clearMetrics() {
  metrics.length = 0;
}

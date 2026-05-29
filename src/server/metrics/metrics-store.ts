type CounterMap = Record<string, number>;

const counters: CounterMap = {};

export function incrementMetric(name: string, amount = 1) {
  counters[name] = (counters[name] ?? 0) + amount;
}

export function getMetrics() {
  return counters;
}

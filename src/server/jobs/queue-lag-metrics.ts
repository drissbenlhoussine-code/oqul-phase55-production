export type QueueLagInput = {
  waiting: number;
  active: number;
  delayed: number;
};

export function calculateQueuePressure(input: QueueLagInput) {
  return input.waiting + input.delayed + input.active;
}

export function classifyQueuePressure(input: QueueLagInput) {
  const pressure = calculateQueuePressure(input);

  if (pressure > 1000) return "critical";
  if (pressure > 250) return "high";
  if (pressure > 50) return "moderate";
  return "normal";
}

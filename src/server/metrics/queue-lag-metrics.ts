export type QueueLagSnapshot = {
  queue: string;
  lag: number;
};

export function collectQueueLagMetrics(): QueueLagSnapshot[] {
  return [
    {
      queue: "ai-runtime",
      lag: 0,
    },
  ];
}
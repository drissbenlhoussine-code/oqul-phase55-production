export type QueueHealthSnapshot = {
  queueName: string;
  waiting: number;
  active: number;
  failed: number;
  delayed: number;
  timestamp: string;
};

export function createQueueHealthSnapshot(
  queueName: string,
  values?: Partial<Omit<QueueHealthSnapshot, "queueName" | "timestamp">>
): QueueHealthSnapshot {
  return {
    queueName,
    waiting: values?.waiting ?? 0,
    active: values?.active ?? 0,
    failed: values?.failed ?? 0,
    delayed: values?.delayed ?? 0,
    timestamp: new Date().toISOString(),
  };
}

export function isQueueLagging(snapshot: QueueHealthSnapshot, threshold = 100) {
  return snapshot.waiting + snapshot.delayed > threshold;
}

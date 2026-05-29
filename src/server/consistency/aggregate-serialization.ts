import { acquireAggregateLock } from "./aggregate-locks";

export async function withAggregateSerialization<T>(input: {
  aggregateId: string;
  ownerId: string;
  ttlMs: number;
  operation: () => Promise<T>;
}) {
  const lock = await acquireAggregateLock({
    aggregateId: input.aggregateId,
    ownerId: input.ownerId,
    ttlMs: input.ttlMs,
  });

  if (!lock.acquired) {
    throw new Error(`Aggregate ${input.aggregateId} is already locked.`);
  }

  return input.operation();
}

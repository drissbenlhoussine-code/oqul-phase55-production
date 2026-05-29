import { recordEffectOnce } from "./effect-receipts";
import { advanceConsumerOffset, getConsumerOffset } from "./consumer-offsets";

export async function applyOrderedEffectOnce(input: {
  consumerName: string;
  eventId: string;
  eventType: string;
  aggregateId: string;
  sequence: number;
  payload: unknown;
}) {
  const currentOffset = await getConsumerOffset(input.consumerName, input.aggregateId);

  if (input.sequence <= currentOffset) {
    return {
      applied: false,
      skipped: true,
      reason: "event already behind consumer offset",
    };
  }

  const effectKey = [
    input.consumerName,
    input.eventType,
    input.aggregateId,
    input.sequence,
  ].join(":");

  const receipt = await recordEffectOnce({
    effectKey,
    eventId: input.eventId,
    effectType: input.eventType,
    aggregateId: input.aggregateId,
    payload: input.payload,
  });

  if (receipt.applied) {
    await advanceConsumerOffset({
      consumerName: input.consumerName,
      aggregateId: input.aggregateId,
      sequence: input.sequence,
    });
  }

  return {
    applied: receipt.applied,
    skipped: !receipt.applied,
    effectKey,
  };
}

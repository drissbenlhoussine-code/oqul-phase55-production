import {
  claimPendingOutboxEvents,
  markOutboxFailed,
  markOutboxProcessed,
} from "./durable-outbox";
import { acceptProcessedEventOnce } from "./durable-dedupe";

export type ReplayResult = {
  claimed: number;
  processed: number;
  duplicates: number;
  failed: number;
};

export async function replayOutboxBatch(limit = 50): Promise<ReplayResult> {
  const events = await claimPendingOutboxEvents(limit);

  const result: ReplayResult = {
    claimed: events.length,
    processed: 0,
    duplicates: 0,
    failed: 0,
  };

  for (const event of events) {
    try {
      const dedupe = await acceptProcessedEventOnce(
        `${event.event_type}:${event.aggregate_id}:${event.id}`,
        event.id
      );

      if (!dedupe.accepted) {
        result.duplicates += 1;
        await markOutboxProcessed(event.id);
        continue;
      }

      await markOutboxProcessed(event.id);
      result.processed += 1;
    } catch (error) {
      result.failed += 1;
      await markOutboxFailed(event.id, error);
    }
  }

  return result;
}

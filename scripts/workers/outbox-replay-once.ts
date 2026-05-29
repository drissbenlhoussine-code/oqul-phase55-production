import {
  claimPendingOutboxEvents,
  markOutboxFailed,
  markOutboxProcessed,
} from "@/server/consistency/durable-outbox";
import { acceptProcessedEventOnce } from "@/server/consistency/durable-dedupe";

async function main() {
  const events = await claimPendingOutboxEvents(25);

  for (const event of events) {
    try {
      const dedupe = await acceptProcessedEventOnce(
        `${event.event_type}:${event.aggregate_id}:${event.id}`,
        event.id
      );

      if (!dedupe.accepted) {
        await markOutboxProcessed(event.id);
        continue;
      }

      // Real side effect would be executed here.
      await markOutboxProcessed(event.id);
    } catch (error) {
      await markOutboxFailed(event.id, error);
    }
  }

  console.log(`[outbox] replayed ${events.length} event(s)`);
}

main().catch((error) => {
  console.error("[outbox] replay failed", error);
  process.exit(1);
});

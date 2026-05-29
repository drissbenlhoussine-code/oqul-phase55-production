import { withConsistencyTransaction } from "./enforced-transaction";
import { insertEnforcedOutboxEvent } from "./enforced-transactional-outbox";
import { hashPayload } from "./effect-receipts";

export async function applyEffectAtomically(input: {
  consumerName: string;
  eventId: string;
  eventType: string;
  aggregateId: string;
  sequence: number;
  effectKey: string;
  payload: unknown;
}) {
  return withConsistencyTransaction(async (client) => {
    const receipt = await client.query(
      `
      INSERT INTO effect_receipts (
        effect_key,
        event_id,
        effect_type,
        aggregate_id,
        payload_hash
      )
      VALUES ($1, $2, $3, $4, $5)
      ON CONFLICT (effect_key) DO NOTHING
      RETURNING effect_key
      `,
      [
        input.effectKey,
        input.eventId,
        input.eventType,
        input.aggregateId,
        hashPayload(input.payload),
      ]
    );

    if (receipt.rowCount === 0) {
      return {
        applied: false,
        skipped: true,
        reason: "effect already applied",
      };
    }

    await client.query(
      `
      INSERT INTO consumer_offsets (
        consumer_name,
        aggregate_id,
        last_sequence
      )
      VALUES ($1, $2, $3)
      ON CONFLICT (consumer_name, aggregate_id)
      DO UPDATE SET
        last_sequence = GREATEST(consumer_offsets.last_sequence, EXCLUDED.last_sequence),
        updated_at = NOW()
      `,
      [input.consumerName, input.aggregateId, input.sequence]
    );

    await insertEnforcedOutboxEvent(client, {
      eventType: `${input.eventType}.applied`,
      aggregateId: input.aggregateId,
      payload: {
        eventId: input.eventId,
        sequence: input.sequence,
        effectKey: input.effectKey,
      },
    });

    return {
      applied: true,
      skipped: false,
    };
  });
}

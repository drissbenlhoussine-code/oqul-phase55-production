import { randomUUID } from "node:crypto";
import type { PoolClient } from "pg";

export async function insertOutboxEventInTransaction(
  client: PoolClient,
  input: {
    id?: string;
    eventType: string;
    aggregateId: string;
    payload: unknown;
  }
) {
  const id = input.id ?? randomUUID();

  await client.query(
    `
    INSERT INTO outbox_events (id, event_type, aggregate_id, payload, status)
    VALUES ($1, $2, $3, $4::jsonb, 'pending')
    ON CONFLICT (id) DO NOTHING
    `,
    [id, input.eventType, input.aggregateId, JSON.stringify(input.payload)]
  );

  return { id };
}

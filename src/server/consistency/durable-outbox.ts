import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export type DurableOutboxEvent<TPayload = unknown> = {
  id: string;
  eventType: string;
  aggregateId: string;
  payload: TPayload;
};

export async function enqueueOutboxEvent<TPayload>(
  input: Omit<DurableOutboxEvent<TPayload>, "id"> & { id?: string }
) {
  const pool = getPostgresPool();
  const id = input.id ?? randomUUID();

  await pool.query(
    `
    INSERT INTO outbox_events (id, event_type, aggregate_id, payload, status)
    VALUES ($1, $2, $3, $4::jsonb, 'pending')
    ON CONFLICT (id) DO NOTHING
    `,
    [id, input.eventType, input.aggregateId, JSON.stringify(input.payload)]
  );

  return {
    id,
    eventType: input.eventType,
    aggregateId: input.aggregateId,
    payload: input.payload,
  };
}

export async function claimPendingOutboxEvents(limit = 10) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    UPDATE outbox_events
    SET status = 'processing', locked_at = NOW(), attempts = attempts + 1
    WHERE id IN (
      SELECT id
      FROM outbox_events
      WHERE status = 'pending'
      ORDER BY created_at ASC
      LIMIT $1
      FOR UPDATE SKIP LOCKED
    )
    RETURNING *
    `,
    [limit]
  );

  return result.rows;
}

export async function markOutboxProcessed(id: string) {
  const pool = getPostgresPool();

  await pool.query(
    `
    UPDATE outbox_events
    SET status = 'processed', processed_at = NOW()
    WHERE id = $1
    `,
    [id]
  );
}

export async function markOutboxFailed(id: string, error: unknown) {
  const pool = getPostgresPool();

  await pool.query(
    `
    UPDATE outbox_events
    SET status = 'pending', last_error = $2
    WHERE id = $1
    `,
    [id, error instanceof Error ? error.message : String(error)]
  );
}

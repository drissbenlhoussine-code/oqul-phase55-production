import { getPostgresPool } from "@/server/db/postgres";

export async function acceptProcessedEventOnce(
  idempotencyKey: string,
  eventId: string
) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    INSERT INTO processed_events (idempotency_key, event_id)
    VALUES ($1, $2)
    ON CONFLICT (idempotency_key) DO NOTHING
    RETURNING idempotency_key
    `,
    [idempotencyKey, eventId]
  );

  return {
    accepted: result.rowCount === 1,
    idempotencyKey,
    eventId,
  };
}

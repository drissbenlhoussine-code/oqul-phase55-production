import { getPostgresPool } from "@/server/db/postgres";

export async function getConsumerOffset(consumerName: string, aggregateId: string) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    SELECT last_sequence
    FROM consumer_offsets
    WHERE consumer_name = $1 AND aggregate_id = $2
    `,
    [consumerName, aggregateId]
  );

  if (result.rowCount === 0) {
    return 0;
  }

  return Number(result.rows[0].last_sequence);
}

export async function advanceConsumerOffset(input: {
  consumerName: string;
  aggregateId: string;
  sequence: number;
}) {
  const pool = getPostgresPool();

  await pool.query(
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
}

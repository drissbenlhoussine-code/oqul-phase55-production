import { getPostgresPool } from "@/server/db/postgres";

export async function acquireAggregateLock(input: {
  aggregateId: string;
  ownerId: string;
  ttlMs: number;
}) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    INSERT INTO aggregate_locks (
      aggregate_id,
      owner_id,
      fencing_token,
      expires_at
    )
    VALUES ($1, $2, 1, NOW() + ($3 || ' milliseconds')::interval)
    ON CONFLICT (aggregate_id)
    DO UPDATE SET
      owner_id = EXCLUDED.owner_id,
      fencing_token = aggregate_locks.fencing_token + 1,
      expires_at = EXCLUDED.expires_at,
      updated_at = NOW()
    WHERE aggregate_locks.expires_at < NOW()
       OR aggregate_locks.owner_id = EXCLUDED.owner_id
    RETURNING fencing_token
    `,
    [input.aggregateId, input.ownerId, input.ttlMs]
  );

  return {
    acquired: result.rowCount === 1,
    aggregateId: input.aggregateId,
    ownerId: input.ownerId,
    fencingToken: result.rows[0]?.fencing_token
      ? Number(result.rows[0].fencing_token)
      : undefined,
  };
}

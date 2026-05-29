import { getPostgresPool } from "@/server/db/postgres";

export async function renewConsumerLease(input: {
  leaseKey: string;
  ownerId: string;
  fencingToken: number;
  ttlMs: number;
}) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    UPDATE consumer_leases
    SET expires_at = NOW() + ($4 || ' milliseconds')::interval,
        heartbeat_at = NOW(),
        updated_at = NOW()
    WHERE lease_key = $1
      AND owner_id = $2
      AND fencing_token = $3
      AND expires_at > NOW()
    RETURNING lease_key
    `,
    [input.leaseKey, input.ownerId, input.fencingToken, input.ttlMs]
  );

  return {
    renewed: result.rowCount === 1,
    leaseKey: input.leaseKey,
  };
}

export async function rejectIfLeaseStale(input: {
  leaseKey: string;
  ownerId: string;
  fencingToken: number;
}) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    SELECT lease_key
    FROM consumer_leases
    WHERE lease_key = $1
      AND owner_id = $2
      AND fencing_token = $3
      AND expires_at > NOW()
    `,
    [input.leaseKey, input.ownerId, input.fencingToken]
  );

  if (result.rowCount !== 1) {
    throw new Error("Stale lease rejected before effect execution.");
  }
}

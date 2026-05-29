import { getPostgresPool } from "@/server/db/postgres";

export type LeaseResult = {
  acquired: boolean;
  leaseKey: string;
  ownerId: string;
  fencingToken?: number;
};

export async function acquireConsumerLease(input: {
  leaseKey: string;
  ownerId: string;
  ttlMs: number;
}): Promise<LeaseResult> {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    INSERT INTO consumer_leases (
      lease_key,
      owner_id,
      fencing_token,
      expires_at
    )
    VALUES ($1, $2, 1, NOW() + ($3 || ' milliseconds')::interval)
    ON CONFLICT (lease_key)
    DO UPDATE SET
      owner_id = EXCLUDED.owner_id,
      fencing_token = consumer_leases.fencing_token + 1,
      expires_at = EXCLUDED.expires_at,
      updated_at = NOW()
    WHERE consumer_leases.expires_at < NOW()
       OR consumer_leases.owner_id = EXCLUDED.owner_id
    RETURNING fencing_token
    `,
    [input.leaseKey, input.ownerId, input.ttlMs]
  );

  return {
    acquired: result.rowCount === 1,
    leaseKey: input.leaseKey,
    ownerId: input.ownerId,
    fencingToken: result.rows[0]?.fencing_token
      ? Number(result.rows[0].fencing_token)
      : undefined,
  };
}

export async function validateConsumerLease(input: {
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

  return result.rowCount === 1;
}

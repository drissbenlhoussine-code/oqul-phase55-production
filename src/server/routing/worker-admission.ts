import { getPostgresPool } from "@/server/db/postgres";

export async function admitWorker(input: {
  workerId: string;
  workerShard: string;
  ownerId: string;
  fencingToken: number;
  ttlMs: number;
}) {
  const pool = getPostgresPool();

  await pool.query(
    `
    INSERT INTO worker_admissions (
      worker_id,
      worker_shard,
      owner_id,
      fencing_token,
      expires_at
    )
    VALUES ($1, $2, $3, $4, NOW() + ($5 || ' milliseconds')::interval)
    ON CONFLICT (worker_id)
    DO UPDATE SET
      worker_shard = EXCLUDED.worker_shard,
      owner_id = EXCLUDED.owner_id,
      fencing_token = EXCLUDED.fencing_token,
      expires_at = EXCLUDED.expires_at,
      revoked_at = NULL
    `,
    [input.workerId, input.workerShard, input.ownerId, input.fencingToken, input.ttlMs]
  );
}

export async function assertWorkerAdmission(input: {
  workerId: string;
  workerShard: string;
  ownerId: string;
  fencingToken: number;
}) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    SELECT worker_id
    FROM worker_admissions
    WHERE worker_id = $1
      AND worker_shard = $2
      AND owner_id = $3
      AND fencing_token = $4
      AND expires_at > NOW()
      AND revoked_at IS NULL
    `,
    [input.workerId, input.workerShard, input.ownerId, input.fencingToken]
  );

  if (result.rowCount !== 1) {
    throw new Error("Worker admission rejected.");
  }

  return true;
}

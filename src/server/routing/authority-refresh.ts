import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";
import { assertWorkerAdmission } from "./worker-admission";

export async function refreshWorkerAuthority(input: {
  workerId: string;
  workerShard: string;
  ownerId: string;
  fencingToken: number;
  routeVersion?: number;
  ttlMs: number;
}) {
  await assertWorkerAdmission({
    workerId: input.workerId,
    workerShard: input.workerShard,
    ownerId: input.ownerId,
    fencingToken: input.fencingToken,
  });

  const pool = getPostgresPool();
  const id = randomUUID();

  await pool.query(
    `
    INSERT INTO authority_refresh_events (
      id,
      worker_id,
      worker_shard,
      owner_id,
      fencing_token,
      route_version,
      valid_until
    )
    VALUES ($1, $2, $3, $4, $5, $6, NOW() + ($7 || ' milliseconds')::interval)
    `,
    [
      id,
      input.workerId,
      input.workerShard,
      input.ownerId,
      input.fencingToken,
      input.routeVersion ?? null,
      input.ttlMs,
    ]
  );

  return { id };
}

export async function assertRuntimeAuthorityFresh(input: {
  workerId: string;
  workerShard: string;
  ownerId: string;
  fencingToken: number;
  routeVersion?: number;
}) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    SELECT id
    FROM authority_refresh_events
    WHERE worker_id = $1
      AND worker_shard = $2
      AND owner_id = $3
      AND fencing_token = $4
      AND ($5::bigint IS NULL OR route_version = $5)
      AND valid_until > NOW()
    ORDER BY refreshed_at DESC
    LIMIT 1
    `,
    [
      input.workerId,
      input.workerShard,
      input.ownerId,
      input.fencingToken,
      input.routeVersion ?? null,
    ]
  );

  if (result.rowCount !== 1) {
    throw new Error("Runtime authority is stale or revoked.");
  }

  return true;
}

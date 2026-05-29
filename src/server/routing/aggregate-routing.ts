import { createHash } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export function resolveAggregateShard(aggregateId: string, shardCount: number) {
  const hash = createHash("sha256").update(aggregateId).digest("hex");
  const value = Number.parseInt(hash.slice(0, 8), 16);
  return `shard-${value % shardCount}`;
}

export async function assignAggregateRoute(input: {
  aggregateId: string;
  shardCount: number;
  ownerId?: string;
  fencingToken?: number;
}) {
  const pool = getPostgresPool();
  const workerShard = resolveAggregateShard(input.aggregateId, input.shardCount);

  await pool.query(
    `
    INSERT INTO aggregate_routes (
      aggregate_id,
      worker_shard,
      owner_id,
      fencing_token
    )
    VALUES ($1, $2, $3, $4)
    ON CONFLICT (aggregate_id)
    DO UPDATE SET
      worker_shard = EXCLUDED.worker_shard,
      owner_id = EXCLUDED.owner_id,
      fencing_token = EXCLUDED.fencing_token,
      updated_at = NOW()
    `,
    [
      input.aggregateId,
      workerShard,
      input.ownerId ?? null,
      input.fencingToken ?? null,
    ]
  );

  return {
    aggregateId: input.aggregateId,
    workerShard,
  };
}

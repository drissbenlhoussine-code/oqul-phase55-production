import { getPostgresPool } from "@/server/db/postgres";
import { resolveAggregateShard } from "./aggregate-routing";

export async function assertWorkerOwnsAggregateRoute(input: {
  aggregateId: string;
  workerShard: string;
  ownerId?: string;
  fencingToken?: number;
}) {
  const pool = getPostgresPool();

  const expectedShard = resolveAggregateShard(
    input.aggregateId,
    Number(process.env.ROUTING_SHARD_COUNT ?? 8)
  );

  if (expectedShard !== input.workerShard) {
    throw new Error(
      `Routing invariant violated: aggregate ${input.aggregateId} belongs to ${expectedShard}, not ${input.workerShard}.`
    );
  }

  const result = await pool.query(
    `
    SELECT aggregate_id
    FROM aggregate_routes
    WHERE aggregate_id = $1
      AND worker_shard = $2
      AND active = TRUE
      AND ($3::text IS NULL OR owner_id = $3)
      AND ($4::bigint IS NULL OR fencing_token = $4)
    `,
    [
      input.aggregateId,
      input.workerShard,
      input.ownerId ?? null,
      input.fencingToken ?? null,
    ]
  );

  if (result.rowCount !== 1) {
    throw new Error(
      `Routing ownership rejected for aggregate ${input.aggregateId}.`
    );
  }

  return true;
}

import { getPostgresPool } from "@/server/db/postgres";

export async function assertRouteVersionFresh(input: {
  aggregateId: string;
  routeVersion: number;
  workerShard: string;
}) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    SELECT aggregate_id
    FROM aggregate_routes
    WHERE aggregate_id = $1
      AND route_version = $2
      AND worker_shard = $3
      AND active = TRUE
    `,
    [input.aggregateId, input.routeVersion, input.workerShard]
  );

  if (result.rowCount !== 1) {
    throw new Error("Stale route version rejected.");
  }

  return true;
}

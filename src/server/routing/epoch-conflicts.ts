import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export async function detectRouteEpochConflict(input: {
  aggregateId: string;
  expectedRouteVersion: number;
  workerId?: string;
}) {
  const pool = getPostgresPool();

  const route = await pool.query(
    "SELECT route_version FROM aggregate_routes WHERE aggregate_id = $1 AND active = TRUE",
    [input.aggregateId]
  );

  const actual = Number(route.rows[0]?.route_version ?? 0);

  if (actual === input.expectedRouteVersion) {
    return {
      conflict: false,
      actualRouteVersion: actual,
    };
  }

  const conflictId = randomUUID();

  await pool.query(
    `
    INSERT INTO route_epoch_conflicts (
      conflict_id,
      aggregate_id,
      expected_route_version,
      actual_route_version,
      worker_id
    )
    VALUES ($1, $2, $3, $4, $5)
    `,
    [
      conflictId,
      input.aggregateId,
      input.expectedRouteVersion,
      actual,
      input.workerId ?? null,
    ]
  );

  return {
    conflict: true,
    conflictId,
    actualRouteVersion: actual,
  };
}

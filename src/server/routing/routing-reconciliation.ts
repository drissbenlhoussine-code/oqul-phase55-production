import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";
import { resolveAggregateShard } from "./aggregate-routing";

export async function reconcileAggregateRoutes(shardCount = 8) {
  const pool = getPostgresPool();
  const runId = randomUUID();

  await pool.query(
    "INSERT INTO routing_reconciliation_runs (id, status) VALUES ($1, 'running')",
    [runId]
  );

  try {
    const routes = await pool.query(
      "SELECT aggregate_id, worker_shard FROM aggregate_routes WHERE active = TRUE"
    );

    let repaired = 0;

    for (const route of routes.rows) {
      const expected = resolveAggregateShard(route.aggregate_id, shardCount);

      if (route.worker_shard !== expected) {
        await pool.query(
          `
          UPDATE aggregate_routes
          SET worker_shard = $2,
              route_version = route_version + 1,
              updated_at = NOW()
          WHERE aggregate_id = $1
          `,
          [route.aggregate_id, expected]
        );
        repaired += 1;
      }
    }

    await pool.query(
      `
      UPDATE routing_reconciliation_runs
      SET status = 'completed',
          checked_routes = $2,
          repaired_routes = $3,
          finished_at = NOW()
      WHERE id = $1
      `,
      [runId, routes.rowCount ?? 0, repaired]
    );

    return {
      runId,
      checked: routes.rowCount ?? 0,
      repaired,
    };
  } catch (error) {
    await pool.query(
      `
      UPDATE routing_reconciliation_runs
      SET status = 'failed',
          finished_at = NOW(),
          last_error = $2
      WHERE id = $1
      `,
      [runId, error instanceof Error ? error.message : String(error)]
    );
    throw error;
  }
}

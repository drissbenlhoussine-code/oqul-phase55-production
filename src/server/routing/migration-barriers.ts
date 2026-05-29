import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export async function createMigrationBarrier(input: {
  aggregateId: string;
  routeVersion: number;
}) {
  const pool = getPostgresPool();
  const barrierId = randomUUID();

  await pool.query(
    `
    INSERT INTO migration_barriers (
      barrier_id,
      aggregate_id,
      route_version,
      status
    )
    VALUES ($1, $2, $3, 'active')
    `,
    [barrierId, input.aggregateId, input.routeVersion]
  );

  return { barrierId };
}

export async function assertNoActiveMigrationBarrier(input: {
  aggregateId: string;
  routeVersion: number;
}) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    SELECT barrier_id
    FROM migration_barriers
    WHERE aggregate_id = $1
      AND route_version = $2
      AND status = 'active'
    `,
    [input.aggregateId, input.routeVersion]
  );

  if ((result.rowCount ?? 0) > 0) {
    throw new Error("Execution blocked by active migration barrier.");
  }

  return true;
}

export async function releaseMigrationBarrier(barrierId: string) {
  const pool = getPostgresPool();

  await pool.query(
    `
    UPDATE migration_barriers
    SET status = 'released',
        released_at = NOW()
    WHERE barrier_id = $1
    `,
    [barrierId]
  );
}

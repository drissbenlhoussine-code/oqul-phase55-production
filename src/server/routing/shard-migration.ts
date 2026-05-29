import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export async function planShardMigration(input: {
  aggregateId: string;
  fromShard: string;
  toShard: string;
  fencingToken: number;
}) {
  const pool = getPostgresPool();
  const id = randomUUID();

  await pool.query(
    `
    INSERT INTO shard_migrations (
      id,
      aggregate_id,
      from_shard,
      to_shard,
      status,
      fencing_token
    )
    VALUES ($1, $2, $3, $4, 'planned', $5)
    `,
    [id, input.aggregateId, input.fromShard, input.toShard, input.fencingToken]
  );

  return { id };
}

export async function completeShardMigration(input: {
  migrationId: string;
}) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    UPDATE shard_migrations
    SET status = 'completed',
        completed_at = NOW()
    WHERE id = $1
      AND status = 'planned'
    RETURNING aggregate_id, to_shard, fencing_token
    `,
    [input.migrationId]
  );

  const migration = result.rows[0];

  if (!migration) {
    throw new Error("Shard migration not found or already completed.");
  }

  await pool.query(
    `
    UPDATE aggregate_routes
    SET worker_shard = $2,
        fencing_token = $3,
        route_version = route_version + 1,
        updated_at = NOW()
    WHERE aggregate_id = $1
    `,
    [migration.aggregate_id, migration.to_shard, migration.fencing_token]
  );

  return {
    aggregateId: migration.aggregate_id,
    toShard: migration.to_shard,
  };
}

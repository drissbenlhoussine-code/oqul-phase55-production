import {
  completeShardMigration,
  planShardMigration,
} from "@/server/routing/shard-migration";

async function main() {
  const aggregateId = process.env.AGGREGATE_ID;
  const fromShard = process.env.FROM_SHARD;
  const toShard = process.env.TO_SHARD;
  const fencingToken = Number(process.env.FENCING_TOKEN ?? 1);

  if (!aggregateId || !fromShard || !toShard) {
    throw new Error("AGGREGATE_ID, FROM_SHARD, and TO_SHARD are required");
  }

  const migration = await planShardMigration({
    aggregateId,
    fromShard,
    toShard,
    fencingToken,
  });

  const result = await completeShardMigration({
    migrationId: migration.id,
  });

  console.log("[routing] migration completed", result);
}

main().catch((error) => {
  console.error("[routing] shard migration failed", error);
  process.exit(1);
});

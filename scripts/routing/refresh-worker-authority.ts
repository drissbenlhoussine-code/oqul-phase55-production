import { refreshWorkerAuthority } from "@/server/routing/authority-refresh";

async function main() {
  const workerId = process.env.WORKER_ID;
  const workerShard = process.env.WORKER_SHARD;
  const ownerId = process.env.OWNER_ID;
  const fencingToken = Number(process.env.FENCING_TOKEN);
  const routeVersion = process.env.ROUTE_VERSION
    ? Number(process.env.ROUTE_VERSION)
    : undefined;

  if (!workerId || !workerShard || !ownerId || !fencingToken) {
    throw new Error("WORKER_ID, WORKER_SHARD, OWNER_ID, and FENCING_TOKEN are required");
  }

  const result = await refreshWorkerAuthority({
    workerId,
    workerShard,
    ownerId,
    fencingToken,
    routeVersion,
    ttlMs: 30_000,
  });

  console.log("[authority] refreshed", result);
}

main().catch((error) => {
  console.error("[authority] refresh failed", error);
  process.exit(1);
});

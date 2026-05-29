import { reconcileAggregateRoutes } from "@/server/routing/routing-reconciliation";

async function main() {
  const result = await reconcileAggregateRoutes(
    Number(process.env.ROUTING_SHARD_COUNT ?? 8)
  );

  console.log("[routing] reconciliation", result);
}

main().catch((error) => {
  console.error("[routing] reconciliation failed", error);
  process.exit(1);
});

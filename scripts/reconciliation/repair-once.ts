import { repairMissingEffectReceipts } from "@/server/consistency/reconciliation-repair";

async function main() {
  const result = await repairMissingEffectReceipts(100);
  console.log("[reconciliation-repair]", result);
}

main().catch((error) => {
  console.error("[reconciliation-repair] failed", error);
  process.exit(1);
});

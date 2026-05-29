import { detectMissingEffectReceipts } from "@/server/consistency/reconciliation";

async function main() {
  const result = await detectMissingEffectReceipts(100);
  console.log("[reconciliation]", result);
}

main().catch((error) => {
  console.error("[reconciliation] failed", error);
  process.exit(1);
});

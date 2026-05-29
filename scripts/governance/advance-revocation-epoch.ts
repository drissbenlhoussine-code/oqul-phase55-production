import { advanceRevocationEpoch } from "@/server/governance/revocation-epochs";

async function main() {
  const reason = process.env.REASON ?? "manual epoch advance";
  const advancedBy = process.env.ADVANCED_BY ?? "operator";

  const result = await advanceRevocationEpoch({
    reason,
    advancedBy,
  });

  console.log("[governance] revocation epoch advanced", result);
}

main().catch((error) => {
  console.error("[governance] epoch advance failed", error);
  process.exit(1);
});

import { approveQuarantinedEffect } from "@/server/effects/quarantine-recovery";

async function main() {
  const effectKey = process.env.EFFECT_KEY;
  const operatorId = process.env.OPERATOR_ID ?? "system";
  const reason = process.env.REASON ?? "manual recovery";

  if (!effectKey) {
    throw new Error("EFFECT_KEY is required");
  }

  await approveQuarantinedEffect({
    effectKey,
    operatorId,
    reason,
  });

  console.log("[quarantine] approved retry", { effectKey, operatorId });
}

main().catch((error) => {
  console.error("[quarantine] recovery failed", error);
  process.exit(1);
});

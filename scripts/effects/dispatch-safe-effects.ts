import { runReplaySafeExternalEffectBatch } from "@/server/effects/safe-effect-runner";

async function main() {
  const result = await runReplaySafeExternalEffectBatch(async (effect) => {
    console.log("[safe-effect] deliver", effect);
    return {
      providerMessageId: `mock-${Date.now()}`,
      rawAck: { ok: true },
    };
  });

  console.log("[safe-effect] result", result);
}

main().catch((error) => {
  console.error("[safe-effect] failed", error);
  process.exit(1);
});

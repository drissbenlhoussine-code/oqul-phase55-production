import { runExternalEffectBatch } from "@/server/effects/external-effect-runner";

async function main() {
  const result = await runExternalEffectBatch(async (effect) => {
    console.log("[external-effect] delivering", effect.integration, effect.effectKey);
  });

  console.log("[external-effect] result", result);
}

main().catch((error) => {
  console.error("[external-effect] replay failed", error);
  process.exit(1);
});

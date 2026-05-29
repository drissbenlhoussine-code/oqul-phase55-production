import { processRevocationEvents } from "@/server/governance/reactive-revocation";

async function main() {
  const consumerId = process.env.CONSUMER_ID ?? "authority-consumer";
  const result = await processRevocationEvents(consumerId);
  console.log("[governance] processed", result);
}

main().catch((error) => {
  console.error("[governance] processing failed", error);
  process.exit(1);
});

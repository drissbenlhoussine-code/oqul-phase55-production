import { validateRecursiveTrustChain } from "@/server/trust/recursive-trust-chain";

async function main() {
  const integration = process.env.INTEGRATION;
  const requestedScope = process.env.SCOPE;
  const childKeyId = process.env.CHILD_KEY_ID;

  if (!integration || !requestedScope || !childKeyId) {
    throw new Error("INTEGRATION, SCOPE, and CHILD_KEY_ID are required");
  }

  const result = await validateRecursiveTrustChain({
    integration,
    requestedScope,
    childKeyId,
  });

  console.log("[trust-chain]", result);
}

main().catch((error) => {
  console.error("[trust-chain] validation failed", error);
  process.exit(1);
});

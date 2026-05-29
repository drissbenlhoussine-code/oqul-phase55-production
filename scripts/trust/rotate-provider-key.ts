import { generateEd25519ProviderKeyPair } from "@/server/trust/asymmetric-provider-trust";
import { registerProviderPublicKey } from "@/server/trust/provider-key-governance";

async function main() {
  const integration = process.env.INTEGRATION;

  if (!integration) {
    throw new Error("INTEGRATION is required");
  }

  const keys = generateEd25519ProviderKeyPair();
  const result = await registerProviderPublicKey({
    integration,
    publicKey: keys.publicKey,
  });

  console.log("[trust] registered provider public key", {
    integration,
    keyId: result.keyId,
    publicKey: keys.publicKey,
  });

  console.log("[trust] private key must be stored by provider only");
  console.log(keys.privateKey);
}

main().catch((error) => {
  console.error("[trust] key rotation failed", error);
  process.exit(1);
});

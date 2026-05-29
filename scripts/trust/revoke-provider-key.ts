import { revokeProviderPublicKey } from "@/server/trust/provider-key-governance";

async function main() {
  const keyId = process.env.KEY_ID;

  if (!keyId) {
    throw new Error("KEY_ID is required");
  }

  await revokeProviderPublicKey(keyId);
  console.log("[trust] revoked provider key", { keyId });
}

main().catch((error) => {
  console.error("[trust] key revocation failed", error);
  process.exit(1);
});

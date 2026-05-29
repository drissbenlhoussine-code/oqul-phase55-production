import { getActiveDelegatedAuthority } from "./delegated-authorities";
import { verifyProviderReceiptAsymmetric } from "./asymmetric-provider-trust";

export async function verifyScopedProviderSignature(input: {
  integration: string;
  scope: string;
  childKeyId: string;
  deliveryId: string;
  providerMessageId: string;
  signature: string;
}) {
  const delegated = await getActiveDelegatedAuthority({
    integration: input.integration,
    scope: input.scope,
    childKeyId: input.childKeyId,
  });

  if (!delegated) {
    return {
      verified: false,
      reason: "missing delegated authority",
    };
  }

  const verified = verifyProviderReceiptAsymmetric({
    publicKeyPem: delegated.public_key,
    deliveryId: input.deliveryId,
    providerMessageId: input.providerMessageId,
    signature: input.signature,
  });

  return {
    verified,
    reason: verified ? "verified" : "invalid scoped signature",
  };
}

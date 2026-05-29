import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";
import { verifyProviderReceiptAsymmetric } from "./asymmetric-provider-trust";
import { getActiveTrustAnchor } from "./trust-anchors";
import { registerProviderPublicKey } from "./provider-key-governance";

export function rotationPayload(input: {
  integration: string;
  oldKeyId?: string;
  newKeyId: string;
}) {
  return [
    "provider-key-rotation",
    input.integration,
    input.oldKeyId ?? "",
    input.newKeyId,
  ].join(":");
}

export async function applySignedProviderKeyRotation(input: {
  integration: string;
  oldKeyId?: string;
  newKeyId: string;
  newPublicKey: string;
  signedByAnchor: string;
  rotationSignature: string;
}) {
  const anchor = await getActiveTrustAnchor(input.signedByAnchor);

  if (!anchor) {
    return {
      applied: false,
      reason: "missing or revoked trust anchor",
    };
  }

  const verified = verifyProviderReceiptAsymmetric({
    publicKeyPem: anchor.public_key,
    deliveryId: "provider-key-rotation",
    providerMessageId: [input.integration, input.oldKeyId ?? "", input.newKeyId].join(":"),
    signature: input.rotationSignature,
  });

  if (!verified) {
    return {
      applied: false,
      reason: "invalid key rotation signature",
    };
  }

  const pool = getPostgresPool();
  const rotationId = randomUUID();

  await registerProviderPublicKey({
    integration: input.integration,
    publicKey: input.newPublicKey,
    keyId: input.newKeyId,
  });

  await pool.query(
    `
    INSERT INTO provider_key_rotations (
      rotation_id,
      integration,
      old_key_id,
      new_key_id,
      signed_by_anchor,
      rotation_signature,
      applied_at
    )
    VALUES ($1, $2, $3, $4, $5, $6, NOW())
    `,
    [
      rotationId,
      input.integration,
      input.oldKeyId ?? null,
      input.newKeyId,
      input.signedByAnchor,
      input.rotationSignature,
    ]
  );

  return {
    applied: true,
    rotationId,
  };
}

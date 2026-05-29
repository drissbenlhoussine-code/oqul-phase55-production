import { getPostgresPool } from "@/server/db/postgres";
import { getActiveProviderPublicKey } from "./provider-key-governance";
import { verifyProviderReceiptAsymmetric } from "./asymmetric-provider-trust";

export async function recordAsymmetricProviderReceipt(input: {
  keyId: string;
  integration: string;
  deliveryId: string;
  effectKey: string;
  providerMessageId: string;
  signature: string;
  rawReceipt?: unknown;
}) {
  const authority = await getActiveProviderPublicKey({
    integration: input.integration,
    keyId: input.keyId,
  });

  if (!authority) {
    return {
      recorded: false,
      verified: false,
      reason: "missing or revoked provider key",
    };
  }

  const verified = verifyProviderReceiptAsymmetric({
    publicKeyPem: authority.public_key,
    deliveryId: input.deliveryId,
    providerMessageId: input.providerMessageId,
    signature: input.signature,
  });

  if (!verified) {
    return {
      recorded: false,
      verified: false,
      reason: "invalid provider signature",
    };
  }

  const providerReceiptId = [
    input.integration,
    input.keyId,
    input.providerMessageId,
    input.deliveryId,
  ].join(":");

  const pool = getPostgresPool();

  const result = await pool.query(
    `
    INSERT INTO provider_delivery_receipts (
      provider_receipt_id,
      delivery_id,
      effect_key,
      integration,
      provider_message_id,
      provider_signature,
      verified,
      verified_at,
      raw_receipt
    )
    VALUES ($1, $2, $3, $4, $5, $6, TRUE, NOW(), $7::jsonb)
    ON CONFLICT (provider_receipt_id) DO NOTHING
    RETURNING provider_receipt_id
    `,
    [
      providerReceiptId,
      input.deliveryId,
      input.effectKey,
      input.integration,
      input.providerMessageId,
      input.signature,
      JSON.stringify(input.rawReceipt ?? {}),
    ]
  );

  return {
    recorded: result.rowCount === 1,
    verified: true,
    providerReceiptId,
  };
}

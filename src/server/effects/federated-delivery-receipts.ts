import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";
import {
  getProviderAuthority,
  verifyProviderReceiptSignature,
} from "./provider-authority";

export async function recordProviderSignedReceipt(input: {
  deliveryId: string;
  effectKey: string;
  integration: string;
  providerMessageId: string;
  providerSignature: string;
  rawReceipt?: unknown;
}) {
  const authority = await getProviderAuthority(input.integration);

  if (!authority) {
    return {
      recorded: false,
      verified: false,
      reason: "missing provider authority",
    };
  }

  const verified = verifyProviderReceiptSignature({
    deliveryId: input.deliveryId,
    providerMessageId: input.providerMessageId,
    signature: input.providerSignature,
    secret: authority.public_key,
  });

  const pool = getPostgresPool();
  const providerReceiptId = [
    input.integration,
    input.providerMessageId,
    input.deliveryId,
  ].join(":");

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
    VALUES ($1, $2, $3, $4, $5, $6, $7, CASE WHEN $7 THEN NOW() ELSE NULL END, $8::jsonb)
    ON CONFLICT (provider_receipt_id) DO NOTHING
    RETURNING provider_receipt_id
    `,
    [
      providerReceiptId,
      input.deliveryId,
      input.effectKey,
      input.integration,
      input.providerMessageId,
      input.providerSignature,
      verified,
      JSON.stringify(input.rawReceipt ?? {}),
    ]
  );

  return {
    recorded: result.rowCount === 1,
    verified,
    providerReceiptId,
  };
}

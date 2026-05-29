import { getPostgresPool } from "@/server/db/postgres";
import {
  createDeterministicDeliveryId,
  createProviderIdempotencyKey,
  signDeliveryReceipt,
  verifyDeliveryReceiptSignature,
} from "./delivery-identity";

export async function recordAuthoritativeDeliveryReceipt(input: {
  effectKey: string;
  integration: string;
  aggregateId: string;
  providerMessageId?: string;
  rawReceipt?: unknown;
  secret?: string;
}) {
  const secret = input.secret ?? process.env.DELIVERY_RECEIPT_SECRET ?? "development-delivery-secret";
  const deliveryId = createDeterministicDeliveryId({
    integration: input.integration,
    aggregateId: input.aggregateId,
    effectKey: input.effectKey,
  });

  const idempotencyKey = createProviderIdempotencyKey({
    integration: input.integration,
    deliveryId,
  });

  const receiptSignature = signDeliveryReceipt({
    deliveryId,
    providerMessageId: input.providerMessageId,
    secret,
  });

  const pool = getPostgresPool();

  const result = await pool.query(
    `
    INSERT INTO authoritative_delivery_receipts (
      delivery_id,
      effect_key,
      integration,
      aggregate_id,
      provider_message_id,
      idempotency_key,
      receipt_signature,
      raw_receipt
    )
    VALUES ($1, $2, $3, $4, $5, $6, $7, $8::jsonb)
    ON CONFLICT (delivery_id) DO NOTHING
    RETURNING delivery_id
    `,
    [
      deliveryId,
      input.effectKey,
      input.integration,
      input.aggregateId,
      input.providerMessageId ?? null,
      idempotencyKey,
      receiptSignature,
      JSON.stringify(input.rawReceipt ?? {}),
    ]
  );

  return {
    recorded: result.rowCount === 1,
    deliveryId,
    idempotencyKey,
    receiptSignature,
  };
}

export function verifyAuthoritativeDeliveryReceipt(input: {
  deliveryId: string;
  providerMessageId?: string;
  signature: string;
  secret?: string;
}) {
  return verifyDeliveryReceiptSignature({
    deliveryId: input.deliveryId,
    providerMessageId: input.providerMessageId,
    secret: input.secret ?? process.env.DELIVERY_RECEIPT_SECRET ?? "development-delivery-secret",
    signature: input.signature,
  });
}

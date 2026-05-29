import { createHash, createHmac } from "node:crypto";

export function createDeterministicDeliveryId(input: {
  integration: string;
  aggregateId: string;
  effectKey: string;
}) {
  return createHash("sha256")
    .update([input.integration, input.aggregateId, input.effectKey].join(":"))
    .digest("hex");
}

export function createProviderIdempotencyKey(input: {
  integration: string;
  deliveryId: string;
}) {
  return `${input.integration}:${input.deliveryId}`;
}

export function signDeliveryReceipt(input: {
  deliveryId: string;
  providerMessageId?: string;
  secret: string;
}) {
  return createHmac("sha256", input.secret)
    .update([input.deliveryId, input.providerMessageId ?? ""].join(":"))
    .digest("hex");
}

export function verifyDeliveryReceiptSignature(input: {
  deliveryId: string;
  providerMessageId?: string;
  secret: string;
  signature: string;
}) {
  return (
    signDeliveryReceipt({
      deliveryId: input.deliveryId,
      providerMessageId: input.providerMessageId,
      secret: input.secret,
    }) === input.signature
  );
}

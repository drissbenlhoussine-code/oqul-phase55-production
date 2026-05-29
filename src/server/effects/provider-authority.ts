import { createHmac, timingSafeEqual } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export function signProviderReceipt(input: {
  deliveryId: string;
  providerMessageId: string;
  secret: string;
}) {
  return createHmac("sha256", input.secret)
    .update([input.deliveryId, input.providerMessageId].join(":"))
    .digest("hex");
}

export function verifyProviderReceiptSignature(input: {
  deliveryId: string;
  providerMessageId: string;
  signature: string;
  secret: string;
}) {
  const expected = Buffer.from(
    signProviderReceipt({
      deliveryId: input.deliveryId,
      providerMessageId: input.providerMessageId,
      secret: input.secret,
    }),
    "hex"
  );

  const actual = Buffer.from(input.signature, "hex");

  if (expected.length !== actual.length) {
    return false;
  }

  return timingSafeEqual(expected, actual);
}

export async function upsertProviderAuthority(input: {
  integration: string;
  publicKey: string;
  algorithm?: string;
}) {
  const pool = getPostgresPool();

  await pool.query(
    `
    INSERT INTO provider_authorities (
      integration,
      public_key,
      algorithm,
      active
    )
    VALUES ($1, $2, $3, TRUE)
    ON CONFLICT (integration)
    DO UPDATE SET
      public_key = EXCLUDED.public_key,
      algorithm = EXCLUDED.algorithm,
      active = TRUE,
      updated_at = NOW()
    `,
    [input.integration, input.publicKey, input.algorithm ?? "hmac-sha256"]
  );
}

export async function getProviderAuthority(integration: string) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    SELECT public_key, algorithm
    FROM provider_authorities
    WHERE integration = $1 AND active = TRUE
    `,
    [integration]
  );

  return result.rows[0] as
    | { public_key: string; algorithm: string }
    | undefined;
}

import { createHash } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export function hashPayload(payload: unknown) {
  return createHash("sha256")
    .update(JSON.stringify(payload))
    .digest("hex");
}

export async function recordEffectOnce(input: {
  effectKey: string;
  eventId: string;
  effectType: string;
  aggregateId: string;
  payload: unknown;
}) {
  const pool = getPostgresPool();
  const payloadHash = hashPayload(input.payload);

  const result = await pool.query(
    `
    INSERT INTO effect_receipts (
      effect_key,
      event_id,
      effect_type,
      aggregate_id,
      payload_hash
    )
    VALUES ($1, $2, $3, $4, $5)
    ON CONFLICT (effect_key) DO NOTHING
    RETURNING effect_key
    `,
    [
      input.effectKey,
      input.eventId,
      input.effectType,
      input.aggregateId,
      payloadHash,
    ]
  );

  return {
    applied: result.rowCount === 1,
    effectKey: input.effectKey,
    payloadHash,
  };
}

export async function hasEffectReceipt(effectKey: string) {
  const pool = getPostgresPool();

  const result = await pool.query(
    "SELECT effect_key FROM effect_receipts WHERE effect_key = $1",
    [effectKey]
  );

  return result.rowCount === 1;
}

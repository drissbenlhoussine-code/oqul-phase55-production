import { getPostgresPool } from "@/server/db/postgres";

export async function recordExternalEffectAck(input: {
  effectKey: string;
  integration: string;
  providerMessageId?: string;
  fencingToken: number;
  rawAck?: unknown;
}) {
  const pool = getPostgresPool();
  const ackKey = [
    input.integration,
    input.providerMessageId ?? input.effectKey,
    input.fencingToken,
  ].join(":");

  const result = await pool.query(
    `
    INSERT INTO external_effect_acks (
      ack_key,
      effect_key,
      integration,
      provider_message_id,
      fencing_token,
      raw_ack
    )
    VALUES ($1, $2, $3, $4, $5, $6::jsonb)
    ON CONFLICT (ack_key) DO NOTHING
    RETURNING ack_key
    `,
    [
      ackKey,
      input.effectKey,
      input.integration,
      input.providerMessageId ?? null,
      input.fencingToken,
      JSON.stringify(input.rawAck ?? {}),
    ]
  );

  return {
    acknowledged: result.rowCount === 1,
    ackKey,
  };
}

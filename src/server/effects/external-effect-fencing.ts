import { getPostgresPool } from "@/server/db/postgres";
import { validateConsumerLease } from "@/server/consistency/consumer-leases";

export type ExternalEffectInput = {
  effectKey: string;
  integration: "email" | "webhook" | "notification" | "analytics";
  aggregateId: string;
  leaseKey: string;
  ownerId: string;
  fencingToken: number;
  payload: unknown;
};

export async function reserveExternalEffect(input: ExternalEffectInput) {
  const leaseValid = await validateConsumerLease({
    leaseKey: input.leaseKey,
    ownerId: input.ownerId,
    fencingToken: input.fencingToken,
  });

  if (!leaseValid) {
    return {
      reserved: false,
      reason: "stale or invalid lease fencing token",
    };
  }

  const pool = getPostgresPool();

  const result = await pool.query(
    `
    INSERT INTO external_effects (
      effect_key,
      integration,
      aggregate_id,
      fencing_token,
      payload,
      status
    )
    VALUES ($1, $2, $3, $4, $5::jsonb, 'pending')
    ON CONFLICT (effect_key) DO NOTHING
    RETURNING effect_key
    `,
    [
      input.effectKey,
      input.integration,
      input.aggregateId,
      input.fencingToken,
      JSON.stringify(input.payload),
    ]
  );

  return {
    reserved: result.rowCount === 1,
    effectKey: input.effectKey,
  };
}

export async function markExternalEffectSent(effectKey: string) {
  const pool = getPostgresPool();

  await pool.query(
    `
    UPDATE external_effects
    SET status = 'sent', sent_at = NOW()
    WHERE effect_key = $1
    `,
    [effectKey]
  );
}

export async function markExternalEffectFailed(effectKey: string, error: unknown) {
  const pool = getPostgresPool();

  await pool.query(
    `
    UPDATE external_effects
    SET status = 'pending',
        attempts = attempts + 1,
        last_error = $2
    WHERE effect_key = $1
    `,
    [effectKey, error instanceof Error ? error.message : String(error)]
  );
}

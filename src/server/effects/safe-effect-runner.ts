import { getPostgresPool } from "@/server/db/postgres";
import { dispatchExternalEffectSafely } from "./replay-safe-dispatcher";

export async function claimDueExternalEffects(limit = 25) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    UPDATE external_effects
    SET status = 'processing'
    WHERE effect_key IN (
      SELECT effect_key
      FROM external_effects
      WHERE status = 'pending'
        AND next_attempt_at <= NOW()
      ORDER BY created_at ASC
      LIMIT $1
      FOR UPDATE SKIP LOCKED
    )
    RETURNING effect_key, integration, fencing_token, payload, attempts
    `,
    [limit]
  );

  return result.rows;
}

export async function runReplaySafeExternalEffectBatch(
  sender: (effect: unknown) => Promise<{ providerMessageId?: string; rawAck?: unknown }>,
  limit = 25
) {
  const effects = await claimDueExternalEffects(limit);

  let delivered = 0;
  let quarantined = 0;
  let skipped = 0;

  for (const effect of effects) {
    const result = await dispatchExternalEffectSafely(effect, sender);

    if (result.delivered) delivered += 1;
    if (result.quarantined) quarantined += 1;
    if (result.skipped) skipped += 1;
  }

  return {
    claimed: effects.length,
    delivered,
    quarantined,
    skipped,
  };
}

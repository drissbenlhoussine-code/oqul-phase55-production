import { getPostgresPool } from "@/server/db/postgres";
import {
  markExternalEffectFailed,
  markExternalEffectSent,
} from "./external-effect-fencing";

export type ExternalEffectDelivery = {
  effectKey: string;
  integration: string;
  payload: unknown;
};

export async function claimPendingExternalEffects(limit = 25) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    UPDATE external_effects
    SET status = 'processing',
        attempts = attempts + 1
    WHERE effect_key IN (
      SELECT effect_key
      FROM external_effects
      WHERE status = 'pending'
      ORDER BY created_at ASC
      LIMIT $1
      FOR UPDATE SKIP LOCKED
    )
    RETURNING effect_key, integration, payload
    `,
    [limit]
  );

  return result.rows as ExternalEffectDelivery[];
}

export async function deliverExternalEffect(
  effect: ExternalEffectDelivery,
  sender: (effect: ExternalEffectDelivery) => Promise<void>
) {
  try {
    await sender(effect);
    await markExternalEffectSent(effect.effectKey);
    return { delivered: true, effectKey: effect.effectKey };
  } catch (error) {
    await markExternalEffectFailed(effect.effectKey, error);
    return { delivered: false, effectKey: effect.effectKey };
  }
}

export async function runExternalEffectBatch(
  sender: (effect: ExternalEffectDelivery) => Promise<void>,
  limit = 25
) {
  const effects = await claimPendingExternalEffects(limit);
  let delivered = 0;
  let failed = 0;

  for (const effect of effects) {
    const result = await deliverExternalEffect(effect, sender);

    if (result.delivered) delivered += 1;
    else failed += 1;
  }

  return {
    claimed: effects.length,
    delivered,
    failed,
  };
}

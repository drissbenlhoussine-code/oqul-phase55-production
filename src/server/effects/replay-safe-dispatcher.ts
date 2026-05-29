import { getPostgresPool } from "@/server/db/postgres";
import { recordExternalEffectAck } from "./external-effect-acks";
import { isIntegrationCircuitOpen, recordIntegrationFailure } from "./integration-circuit-breaker";
import { calculateExternalEffectRetry } from "./retry-policy";

export type ReplaySafeDeliveryResult = {
  delivered: boolean;
  quarantined: boolean;
  skipped: boolean;
  effectKey: string;
};

export type ReplaySafeSenderResult = {
  providerMessageId?: string;
  rawAck?: unknown;
};

export async function dispatchExternalEffectSafely(
  effect: {
    effect_key: string;
    integration: string;
    fencing_token: number;
    payload: unknown;
    attempts: number;
  },
  sender: (effect: unknown) => Promise<ReplaySafeSenderResult>
): Promise<ReplaySafeDeliveryResult> {
  const pool = getPostgresPool();

  if (await isIntegrationCircuitOpen(effect.integration)) {
    return {
      delivered: false,
      quarantined: false,
      skipped: true,
      effectKey: effect.effect_key,
    };
  }

  const existingAck = await pool.query(
    "SELECT ack_key FROM external_effect_acks WHERE effect_key = $1",
    [effect.effect_key]
  );
  const existingAckCount = existingAck.rowCount ?? 0;

  if (existingAckCount > 0) {
    await pool.query(
      "UPDATE external_effects SET status = 'sent', sent_at = NOW() WHERE effect_key = $1",
      [effect.effect_key]
    );

    return {
      delivered: false,
      quarantined: false,
      skipped: true,
      effectKey: effect.effect_key,
    };
  }

  try {
    const ack = await sender(effect);

    await recordExternalEffectAck({
      effectKey: effect.effect_key,
      integration: effect.integration,
      providerMessageId: ack.providerMessageId,
      fencingToken: effect.fencing_token,
      rawAck: ack.rawAck,
    });

    await pool.query(
      `
      UPDATE external_effects
      SET status = 'sent',
          sent_at = NOW(),
          last_provider_message_id = $2
      WHERE effect_key = $1
      `,
      [effect.effect_key, ack.providerMessageId ?? null]
    );

    return {
      delivered: true,
      quarantined: false,
      skipped: false,
      effectKey: effect.effect_key,
    };
  } catch (error) {
    await recordIntegrationFailure({ integration: effect.integration });

    const retry = calculateExternalEffectRetry({
      attempts: effect.attempts + 1,
    });

    if (retry.quarantine) {
      await pool.query(
        `
        INSERT INTO external_effect_quarantine (
          effect_key,
          reason,
          attempts
        )
        VALUES ($1, $2, $3)
        ON CONFLICT (effect_key)
        DO UPDATE SET
          reason = EXCLUDED.reason,
          attempts = EXCLUDED.attempts,
          quarantined_at = NOW()
        `,
        [effect.effect_key, retry.reason, effect.attempts + 1]
      );

      await pool.query(
        "UPDATE external_effects SET status = 'quarantined', attempts = attempts + 1, last_error = $2 WHERE effect_key = $1",
        [effect.effect_key, error instanceof Error ? error.message : String(error)]
      );

      return {
        delivered: false,
        quarantined: true,
        skipped: false,
        effectKey: effect.effect_key,
      };
    }

    await pool.query(
      `
      UPDATE external_effects
      SET status = 'pending',
          attempts = attempts + 1,
          next_attempt_at = NOW() + ($2 || ' milliseconds')::interval,
          last_error = $3
      WHERE effect_key = $1
      `,
      [
        effect.effect_key,
        retry.delayMs,
        error instanceof Error ? error.message : String(error),
      ]
    );

    return {
      delivered: false,
      quarantined: false,
      skipped: false,
      effectKey: effect.effect_key,
    };
  }
}

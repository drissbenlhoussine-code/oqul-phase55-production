import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export async function approveQuarantinedEffect(input: {
  effectKey: string;
  operatorId: string;
  reason: string;
}) {
  const pool = getPostgresPool();

  await pool.query(
    `
    INSERT INTO quarantine_recovery_actions (
      id,
      effect_key,
      action,
      operator_id,
      reason
    )
    VALUES ($1, $2, 'approve-retry', $3, $4)
    `,
    [randomUUID(), input.effectKey, input.operatorId, input.reason]
  );

  await pool.query(
    `
    UPDATE external_effects
    SET status = 'pending',
        next_attempt_at = NOW(),
        last_error = NULL
    WHERE effect_key = $1
      AND status = 'quarantined'
    `,
    [input.effectKey]
  );
}

export async function discardQuarantinedEffect(input: {
  effectKey: string;
  operatorId: string;
  reason: string;
}) {
  const pool = getPostgresPool();

  await pool.query(
    `
    INSERT INTO quarantine_recovery_actions (
      id,
      effect_key,
      action,
      operator_id,
      reason
    )
    VALUES ($1, $2, 'discard', $3, $4)
    `,
    [randomUUID(), input.effectKey, input.operatorId, input.reason]
  );

  await pool.query(
    `
    UPDATE external_effects
    SET status = 'discarded'
    WHERE effect_key = $1
      AND status = 'quarantined'
    `,
    [input.effectKey]
  );
}

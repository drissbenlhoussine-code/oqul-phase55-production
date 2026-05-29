import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export async function getCurrentRevocationEpoch() {
  const pool = getPostgresPool();

  const result = await pool.query(
    "SELECT COALESCE(MAX(epoch_number), 0) AS epoch FROM revocation_epochs"
  );

  return Number(result.rows[0]?.epoch ?? 0);
}

export async function advanceRevocationEpoch(input: {
  reason: string;
  advancedBy: string;
}) {
  const pool = getPostgresPool();
  const current = await getCurrentRevocationEpoch();
  const next = current + 1;
  const epochId = randomUUID();

  await pool.query(
    `
    INSERT INTO revocation_epochs (
      epoch_id,
      epoch_number,
      reason,
      advanced_by
    )
    VALUES ($1, $2, $3, $4)
    `,
    [epochId, next, input.reason, input.advancedBy]
  );

  return {
    epochId,
    epochNumber: next,
  };
}

export async function invalidateReplayAfterRevocation(input: {
  subjectType: string;
  subjectId: string;
  reason: string;
}) {
  const pool = getPostgresPool();
  const epoch = await advanceRevocationEpoch({
    reason: input.reason,
    advancedBy: "revocation-system",
  });

  await pool.query(
    `
    INSERT INTO trust_replay_invalidations (
      invalidation_id,
      subject_type,
      subject_id,
      epoch_number,
      reason
    )
    VALUES ($1, $2, $3, $4, $5)
    `,
    [randomUUID(), input.subjectType, input.subjectId, epoch.epochNumber, input.reason]
  );

  return epoch;
}

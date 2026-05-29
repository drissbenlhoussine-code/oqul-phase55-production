import { getPostgresPool } from "@/server/db/postgres";

export async function verifyDelegationAtTime(input: {
  delegationId: string;
  at: Date;
}) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    SELECT delegation_id
    FROM delegated_authorities
    WHERE delegation_id = $1
      AND active = TRUE
      AND (revoked_at IS NULL OR revoked_at > $2)
      AND valid_from <= $2
      AND (valid_until IS NULL OR valid_until > $2)
    `,
    [input.delegationId, input.at]
  );

  return {
    valid: result.rowCount === 1,
    delegationId: input.delegationId,
    at: input.at,
  };
}

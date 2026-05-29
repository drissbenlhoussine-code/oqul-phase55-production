import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export async function registerTrustAnchor(input: {
  name: string;
  publicKey: string;
  algorithm?: string;
  anchorId?: string;
}) {
  const pool = getPostgresPool();
  const anchorId = input.anchorId ?? randomUUID();

  await pool.query(
    `
    INSERT INTO trust_anchors (
      anchor_id,
      name,
      public_key,
      algorithm,
      active
    )
    VALUES ($1, $2, $3, $4, TRUE)
    ON CONFLICT (anchor_id)
    DO UPDATE SET
      public_key = EXCLUDED.public_key,
      algorithm = EXCLUDED.algorithm,
      active = TRUE,
      revoked_at = NULL
    `,
    [anchorId, input.name, input.publicKey, input.algorithm ?? "ed25519"]
  );

  return { anchorId };
}

export async function revokeTrustAnchor(anchorId: string) {
  const pool = getPostgresPool();

  await pool.query(
    `
    UPDATE trust_anchors
    SET active = FALSE,
        revoked_at = NOW()
    WHERE anchor_id = $1
    `,
    [anchorId]
  );
}

export async function getActiveTrustAnchor(anchorId: string) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    SELECT public_key, algorithm
    FROM trust_anchors
    WHERE anchor_id = $1
      AND active = TRUE
      AND revoked_at IS NULL
    `,
    [anchorId]
  );

  return result.rows[0] as
    | { public_key: string; algorithm: string }
    | undefined;
}

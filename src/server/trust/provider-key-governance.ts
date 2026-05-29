import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export async function registerProviderPublicKey(input: {
  integration: string;
  publicKey: string;
  algorithm?: string;
  keyId?: string;
}) {
  const pool = getPostgresPool();
  const keyId = input.keyId ?? randomUUID();

  await pool.query(
    `
    INSERT INTO provider_authority_keys (
      key_id,
      integration,
      public_key,
      algorithm,
      active
    )
    VALUES ($1, $2, $3, $4, TRUE)
    ON CONFLICT (key_id)
    DO UPDATE SET
      public_key = EXCLUDED.public_key,
      algorithm = EXCLUDED.algorithm,
      active = TRUE,
      revoked_at = NULL
    `,
    [keyId, input.integration, input.publicKey, input.algorithm ?? "ed25519"]
  );

  return { keyId };
}

export async function revokeProviderPublicKey(keyId: string) {
  const pool = getPostgresPool();

  await pool.query(
    `
    UPDATE provider_authority_keys
    SET active = FALSE,
        revoked_at = NOW()
    WHERE key_id = $1
    `,
    [keyId]
  );
}

export async function getActiveProviderPublicKey(input: {
  integration: string;
  keyId: string;
}) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    SELECT public_key, algorithm
    FROM provider_authority_keys
    WHERE integration = $1
      AND key_id = $2
      AND active = TRUE
      AND revoked_at IS NULL
      AND valid_from <= NOW()
      AND (valid_until IS NULL OR valid_until > NOW())
    `,
    [input.integration, input.keyId]
  );

  return result.rows[0] as
    | { public_key: string; algorithm: string }
    | undefined;
}

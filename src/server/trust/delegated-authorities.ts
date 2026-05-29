import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";
import { getActiveTrustAnchor } from "./trust-anchors";
import {
  signProviderReceiptAsymmetric,
  verifyProviderReceiptAsymmetric,
} from "./asymmetric-provider-trust";

export function delegationPayload(input: {
  integration: string;
  scope: string;
  childKeyId: string;
}) {
  return ["delegation", input.integration, input.scope, input.childKeyId].join(":");
}

export function signDelegation(input: {
  privateKeyPem: string;
  integration: string;
  scope: string;
  childKeyId: string;
}) {
  return signProviderReceiptAsymmetric({
    privateKeyPem: input.privateKeyPem,
    deliveryId: "delegation",
    providerMessageId: [input.integration, input.scope, input.childKeyId].join(":"),
  });
}

export async function registerDelegatedAuthority(input: {
  parentAnchorId: string;
  childKeyId: string;
  integration: string;
  scope: string;
  publicKey: string;
  signature: string;
  validUntil?: Date;
}) {
  const parent = await getActiveTrustAnchor(input.parentAnchorId);

  if (!parent) {
    return {
      registered: false,
      reason: "missing or revoked trust anchor",
    };
  }

  const verified = verifyProviderReceiptAsymmetric({
    publicKeyPem: parent.public_key,
    deliveryId: "delegation",
    providerMessageId: [input.integration, input.scope, input.childKeyId].join(":"),
    signature: input.signature,
  });

  if (!verified) {
    return {
      registered: false,
      reason: "invalid delegation signature",
    };
  }

  const pool = getPostgresPool();
  const delegationId = randomUUID();

  await pool.query(
    `
    INSERT INTO delegated_authorities (
      delegation_id,
      parent_anchor_id,
      child_key_id,
      integration,
      scope,
      public_key,
      signature,
      valid_until
    )
    VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
    `,
    [
      delegationId,
      input.parentAnchorId,
      input.childKeyId,
      input.integration,
      input.scope,
      input.publicKey,
      input.signature,
      input.validUntil ?? null,
    ]
  );

  return {
    registered: true,
    delegationId,
  };
}

export async function getActiveDelegatedAuthority(input: {
  integration: string;
  scope: string;
  childKeyId: string;
}) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    SELECT public_key
    FROM delegated_authorities
    WHERE integration = $1
      AND scope = $2
      AND child_key_id = $3
      AND active = TRUE
      AND revoked_at IS NULL
      AND (valid_until IS NULL OR valid_until > NOW())
    ORDER BY created_at DESC
    LIMIT 1
    `,
    [input.integration, input.scope, input.childKeyId]
  );

  return result.rows[0] as { public_key: string } | undefined;
}

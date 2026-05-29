import { randomUUID } from "node:crypto";
import type { QueryResult } from "pg";
import { getPostgresPool } from "@/server/db/postgres";
import { assertScopeAllowed } from "./scope-policy";

export type TrustChainResult = {
  valid: boolean;
  depth: number;
  reason: string;
  visited: string[];
};

type DelegationRow = {
  delegation_id: string;
  parent_anchor_id: string | null;
  parent_delegation_id: string | null;
  child_key_id: string;
  scope: string;
  deny_scope: string | null;
  revoked_at: Date | null;
  valid_from: Date | null;
  valid_until: Date | null;
  active: boolean;
};

type ParentDelegationRow = {
  child_key_id: string;
};

export async function validateRecursiveTrustChain(input: {
  integration: string;
  requestedScope: string;
  childKeyId: string;
  maxDepth?: number;
}): Promise<TrustChainResult> {
  const pool = getPostgresPool();
  const maxDepth = input.maxDepth ?? 5;
  const visited = new Set<string>();
  let currentChildKeyId: string | null = input.childKeyId;
  let depth = 0;

  while (currentChildKeyId) {
    if (visited.has(currentChildKeyId)) {
      await recordTrustChainValidation({
        integration: input.integration,
        scope: input.requestedScope,
        childKeyId: input.childKeyId,
        result: "invalid",
        depth,
        reason: "cycle detected",
      });

      return {
        valid: false,
        depth,
        reason: "cycle detected",
        visited: Array.from(visited),
      };
    }

    visited.add(currentChildKeyId);
    depth += 1;

    if (depth > maxDepth) {
      await recordTrustChainValidation({
        integration: input.integration,
        scope: input.requestedScope,
        childKeyId: input.childKeyId,
        result: "invalid",
        depth,
        reason: "max trust-chain depth exceeded",
      });

      return {
        valid: false,
        depth,
        reason: "max trust-chain depth exceeded",
        visited: Array.from(visited),
      };
    }

    const result: QueryResult<DelegationRow> = await pool.query<DelegationRow>(
      `
      SELECT
        delegation_id,
        parent_anchor_id,
        parent_delegation_id,
        child_key_id,
        scope,
        deny_scope,
        revoked_at,
        valid_from,
        valid_until,
        active
      FROM delegated_authorities
      WHERE integration = $1
        AND child_key_id = $2
      ORDER BY created_at DESC
      LIMIT 1
      `,
      [input.integration, currentChildKeyId]
    );

    const delegation = result.rows[0];

    if (!delegation || !delegation.active || delegation.revoked_at) {
      await recordTrustChainValidation({
        integration: input.integration,
        scope: input.requestedScope,
        childKeyId: input.childKeyId,
        result: "invalid",
        depth,
        reason: "missing or revoked delegation",
      });

      return {
        valid: false,
        depth,
        reason: "missing or revoked delegation",
        visited: Array.from(visited),
      };
    }

    const scope = assertScopeAllowed({
      grantedScope: delegation.scope,
      requestedScope: input.requestedScope,
      denyScope: delegation.deny_scope,
    });

    if (!scope.allowed) {
      await recordTrustChainValidation({
        integration: input.integration,
        scope: input.requestedScope,
        childKeyId: input.childKeyId,
        result: "invalid",
        depth,
        reason: scope.reason,
      });

      return {
        valid: false,
        depth,
        reason: scope.reason,
        visited: Array.from(visited),
      };
    }

    if (!delegation.parent_delegation_id) {
      await recordTrustChainValidation({
        integration: input.integration,
        scope: input.requestedScope,
        childKeyId: input.childKeyId,
        result: "valid",
        depth,
        reason: "root trust anchor reached",
      });

      return {
        valid: true,
        depth,
        reason: "root trust anchor reached",
        visited: Array.from(visited),
      };
    }

    const parent: QueryResult<ParentDelegationRow> = await pool.query<ParentDelegationRow>(
      `
      SELECT child_key_id
      FROM delegated_authorities
      WHERE delegation_id = $1
      `,
      [delegation.parent_delegation_id]
    );

    currentChildKeyId = parent.rows[0]?.child_key_id ?? null;
  }

  return {
    valid: false,
    depth,
    reason: "chain terminated unexpectedly",
    visited: Array.from(visited),
  };
}

async function recordTrustChainValidation(input: {
  integration: string;
  scope: string;
  childKeyId: string;
  result: "valid" | "invalid";
  depth: number;
  reason: string;
}) {
  const pool = getPostgresPool();

  await pool.query(
    `
    INSERT INTO trust_chain_validations (
      validation_id,
      integration,
      scope,
      child_key_id,
      result,
      depth,
      reason
    )
    VALUES ($1, $2, $3, $4, $5, $6, $7)
    `,
    [
      randomUUID(),
      input.integration,
      input.scope,
      input.childKeyId,
      input.result,
      input.depth,
      input.reason,
    ]
  );
}

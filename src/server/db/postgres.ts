import { Pool } from "pg";

/**
 * PostgreSQL pool compatibility shim.
 * Phase 26 governance/consistency modules use raw SQL via pg pool.
 * This bridges to the database — COMPANION uses Drizzle for business logic,
 * Phase 26 governance uses raw SQL for deterministic consistency operations.
 */

let _pool: Pool | null = null;

export function getPostgresPool() {
  if (_pool) return _pool;

  const connectionString = process.env.DATABASE_URL;
  if (!connectionString) {
    throw new Error("DATABASE_URL required for consistency runtime");
  }

  try {
    _pool = new Pool({
      connectionString,
      ssl: connectionString.includes("localhost") ? false : { rejectUnauthorized: false },
      max: Number(process.env.POSTGRES_POOL_MAX ?? 10),
      idleTimeoutMillis: 10_000,
      connectionTimeoutMillis: 2_000,
    });
    return _pool;
  } catch {
    // pg not installed — this module is only used by Phase 26 governance subsystems
    // In dev without governance, this is safe to skip
    throw new Error("pg package required for governance modules. Run: npm install pg @types/pg");
  }
}

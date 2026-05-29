import type { PoolClient } from "pg";
import { getPostgresPool } from "./postgres";

/**
 * Runs a raw PostgreSQL transaction for governance/consistency modules.
 * This file was missing in earlier local zips, causing TypeScript/module errors.
 */
export async function withPostgresTransaction<T>(
  operation: (client: PoolClient) => Promise<T>
): Promise<T> {
  const pool = getPostgresPool();
  const client = await pool.connect();

  try {
    await client.query("BEGIN");
    const result = await operation(client);
    await client.query("COMMIT");
    return result;
  } catch (error) {
    try {
      await client.query("ROLLBACK");
    } catch {
      // Preserve original error.
    }
    throw error;
  } finally {
    client.release();
  }
}

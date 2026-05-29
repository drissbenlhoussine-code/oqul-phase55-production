import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export type AuthUser = {
  id: string;
  email: string;
  password_hash: string;
};

export async function findAuthUserByEmail(email: string): Promise<AuthUser | null> {
  const pool = getPostgresPool();

  const result = await pool.query(
    "SELECT id, email, password_hash FROM users WHERE lower(email) = lower($1) LIMIT 1",
    [email]
  );

  return result.rows[0] ?? null;
}

export async function createAuthUser(input: {
  email: string;
  passwordHash: string;
  name?: string;
}) {
  const pool = getPostgresPool();
  const id = randomUUID();

  const result = await pool.query(
    `
    INSERT INTO users (id, email, password_hash, name)
    VALUES ($1, lower($2), $3, $4)
    ON CONFLICT (email) DO NOTHING
    RETURNING id, email
    `,
    [id, input.email, input.passwordHash, input.name ?? null]
  );

  if (result.rowCount !== 1) {
    throw new Error("A user with this email already exists.");
  }

  return result.rows[0] as { id: string; email: string };
}

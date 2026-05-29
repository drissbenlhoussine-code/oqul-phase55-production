import { drizzle } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import * as schema from "./schema";

function createDb() {
  const url = process.env.DATABASE_URL;
  if (!url) throw new Error("DATABASE_URL environment variable is required");
  const client = postgres(url, { ssl: url.includes("localhost") ? false : "require" });
  return drizzle(client, { schema });
}

const globalForDb = globalThis as unknown as { _db?: ReturnType<typeof createDb> };
export const db = globalForDb._db ?? createDb();
if (process.env.NODE_ENV !== "production") globalForDb._db = db;

export * from "./schema";

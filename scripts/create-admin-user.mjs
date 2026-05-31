import pg from "pg";
import dotenv from "dotenv";

dotenv.config({ path: ".env.local" });
dotenv.config({ path: ".env" });

const { Client } = pg;

function parseArgs(argv = process.argv.slice(2)) {
  const args = {};
  for (const arg of argv) {
    if (!arg.startsWith("--")) continue;
    const [key, ...rest] = arg.slice(2).split("=");
    args[key] = rest.length ? rest.join("=") : true;
  }
  return args;
}

function requireEmail(value) {
  const email = String(value ?? "").trim().toLowerCase();
  if (!email || !email.includes("@")) {
    throw new Error("Usage: node scripts/create-admin-user.mjs --email=user@example.com [--apply]");
  }
  return email;
}

function requireDatabaseUrl() {
  if (!process.env.DATABASE_URL) {
    throw new Error("DATABASE_URL is required. Load it from .env.local, .env, or your shell.");
  }
  return process.env.DATABASE_URL;
}

async function main() {
  const args = parseArgs();
  const email = requireEmail(args.email);
  const apply = args.apply === true;
  const allowCreate = args.create === true;

  console.log("Admin user safety tool");
  console.log("----------------------");
  console.log(`Mode: ${apply ? "APPLY" : "DRY RUN"}`);
  console.log(`Target email: ${email}`);

  const client = new Client({
    connectionString: requireDatabaseUrl(),
    connectionTimeoutMillis: Number(process.env.PGCONNECT_TIMEOUT_MS ?? 15000),
    query_timeout: Number(process.env.PGQUERY_TIMEOUT_MS ?? 30000),
    statement_timeout: Number(process.env.PGSTATEMENT_TIMEOUT_MS ?? 30000),
  });

  await client.connect();
  try {
    const existing = await client.query(
      "select id, email, role from users where lower(email) = lower($1) limit 1",
      [email]
    );

    if (existing.rows.length === 0) {
      if (!allowCreate) {
        throw new Error("User not found. Refusing to create a new user unless --create is passed.");
      }
      throw new Error("Safe creation is not implemented because no password should be hardcoded. Register the user first, then rerun this script.");
    }

    const user = existing.rows[0];
    console.log(`User found: yes`);
    console.log(`Current role: ${user.role}`);

    if (user.role === "admin") {
      console.log("No change needed: user is already admin.");
      return;
    }

    if (!apply) {
      console.log("Dry run: would promote this existing user to admin.");
      console.log("Apply with: node scripts/create-admin-user.mjs --email=<email> --apply");
      return;
    }

    const updated = await client.query(
      "update users set role = 'admin' where id = $1 and role <> 'admin' returning id, email, role",
      [user.id]
    );

    if ((updated.rowCount ?? 0) !== 1) {
      throw new Error(`Expected to update 1 user, updated ${updated.rowCount ?? 0}.`);
    }

    console.log("User promoted successfully.");
    console.log(`Updated role: ${updated.rows[0].role}`);
  } finally {
    await client.end();
  }
}

main()
  .then(() => {
    process.exit(0);
  })
  .catch((error) => {
    console.error(`Error: ${error instanceof Error ? error.message : String(error)}`);
    process.exit(1);
  });

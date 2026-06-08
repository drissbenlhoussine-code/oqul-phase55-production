/**
 * scripts/check-user-email-exists.mjs
 *
 * Admin-only diagnostic: checks whether an email exists in the production DB.
 * Read-only — never modifies the database.
 * Safe  — never prints password hash, token, or any credential.
 *
 * Usage:
 *   node scripts/check-user-email-exists.mjs --email user@example.com
 *
 * Requires DATABASE_URL in .env.local
 */

import { createHash }    from "crypto";
import path              from "path";
import { fileURLToPath } from "url";
import dotenv            from "dotenv";
import postgres          from "postgres";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root      = path.resolve(__dirname, "..");

dotenv.config({ path: path.join(root, ".env.local") });
dotenv.config({ path: path.join(root, ".env") });

// ── Arg parsing ───────────────────────────────────────────────────────────────

const args = process.argv.slice(2);
function getArg(flag) {
  const i = args.indexOf(flag);
  return i !== -1 ? args[i + 1] : undefined;
}

const rawEmail = getArg("--email");
if (!rawEmail || !rawEmail.includes("@")) {
  console.error("Usage: node scripts/check-user-email-exists.mjs --email user@example.com");
  process.exit(1);
}

const normalized = rawEmail.trim().toLowerCase();
const emailHash  = createHash("sha256").update(normalized).digest("hex").slice(0, 16);

function redactId(id) {
  return createHash("sha256").update(String(id)).digest("hex").slice(0, 12) + "...";
}

// ── DB check ──────────────────────────────────────────────────────────────────

const dbUrl = process.env.DATABASE_URL;
if (!dbUrl) {
  console.error("❌ DATABASE_URL is not set. Add it to .env.local");
  process.exit(1);
}

console.log("──────────────────────────────────────────────────────────────");
console.log("  User Email Lookup (read-only — production DB)");
console.log("──────────────────────────────────────────────────────────────");
console.log(`  Normalized email: ${normalized}`);
console.log(`  emailHash:        ${emailHash}  ← use this to search Vercel logs`);
console.log(`  DB host:          ${dbUrl.split("@")[1]?.split("/")[0] ?? "(hidden)"}`);
console.log("──────────────────────────────────────────────────────────────\n");

const sql = postgres(dbUrl, { ssl: "require", max: 1, idle_timeout: 8 });

try {
  const rows = await sql`
    SELECT
      id,
      email,
      full_name,
      CASE WHEN password_hash IS NOT NULL AND length(password_hash) > 10
           THEN true ELSE false END                        AS has_password_hash,
      email_verified,
      CASE WHEN password_reset_token IS NOT NULL
           THEN true ELSE false END                        AS has_pending_reset_token,
      password_reset_expires_at,
      created_at
    FROM users
    WHERE lower(trim(email)) = ${normalized}
    LIMIT 1
  `;

  if (rows.length === 0) {
    console.log("userFound:          false");
    console.log("");
    console.log("→ The email does NOT exist in the production users table.");
    console.log("  Possible causes:");
    console.log("  • Account was created on a local/dev DB, not on production.");
    console.log("  • Account was registered with a different email address.");
    console.log("  • Vercel's DATABASE_URL points to a different DB than .env.local.");
    console.log("  • Email was entered with a typo.");
    console.log("");
    console.log("  Fix: Register at https://www.oqul.tech/register and use THAT email.");
  } else {
    const row = rows[0];
    const now = new Date();
    const hasExpiredToken = row.password_reset_expires_at
      ? now > new Date(row.password_reset_expires_at)
      : null;

    console.log(`userFound:                  true`);
    console.log(`userId (redacted):          ${redactId(row.id)}`);
    console.log(`hasPasswordHash:            ${row.has_password_hash}`);
    console.log(`emailVerified:              ${row.email_verified}`);
    console.log(`hasPendingResetToken:       ${row.has_pending_reset_token}`);

    if (row.has_pending_reset_token) {
      console.log(`resetTokenExpired:          ${hasExpiredToken}`);
      console.log(`resetTokenExpiresAt:        ${row.password_reset_expires_at}`);
    }

    console.log(`accountCreatedAt:           ${row.created_at}`);

    if (!row.has_password_hash) {
      console.log("\n⚠  User has NO password hash.");
      console.log("   Account may have been created via OAuth (no password set).");
      console.log("   Forgot-password will set a new bcrypt password — this is fine.");
    }
  }
} catch (err) {
  console.error("❌ DB query failed:", err.message);
  console.error("  → Verify DATABASE_URL in .env.local is the correct production Neon URL.");
} finally {
  await sql.end();
}

/**
 * scripts/check-prod-auth-user.mjs
 *
 * Read-only lookup: prints whether a user exists in the production DB
 * and their auth state (password set, email verified, pending reset token).
 *
 * Safe: never prints password hash, reset token, or any credential.
 *
 * Usage:
 *   node scripts/check-prod-auth-user.mjs --email user@example.com
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

// ── Args ──────────────────────────────────────────────────────────────────────

const args = process.argv.slice(2);
function getArg(flag) {
  const i = args.indexOf(flag);
  return i !== -1 ? args[i + 1] : undefined;
}

const rawEmail = getArg("--email");
if (!rawEmail?.includes("@")) {
  console.error("Usage: node scripts/check-prod-auth-user.mjs --email user@example.com");
  process.exit(1);
}

const normalized = rawEmail.trim().toLowerCase();
const emailHash  = createHash("sha256").update(normalized).digest("hex").slice(0, 16);

function redactId(id) {
  return createHash("sha256").update(String(id)).digest("hex").slice(0, 12) + "...";
}

// ── DB ────────────────────────────────────────────────────────────────────────

const dbUrl = process.env.DATABASE_URL;
if (!dbUrl) {
  console.error("❌ DATABASE_URL is not set. Add it to .env.local");
  process.exit(1);
}

const dbHost = dbUrl.split("@")[1]?.split("/")[0] ?? "(hidden)";

console.log("──────────────────────────────────────────────────────────────");
console.log("  Production Auth User Check (read-only)");
console.log("──────────────────────────────────────────────────────────────");
console.log(`  normalized email : ${normalized}`);
console.log(`  emailHash        : ${emailHash}  ← use in Vercel log filter`);
console.log(`  DB host          : ${dbHost}`);
console.log("──────────────────────────────────────────────────────────────\n");

const sql = postgres(dbUrl, { ssl: "require", max: 1, idle_timeout: 8 });

try {
  const rows = await sql`
    SELECT
      id,
      full_name,
      CASE WHEN password_hash IS NOT NULL AND length(password_hash) > 10
           THEN true ELSE false END                            AS has_password,
      email_verified,
      CASE WHEN password_reset_token IS NOT NULL
           THEN true ELSE false END                            AS has_reset_token,
      password_reset_expires_at,
      created_at
    FROM users
    WHERE lower(trim(email)) = ${normalized}
    LIMIT 1
  `;

  if (rows.length === 0) {
    console.log("userFound          : false");
    console.log("\n→ No account with this email in the production DB.");
    console.log("  Possible causes:");
    console.log("  • Registered on a local/dev DB, not production.");
    console.log("  • Different email address used at registration.");
    console.log("  • DATABASE_URL in .env.local points to a different DB than Vercel's.");
    console.log("  Fix: sign up at https://www.oqul.tech/register then use THAT email.");
  } else {
    const r = rows[0];
    const now = new Date();
    const tokenExpired = r.password_reset_expires_at
      ? now > new Date(r.password_reset_expires_at)
      : null;

    console.log(`userFound          : true`);
    console.log(`userId (redacted)  : ${redactId(r.id)}`);
    console.log(`fullName           : ${r.full_name}`);
    console.log(`hasPassword        : ${r.has_password}`);
    console.log(`emailVerified      : ${r.email_verified}`);
    console.log(`hasPendingReset    : ${r.has_reset_token}`);
    if (r.has_reset_token) {
      console.log(`resetTokenExpired  : ${tokenExpired}`);
      console.log(`resetExpiresAt     : ${r.password_reset_expires_at}`);
    }
    console.log(`accountCreatedAt   : ${r.created_at}`);

    if (!r.has_password) {
      console.log("\n⚠  No password hash — account may use OAuth (Google/etc).");
      console.log("   Forgot-password will set a new bcrypt password. This is expected behaviour.");
    }
    if (!r.email_verified) {
      console.log("\n⚠  Email not verified. The forgot-password route still works,");
      console.log("   but consider reminding the user to verify their email first.");
    }
  }
} catch (err) {
  console.error("❌ DB query failed:", err.message);
  console.error("  → Verify DATABASE_URL in .env.local is the correct production Neon URL.");
} finally {
  await sql.end();
}

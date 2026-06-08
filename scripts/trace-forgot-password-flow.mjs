/**
 * scripts/trace-forgot-password-flow.mjs
 *
 * Surgical diagnostic: traces the full forgot-password production flow
 * against the REAL production database and Resend API.
 *
 * Read-only — never modifies the database, never sends email.
 * Safe  — never prints raw email, password hash, API key, or reset token.
 *
 * Usage:
 *   node scripts/trace-forgot-password-flow.mjs --email user@example.com
 *
 * Requires:
 *   DATABASE_URL   in .env.local (production Neon URL)
 *   RESEND_API_KEY in .env.local
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
  console.error("Usage: node scripts/trace-forgot-password-flow.mjs --email user@example.com");
  process.exit(1);
}

// ── Normalize email exactly as the route does ─────────────────────────────────
// Mirrors: z.string().trim().toLowerCase().email()

const normalized = rawEmail.trim().toLowerCase();
const emailHash  = createHash("sha256").update(normalized).digest("hex").slice(0, 16);

// ── Helpers ───────────────────────────────────────────────────────────────────

const PASS = "  ✅";
const FAIL = "  ❌";
const WARN = "  ⚠️ ";

function redact(id) {
  if (!id) return "(null)";
  return createHash("sha256").update(String(id)).digest("hex").slice(0, 12) + "...";
}

function domainOf(emailOrFrom) {
  const m = emailOrFrom?.match(/<([^>]+)>/) ?? emailOrFrom?.match(/(\S+@(\S+))/);
  const addr = m?.[1] ?? emailOrFrom ?? "";
  return addr.split("@")[1] ?? addr;
}

function banner(title) {
  const line = "─".repeat(58);
  console.log(`\n${line}`);
  console.log(`  ${title}`);
  console.log(line);
}

// ── 1. Configuration ──────────────────────────────────────────────────────────

banner("1. Configuration");

const dbUrl        = process.env.DATABASE_URL;
const resendKey    = process.env.RESEND_API_KEY;
const appUrl       = process.env.NEXT_PUBLIC_APP_URL;
const emailFrom    = process.env.EMAIL_FROM ?? "(not set — fallback: Oqul <no-reply@oqul.tech>)";

const dbPresent    = Boolean(dbUrl?.trim());
const resendPresent = Boolean(resendKey?.trim());
const appUrlPresent = Boolean(appUrl?.trim());

console.log(`DATABASE_URL:        ${dbPresent   ? "PRESENT" : "MISSING"} ${dbPresent ? "(host: " + (dbUrl.split("@")[1]?.split("/")[0] ?? "hidden") + ")" : ""}`);
console.log(`RESEND_API_KEY:      ${resendPresent ? "PRESENT" : "MISSING"}`);
console.log(`NEXT_PUBLIC_APP_URL: ${appUrlPresent ? appUrl : "MISSING"}`);
console.log(`EMAIL_FROM:          ${emailFrom}`);

let configOk = true;
if (!dbPresent)    { console.log(`${FAIL} DATABASE_URL is missing — add to .env.local`);           configOk = false; }
if (!resendPresent){ console.log(`${FAIL} RESEND_API_KEY is missing — add to .env.local`);         configOk = false; }
if (!appUrlPresent){ console.log(`${WARN} NEXT_PUBLIC_APP_URL missing — reset links will be broken`); }

// ── 2. Email normalization ────────────────────────────────────────────────────

banner("2. Email Normalization (mirrors route schema)");

console.log(`raw input:           "${rawEmail}"`);
console.log(`normalized:          "${normalized}"`);
console.log(`emailHash (SHA-256): ${emailHash}  ← search this in Vercel Logs`);
console.log(`\n  Use this in Vercel → Functions → forgot-password → Filter by: ${emailHash}`);

// ── 3. Database lookup ────────────────────────────────────────────────────────

banner("3. Database Lookup (production DB)");

if (!dbPresent) {
  console.log(`${FAIL} Cannot query DB — DATABASE_URL missing.`);
  console.log(`  Add DATABASE_URL to .env.local and re-run.`);
  console.log(`  → This is the most likely root cause if the production DB differs from local.`);
} else {
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
        created_at,
        updated_at
      FROM users
      WHERE lower(trim(email)) = ${normalized}
      LIMIT 1
    `;

    if (rows.length === 0) {
      console.log(`${FAIL} userFound: false`);
      console.log(`\n  The email does NOT exist in the production users table.`);
      console.log(`  Root causes to check:`);
      console.log(`    a) Account was created locally (different DB) — not on production.`);
      console.log(`    b) Account registered with a different email address.`);
      console.log(`    c) Vercel's DATABASE_URL points to a different DB than .env.local.`);
      console.log(`    d) Email was entered with a typo.`);
      console.log(`\n  → Fix: Register an account on https://www.oqul.tech/register`);
      console.log(`         then use THAT email for forgot-password.`);
    } else {
      const row = rows[0];
      const now = new Date();
      const hasExpiredToken = row.password_reset_expires_at
        ? now > new Date(row.password_reset_expires_at)
        : null;

      console.log(`${PASS} userFound: true`);
      console.log(`  userId (redacted):         ${redact(row.id)}`);
      console.log(`  hasPasswordHash:           ${row.has_password_hash}`);
      console.log(`  emailVerified:             ${row.email_verified}`);
      console.log(`  hasPendingResetToken:      ${row.has_pending_reset_token}`);

      if (row.has_pending_reset_token) {
        console.log(`  resetTokenExpired:         ${hasExpiredToken}`);
        console.log(`  resetTokenExpiresAt:       ${row.password_reset_expires_at}`);
      }

      console.log(`  accountCreatedAt:          ${row.created_at}`);

      if (!row.has_password_hash) {
        console.log(`\n${WARN} User has NO password hash.`);
        console.log(`  This account may have been created via OAuth (Google/GitHub) without setting a password.`);
        console.log(`  The forgot-password flow WILL still set a new password — bcrypt is applied during reset.`);
      }

      if (!row.email_verified) {
        console.log(`\n${WARN} Email is not verified.`);
        console.log(`  Forgot-password still works for unverified emails.`);
      }
    }
  } catch (err) {
    console.log(`${FAIL} DB query failed: ${err.message}`);
    console.log(`  → Check DATABASE_URL in .env.local is the PRODUCTION Neon URL.`);
  } finally {
    await sql.end();
  }
}

// ── 4. Resend API key validation ──────────────────────────────────────────────

banner("4. Resend API Key & Domain Verification");

if (!resendPresent) {
  console.log(`${FAIL} RESEND_API_KEY not set — cannot validate.`);
} else {
  try {
    // GET /domains returns list of verified domains — validates key without sending email
    const resp = await fetch("https://api.resend.com/domains", {
      method:  "GET",
      headers: { "Authorization": `Bearer ${resendKey}` },
    });

    if (resp.status === 401) {
      console.log(`${FAIL} API key INVALID (401 Unauthorized).`);
      console.log(`  → Fix: Update RESEND_API_KEY in Vercel with the correct key from resend.com.`);
    } else if (resp.status === 200) {
      const data = await resp.json();
      const domains = data?.data ?? [];
      const verifiedDomains = domains
        .filter(d => d.status === "verified")
        .map(d => d.name);

      console.log(`${PASS} API key is VALID.`);
      console.log(`  Verified domains in Resend: ${verifiedDomains.length === 0 ? "(none)" : verifiedDomains.join(", ")}`);

      // Check EMAIL_FROM domain vs verified domains
      const fromDomain = domainOf(process.env.EMAIL_FROM ?? "no-reply@oqul.tech");
      const fallbackDomain = "oqul.tech";
      const effectiveDomain = fromDomain || fallbackDomain;

      console.log(`  EMAIL_FROM domain:          ${effectiveDomain}`);

      const domainMatch = verifiedDomains.some(d =>
        d === effectiveDomain || effectiveDomain.endsWith("." + d)
      );

      if (verifiedDomains.length === 0) {
        console.log(`${FAIL} No verified domains found in Resend.`);
        console.log(`  → Fix: Go to resend.com → Domains → Verify ${effectiveDomain}`);
      } else if (!domainMatch) {
        console.log(`${FAIL} EMAIL_FROM domain "${effectiveDomain}" is NOT in verified domains.`);
        console.log(`  → Fix: Either verify "${effectiveDomain}" in Resend,`);
        console.log(`          or set EMAIL_FROM in Vercel to use a verified domain.`);
        console.log(`  → Alternatively: set EMAIL_FROM=onboarding@resend.dev for testing.`);
      } else {
        console.log(`${PASS} EMAIL_FROM domain "${effectiveDomain}" is VERIFIED in Resend.`);
      }
    } else {
      const body = await resp.text();
      console.log(`${WARN} Resend returned HTTP ${resp.status}: ${body.slice(0, 200)}`);
    }
  } catch (err) {
    console.log(`${FAIL} Could not reach Resend API: ${err.message}`);
    console.log(`  → Check internet connectivity.`);
  }
}

// ── 5. Reset link preview ─────────────────────────────────────────────────────

banner("5. Reset Link Preview");

const baseUrl = appUrl ?? "http://localhost:3000";
const linkPreview = `${baseUrl}/reset-password?token=<64-char-hex-token>`;
console.log(`  Reset link format: ${linkPreview}`);

if (!appUrlPresent) {
  console.log(`${FAIL} NEXT_PUBLIC_APP_URL is not set.`);
  console.log(`  In production this throws EmailDeliveryError("EMAIL_CONFIG_MISSING")`);
  console.log(`  — the email is NEVER sent, but the API still returns 200.`);
  console.log(`  → Fix: In Vercel → Settings → Environment Variables → add:`);
  console.log(`         NEXT_PUBLIC_APP_URL = https://www.oqul.tech`);
  console.log(`         Then click Redeploy.`);
} else {
  console.log(`${PASS} NEXT_PUBLIC_APP_URL is set correctly.`);
  if (!baseUrl.startsWith("https://")) {
    console.log(`${WARN} URL does not start with https:// — check if this is the correct production URL.`);
  }
}

// ── 6. Summary & next steps ───────────────────────────────────────────────────

banner("6. Summary & Next Steps");

console.log(`  emailHash for Vercel Logs: ${emailHash}`);
console.log(`\n  After submitting forgot-password on the website:`);
console.log(`    1. Open Vercel → Project → Functions → /api/auth/forgot-password`);
console.log(`    2. Filter logs by: ${emailHash}`);
console.log(`    3. Look for these log lines:`);
console.log(`       [forgot-password] email config   → RESEND_API_KEY/NEXT_PUBLIC_APP_URL PRESENT/MISSING`);
console.log(`       [forgot-password] user lookup    → { userFound: true/false }`);
console.log(`       [forgot-password] email send accepted → { resendId: "..." }`);
console.log(`       [forgot-password] email failed   → { code: "RESEND_SENDER_REJECTED"|... }`);
console.log(`\n  If resendId is present in logs:`);
console.log(`    → Open resend.com → Emails → search for that resendId`);
console.log(`    → Check if it shows: delivered / bounced / suppressed`);
console.log(`    → Check Gmail → Spam / Junk folder`);
console.log(`\n  Vercel env vars required in Production environment:`);
console.log(`    RESEND_API_KEY        = re_xxxx...`);
console.log(`    EMAIL_FROM            = Oqul <no-reply@oqul.tech>`);
console.log(`    NEXT_PUBLIC_APP_URL   = https://www.oqul.tech`);
console.log(`    DATABASE_URL          = postgresql://... (Neon production URL)`);
console.log(`\n  After any Vercel env change → Redeploy is required.`);

/**
 * scripts/verify-production-forgot-password.mjs
 *
 * End-to-end verification of the production forgot-password flow.
 * Calls all three debug endpoints and prints a pass/fail table.
 *
 * Usage:
 *   node scripts/verify-production-forgot-password.mjs \
 *     --email user@example.com \
 *     --base-url https://www.oqul.tech \
 *     --debug-secret YOUR_DEBUG_SECRET
 *
 * The debug-secret must match the DEBUG_SECRET env var set in Vercel.
 */

// ── Args ──────────────────────────────────────────────────────────────────────

const args = process.argv.slice(2);
function getArg(flag) {
  const i = args.indexOf(flag);
  return i !== -1 ? args[i + 1] : undefined;
}

const email       = getArg("--email");
const baseUrl     = (getArg("--base-url") ?? "").replace(/\/$/, "");
const debugSecret = getArg("--debug-secret");

if (!email?.includes("@") || !baseUrl || !debugSecret) {
  console.error("Usage:");
  console.error("  node scripts/verify-production-forgot-password.mjs \\");
  console.error("    --email user@example.com \\");
  console.error("    --base-url https://www.oqul.tech \\");
  console.error("    --debug-secret YOUR_DEBUG_SECRET");
  process.exit(1);
}

// ── Helpers ───────────────────────────────────────────────────────────────────

const headers = {
  "Authorization": `Bearer ${debugSecret}`,
  "Content-Type":  "application/json",
};

function pass(label, detail = "") {
  console.log(`  ✅  ${label}${detail ? "  →  " + detail : ""}`);
}
function fail(label, detail = "") {
  console.log(`  ❌  ${label}${detail ? "  →  " + detail : ""}`);
}
function warn(label, detail = "") {
  console.log(`  ⚠️   ${label}${detail ? "  →  " + detail : ""}`);
}
function info(label, detail = "") {
  console.log(`  ℹ️   ${label}${detail ? "  →  " + detail : ""}`);
}

async function callEndpoint(method, path, body) {
  const url = `${baseUrl}${path}`;
  try {
    const res = await fetch(url, {
      method,
      headers,
      ...(body ? { body: JSON.stringify(body) } : {}),
    });
    const text = await res.text();
    let json = null;
    try { json = JSON.parse(text); } catch { /* not JSON */ }
    return { status: res.status, ok: res.ok, json, text };
  } catch (err) {
    return { status: 0, ok: false, json: null, text: "", networkError: err.message };
  }
}

// ── Run ───────────────────────────────────────────────────────────────────────

console.log("══════════════════════════════════════════════════════════════");
console.log("  Oqul Production — Forgot-Password Flow Verification");
console.log("══════════════════════════════════════════════════════════════");
console.log(`  base URL : ${baseUrl}`);
console.log(`  email    : ${email}`);
console.log("══════════════════════════════════════════════════════════════\n");

// ── 1. Health Check ───────────────────────────────────────────────────────────

console.log("── Step 1: Health Check (/api/debug/forgot-password-health) ──\n");

const health = await callEndpoint("GET", "/api/debug/forgot-password-health");

if (health.networkError) {
  fail("Endpoint reachable", health.networkError);
  console.log("\n→ Cannot reach the server. Check base URL and network.");
  process.exit(1);
}

if (health.status === 401) {
  fail("Auth", "DEBUG_SECRET rejected (401). Verify --debug-secret matches Vercel DEBUG_SECRET.");
  process.exit(1);
}

if (!health.ok || !health.json) {
  fail("Health endpoint", `HTTP ${health.status} — ${health.text.slice(0, 200)}`);
  process.exit(1);
}

const h = health.json;

// NODE_ENV
if (h.runtime?.NODE_ENV === "production") {
  pass("NODE_ENV", "production");
} else {
  warn("NODE_ENV", h.runtime?.NODE_ENV ?? "(missing)");
}

// NEXT_PUBLIC_APP_URL
const appUrl = h.email?.NEXT_PUBLIC_APP_URL;
if (!appUrl || appUrl === "MISSING") {
  fail("NEXT_PUBLIC_APP_URL", "MISSING — reset links will not work");
} else if (appUrl.includes("localhost") || appUrl.includes("127.0.0.1")) {
  fail("NEXT_PUBLIC_APP_URL", `${appUrl} ← LOCALHOST IN PRODUCTION — fix in Vercel env vars`);
} else if (!appUrl.startsWith("https://")) {
  warn("NEXT_PUBLIC_APP_URL", `${appUrl} ← not https — check if this is correct`);
} else {
  pass("NEXT_PUBLIC_APP_URL", appUrl);
}

// RESEND_API_KEY
if (h.email?.RESEND_API_KEY === "PRESENT") {
  pass("RESEND_API_KEY", "PRESENT");
} else {
  fail("RESEND_API_KEY", "MISSING — no emails will be sent");
}

// EMAIL_FROM domain
const fromDomain = h.email?.EMAIL_FROM_DOMAIN;
if (fromDomain && fromDomain !== "(default: oqul.tech)") {
  if (fromDomain.includes("oqul.tech")) {
    pass("EMAIL_FROM_DOMAIN", fromDomain);
  } else {
    warn("EMAIL_FROM_DOMAIN", `${fromDomain} ← verify this domain is verified in Resend`);
  }
} else {
  info("EMAIL_FROM_DOMAIN", "(default: oqul.tech)");
}

// DB
if (h.database?.status === "connected") {
  pass("DATABASE", `connected to ${h.database.host}`);
} else if (h.database?.status === "failed") {
  fail("DATABASE", h.database.error ?? "connection failed");
} else {
  fail("DATABASE_URL", "MISSING — cannot look up users");
}

// Request headers
info("Canonical host",   h.request?.canonicalHost   ?? "(unknown)");
info("x-forwarded-host", h.request?.xForwardedHost  ?? "(none)");
info("x-forwarded-proto",h.request?.xForwardedProto ?? "(none)");

console.log();

// ── 2. Test Email Send ────────────────────────────────────────────────────────

console.log("── Step 2: Test Email (/api/debug/send-test-email) ──────────\n");

const testEmail = await callEndpoint("POST", "/api/debug/send-test-email", { to: email });

if (testEmail.networkError) {
  fail("Test email endpoint", testEmail.networkError);
} else if (testEmail.status === 401) {
  fail("Test email auth", "DEBUG_SECRET rejected");
} else if (testEmail.json?.ok) {
  pass("Test email send accepted", `resendId: ${testEmail.json.resendId ?? "(null — dev mode)"}`);
  if (testEmail.json.resendId) {
    info("Next step", `Open resend.com → Emails → search for resendId: ${testEmail.json.resendId}`);
  }
} else {
  const code    = testEmail.json?.code    ?? `HTTP ${testEmail.status}`;
  const details = testEmail.json?.details ?? testEmail.text.slice(0, 200);
  fail("Test email send failed", `${code}  →  ${details}`);

  if (code === "RESEND_INVALID_API_KEY") {
    info("Fix", "RESEND_API_KEY in Vercel is invalid or expired. Regenerate at resend.com/api-keys.");
  } else if (code === "RESEND_SENDER_REJECTED") {
    info("Fix", `The EMAIL_FROM domain (${fromDomain}) is not verified in Resend. Add & verify it at resend.com/domains.`);
  } else if (code === "RESEND_RATE_LIMITED") {
    info("Fix", "Rate limited by Resend. Wait a moment and retry.");
  } else if (code === "EMAIL_CONFIG_MISSING") {
    info("Fix", "RESEND_API_KEY or NEXT_PUBLIC_APP_URL missing in Vercel production env vars. Add and redeploy.");
  }
}

console.log();

// ── 3. Full Trace ─────────────────────────────────────────────────────────────

console.log("── Step 3: Full Flow Trace (/api/debug/trace-forgot-password) \n");

const trace = await callEndpoint("POST", "/api/debug/trace-forgot-password", { email });

if (trace.networkError) {
  fail("Trace endpoint", trace.networkError);
} else if (trace.status === 401) {
  fail("Trace auth", "DEBUG_SECRET rejected");
} else if (!trace.json) {
  fail("Trace endpoint", `HTTP ${trace.status} — ${trace.text.slice(0, 200)}`);
} else {
  const s = trace.json.steps ?? {};

  // DB lookup
  if (s.dbLookup === "ok") {
    if (s.userFound) {
      pass("DB user lookup", `found  (userId hash: ${s.userIdHash ?? "?"})`);
    } else {
      fail("DB user lookup", "user NOT found in production DB — account may not exist");
      info("Fix", "Register at https://www.oqul.tech/register and use that email for password reset.");
    }
  } else {
    fail("DB lookup", s.dbError ?? "failed");
  }

  // Reset token
  if (s.userFound) {
    s.resetTokenCreated ? pass("Reset token created") : fail("Reset token created", "failed");
    s.resetTokenStored  ? pass("Reset token stored in DB") : fail("Reset token stored in DB", "failed");

    // Email
    if (s.emailSendAttempted) {
      if (s.emailSendAccepted) {
        pass("Email accepted by Resend", `resendId: ${s.resendId ?? "(null)"}`);
      } else {
        fail("Email send failed", `${s.emailErrorCode}  →  ${s.emailErrorDetails ?? ""}`);
      }
    }
  }
}

console.log();

// ── Summary ───────────────────────────────────────────────────────────────────

console.log("══════════════════════════════════════════════════════════════");
console.log("  Vercel env vars that must be set in Production environment:");
console.log("══════════════════════════════════════════════════════════════");
console.log("  RESEND_API_KEY        = re_xxxx...");
console.log("  EMAIL_FROM            = Oqul <no-reply@oqul.tech>");
console.log("  NEXT_PUBLIC_APP_URL   = https://www.oqul.tech");
console.log("  DATABASE_URL          = postgresql://... (Neon production URL)");
console.log("  DEBUG_SECRET          = (random secret — keep private)");
console.log("══════════════════════════════════════════════════════════════");
console.log("  After any Vercel env change → Redeploy is required.");
console.log("══════════════════════════════════════════════════════════════\n");

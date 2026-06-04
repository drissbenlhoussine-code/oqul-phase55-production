/**
 * scripts/test-password-reset-email.mjs
 * Sends a single test password-reset email via Resend.
 * Does NOT touch the database, lessons, or curriculum data.
 * Never prints API keys or tokens.
 *
 * Usage: node scripts/test-password-reset-email.mjs <recipient@example.com>
 */
import dotenv from "dotenv";

dotenv.config({ path: ".env.local" });
dotenv.config({ path: ".env" });

// ── Arg check ────────────────────────────────────────────────────────────────
const [to] = process.argv.slice(2);
if (!to || !to.includes("@")) {
  console.error("Usage: node scripts/test-password-reset-email.mjs <recipient@example.com>");
  process.exit(1);
}

// ── Env check ────────────────────────────────────────────────────────────────
const apiKey = process.env.RESEND_API_KEY;
const from   = process.env.EMAIL_FROM ?? "Oqul <no-reply@oqul.ma>";
const appUrl = process.env.NEXT_PUBLIC_APP_URL ?? "http://localhost:3000";

console.log("── Environment ──────────────────────────────────────────────");
console.log(`RESEND_API_KEY:      ${apiKey && apiKey.trim() ? "PRESENT" : "MISSING"}`);
console.log(`EMAIL_FROM:          ${from}`);
console.log(`NEXT_PUBLIC_APP_URL: ${appUrl}`);
console.log(`Recipient:           ${to}`);
console.log("─────────────────────────────────────────────────────────────");

if (!apiKey || !apiKey.trim()) {
  console.error("\n❌ RESEND_API_KEY is missing. Add it to .env.local.");
  process.exit(1);
}

// ── Build test email ─────────────────────────────────────────────────────────
const resetLink = `${appUrl}/reset-password?token=TEST_TOKEN_NOT_VALID`;

const html = `<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head><meta charset="UTF-8" /><title>اختبار البريد</title></head>
<body style="font-family:Arial,sans-serif;direction:rtl;background:#F7F0E3;padding:40px;">
  <div style="max-width:560px;margin:auto;background:#fff;border-radius:16px;padding:32px;box-shadow:0 4px 24px rgba(0,0,0,0.08);">
    <h2 style="color:#1A1025;">🔑 اختبار: إعادة تعيين كلمة المرور</h2>
    <p style="color:#555;line-height:1.8;">
      هذه رسالة اختبار تأكيد لإعداد البريد الإلكتروني على منصة Oqul.
      الرابط أدناه <strong>غير صالح</strong> وليس رمزاً حقيقياً.
    </p>
    <div style="text-align:center;margin:32px 0;">
      <a href="${resetLink}"
         style="background:#C4622D;color:#fff;padding:16px 36px;border-radius:14px;font-size:16px;font-weight:700;text-decoration:none;display:inline-block;">
        رابط الاختبار (غير صالح) 🔑
      </a>
    </div>
    <p style="color:#999;font-size:12px;text-align:center;">
      إذا وصلت هذه الرسالة فإعداد Resend يعمل بنجاح. ✅
    </p>
  </div>
</body>
</html>`;

// ── Send ──────────────────────────────────────────────────────────────────────
console.log("\nSending test email via Resend…");

try {
  const res = await fetch("https://api.resend.com/emails", {
    method:  "POST",
    headers: {
      "Authorization": `Bearer ${apiKey}`,
      "Content-Type":  "application/json",
    },
    body: JSON.stringify({
      from,
      to,
      subject: "🔑 [TEST] إعادة تعيين كلمة المرور — Oqul",
      html,
    }),
  });

  const responseBody = await res.text();

  if (res.ok) {
    let messageId = "unknown";
    try { messageId = JSON.parse(responseBody).id ?? "unknown"; } catch {}
    console.log(`✅ Email sent successfully!`);
    console.log(`   Resend message ID: ${messageId}`);
    console.log(`   Recipient: ${to}`);
    console.log(`   From: ${from}`);
    console.log(`   App URL used: ${appUrl}`);
  } else {
    console.error(`\n❌ Resend returned HTTP ${res.status}`);
    console.error(`   Response: ${responseBody}`);

    // Structured diagnosis
    if (res.status === 401) {
      console.error("\n→ ROOT CAUSE: Invalid or missing API key.");
      console.error("  Fix: Verify RESEND_API_KEY in .env.local matches your Resend dashboard.");
      console.error("  Note: Check for non-ASCII characters (e.g. Cyrillic vs Latin letters).");
    } else if (res.status === 403) {
      console.error("\n→ ROOT CAUSE: Sender domain not verified.");
      console.error("  Fix: Go to resend.com → Domains → verify oqul.ma");
      console.error("  Or use onboarding@resend.dev as EMAIL_FROM for testing.");
    } else if (res.status === 422) {
      console.error("\n→ ROOT CAUSE: Invalid request payload.");
      console.error("  Fix: Check EMAIL_FROM format — expected: 'Name <email@domain>'");
    } else if (res.status === 429) {
      console.error("\n→ ROOT CAUSE: Rate limit exceeded.");
      console.error("  Fix: Wait and retry.");
    } else {
      console.error("\n→ Unexpected error. Check the Resend dashboard for details.");
    }
    process.exit(1);
  }
} catch (err) {
  console.error("\n❌ Network error — could not reach Resend API.");
  console.error(`   ${err.message}`);
  console.error("→ Fix: Check internet connectivity and that api.resend.com is reachable.");
  process.exit(1);
}

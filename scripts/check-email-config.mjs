/**
 * scripts/check-email-config.mjs
 * Checks whether all required email environment variables are present.
 * Never prints secret values.
 *
 * Usage: node scripts/check-email-config.mjs
 */
import dotenv from "dotenv";

dotenv.config({ path: ".env.local" });
dotenv.config({ path: ".env" });

const REQUIRED = ["RESEND_API_KEY", "NEXT_PUBLIC_APP_URL", "EMAIL_FROM"];

let allPresent = true;

console.log("── Email Configuration Check ─────────────────────────────────");
for (const name of REQUIRED) {
  const val = process.env[name];
  const present = Boolean(val && val.trim());
  console.log(`${name}: ${present ? "PRESENT" : "MISSING"}`);
  if (!present) allPresent = false;
}
console.log("──────────────────────────────────────────────────────────────");

if (!allPresent) {
  console.error("\n❌ One or more required variables are missing.");
  console.error("   Add them to .env.local (development) or your hosting provider (production).");
  process.exit(1);
} else {
  console.log("\n✅ All required email variables are present.");
}

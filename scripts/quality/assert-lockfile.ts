import { existsSync } from "node:fs";

if (!existsSync("package-lock.json")) {
  console.error("");
  console.error("❌ package-lock.json is missing.");
  console.error("");
  console.error("This repository is frozen until a deterministic lockfile exists.");
  console.error("");
  console.error("Run in a machine with npm registry access:");
  console.error("");
  console.error("  rm -rf node_modules package-lock.json");
  console.error("  npm install");
  console.error("  npm ci");
  console.error("");
  console.error("Then commit package-lock.json.");
  console.error("");
  process.exit(1);
}

console.log("✅ package-lock.json exists.");

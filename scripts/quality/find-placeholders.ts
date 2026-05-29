import { readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";

const root = process.cwd();

const ignoredPathFragments = [
  "node_modules",
  ".next",
  ".git",
  "coverage",
  "tests/_removed_placeholder_tests",
  "tests/_removed_placeholder_tests_phase25_7",
  "docs/PHASE25_",
  "docs/COMPLEXITY_AUDIT.md",
  "docs/DETERMINISTIC_BUILD_CONTRACT.md",
];

const placeholderPatterns = [
  /expect\s*\(\s*true\s*\)\s*\.toBe\s*\(\s*true\s*\)/,
  /Validation architecture placeholder/i,
  /TODO:\s*production/i,
  /fake runtime/i,
  /placeholder implementation/i,
];

const findings: string[] = [];

function ignored(path: string) {
  return ignoredPathFragments.some((fragment) => path.includes(fragment));
}

function walk(dir: string) {
  for (const entry of readdirSync(dir)) {
    const path = join(dir, entry);
    if (ignored(path)) continue;

    const stat = statSync(path);

    if (stat.isDirectory()) {
      walk(path);
      continue;
    }

    if (!/\.(ts|tsx|js|mjs|md)$/.test(path)) continue;

    const content = readFileSync(path, "utf8");

    for (const pattern of placeholderPatterns) {
      if (pattern.test(content)) {
        findings.push(path.replace(root + "/", ""));
        break;
      }
    }
  }
}

walk(root);

if (findings.length > 0) {
  console.error("Placeholder/conceptual leftovers detected:");
  for (const finding of findings) console.error(`- ${finding}`);
  process.exit(1);
}

console.log("No placeholder/conceptual leftovers detected by quality scan.");

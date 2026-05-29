import { existsSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";

const productRoutes = [
  "src/app/api/auth/register/route.ts",
  "src/app/api/auth/login/route.ts",
  "src/app/api/auth/me/route.ts",
  "src/app/api/onboarding/route.ts",
  "src/app/api/lessons/route.ts",
  "src/app/api/progress/route.ts",
  "src/app/api/recommendations/route.ts",
  "src/app/api/ai/leila/route.ts",
];

const missing = productRoutes.filter((route) => !existsSync(route));

if (missing.length > 0) {
  console.error("Missing product runtime routes:");
  for (const route of missing) console.error(`- ${route}`);
  process.exit(1);
}

function countTsFiles(dir: string): number {
  if (!existsSync(dir)) return 0;
  let count = 0;

  for (const entry of readdirSync(dir)) {
    const path = join(dir, entry);
    const stat = statSync(path);

    if (stat.isDirectory()) count += countTsFiles(path);
    else if (/\.tsx?$/.test(entry)) count += 1;
  }

  return count;
}

const productCount =
  countTsFiles("src/app/api") +
  countTsFiles("src/server/learning") +
  countTsFiles("src/server/onboarding") +
  countTsFiles("src/server/recommendations");

const advancedInfraCount =
  countTsFiles("src/server/trust") +
  countTsFiles("src/server/routing");

console.log("Product/API TS files:", productCount);
console.log("Advanced trust/routing TS files:", advancedInfraCount);

if (productCount < 8) {
  console.error("Product runtime surface is too thin for the current infrastructure level.");
  process.exit(1);
}

console.log("Product balance audit passed.");

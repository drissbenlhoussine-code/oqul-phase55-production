import { readdirSync, statSync } from "node:fs";
import { join } from "node:path";

const root = process.cwd();

const frozenAreas = [
  "src/server/trust",
  "src/server/routing",
  "src/server/effects",
];

const counts: Record<string, number> = {};

function countFiles(dir: string) {
  let count = 0;
  try {
    for (const entry of readdirSync(join(root, dir))) {
      const path = join(root, dir, entry);
      const stat = statSync(path);
      if (stat.isDirectory()) {
        count += countFiles(join(dir, entry));
      } else if (/\.(ts|tsx)$/.test(entry)) {
        count += 1;
      }
    }
  } catch {
    return 0;
  }

  return count;
}

for (const area of frozenAreas) {
  counts[area] = countFiles(area);
}

console.log("Complexity audit:", counts);
console.log("Frozen advanced runtime areas must not expand until product/build maturity is proven.");

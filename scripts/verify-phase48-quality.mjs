import fs from "node:fs";
import path from "node:path";

const root = process.cwd();

const required = [
  "src/features/quality/types.ts",
  "src/features/quality/quality-engine.ts",
  "src/features/quality/remediation-engine.ts",
  "src/features/quality/exercise-quality.ts",
  "src/features/quality/learner-memory.ts",
  "src/app/api/learning/quality/route.ts",
  "src/features/primary/lib/primary-quality.ts",
  "src/features/primary/lib/primary-mini-games.ts",
  "src/features/middle-school/lib/middle-school-quality.ts",
  "src/features/middle-school/lib/misconception-map.ts",
  "src/features/secondary/lib/secondary-quality.ts",
  "src/features/secondary/lib/exam-correction-rubric.ts",
  "src/app/dashboard/quality-depth/page.tsx",
];

for (const rel of required) {
  if (!fs.existsSync(path.join(root, rel))) {
    console.error(`Missing ${rel}`);
    process.exit(1);
  }
}

console.log("Phase48 quality depth layer verified.");
console.log(`Checked files: ${required.length}`);
import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const dataDir = path.join(root, "src", "features", "secondary", "data");

if (!fs.existsSync(dataDir)) {
  console.error("Missing secondary data directory");
  process.exit(1);
}

let total = 0;
let files = 0;

for (const grade of fs.readdirSync(dataDir)) {
  const gradeDir = path.join(dataDir, grade);
  if (!fs.statSync(gradeDir).isDirectory()) continue;

  for (const file of fs.readdirSync(gradeDir)) {
    if (!file.endsWith(".json")) continue;
    files++;
    const data = JSON.parse(fs.readFileSync(path.join(gradeDir, file), "utf8"));
    total += data.length;
  }
}

const required = [
  "src/features/secondary/lib/secondary-curriculum.ts",
  "src/features/secondary/lib/bac-exam-engine.ts",
  "src/features/secondary/lib/reasoning-tutor.ts",
  "src/app/api/learning/secondary/route.ts",
  "src/app/dashboard/secondary-school/page.tsx",
];

for (const rel of required) {
  if (!fs.existsSync(path.join(root, rel))) {
    console.error(`Missing ${rel}`);
    process.exit(1);
  }
}

console.log("Phase47 secondary layer verified.");
console.log(`Files: ${files}`);
console.log(`Lessons: ${total}`);
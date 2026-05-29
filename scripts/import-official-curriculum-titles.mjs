import fs from "node:fs";
import path from "node:path";

const target = path.join(process.cwd(), "curriculum-registry", "verified-official-curriculum.json");

if (!fs.existsSync(target)) {
  fs.writeFileSync(target, JSON.stringify({
    instructions: [
      "Fill this file with verified lesson titles from TelmidTICE.",
      "Use Moutamadris and AlloSchool only for cross-checking order/coverage.",
      "Do not copy lesson explanations. Titles/order only."
    ],
    items: []
  }, null, 2), "utf8");

  console.log("Created:", target);
  console.log("Now fill items with verified official lesson titles.");
  process.exit(0);
}

const data = JSON.parse(fs.readFileSync(target, "utf8"));
console.log("Verified official curriculum items:", data.items?.length ?? 0);
console.log("Next: connect this file to deep lesson reconstruction.");
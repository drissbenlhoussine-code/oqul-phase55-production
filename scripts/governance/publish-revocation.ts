import { publishRevocationEvent } from "@/server/governance/reactive-revocation";

async function main() {
  const subjectType = process.env.SUBJECT_TYPE as
    | "trust-anchor"
    | "provider-key"
    | "delegation"
    | "worker"
    | "route";
  const subjectId = process.env.SUBJECT_ID;
  const reason = process.env.REASON ?? "manual revocation";
  const issuedBy = process.env.ISSUED_BY ?? "operator";

  if (!subjectType || !subjectId) {
    throw new Error("SUBJECT_TYPE and SUBJECT_ID are required");
  }

  const result = await publishRevocationEvent({
    subjectType,
    subjectId,
    reason,
    issuedBy,
  });

  console.log("[governance] revocation published", result);
}

main().catch((error) => {
  console.error("[governance] publish failed", error);
  process.exit(1);
});

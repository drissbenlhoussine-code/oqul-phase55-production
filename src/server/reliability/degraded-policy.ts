export type RuntimeArea =
  | "auth"
  | "ai"
  | "billing"
  | "learning"
  | "analytics"
  | "public";

export type DegradedDecision = {
  allow: boolean;
  mode: "fail-open" | "fail-closed";
  reason: string;
};

const failClosedAreas = new Set<RuntimeArea>(["auth", "ai", "billing"]);

export function decideDegradedBehavior(area: RuntimeArea): DegradedDecision {
  if (failClosedAreas.has(area)) {
    return {
      allow: false,
      mode: "fail-closed",
      reason: `${area} is sensitive and must fail closed during degraded runtime.`,
    };
  }

  return {
    allow: true,
    mode: "fail-open",
    reason: `${area} can run in degraded mode with reduced guarantees.`,
  };
}

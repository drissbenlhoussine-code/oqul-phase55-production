export function scopeMatches(input: {
  grantedScope: string;
  requestedScope: string;
}) {
  if (input.grantedScope === input.requestedScope) return true;

  if (input.grantedScope.endsWith(".*")) {
    const prefix = input.grantedScope.slice(0, -2);
    return input.requestedScope === prefix || input.requestedScope.startsWith(`${prefix}.`);
  }

  return false;
}

export function isScopeDenied(input: {
  denyScope?: string | null;
  requestedScope: string;
}) {
  if (!input.denyScope) return false;

  return input.denyScope
    .split(",")
    .map((scope) => scope.trim())
    .filter(Boolean)
    .some((scope) =>
      scopeMatches({
        grantedScope: scope,
        requestedScope: input.requestedScope,
      })
    );
}

export function assertScopeAllowed(input: {
  grantedScope: string;
  requestedScope: string;
  denyScope?: string | null;
}) {
  if (isScopeDenied({ denyScope: input.denyScope, requestedScope: input.requestedScope })) {
    return {
      allowed: false,
      reason: "scope explicitly denied",
    };
  }

  if (!scopeMatches({ grantedScope: input.grantedScope, requestedScope: input.requestedScope })) {
    return {
      allowed: false,
      reason: "scope not covered by delegation",
    };
  }

  return {
    allowed: true,
    reason: "scope allowed",
  };
}

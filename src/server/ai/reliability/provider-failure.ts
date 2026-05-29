export type ProviderFailure = {
  provider: string;
  model?: string;
  reason: "timeout" | "rate-limit" | "server-error" | "unknown";
  occurredAt: string;
};

export function classifyProviderFailure(status?: number): ProviderFailure["reason"] {
  if (!status) return "unknown";
  if (status === 408 || status === 504) return "timeout";
  if (status === 429) return "rate-limit";
  if (status >= 500) return "server-error";
  return "unknown";
}

export function detectPromptAbuse(input: string) {
  const suspiciousPatterns = [
    "ignore previous instructions",
    "system prompt",
    "developer message",
  ];

  return suspiciousPatterns.some((pattern) =>
    input.toLowerCase().includes(pattern)
  );
}

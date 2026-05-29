export function getRetryDelay(attempt: number) {
  return Math.min(1000 * 2 ** attempt, 30000);
}

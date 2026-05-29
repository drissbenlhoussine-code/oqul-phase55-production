export function calculateReconnectDelay(attempt: number) {
  const capped = Math.min(attempt, 10);

  return Math.min(1000 * 2 ** capped, 30000);
}

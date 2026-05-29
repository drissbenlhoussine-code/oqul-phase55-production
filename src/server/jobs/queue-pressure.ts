export function detectQueueSaturation(
  waiting: number,
  active: number,
  threshold = 500
) {
  return waiting + active >= threshold;
}

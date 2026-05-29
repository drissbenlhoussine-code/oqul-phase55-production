const processedKeys = new Set<string>();

export function hasProcessedKey(key: string) {
  return processedKeys.has(key);
}

export function markProcessedKey(key: string) {
  processedKeys.add(key);
}

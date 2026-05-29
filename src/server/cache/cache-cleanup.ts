import { memoryCache } from "./memory-cache";

/**
 * Foundation cleanup scheduler.
 * Real production cleanup should use Redis TTL or LRU eviction.
 */
export function startMemoryCacheCleanup(intervalMs = 60_000) {
  return setInterval(() => {
    const store = (memoryCache as unknown as { store?: Map<string, { expiresAt: number }> }).store;
    if (!store) return;
    const now = Date.now();

    for (const [key, entry] of store.entries()) {
      if (entry.expiresAt < now) {
        store.delete(key);
      }
    }
  }, intervalMs);
}

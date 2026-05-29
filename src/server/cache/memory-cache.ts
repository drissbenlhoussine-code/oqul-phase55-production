import type { CacheEntry, CacheOptions, CacheStore } from "./cache-types";

export class MemoryCacheStore implements CacheStore {
  private readonly store = new Map<string, CacheEntry<unknown>>();

  async get<T>(key: string): Promise<T | null> {
    const entry = this.store.get(key);
    if (!entry) return null;

    if (Date.now() > entry.expiresAt) {
      this.store.delete(key);
      return null;
    }

    return entry.value as T;
  }

  async set<T>(key: string, value: T, options: CacheOptions): Promise<void> {
    this.store.set(key, {
      value,
      expiresAt: Date.now() + options.ttlMs,
    });
  }

  async delete(key: string): Promise<void> {
    this.store.delete(key);
  }
}

export const memoryCache = new MemoryCacheStore();

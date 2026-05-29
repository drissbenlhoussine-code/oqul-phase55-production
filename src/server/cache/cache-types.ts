export type CacheEntry<T> = {
  value: T;
  expiresAt: number;
};

export type CacheOptions = {
  ttlMs: number;
};

export interface CacheStore {
  get<T>(key: string): Promise<T | null>;
  set<T>(key: string, value: T, options: CacheOptions): Promise<void>;
  delete(key: string): Promise<void>;
}

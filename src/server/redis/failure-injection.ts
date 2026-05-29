export type RedisFailureMode =
  | "none"
  | "timeout"
  | "disconnect"
  | "reconnect-storm";

let currentFailureMode: RedisFailureMode = "none";

export function setRedisFailureMode(mode: RedisFailureMode) {
  currentFailureMode = mode;
}

export function getRedisFailureMode() {
  return currentFailureMode;
}

export async function withRedisFailureInjection<T>(
  operation: () => Promise<T>,
  fallback: T
): Promise<T> {
  if (currentFailureMode === "timeout") {
    await new Promise((resolve) => setTimeout(resolve, 50));
    return fallback;
  }

  if (currentFailureMode === "disconnect") {
    return fallback;
  }

  if (currentFailureMode === "reconnect-storm") {
    return fallback;
  }

  return operation();
}

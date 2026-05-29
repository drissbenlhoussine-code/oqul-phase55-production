/**
 * Placeholder Sentry integration foundation.
 */

export function captureException(error: unknown) {
  console.error("[SENTRY_CAPTURE]", error);
}

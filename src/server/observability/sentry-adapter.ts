import * as Sentry from "@sentry/nextjs";

export function reportRuntimeError(
  error: unknown,
  context?: Record<string, unknown>
) {
  Sentry.withScope((scope) => {
    if (context) {
      for (const [key, value] of Object.entries(context)) {
        scope.setExtra(key, value);
      }
    }

    Sentry.captureException(error);
  });
}

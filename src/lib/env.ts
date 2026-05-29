import { z } from "zod";

/**
 * Central environment validation for OQUL.
 * Phase 31: Added RESEND_API_KEY and EMAIL_FROM.
 *
 * Rules:
 * - This file is safe to exist before the database/auth phases.
 * - Server variables may be optional during development.
 * - Do not import this file inside client components unless you only use `clientEnv`.
 * - Server code should use `getServerEnv()` when it needs secrets.
 */

const emptyStringToUndefined = (value: unknown) => (value === "" ? undefined : value);

const serverEnvSchema = z.object({
  NODE_ENV:                  z.enum(["development", "test", "production"]).default("development"),
  DATABASE_URL:              z.preprocess(emptyStringToUndefined, z.string().url().optional()),
  AUTH_SECRET:               z.preprocess(emptyStringToUndefined, z.string().min(32).optional()),
  GROQ_API_KEY:              z.preprocess(emptyStringToUndefined, z.string().min(10).optional()),
  UPSTASH_REDIS_REST_URL:    z.preprocess(emptyStringToUndefined, z.string().url().optional()),
  UPSTASH_REDIS_REST_TOKEN:  z.preprocess(emptyStringToUndefined, z.string().optional()),
  // Phase 31 — Email
  RESEND_API_KEY:            z.preprocess(emptyStringToUndefined, z.string().optional()),
  EMAIL_FROM:                z.preprocess(emptyStringToUndefined, z.string().optional()),
});

const clientEnvSchema = z.object({
  NEXT_PUBLIC_APP_URL: z.string().url().default("http://localhost:3000"),
});

export type ServerEnv = z.infer<typeof serverEnvSchema>;
export type ClientEnv = z.infer<typeof clientEnvSchema>;

export function getServerEnv(): ServerEnv {
  const parsed = serverEnvSchema.safeParse(process.env);

  if (!parsed.success) {
    const issues = parsed.error.issues
      .map((issue) => `${issue.path.join(".")}: ${issue.message}`)
      .join("; ");
    throw new Error(`Invalid server environment configuration: ${issues}`);
  }

  return parsed.data;
}

export const clientEnv: ClientEnv = clientEnvSchema.parse({
  NEXT_PUBLIC_APP_URL: process.env.NEXT_PUBLIC_APP_URL ?? "http://localhost:3000",
});

/**
 * Use this helper when a feature truly requires an env var at runtime.
 * Gives a clear error message pointing to .env.example.
 */
export function requireEnv(name: keyof ServerEnv): string {
  const value = getServerEnv()[name];

  if (!value) {
    throw new Error(
      `Missing required environment variable: ${name}\n` +
      `See .env.example for setup instructions.`
    );
  }

  return String(value);
}

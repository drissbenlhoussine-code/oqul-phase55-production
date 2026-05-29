import { z } from "zod";

export const emailSchema = z.string().email();
export const passwordSchema = z.string().min(8).max(128);
export const idSchema = z.string().min(1);

export const paginationSchema = z.object({
  limit: z.coerce.number().int().min(1).max(100).default(20),
  cursor: z.string().optional(),
});

export function parseJsonBody<T>(schema: z.ZodSchema<T>, value: unknown): T {
  return schema.parse(value);
}

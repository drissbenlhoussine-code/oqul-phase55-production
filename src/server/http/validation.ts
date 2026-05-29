import { z } from "zod";
import { AppError } from "@/server/errors/app-error";
import { ERROR_CODES } from "@/server/errors/error-codes";

export function validateBody<TSchema extends z.ZodTypeAny>(
  schema: TSchema,
  input: unknown
): z.infer<TSchema> {
  const result = schema.safeParse(input);

  if (!result.success) {
    throw new AppError(
      "Invalid request payload",
      ERROR_CODES.VALIDATION_ERROR,
      400
    );
  }

  return result.data;
}

export function validateSearchParams<TSchema extends z.ZodTypeAny>(
  schema: TSchema,
  searchParams: URLSearchParams
): z.infer<TSchema> {
  const input = Object.fromEntries(searchParams.entries());
  return validateBody(schema, input);
}

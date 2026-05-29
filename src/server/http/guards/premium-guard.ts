import { AppError } from "@/server/errors/app-error";
import { ERROR_CODES } from "@/server/errors/error-codes";

export function requirePremium(plan: string) {
  if (plan === "free") {
    throw new AppError("Premium subscription required", ERROR_CODES.FORBIDDEN, 403);
  }
}

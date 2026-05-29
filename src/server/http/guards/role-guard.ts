import { AppError } from "@/server/errors/app-error";
import { ERROR_CODES } from "@/server/errors/error-codes";

export function requireRole(currentRole: string, allowedRoles: string[]) {
  if (!allowedRoles.includes(currentRole)) {
    throw new AppError("Insufficient permissions", ERROR_CODES.FORBIDDEN, 403);
  }
}

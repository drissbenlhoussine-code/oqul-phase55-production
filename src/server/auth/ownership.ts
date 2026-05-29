/**
 * Centralized ownership enforcement.
 * Every endpoint that touches child data MUST call one of these.
 */
import { childrenRepo } from "@/server/repositories/children";
import { AppError } from "@/server/errors";

/**
 * Verify that childId belongs to userId.
 * Throws FORBIDDEN if not. Returns the child if valid.
 */
export async function assertOwnsChild(userId: string, childId: string) {
  const children = await childrenRepo.findByUser(userId);
  const child = children.find((c) => c.id === childId);
  if (!child) {
    throw new AppError(
      "ليس لديك صلاحية الوصول لهذا الطفل",
      "FORBIDDEN",
      403
    );
  }
  return child;
}

/**
 * Verify userId owns AT LEAST ONE child (for listing-style endpoints).
 */
export async function getOwnedChildren(userId: string) {
  return childrenRepo.findByUser(userId);
}

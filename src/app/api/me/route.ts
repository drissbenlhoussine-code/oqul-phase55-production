import { requireAuth } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";
import { usersRepo } from "@/server/repositories/users";
import { AppError } from "@/server/errors";

export async function GET() {
  try {
    const session = await requireAuth();
    const user = await usersRepo.findById(session.sub);
    if (!user) throw new AppError("المستخدم غير موجود", "NOT_FOUND", 404);
    return ok({
      id: user.id,
      fullName: user.fullName,
      email: user.email,
      plan: user.plan,
      trialEndsAt: user.trialEndsAt,
      isOnTrial: user.trialEndsAt ? new Date(user.trialEndsAt) > new Date() : false,
    });
  } catch (e) {
    return errorResponse(e);
  }
}

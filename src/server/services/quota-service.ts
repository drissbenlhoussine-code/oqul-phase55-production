import { AppError } from "@/server/errors/app-error";
import { ERROR_CODES } from "@/server/errors/error-codes";
import { progressRepo } from "@/server/repositories/progress";

export type QuotaFeature = "leila_text" | "leila_voice" | "quiz" | "lesson";

const FREE_LIMITS: Record<QuotaFeature, number> = {
  leila_text:  30,
  leila_voice: 0,
  quiz:        50,
  lesson:      200,
};

const PAID_LIMITS: Record<QuotaFeature, number> = {
  leila_text:  200,
  leila_voice: 50,
  quiz:        500,
  lesson:      10000,
};

export class QuotaService {
  async assertWithinQuota(userId: string, feature: QuotaFeature, plan = "free") {
    const limits = plan === "free" ? FREE_LIMITS : PAID_LIMITS;
    const limit = limits[feature];

    if (limit <= 0) {
      throw new AppError(
        "هذه الميزة غير متاحة في خطتك الحالية. يرجى الترقية.",
        ERROR_CODES.FORBIDDEN,
        403
      );
    }

    // Real DB-backed daily usage check
    const used = await progressRepo.getDailyAiUsage(userId, feature);

    if (used >= limit) {
      throw new AppError(
        `وصلت إلى حد الاستخدام اليومي (${limit} مرة). يرجى المحاولة غداً أو الترقية للمزيد.`,
        ERROR_CODES.FORBIDDEN,
        429
      );
    }

    return { userId, feature, allowed: true, used, limit, remaining: limit - used };
  }

  async getUsageSummary(userId: string, plan = "free") {
    const limits = plan === "free" ? FREE_LIMITS : PAID_LIMITS;
    const features: QuotaFeature[] = ["leila_text", "leila_voice", "quiz", "lesson"];

    const summary = await Promise.all(
      features.map(async (feature) => {
        const used = await progressRepo.getDailyAiUsage(userId, feature);
        return { feature, used, limit: limits[feature], remaining: Math.max(0, limits[feature] - used) };
      })
    );

    return summary;
  }
}

export const quotaService = new QuotaService();

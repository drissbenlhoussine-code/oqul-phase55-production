import { progressRepo } from "@/server/repositories/progress";
import { childrenRepo } from "@/server/repositories/children";

export interface Recommendation {
  type: "lesson" | "review" | "quiz";
  lessonId?: string;
  title: string;
  reason: string;
  priority: number;
}

export class RecommendationService {
  async getRecommendations(childId: string): Promise<Recommendation[]> {
    const [child, progress] = await Promise.all([
      childrenRepo.findById(childId),
      progressRepo.getChildProgress(childId),
    ]);

    const recommendations: Recommendation[] = [];

    // Recommend reviewing lessons that need review
    const needsReview = progress.filter((p) => p.status === "needs_review");
    for (const item of needsReview.slice(0, 2)) {
      recommendations.push({
        type:     "review",
        lessonId: item.lessonId,
        title:    `راجع: ${item.lesson?.titleAr ?? "درس سابق"}`,
        reason:   "أداؤك في هذا الدرس يحتاج تحسين",
        priority: 1,
      });
    }

    // Recommend in-progress lessons
    const inProgress = progress.filter((p) => p.status === "in_progress");
    for (const item of inProgress.slice(0, 2)) {
      recommendations.push({
        type:     "lesson",
        lessonId: item.lessonId,
        title:    `أكمل: ${item.lesson?.titleAr ?? "درس قيد التقدم"}`,
        reason:   "لم تُكمل هذا الدرس بعد",
        priority: 2,
      });
    }

    // If nothing specific, suggest taking a quiz
    if (recommendations.length === 0) {
      const completed = progress.filter((p) => p.status === "completed");
      if (completed.length > 0) {
        const random = completed[Math.floor(Math.random() * completed.length)];
        recommendations.push({
          type:     "quiz",
          lessonId: random.lessonId,
          title:    `اختبر نفسك: ${random.lesson?.titleAr ?? "درس مكتمل"}`,
          reason:   "المراجعة تثبت المعلومات",
          priority: 3,
        });
      }
    }

    // Add weak points info
    if (child?.weakPoints?.length) {
      recommendations.push({
        type:   "review",
        title:  `نقطة ضعف: ${child.weakPoints[0].topic}`,
        reason: "ليلى تنصح بمراجعة هذا الموضوع",
        priority: 1,
      });
    }

    return recommendations.sort((a, b) => a.priority - b.priority).slice(0, 4);
  }
}

export const recommendationService = new RecommendationService();

import { progressRepo } from "@/server/repositories/progress";
import { childrenRepo } from "@/server/repositories/children";

export type LearningSummary = {
  completedLessons: number;
  averageScore: number;
  weakPointCount: number;
  streakDays: number;
  xp: number;
};

export class LearningAnalyticsService {
  async getChildSummary(childId: string): Promise<LearningSummary> {
    const child = await childrenRepo.findById(childId);
    const progress = await progressRepo.getChildProgress(childId);

    const completedLessons = progress.filter((p) => p.status === "completed").length;
    const scores = progress.filter((p) => p.score != null).map((p) => p.score!);
    const averageScore = scores.length
      ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length)
      : 0;

    return {
      completedLessons,
      averageScore,
      weakPointCount: child?.weakPoints?.length ?? 0,
      streakDays: child?.streak ?? 0,
      xp: child?.xp ?? 0,
    };
  }
}

export const learningAnalyticsService = new LearningAnalyticsService();

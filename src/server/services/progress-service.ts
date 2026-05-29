import { progressRepo } from "@/server/repositories/progress";
import { childrenRepo } from "@/server/repositories/children";

export class ProgressService {
  async getUserProgress(userId: string) {
    const children = await childrenRepo.findByUser(userId);

    const allProgress = await Promise.all(
      children.map(async (child) => {
        const progress = await progressRepo.getChildProgress(child.id);
        const completed = progress.filter((p) => p.status === "completed").length;
        const scores = progress.filter((p) => p.score != null).map((p) => p.score!);
        const avgScore = scores.length ? scores.reduce((a, b) => a + b, 0) / scores.length : 0;

        return {
          childId: child.id,
          childName: child.name,
          xp: child.xp,
          streak: child.streak,
          completedLessons: completed,
          totalLessons: progress.length,
          avgScore: Math.round(avgScore),
          progress,
        };
      })
    );

    return allProgress;
  }

  async completeLesson(childId: string, lessonId: string, score?: number) {
    return progressRepo.upsertLessonProgress({
      childId,
      lessonId,
      status: "completed",
      score,
    });
  }
}

export const progressService = new ProgressService();

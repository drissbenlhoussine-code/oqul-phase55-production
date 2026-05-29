import { eq, desc, and, sql, gte } from "drizzle-orm";
import { db, lessonProgress, quizAttempts, weakPoints, children, aiUsageEvents } from "@/db";

export const progressRepo = {
  async getChildProgress(childId: string) {
    return db.query.lessonProgress.findMany({
      where: eq(lessonProgress.childId, childId),
      with: { lesson: { with: { unit: { with: { subject: true } } } } },
    });
  },

  async upsertLessonProgress(data: {
    childId: string;
    lessonId: string;
    status: "in_progress" | "completed" | "needs_review";
    score?: number;
    timeSpentSecs?: number;
  }) {
    const existing = await db.query.lessonProgress.findFirst({
      where: and(eq(lessonProgress.childId, data.childId), eq(lessonProgress.lessonId, data.lessonId)),
    });

    if (existing) {
      const [updated] = await db.update(lessonProgress)
        .set({ ...data, updatedAt: new Date(), completedAt: data.status === "completed" ? new Date() : existing.completedAt })
        .where(eq(lessonProgress.id, existing.id))
        .returning();
      return updated;
    }

    const [created] = await db.insert(lessonProgress).values({
      ...data,
      completedAt: data.status === "completed" ? new Date() : undefined,
    }).returning();
    return created;
  },

  async saveQuizAttempt(data: {
    childId: string;
    lessonId: string;
    score: number;
    totalPoints: number;
    earnedPoints: number;
    answers: Record<string, string>;
  }) {
    const [attempt] = await db.insert(quizAttempts).values(data).returning();

    // Update XP
    const xpGain = Math.round(data.earnedPoints * 0.5);
    await db.update(children).set({ xp: sql`xp + ${xpGain}` }).where(eq(children.id, data.childId));

    return attempt;
  },

  async getDailyAiUsage(userId: string, feature: string): Promise<number> {
    const startOfDay = new Date();
    startOfDay.setHours(0, 0, 0, 0);

    const result = await db
      .select({ count: sql<number>`count(*)::int` })
      .from(aiUsageEvents)
      .where(
        and(
          eq(aiUsageEvents.userId, userId),
          eq(aiUsageEvents.feature, feature as "leila_text" | "leila_voice" | "quiz" | "lesson"),
          gte(aiUsageEvents.createdAt, startOfDay),
        )
      );

    return result[0]?.count ?? 0;
  },

  async logAiUsage(data: {
    userId: string;
    feature: "leila_text" | "leila_voice" | "quiz" | "lesson";
    tokens: number;
    provider: string;
    model: string;
    success: boolean;
  }) {
    await db.insert(aiUsageEvents).values(data);
  },
};

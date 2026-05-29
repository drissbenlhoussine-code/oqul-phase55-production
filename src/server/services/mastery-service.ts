/**
 * Mastery Service — tracks topic mastery and updates weak points.
 * Called after every quiz to build an adaptive learning profile.
 */
import { and, eq, desc } from "drizzle-orm";
import { db, weakPoints, children, quizAttempts, lessonProgress } from "@/db";
import { sql } from "drizzle-orm";

export interface MasteryUpdate {
  childId:    string;
  subjectId:  string;
  topic:      string;
  score:      number;  // 0-100
}

export class MasteryService {
  /**
   * After a quiz, update the child's weak points for the subject.
   * Severity 1 = slight weakness, 3 = critical weakness.
   */
  async updateAfterQuiz(update: MasteryUpdate) {
    if (update.score >= 80) {
      // Remove weak point if mastered
      await db
        .delete(weakPoints)
        .where(
          and(
            eq(weakPoints.childId, update.childId),
            eq(weakPoints.topic, update.topic)
          )
        );
      return { action: "mastered", topic: update.topic };
    }

    const severity = update.score < 40 ? 3 : update.score < 60 ? 2 : 1;

    // Upsert weak point
    const existing = await db.query.weakPoints.findFirst({
      where: and(eq(weakPoints.childId, update.childId), eq(weakPoints.topic, update.topic)),
    });

    if (existing) {
      await db
        .update(weakPoints)
        .set({ severity: Math.max(existing.severity, severity), updatedAt: new Date() })
        .where(eq(weakPoints.id, existing.id));
    } else {
      await db.insert(weakPoints).values({
        childId:   update.childId,
        subjectId: update.subjectId,
        topic:     update.topic,
        severity,
      });
    }

    return { action: "weak_point_recorded", topic: update.topic, severity };
  }

  async getWeakPoints(childId: string) {
    return db.query.weakPoints.findMany({
      where: eq(weakPoints.childId, childId),
      with:  { subject: true },
      orderBy: desc(weakPoints.severity),
    });
  }

  /** Generate a mastery summary for the AI context */
  async buildAIContext(childId: string) {
    const [wps, progress] = await Promise.all([
      this.getWeakPoints(childId),
      db.query.lessonProgress.findMany({
        where: eq(lessonProgress.childId, childId),
        with:  { lesson: { with: { unit: { with: { subject: true } } } } },
      }),
    ]);

    const completed    = progress.filter((p) => p.status === "completed");
    const needsReview  = progress.filter((p) => p.status === "needs_review");
    const scores       = completed.filter((p) => p.score != null).map((p) => p.score!);
    const avgScore     = scores.length ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : 0;

    return {
      weakPoints:      wps.map((w) => w.topic),
      completedCount:  completed.length,
      needsReviewCount: needsReview.length,
      avgScore,
      recentErrors:    needsReview.slice(0, 3).map((p) => p.lesson?.titleAr ?? "").filter(Boolean),
    };
  }
}

export const masteryService = new MasteryService();

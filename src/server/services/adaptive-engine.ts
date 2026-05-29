import { getDueForReview } from "./spaced-repetition";
/**
 * Adaptive Progression Engine
 * Decides what the child should study next based on their actual performance.
 * This is the "intelligence" behind the learning experience.
 */
import { progressRepo } from "@/server/repositories/progress";
import { curriculumRepo } from "@/server/repositories/curriculum";
import { childrenRepo } from "@/server/repositories/children";

export type LearningAction =
  | { type: "review_lesson";  lessonId: string; lessonTitle: string; reason: string; urgency: "high" | "medium" }
  | { type: "next_lesson";    lessonId: string; lessonTitle: string; reason: string; urgency: "low" }
  | { type: "practice_quiz";  lessonId: string; lessonTitle: string; reason: string; urgency: "medium" }
  | { type: "ask_leila";      topic: string;    reason: string;      urgency: "medium" }
  | { type: "take_break";     reason: string;   urgency: "low" };

export interface LearningState {
  childId:         string;
  todayXP:         number;
  streak:          number;
  weakestTopics:   string[];
  nextLesson?:     { id: string; title: string };
  actions:         LearningAction[];
  engagementScore: number; // 0-100, drives notification urgency
}

export class AdaptiveEngine {
  /**
   * Analyze child's learning state and produce prioritized actions.
   * This runs on every dashboard load.
   */
  async analyze(childId: string): Promise<LearningState> {
    const [child, progress] = await Promise.all([
      childrenRepo.findById(childId),
      progressRepo.getChildProgress(childId),
    ]);

    const actions: LearningAction[] = [];

    const needsReview   = progress.filter((p) => p.status === "needs_review");
    const inProgress    = progress.filter((p) => p.status === "in_progress");
    const completed     = progress.filter((p) => p.status === "completed");
    const scores        = completed.filter((p) => p.score != null).map((p) => p.score!);
    const avgScore      = scores.length ? scores.reduce((a, b) => a + b, 0) / scores.length : 0;

    // 1. CRITICAL: Review failing lessons first
    for (const item of needsReview.slice(0, 2)) {
      const score = item.score ?? 0;
      actions.push({
        type:       "review_lesson",
        lessonId:   item.lessonId,
        lessonTitle: item.lesson?.titleAr ?? "درس سابق",
        reason:     score < 40
          ? `نتيجتك كانت ${Math.round(score)}% — ليلى تقترح مراجعة مهمة قبل المتابعة`
          : `حصلت على ${Math.round(score)}% — مراجعة سريعة ستثبت المعلومات`,
        urgency:    score < 40 ? "high" : "medium",
      });
    }

    // 1.5 SRS: lessons due for review based on spaced repetition
    const srsLessonIds = getDueForReview(progress.map((p) => ({
      lessonId:    p.lessonId,
      score:       p.score ?? undefined,
      completedAt: p.completedAt ?? null,
      status:      p.status,
    })));

    for (const lessonId of srsLessonIds.slice(0, 1)) {
      const item = progress.find((p) => p.lessonId === lessonId);
      if (item) {
        actions.push({
          type:       "review_lesson",
          lessonId,
          lessonTitle: item.lesson?.titleAr ?? "درس للمراجعة",
          reason:     `حان وقت مراجعة هذا الدرس — التكرار المتباعد يثبت المعلومات للأبد`,
          urgency:    "medium",
        });
      }
    }

    // 0. NEW USER: if no progress at all → suggest the first available lesson
    if (progress.length === 0 && child) {
      try {
        const { curriculumRepo } = await import("@/server/repositories/curriculum");
        const { db, subjects, units, lessons } = await import("@/db");
        const { eq, asc } = await import("drizzle-orm");
        // Find first subject for child's grade
        if (child.grade?.id) {
          const firstSubject = await db.query.subjects.findFirst({
            where: eq(subjects.gradeId, child.grade.id),
            orderBy: asc(subjects.orderIndex),
          });
          if (firstSubject) {
            const firstUnit = await db.query.units.findFirst({
              where: eq(units.subjectId, firstSubject.id),
              orderBy: asc(units.orderIndex),
            });
            if (firstUnit) {
              const firstLesson = await db.query.lessons.findFirst({
                where: eq(lessons.unitId, firstUnit.id),
                orderBy: asc(lessons.orderIndex),
              });
              if (firstLesson) {
                actions.push({
                  type:       "next_lesson",
                  lessonId:   firstLesson.id,
                  lessonTitle: firstLesson.titleAr,
                  reason:     "ابدأ رحلتك التعليمية مع ليلى — أول درس بانتظارك! 🌟",
                  urgency:    "low",
                });
              }
            }
          }
        }
        if (actions.length === 0) {
          // Fallback: suggest Leila chat
          actions.push({ type: "ask_leila", topic: "البداية", reason: "ليلى هنا لمساعدتك — اسألها أي شيء! 😊", urgency: "medium" });
        }
      } catch {}
    }

    // 2. Continue in-progress lessons
    for (const item of inProgress.slice(0, 1)) {
      actions.push({
        type:       "next_lesson",
        lessonId:   item.lessonId,
        lessonTitle: item.lesson?.titleAr ?? "الدرس المتوقف",
        reason:     "واصل من حيث توقفت — أنت في منتصف الطريق!",
        urgency:    "low",
      });
    }

    // 3. Suggest quiz on recently completed lessons
    const recentCompleted = completed.filter((p) => p.score == null || p.score < 80).slice(0, 1);
    for (const item of recentCompleted) {
      actions.push({
        type:       "practice_quiz",
        lessonId:   item.lessonId,
        lessonTitle: item.lesson?.titleAr ?? "درس مكتمل",
        reason:     "اختبر نفسك — المراجعة تثبت 80% من المعلومات",
        urgency:    "medium",
      });
    }

    // 4. If weak points, suggest Leila chat
    const weakPoints = child?.weakPoints ?? [];
    if (weakPoints.length > 0 && actions.length < 3) {
      actions.push({
        type:    "ask_leila",
        topic:   weakPoints[0].topic,
        reason:  `ليلى يمكنها شرح "${weakPoints[0].topic}" بطريقة مختلفة`,
        urgency: "medium",
      });
    }

    // 5. Break suggestion if overdoing it
    const todayXP = Math.min(child?.xp ?? 0, 500); // simplified
    if (completed.length > 5 && todayXP > 200) {
      actions.push({
        type:   "take_break",
        reason: "شطارة! خدت راحة صغيرة باش تثبت اللي تعلمتي",
        urgency: "low",
      });
    }

    // Engagement score: 100 if streak > 0, decreases with missed days
    const engagementScore = Math.min(100,
      (child?.streak ?? 0) * 15 +
      Math.min(completed.length * 5, 50) +
      (avgScore > 70 ? 20 : 0)
    );

    return {
      childId,
      todayXP,
      streak:         child?.streak ?? 0,
      weakestTopics:  weakPoints.slice(0, 3).map((w) => w.topic),
      actions:        actions.slice(0, 4), // max 4 recommendations
      engagementScore,
    };
  }
}

export const adaptiveEngine = new AdaptiveEngine();

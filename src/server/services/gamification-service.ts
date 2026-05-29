/**
 * Gamification Service
 * Handles XP, streaks, badges, and level progression.
 * Called after quiz completion, lesson finish, daily logins.
 */
import { eq, and, desc } from "drizzle-orm";
import { db, children, badges, childBadges, streakEvents } from "@/db";
import { sql } from "drizzle-orm";

export interface XPEvent {
  childId:  string;
  source:   "quiz_pass" | "lesson_complete" | "streak_bonus" | "perfect_score" | "first_lesson";
  xpAmount: number;
  meta?:    Record<string, unknown>;
}

export interface LevelInfo {
  level: number;
  title: string;
  xpRequired: number;
  xpToNext: number;
  progress: number; // 0-100
}

// XP required to reach each level
const LEVEL_THRESHOLDS = [
  0, 100, 250, 500, 900, 1400, 2100, 3000, 4200, 5800, 7800,
];

const LEVEL_TITLES = [
  "مبتدئ", "طالب نشيط", "متعلم جيد", "متميز", "نجم الفصل",
  "موهبة", "عبقري صغير", "أستاذ المستقبل", "خبير", "عالم", "أسطورة عقول",
];

const BADGE_DEFINITIONS = [
  { slug: "first-lesson",    titleAr: "أول درس",         icon: "🌟", xpReward: 50,  condition: "complete_first_lesson" },
  { slug: "perfect-quiz",    titleAr: "علامة كاملة",      icon: "💯", xpReward: 100, condition: "quiz_score_100" },
  { slug: "streak-3",        titleAr: "3 أيام متتالية",   icon: "🔥", xpReward: 75,  condition: "streak_3" },
  { slug: "streak-7",        titleAr: "أسبوع كامل",       icon: "🏆", xpReward: 200, condition: "streak_7" },
  { slug: "streak-30",       titleAr: "بطل الشهر",        icon: "👑", xpReward: 500, condition: "streak_30" },
  { slug: "ten-lessons",     titleAr: "10 دروس",          icon: "📚", xpReward: 150, condition: "complete_10_lessons" },
  { slug: "leila-friend",    titleAr: "صديق ليلى",        icon: "🤖", xpReward: 50,  condition: "first_ai_chat" },
  { slug: "math-star",       titleAr: "نجم الرياضيات",    icon: "➕", xpReward: 100, condition: "complete_math_unit" },
  { slug: "arabic-star",     titleAr: "نجم العربية",      icon: "✍️", xpReward: 100, condition: "complete_arabic_unit" },
];

export function getLevelInfo(xp: number): LevelInfo {
  let level = 0;
  for (let i = LEVEL_THRESHOLDS.length - 1; i >= 0; i--) {
    if (xp >= LEVEL_THRESHOLDS[i]) { level = i; break; }
  }
  const xpRequired   = LEVEL_THRESHOLDS[level] ?? 0;
  const xpForNext    = LEVEL_THRESHOLDS[level + 1] ?? xpRequired + 1000;
  const xpInLevel    = xp - xpRequired;
  const xpNeeded     = xpForNext - xpRequired;
  const progress = Math.round((xpInLevel / xpNeeded) * 100);
  return {
    level:       level + 1,
    title:       LEVEL_TITLES[level] ?? "خبير",
    xpRequired,
    xpToNext:    Math.max(0, xpForNext - xp),
    progress:    Math.min(100, Math.max(0, progress)),
  };
}

export class GamificationService {
  /** Seed all badge definitions into DB */
  async seedBadges() {
    for (const b of BADGE_DEFINITIONS) {
      await db
        .insert(badges)
        .values(b)
        .onConflictDoNothing();
    }
  }

  /** Award XP and return updated level info + any newly earned badges */
  async awardXP(event: XPEvent): Promise<{ newXP: number; levelInfo: LevelInfo; newBadges: string[] }> {
    // Add XP to child
    const [updated] = await db
      .update(children)
      .set({ xp: sql`xp + ${event.xpAmount}` })
      .where(eq(children.id, event.childId))
      .returning({ xp: children.xp });

    const newXP       = updated?.xp ?? 0;
    const levelInfo   = getLevelInfo(newXP);
    const newBadges   = await this.checkAndAwardBadges(event);

    return { newXP, levelInfo, newBadges };
  }

  /** Update daily streak — call on any learning activity */
  async updateStreak(childId: string): Promise<{ streak: number; streakBonus: boolean }> {
    const today  = new Date().toISOString().slice(0, 10);
    const yesterday = new Date(Date.now() - 86400000).toISOString().slice(0, 10);

    // Upsert today's event
    await db
      .insert(streakEvents)
      .values({ childId, date: today, xpEarned: 10 })
      .onConflictDoNothing();

    // Check if yesterday had activity
    const [yesterdayEvent] = await db
      .select()
      .from(streakEvents)
      .where(and(eq(streakEvents.childId, childId), eq(streakEvents.date, yesterday)));

    const [child] = await db.select({ streak: children.streak }).from(children).where(eq(children.id, childId));
    const currentStreak = child?.streak ?? 0;

    let newStreak: number;
    if (yesterdayEvent || currentStreak === 0) {
      newStreak = currentStreak + 1;
    } else {
      newStreak = 1; // streak broken
    }

    await db.update(children).set({ streak: newStreak }).where(eq(children.id, childId));

    // Streak badges
    const streakBonus = newStreak % 7 === 0;

    return { streak: newStreak, streakBonus };
  }

  /** Check which badges the child just earned */
  private async checkAndAwardBadges(event: XPEvent): Promise<string[]> {
    const earned: string[] = [];

    // Get all badges and child's existing badges
    const [allBadges, existingBadges] = await Promise.all([
      db.select().from(badges),
      db.select({ badgeId: childBadges.badgeId }).from(childBadges).where(eq(childBadges.childId, event.childId)),
    ]);

    const existingIds = new Set(existingBadges.map((b) => b.badgeId));
    const unearned    = allBadges.filter((b) => !existingIds.has(b.id));

    const [child] = await db
      .select({ xp: children.xp, streak: children.streak })
      .from(children)
      .where(eq(children.id, event.childId));

    const completedCount = await db
      .select({ count: sql<number>`count(*)::int` })
      .from(await import("@/db").then((m) => m.lessonProgress))
      .where(
        and(
          eq((await import("@/db")).lessonProgress.childId, event.childId),
          eq((await import("@/db")).lessonProgress.status, "completed")
        )
      );
    const totalCompleted = completedCount[0]?.count ?? 0;

    for (const badge of unearned) {
      let shouldAward = false;

      switch (badge.condition) {
        case "complete_first_lesson":   shouldAward = totalCompleted >= 1; break;
        case "quiz_score_100":          shouldAward = event.source === "perfect_score"; break;
        case "streak_3":                shouldAward = (child?.streak ?? 0) >= 3; break;
        case "streak_7":                shouldAward = (child?.streak ?? 0) >= 7; break;
        case "streak_30":               shouldAward = (child?.streak ?? 0) >= 30; break;
        case "complete_10_lessons":     shouldAward = totalCompleted >= 10; break;
        case "first_ai_chat":           shouldAward = event.source === "lesson_complete"; break;
      }

      if (shouldAward) {
        await db.insert(childBadges).values({ childId: event.childId, badgeId: badge.id }).catch(() => {});
        // Award badge XP
        await db.update(children).set({ xp: sql`xp + ${badge.xpReward}` }).where(eq(children.id, event.childId));
        earned.push(badge.titleAr);
      }
    }

    return earned;
  }

  async getChildBadges(childId: string) {
    return db.query.childBadges.findMany({
      where: eq(childBadges.childId, childId),
      with: { badge: true },
      orderBy: desc(childBadges.earnedAt),
    });
  }
}

export const gamificationService = new GamificationService();

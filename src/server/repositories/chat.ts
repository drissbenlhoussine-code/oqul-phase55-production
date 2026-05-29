/**
 * Chat repository — persists Leila conversations in DB.
 * Enables multi-session memory: child can continue past conversations.
 */
import { desc, eq, and } from "drizzle-orm";
import { db, chatSessions, chatMessages } from "@/db";

export const chatRepo = {
  /** Get or create a session for a child + optional lesson */
  async getOrCreateSession(childId: string, lessonId?: string) {
    // Look for an active session (today's)
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    const existing = await db.query.chatSessions.findFirst({
      where: and(
        eq(chatSessions.childId, childId),
        lessonId ? eq(chatSessions.lessonId, lessonId) : eq(chatSessions.childId, childId)
      ),
      orderBy: desc(chatSessions.updatedAt),
    });

    // Reuse if updated today
    if (existing && new Date(existing.updatedAt) >= today) {
      return existing;
    }

    // Create new session
    const [session] = await db
      .insert(chatSessions)
      .values({ childId, lessonId: lessonId ?? null, title: lessonId ? "جلسة درس" : "جلسة عامة" })
      .returning();
    return session;
  },

  /** Save a message to a session */
  async saveMessage(sessionId: string, role: "user" | "assistant" | "system", content: string) {
    const [msg] = await db
      .insert(chatMessages)
      .values({ sessionId, role, content })
      .returning();
    // Touch updatedAt on session
    await db
      .update(chatSessions)
      .set({ updatedAt: new Date() })
      .where(eq(chatSessions.id, sessionId));
    return msg;
  },

  /** Get recent messages for context (last N messages) */
  async getRecentMessages(sessionId: string, limit = 20) {
    const msgs = await db.query.chatMessages.findMany({
      where: eq(chatMessages.sessionId, sessionId),
      orderBy: desc(chatMessages.createdAt),
      limit,
    });
    return msgs.reverse(); // chronological order
  },

  /** Get all sessions for a child */
  async getChildSessions(childId: string, limit = 10) {
    return db.query.chatSessions.findMany({
      where: eq(chatSessions.childId, childId),
      orderBy: desc(chatSessions.updatedAt),
      limit,
      with: { lesson: { columns: { titleAr: true } } },
    });
  },
};

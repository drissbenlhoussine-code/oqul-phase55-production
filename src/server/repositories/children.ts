import { eq } from "drizzle-orm";
import { db, children, weakPoints } from "@/db";

export const childrenRepo = {
  async findByUser(userId: string) {
    return db.query.children.findMany({
      where: eq(children.userId, userId),
      with: { grade: true },
    });
  },

  async findById(id: string) {
    const child = await db.query.children.findFirst({
      where: eq(children.id, id),
      with: { grade: true },
    });
    if (!child) return null;

    // Keep this query explicit instead of relying on a nested relation inference.
    // This avoids runtime crashes when Drizzle cannot infer children.weakPoints.
    const childWeakPoints = await db.query.weakPoints.findMany({
      where: eq(weakPoints.childId, id),
    });

    return { ...child, weakPoints: childWeakPoints };
  },

  async create(data: { userId: string; name: string; gradeId?: string }) {
    const [child] = await db.insert(children).values(data).returning();
    return child;
  },
};

import { eq } from "drizzle-orm";
import { db, users } from "@/db";
import { hash, compare } from "bcryptjs";

export const usersRepo = {
  async findByEmail(email: string) {
    const [user] = await db.select().from(users).where(eq(users.email, email.toLowerCase())).limit(1);
    return user ?? null;
  },

  async findById(id: string) {
    const [user] = await db.select().from(users).where(eq(users.id, id)).limit(1);
    return user ?? null;
  },

  async create(data: { fullName: string; email: string; password: string }) {
    const passwordHash = await hash(data.password, 12);
    const trialEndsAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000);
    const [user] = await db.insert(users).values({
      fullName: data.fullName,
      email: data.email.toLowerCase(),
      passwordHash,
      trialEndsAt,
    }).returning();
    return user;
  },

  async verifyPassword(plain: string, passwordHash: string) {
    return compare(plain, passwordHash);
  },
};

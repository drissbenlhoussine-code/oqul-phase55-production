import { and, eq, asc } from "drizzle-orm";
import { db, cycles, grades, subjects, units, lessons, lessonContents, exercises } from "@/db";
import { buildExamIntelligence } from "@/server/curriculum/exam-intelligence";
import { buildCurriculumKnowledge } from "@/server/curriculum/knowledge-engine";

export const curriculumRepo = {
  async getCycles() {
    return db.query.cycles.findMany({ orderBy: asc(cycles.orderIndex) });
  },

  async getGrades(cycleSlug?: string) {
    if (cycleSlug) {
      const cycle = await db.query.cycles.findFirst({ where: eq(cycles.slug, cycleSlug as "primary" | "middle" | "high") });
      if (!cycle) return [];
      return db.query.grades.findMany({ where: eq(grades.cycleId, cycle.id), orderBy: asc(grades.orderIndex) });
    }
    return db.query.grades.findMany({ orderBy: asc(grades.orderIndex) });
  },

  async getSubjects(gradeId: string) {
    return db.query.subjects.findMany({
      where: and(eq(subjects.gradeId, gradeId), eq(subjects.isActive, true)),
      orderBy: asc(subjects.orderIndex),
    });
  },

  async getUnitsWithLessons(subjectId: string) {
    return db.query.units.findMany({
      where: eq(units.subjectId, subjectId),
      orderBy: asc(units.orderIndex),
      with: {
        lessons: {
          where: eq(lessons.isPublished, true),
          orderBy: asc(lessons.orderIndex),
        },
      },
    });
  },

  async getLessonsByUnit(unitId: string) {
    return db.query.lessons.findMany({
      where: and(eq(lessons.unitId, unitId), eq(lessons.isPublished, true)),
      orderBy: asc(lessons.orderIndex),
    });
  },

  async getLessonWithContent(lessonId: string) {
    return db.query.lessons.findFirst({
      where: eq(lessons.id, lessonId),
      with: {
        content: true,
        exercises: { orderBy: asc(exercises.orderIndex) },
        unit: { with: { subject: { with: { grade: { with: { cycle: true } } } } } },
      },
    });
  },

  async getLessonKnowledge(lessonId: string) {
    const lesson = await this.getLessonWithContent(lessonId);
    return lesson ? buildCurriculumKnowledge(lesson) : null;
  },

  async getLessonExamIntelligence(lessonId: string) {
    const knowledge = await this.getLessonKnowledge(lessonId);
    return knowledge ? buildExamIntelligence(knowledge) : null;
  },
};

/**
 * Complete Curriculum Seed — All Grades
 * Run: npx tsx src/db/seed-curriculum.ts
 */
import postgres from "postgres";
import { drizzle } from "drizzle-orm/postgres-js";
import * as schema from "./schema";
import { eq, and, asc } from "drizzle-orm";
import type { SubjectData, LessonData } from "./curriculum/types";
import { grade1, grade1Science, grade1FrenchExtra, grade1IslamicExtra } from "./curriculum/grade1";
import { grade2 } from "./curriculum/grade2";
import { grade3 } from "./curriculum/grade3";
import { grade4 } from "./curriculum/grade4";
import { grade5, grade6 } from "./curriculum/grade5-6";
import { grade1ac } from "./curriculum/middle";

const url = process.env.DATABASE_URL;
if (!url) throw new Error("DATABASE_URL required");
const client = postgres(url, { ssl: url.includes("localhost") ? false : "require" });
const db = drizzle(client, { schema });

async function findOrCreateSubject(gradeId: string, data: {
  slug: string; titleAr: string; icon: string; color: string; orderIndex: number;
}) {
  const existing = await db.query.subjects.findFirst({
    where: and(eq(schema.subjects.gradeId, gradeId), eq(schema.subjects.slug, data.slug)),
  });
  if (existing) return existing;
  const [created] = await db.insert(schema.subjects).values({
    gradeId, ...data, isActive: true,
  }).returning();
  console.log(`    + مادة: ${data.titleAr}`);
  return created;
}

async function findOrCreateUnit(subjectId: string, slug: string, titleAr: string, orderIndex: number) {
  const existing = await db.query.units.findFirst({
    where: and(eq(schema.units.subjectId, subjectId), eq(schema.units.slug, slug)),
  });
  if (existing) return existing;
  const [created] = await db.insert(schema.units).values({ subjectId, slug, titleAr, orderIndex }).returning();
  return created;
}

async function insertLesson(unitId: string, lesson: LessonData, orderIndex: number) {
  const existing = await db.query.lessons.findFirst({
    where: and(eq(schema.lessons.unitId, unitId), eq(schema.lessons.slug, lesson.slug)),
  });
  if (existing) return; // skip if exists

  const [created] = await db.insert(schema.lessons).values({
    unitId, slug: lesson.slug, titleAr: lesson.titleAr,
    objectives: lesson.objectives, difficulty: lesson.difficulty,
    estimatedDurationMinutes: lesson.durationMin,
    orderIndex, isPublished: true,
  }).returning();

  await db.insert(schema.lessonContents).values({
    lessonId: created.id, explanation: lesson.explanation,
    vocabulary: lesson.vocabulary, examples: lesson.examples, summary: lesson.summary,
  });

  await db.insert(schema.exercises).values(
    lesson.exercises.map((ex, i) => ({
      lessonId: created.id, type: ex.type, question: ex.question,
      options: ex.options ?? null, correctAnswer: ex.correctAnswer,
      explanation: ex.explanation, orderIndex: i + 1, points: ex.points,
    }))
  );

  console.log(`      ✅ ${lesson.titleAr} (${lesson.exercises.length} تمارين)`);
}

async function insertSubjectData(gradeSlug: string, subjects: SubjectData[]) {
  const grade = await db.query.grades.findFirst({ where: eq(schema.grades.slug, gradeSlug) });
  if (!grade) { console.log(`  ⚠️  Grade ${gradeSlug} not found`); return 0; }

  let count = 0;
  for (const subData of subjects) {
    const subject = await findOrCreateSubject(grade.id, {
      slug: subData.slug, titleAr: subData.titleAr,
      icon: subData.icon, color: subData.color, orderIndex: subData.orderIndex,
    });

    for (const unitData of subData.units) {
      const unit = await findOrCreateUnit(subject.id, unitData.slug, unitData.titleAr, unitData.orderIndex);
      for (const [i, lesson] of unitData.lessons.entries()) {
        await insertLesson(unit.id, lesson, i + 1);
        count++;
      }
    }
  }
  return count;
}

async function addExtraLessons(gradeSlug: string, subjectSlug: string, unitSlug: string, unitTitle: string, lessons: LessonData[]) {
  const grade = await db.query.grades.findFirst({ where: eq(schema.grades.slug, gradeSlug) });
  if (!grade) return;
  const subject = await db.query.subjects.findFirst({
    where: and(eq(schema.subjects.gradeId, grade.id), eq(schema.subjects.slug, subjectSlug)),
  });
  if (!subject) return;
  const unit = await findOrCreateUnit(subject.id, unitSlug, unitTitle, 99);

  // Get current lesson count for ordering
  const existing = await db.query.lessons.findMany({ where: eq(schema.lessons.unitId, unit.id), orderBy: asc(schema.lessons.orderIndex) });
  const startIdx = existing.length + 1;
  for (const [i, lesson] of lessons.entries()) {
    await insertLesson(unit.id, lesson, startIdx + i);
  }
}

async function main() {
  console.log("🌱 OQUL — إضافة المحتوى الكامل للمنهج\n");

  // Grade 1 — complete
  console.log("\n📚 السنة الأولى ابتدائي");
  let n = await insertSubjectData("1ap", grade1);
  // Add science subject
  const g1 = await db.query.grades.findFirst({ where: eq(schema.grades.slug, "1ap") });
  if (g1) {
    await findOrCreateSubject(g1.id, { slug: "science", titleAr: "التربية العلمية", icon: "Microscope", color: "#0891b2", orderIndex: 5 });
    for (const unitData of grade1Science.units) {
      const sciSubject = await db.query.subjects.findFirst({ where: and(eq(schema.subjects.gradeId, g1.id), eq(schema.subjects.slug, "science")) });
      if (sciSubject) {
        const unit = await findOrCreateUnit(sciSubject.id, unitData.slug, unitData.titleAr, unitData.orderIndex);
        for (const [i, lesson] of unitData.lessons.entries()) {
          await insertLesson(unit.id, lesson, i + 1);
          n++;
        }
      }
    }
  }
  // Add extra French lessons
  await addExtraLessons("1ap", "french", "la-famille", "العائلة والجسم", grade1FrenchExtra);
  n += grade1FrenchExtra.length;
  // Add extra Islamic lessons
  await addExtraLessons("1ap", "islamic", "ibadaat", "العبادات والأخلاق", grade1IslamicExtra);
  n += grade1IslamicExtra.length;
  console.log(`  → ${n} درس`);

  const other = [
    { slug: "2ap", data: grade2,   label: "السنة الثانية" },
    { slug: "3ap", data: grade3,   label: "السنة الثالثة" },
    { slug: "4ap", data: grade4,   label: "السنة الرابعة" },
    { slug: "5ap", data: grade5,   label: "السنة الخامسة" },
    { slug: "6ap", data: grade6,   label: "السنة السادسة" },
    { slug: "1ac", data: grade1ac, label: "الأولى إعدادي" },
  ];

  let total = n;
  for (const { slug, data, label } of other) {
    console.log(`\n📚 ${label}`);
    const count = await insertSubjectData(slug, data);
    console.log(`  → ${count} درس`);
    total += count;
  }

  console.log(`\n✅ اكتمل! أضفنا ${total} درس بمحتوى حقيقي`);
  await client.end();
}

main().catch((e) => { console.error(e); process.exit(1); });

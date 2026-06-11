import { ilike, or, sql } from "drizzle-orm";
import { buildWeakGrounding, classifySubject, examContextFor, extractRequestedTopic, inferGrade } from "./quality";
import type { CurriculumGrounding, PipelineSubject } from "./quality";

function subjectSearchTerms(subject: PipelineSubject): string[] {
  switch (subject) {
    case "french":
      return ["french", "français", "francais", "الفرنسية"];
    case "arabic":
      return ["arabic", "العربية", "لغة عربية"];
    case "math":
      return ["math", "رياضيات", "mathematics", "advanced-math"];
    case "physics":
      return ["physics", "physique", "فيزياء"];
    case "svt":
      return ["svt", "علوم الحياة", "biology"];
    case "philosophy":
      return ["philosophy", "philosophie", "فلسفة"];
    default:
      return [];
  }
}

export async function buildCurriculumGrounding(input: string): Promise<CurriculumGrounding> {
  const weak = buildWeakGrounding(input);
  const topic = extractRequestedTopic(input);
  const subject = classifySubject(input);
  const grade = inferGrade(input);
  const terms = [
    topic,
    ...subjectSearchTerms(subject),
  ].filter((term): term is string => Boolean(term && term.trim().length >= 2));

  if (!process.env.DATABASE_URL || terms.length === 0) return weak;

  try {
    const dbModule = await import("@/db");
    const { db, grades, subjects, units, lessons, lessonContents, exercises } = dbModule;
    const termConditions = terms.flatMap((term) => {
      const like = `%${term}%`;
      return [
        ilike(lessons.titleAr, like),
        ilike(lessons.slug, like),
        ilike(units.titleAr, like),
        ilike(units.slug, like),
        ilike(subjects.titleAr, like),
        ilike(subjects.titleFr, like),
        ilike(subjects.slug, like),
      ];
    });

    const rows = await db
      .select({
        lessonId: lessons.id,
        lessonTitle: lessons.titleAr,
        lessonSlug: lessons.slug,
        objectives: lessons.objectives,
        unitTitle: units.titleAr,
        subjectTitle: subjects.titleAr,
        subjectFr: subjects.titleFr,
        gradeTitle: grades.titleAr,
        explanation: lessonContents.explanation,
        exerciseCount: sql<number>`count(${exercises.id})::int`,
      })
      .from(lessons)
      .innerJoin(units, sql`${units.id} = ${lessons.unitId}`)
      .innerJoin(subjects, sql`${subjects.id} = ${units.subjectId}`)
      .innerJoin(grades, sql`${grades.id} = ${subjects.gradeId}`)
      .leftJoin(lessonContents, sql`${lessonContents.lessonId} = ${lessons.id}`)
      .leftJoin(exercises, sql`${exercises.lessonId} = ${lessons.id}`)
      .where(or(...termConditions))
      .groupBy(
        lessons.id,
        lessons.titleAr,
        lessons.slug,
        lessons.objectives,
        units.titleAr,
        subjects.titleAr,
        subjects.titleFr,
        grades.titleAr,
        lessonContents.explanation,
      )
      .limit(5);

    const matches = rows.map((row) => ({
      lessonId: row.lessonId,
      title: row.lessonTitle,
      grade: row.gradeTitle,
      subject: row.subjectFr ? `${row.subjectTitle} / ${row.subjectFr}` : row.subjectTitle,
      unit: row.unitTitle,
      objectives: Array.isArray(row.objectives) ? row.objectives : [],
      contentSnippet: row.explanation ? row.explanation.slice(0, 700) : null,
      exerciseCount: Number(row.exerciseCount ?? 0),
    }));

    if (!matches.length) return weak;

    return {
      grade,
      subject,
      topic,
      examContext: examContextFor(input, subject),
      strength: "strong",
      matches,
      warnings: [],
    };
  } catch (error) {
    console.error("[pipeline-grounding] failed", error);
    return {
      ...weak,
      warnings: [...weak.warnings, "تعذر تحميل سياق قاعدة البيانات. المتابعة ستكون بسياق ضعيف وصارم."],
    };
  }
}

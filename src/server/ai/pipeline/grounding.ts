import { ilike, or, sql } from "drizzle-orm";
import { buildWeakGrounding, classifySubject, examContextFor, extractRequestedTopic, inferGrade } from "./quality";
import type { CurriculumGrounding, PipelineSubject } from "./quality";

function subjectSearchTerms(subject: PipelineSubject): string[] {
  switch (subject) {
    case "french":
      return ["french", "français", "francais", "الفرنسية", "لغة فرنسية", "قواعد فرنسية"];
    case "arabic":
      return ["arabic", "العربية", "لغة عربية", "النحو", "الصرف"];
    case "math":
      return ["math", "رياضيات", "mathematics", "advanced-math"];
    case "physics":
      return ["physics", "physique", "فيزياء", "كيمياء"];
    case "svt":
      return ["svt", "علوم الحياة", "الأرض", "biology"];
    case "philosophy":
      return ["philosophy", "philosophie", "فلسفة"];
    default:
      return [];
  }
}

function topicAliases(topic: string | null, subject: PipelineSubject): string[] {
  const aliases = new Set<string>();
  if (topic?.trim()) aliases.add(topic.trim());
  if (subject === "french" && topic && /grammaire|grammar|قواعد/i.test(topic)) {
    [
      "grammaire",
      "grammaire française",
      "قواعد اللغة الفرنسية",
      "القواعد الفرنسية",
      "nature des mots",
      "fonctions grammaticales",
      "fonction grammaticale",
      "groupe nominal",
      "phrase simple",
      "conjugaison",
      "accord",
    ].forEach((term) => aliases.add(term));
  }
  return [...aliases].filter((term) => term.length >= 2);
}

function includesAny(text: string, terms: string[]): boolean {
  const lower = text.toLowerCase();
  return terms.some((term) => lower.includes(term.toLowerCase()));
}

function scoreMatch(
  row: {
    lessonTitle: string;
    lessonSlug: string;
    unitTitle: string;
    subjectTitle: string;
    subjectFr: string | null;
    gradeTitle: string;
    explanation: string | null;
  },
  topicTerms: string[],
  subjectTerms: string[],
  requestedGrade: string | null,
): number {
  const lessonText = [row.lessonTitle, row.lessonSlug, row.unitTitle, row.explanation ?? ""].join(" ");
  const subjectText = [row.subjectTitle, row.subjectFr ?? ""].join(" ");
  const gradeText = row.gradeTitle;
  let score = 0;

  if (includesAny(lessonText, topicTerms)) score += 5;
  if (includesAny(subjectText, topicTerms)) score += 2;
  if (includesAny(subjectText, subjectTerms)) score += 2;
  if (requestedGrade && includesAny(gradeText, [requestedGrade])) score += 2;
  if (row.explanation && row.explanation.length > 80) score += 1;

  return score;
}

export async function buildCurriculumGrounding(input: string): Promise<CurriculumGrounding> {
  const fallback = buildWeakGrounding(input);
  if (fallback.mode === "clarification_needed") return fallback;

  const topic = extractRequestedTopic(input);
  const subject = classifySubject(input);
  const grade = inferGrade(input);
  const topicTerms = topicAliases(topic, subject);
  const subjectTerms = subjectSearchTerms(subject);
  const terms = [...topicTerms, ...subjectTerms].filter((term) => term.trim().length >= 2);

  if (!process.env.DATABASE_URL || terms.length === 0) return fallback;

  try {
    const dbModule = await import("@/db");
    const { db, cycles, grades, subjects, units, lessons, lessonContents, exercises } = dbModule;
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
        ilike(lessonContents.explanation, like),
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
        cycleTitle: cycles.titleAr,
        explanation: lessonContents.explanation,
        exerciseCount: sql<number>`count(${exercises.id})::int`,
      })
      .from(lessons)
      .innerJoin(units, sql`${units.id} = ${lessons.unitId}`)
      .innerJoin(subjects, sql`${subjects.id} = ${units.subjectId}`)
      .innerJoin(grades, sql`${grades.id} = ${subjects.gradeId}`)
      .innerJoin(cycles, sql`${cycles.id} = ${grades.cycleId}`)
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
        cycles.titleAr,
        lessonContents.explanation,
      )
      .limit(12);

    const rankedRows = rows
      .map((row) => ({ row, score: scoreMatch(row, topicTerms, subjectTerms, grade) }))
      .filter(({ score }) => score >= 5)
      .sort((a, b) => b.score - a.score)
      .slice(0, 5);

    const matches = rankedRows.map(({ row }) => ({
      lessonId: row.lessonId,
      title: row.lessonTitle,
      cycle: row.cycleTitle,
      grade: row.gradeTitle,
      subject: row.subjectFr ? `${row.subjectTitle} / ${row.subjectFr}` : row.subjectTitle,
      unit: row.unitTitle,
      objectives: Array.isArray(row.objectives) ? row.objectives : [],
      contentSnippet: row.explanation ? row.explanation.slice(0, 900) : null,
      exerciseCount: Number(row.exerciseCount ?? 0),
    }));

    if (!matches.length) return fallback;

    return {
      mode: "grounded",
      languageOfInstruction: fallback.languageOfInstruction,
      confidence: "high",
      missingDbLesson: false,
      cycle: matches[0]?.cycle ?? null,
      grade: matches[0]?.grade ?? grade,
      subject,
      unit: matches[0]?.unit ?? null,
      lesson: matches[0]?.title ?? null,
      topic,
      examContext: examContextFor(input, subject),
      strength: "strong",
      matches,
      warnings: [],
    };
  } catch (error) {
    console.error("[pipeline-grounding] failed", error);
    return {
      ...fallback,
      warnings: [
        ...fallback.warnings,
        "تعذر تحميل سياق قاعدة البيانات. سيتم استعمال وضع fallback متوافق مع توقعات المنهاج المغربي دون الادعاء بوجود درس محفوظ.",
      ],
    };
  }
}

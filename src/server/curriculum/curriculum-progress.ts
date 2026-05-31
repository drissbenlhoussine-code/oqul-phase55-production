import { asc, eq, sql } from "drizzle-orm";
import { cycles, db, exercises, grades, lessonContents, lessons, subjects, units } from "@/db";

export type CurriculumLessonStatus = "excellent" | "needs_improvement" | "placeholder";

export type CurriculumProgressLesson = {
  lessonId: string;
  title: string;
  subject: string;
  subjectSlug: string;
  grade: string;
  gradeSlug: string;
  unit: string;
  qualityScore: number;
  status: CurriculumLessonStatus;
  reason: string;
  contentLength: number;
  exerciseCount: number;
  hasContent: boolean;
  isPlaceholder: boolean;
  completed: boolean;
};

export type CurriculumProgressGrade = {
  grade: string;
  gradeSlug: string;
  totalLessons: number;
  completedLessons: number;
  remainingLessons: number;
  placeholderLessons: number;
  averageQuality: number;
  completionPercentage: number;
};

export type CurriculumProgressSummary = {
  totalLessons: number;
  completedLessons: number;
  remainingLessons: number;
  placeholderLessons: number;
  averageQualityScore: number;
  completionPercentage: number;
};

export type CurriculumProgressReport = {
  summary: CurriculumProgressSummary;
  grades: CurriculumProgressGrade[];
  lessonsNeedingImprovement: CurriculumProgressLesson[];
  generatedAt: string;
};

const PRIMARY_MATH_GRADES = ["1ap", "2ap", "3ap", "4ap", "5ap", "6ap"] as const;

type LessonRow = {
  lessonId: string;
  title: string;
  subject: string;
  subjectSlug: string;
  grade: string;
  gradeSlug: string;
  unit: string;
  explanation: string | null;
  summary: string | null;
  objectives: string[] | null;
  vocabulary: { word: string; definition: string }[] | null;
  examples: { text: string; note?: string }[] | null;
  exerciseCount: number;
};

function lessonText(row: LessonRow) {
  return [
    row.title,
    row.unit,
    row.subject,
    row.grade,
    row.explanation,
    row.summary,
    JSON.stringify(row.objectives ?? []),
    JSON.stringify(row.vocabulary ?? []),
    JSON.stringify(row.examples ?? []),
  ]
    .filter(Boolean)
    .join("\n");
}

function evaluateLesson(row: LessonRow) {
  const issues: string[] = [];
  const text = lessonText(row);
  const normalized = text.toLowerCase();
  const explanation = row.explanation ?? "";

  const placeholderMarkers = [
    "هذا درس في",
    "هذا درس تمهيدي",
    "درس أصلي من oqul مبني على عنوان المنهج فقط",
    "تمرين 1 سهل",
    "جواب نموذجي مختصر",
    "مثال مبسط حول",
    "يحتاج مطابقة",
    "placeholder",
    "generic",
    "Ã˜",
    "Ã™",
  ];

  if (!explanation.trim()) issues.push("missing_content");
  if (explanation.trim().length < 900) issues.push("too_short");
  if (placeholderMarkers.some((marker) => normalized.includes(marker.toLowerCase()))) {
    issues.push("placeholder_text");
  }
  if (!/المغرب|مغربي|مغربية|المنهاج|القسم|المدرسة|الرياضيات/.test(text)) {
    issues.push("missing_moroccan_context");
  }
  if (!/تعريف|مفهوم|نسمي|يرمز|قاعدة/.test(text)) issues.push("missing_definitions");
  if (!/مثال|خطوة|نحسب|الحل/.test(text)) issues.push("missing_worked_examples");
  if (!/تمرين|تطبيق|تدريب|أجب|احسب/.test(text)) issues.push("missing_guided_practice");
  if (row.exerciseCount < 3) issues.push("missing_exercises");
  if (!/الجواب|تصحيح|correct|answer|شرح/.test(text)) issues.push("missing_answers");
  if (!/خطأ|أخطاء|خلط|نسيان/.test(text)) issues.push("missing_common_mistakes");
  if (!/تلميح|العلاج|تصحيح|إعادة|remediation/.test(text)) issues.push("missing_remediation");
  if (!/فرض|امتحان|وضعية|استعداد|تقويم/.test(text)) issues.push("missing_exam_prep");
  if (!/ملخص|خلاصة/.test(text)) issues.push("missing_summary");
  if (!/ليلى|Leila|leila/.test(text)) issues.push("missing_leila_instructions");

  const score = Math.max(0, Math.min(100, 100 - issues.length * 8));
  const isPlaceholder = issues.includes("placeholder_text");
  const hasContent = Boolean(explanation.trim());
  const completed = score >= 85 && !isPlaceholder && hasContent && row.exerciseCount > 0;

  let status: CurriculumLessonStatus = "needs_improvement";
  if (isPlaceholder) status = "placeholder";
  else if (completed) status = "excellent";

  return { issues, score, isPlaceholder, hasContent, completed, status };
}

function reasonFromIssues(issues: string[]) {
  if (issues.length === 0) return "Ready";
  const labels: Record<string, string> = {
    missing_content: "Missing lesson content",
    too_short: "Content is too short",
    placeholder_text: "Placeholder text detected",
    missing_moroccan_context: "Missing Moroccan classroom context",
    missing_definitions: "Missing definitions",
    missing_worked_examples: "Missing worked examples",
    missing_guided_practice: "Missing guided practice",
    missing_exercises: "Missing exercises",
    missing_answers: "Missing answers or explanations",
    missing_common_mistakes: "Missing common mistakes",
    missing_remediation: "Missing remediation",
    missing_exam_prep: "Missing assessment preparation",
    missing_summary: "Missing summary",
    missing_leila_instructions: "Missing Leila tutor instructions",
  };
  return issues.map((issue) => labels[issue] ?? issue).join(", ");
}

function percentage(completed: number, total: number) {
  if (total === 0) return 0;
  return Math.round((completed / total) * 100);
}

function average(values: number[]) {
  if (values.length === 0) return 0;
  return Math.round(values.reduce((sum, value) => sum + value, 0) / values.length);
}

export async function getPrimaryMathCurriculumProgress(): Promise<CurriculumProgressReport> {
  const rows = await db
    .select({
      lessonId: lessons.id,
      title: lessons.titleAr,
      subject: subjects.titleAr,
      subjectSlug: subjects.slug,
      grade: grades.titleAr,
      gradeSlug: grades.slug,
      unit: units.titleAr,
      explanation: lessonContents.explanation,
      summary: lessonContents.summary,
      objectives: lessons.objectives,
      vocabulary: lessonContents.vocabulary,
      examples: lessonContents.examples,
      exerciseCount: sql<number>`count(${exercises.id})::int`,
    })
    .from(lessons)
    .innerJoin(units, eq(units.id, lessons.unitId))
    .innerJoin(subjects, eq(subjects.id, units.subjectId))
    .innerJoin(grades, eq(grades.id, subjects.gradeId))
    .innerJoin(cycles, eq(cycles.id, grades.cycleId))
    .leftJoin(lessonContents, eq(lessonContents.lessonId, lessons.id))
    .leftJoin(exercises, eq(exercises.lessonId, lessons.id))
    .where(eq(cycles.slug, "primary"))
    .groupBy(
      lessons.id,
      units.id,
      subjects.id,
      grades.id,
      lessonContents.id
    )
    .orderBy(asc(grades.orderIndex), asc(units.orderIndex), asc(lessons.orderIndex));

  const mathRows = rows
    .filter((row) => row.subjectSlug === "math" && PRIMARY_MATH_GRADES.includes(row.gradeSlug as typeof PRIMARY_MATH_GRADES[number]))
    .map((row): LessonRow => ({
      lessonId: row.lessonId,
      title: row.title,
      subject: row.subject,
      subjectSlug: row.subjectSlug,
      grade: row.grade,
      gradeSlug: row.gradeSlug,
      unit: row.unit,
      explanation: row.explanation,
      summary: row.summary,
      objectives: row.objectives,
      vocabulary: row.vocabulary,
      examples: row.examples,
      exerciseCount: Number(row.exerciseCount ?? 0),
    }));

  const lessonsWithQuality = mathRows.map((row): CurriculumProgressLesson => {
    const quality = evaluateLesson(row);
    return {
      lessonId: row.lessonId,
      title: row.title,
      subject: row.subject,
      subjectSlug: row.subjectSlug,
      grade: row.grade,
      gradeSlug: row.gradeSlug,
      unit: row.unit,
      qualityScore: quality.score,
      status: quality.status,
      reason: reasonFromIssues(quality.issues),
      contentLength: (row.explanation ?? "").length,
      exerciseCount: row.exerciseCount,
      hasContent: quality.hasContent,
      isPlaceholder: quality.isPlaceholder,
      completed: quality.completed,
    };
  });

  const gradeSummaries = PRIMARY_MATH_GRADES.map((gradeSlug) => {
    const gradeLessons = lessonsWithQuality.filter((lesson) => lesson.gradeSlug === gradeSlug);
    const completedLessons = gradeLessons.filter((lesson) => lesson.completed).length;
    return {
      grade: gradeLessons[0]?.grade ?? gradeSlug,
      gradeSlug,
      totalLessons: gradeLessons.length,
      completedLessons,
      remainingLessons: gradeLessons.length - completedLessons,
      placeholderLessons: gradeLessons.filter((lesson) => lesson.isPlaceholder).length,
      averageQuality: average(gradeLessons.map((lesson) => lesson.qualityScore)),
      completionPercentage: percentage(completedLessons, gradeLessons.length),
    };
  });

  const totalLessons = lessonsWithQuality.length;
  const completedLessons = lessonsWithQuality.filter((lesson) => lesson.completed).length;

  return {
    summary: {
      totalLessons,
      completedLessons,
      remainingLessons: totalLessons - completedLessons,
      placeholderLessons: lessonsWithQuality.filter((lesson) => lesson.isPlaceholder).length,
      averageQualityScore: average(lessonsWithQuality.map((lesson) => lesson.qualityScore)),
      completionPercentage: percentage(completedLessons, totalLessons),
    },
    grades: gradeSummaries,
    lessonsNeedingImprovement: lessonsWithQuality
      .filter((lesson) => !lesson.completed)
      .sort((a, b) => a.qualityScore - b.qualityScore || a.gradeSlug.localeCompare(b.gradeSlug)),
    generatedAt: new Date().toISOString(),
  };
}

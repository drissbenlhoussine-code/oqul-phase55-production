import {
  fetchLessonForViewer,
  fetchLessons,
  getPilotSourceLesson,
  parseArgs,
  printLessonSummary,
  scoreLessonQuality,
  withDb,
} from "./lib/lesson-quality-tools.mjs";

const args = parseArgs();

function printUsage() {
  console.log("Usage examples:");
  console.log("  node scripts/verify-lesson-db-content.mjs --lesson-id=<uuid>");
  console.log("  node scripts/verify-lesson-db-content.mjs --grade=TC --subject=math --unit=probability --title=الاحتمالات");
  console.log("  node scripts/verify-lesson-db-content.mjs --pilot");
}

if (args.help) {
  printUsage();
  process.exit(0);
}

let filters = {
  lessonId: args["lesson-id"],
  grade: args.grade,
  subject: args.subject,
  unit: args.unit,
  title: args.title,
  limit: Number(args.limit ?? 20),
};

if (args.pilot) {
  const { lesson } = getPilotSourceLesson();
  filters = {
    grade: "tc",
    subject: "math,advanced_math,advanced-math",
    title: lesson.title,
    limit: 20,
  };
}

await withDb(async (client) => {
  const matches = await fetchLessons(client, filters);
  if (matches.length === 0) {
    throw new Error("No matching lesson rows found.");
  }

  console.log(`Matched lessons: ${matches.length}`);
  console.table(
    matches.map((row) => {
      const quality = scoreLessonQuality(row);
      return {
        id: row.lesson_id,
        title: row.lesson_title,
        grade: row.grade_slug ?? row.grade_title,
        subject: row.subject_slug ?? row.subject_title,
        unit: row.unit_slug ?? row.unit_title,
        contentChars: String(row.explanation ?? "").length,
        exercises: row.exercise_count,
        score: quality.score,
        status: quality.status,
      };
    })
  );

  if (matches.length === 1) {
    const row = matches[0];
    printLessonSummary("Database content", row);
    const viewerLesson = await fetchLessonForViewer(client, row.lesson_id);
    console.log("\nRepository-path shape used by curriculumRepo.getLessonWithContent():");
    console.log({
      lessonId: viewerLesson.id,
      title: viewerLesson.titleAr,
      contentChars: viewerLesson.content?.explanation?.length ?? 0,
      exercises: viewerLesson.exercises.length,
      grade: viewerLesson.unit?.subject?.grade?.slug,
      subject: viewerLesson.unit?.subject?.slug,
      unit: viewerLesson.unit?.slug,
    });
  } else {
    console.log("Multiple rows matched. Re-run with --lesson-id=<uuid> to inspect one repository-shaped lesson.");
  }
});

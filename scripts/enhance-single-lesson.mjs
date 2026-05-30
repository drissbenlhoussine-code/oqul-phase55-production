import { generateEnhancedLesson } from "./lib/ai-lesson-enhancer.mjs";
import {
  DEFAULT_PLACEHOLDER_THRESHOLD,
  fetchLessonForViewer,
  fetchLessons,
  parseArgs,
  printLessonSummary,
  scoreLessonQuality,
  updateLessonWithPayload,
  withDb,
} from "./lib/lesson-quality-tools.mjs";

const args = parseArgs();
const apply = Boolean(args.apply || args["apply-db"]);
const force = Boolean(args.force);
const threshold = Number(args.threshold ?? DEFAULT_PLACEHOLDER_THRESHOLD);

if (!args["lesson-id"] && !args.title) {
  throw new Error("Provide --lesson-id=<uuid> or a narrow --title=<text> filter.");
}

await withDb(async (client) => {
  const matches = await fetchLessons(client, {
    lessonId: args["lesson-id"],
    grade: args.grade,
    subject: args.subject,
    unit: args.unit,
    title: args.title,
    limit: Number(args.limit ?? 20),
  });

  if (matches.length === 0) throw new Error("No matching lesson found.");
  if (matches.length > 1) {
    console.table(matches.map((row) => ({ id: row.lesson_id, title: row.lesson_title, grade: row.grade_slug, subject: row.subject_slug, unit: row.unit_slug })));
    throw new Error("Safety abort: multiple lessons matched. Re-run with --lesson-id=<uuid>.");
  }

  const lesson = matches[0];
  printLessonSummary("Current lesson", lesson);
  const quality = scoreLessonQuality(lesson);
  if (!force && quality.score >= threshold) {
    console.log(`Skipping: quality score ${quality.score} is >= threshold ${threshold}. Use --force to override.`);
    return;
  }

  if (!apply) {
    console.log("\nDry run only. This lesson is eligible for enhancement.");
    console.log("Apply with: node scripts/enhance-single-lesson.mjs --lesson-id=" + lesson.lesson_id + " --apply");
    return;
  }

  const payload = await generateEnhancedLesson(lesson);
  const generatedQuality = scoreLessonQuality({ ...lesson, ...payload, exercise_count: payload.exercises.length });
  console.log("Generated quality:", generatedQuality);
  if (generatedQuality.score < threshold && !force) {
    throw new Error(`Generated content scored ${generatedQuality.score}, below threshold ${threshold}. Use --force only after manual review.`);
  }

  const counts = await updateLessonWithPayload(client, lesson.lesson_id, payload, { replaceExercises: true });
  console.log("Rows changed:");
  console.table([counts]);

  const viewerLesson = await fetchLessonForViewer(client, lesson.lesson_id);
  console.log("Verified repository-path lesson:", {
    lessonId: viewerLesson.id,
    title: viewerLesson.titleAr,
    contentChars: viewerLesson.content.explanation.length,
    exercises: viewerLesson.exercises.length,
  });
});

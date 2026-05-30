import { generateEnhancedLesson } from "./lib/ai-lesson-enhancer.mjs";
import {
  DEFAULT_PLACEHOLDER_THRESHOLD,
  fetchLessons,
  parseArgs,
  scoreLessonQuality,
  updateLessonWithPayload,
  withDb,
} from "./lib/lesson-quality-tools.mjs";

const args = parseArgs();
const apply = Boolean(args.apply || args["apply-db"]);
const force = Boolean(args.force);
const threshold = Number(args.threshold ?? DEFAULT_PLACEHOLDER_THRESHOLD);
const limit = Number(args.limit ?? 5);

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

await withDb(async (client) => {
  const lessons = await fetchLessons(client, {
    grade: args.grade,
    subject: args.subject,
    unit: args.unit,
    title: args.title,
    limit: Math.max(limit * 4, limit),
  });

  const candidates = lessons
    .map((lesson) => ({ lesson, quality: scoreLessonQuality(lesson) }))
    .filter(({ quality }) => force || quality.score < threshold || quality.issues.includes("placeholder_text"))
    .sort((a, b) => a.quality.score - b.quality.score)
    .slice(0, limit);

  console.log("Enhancement candidates:");
  console.table(
    candidates.map(({ lesson, quality }) => ({
      id: lesson.lesson_id,
      title: lesson.lesson_title,
      grade: lesson.grade_slug ?? lesson.grade_title,
      subject: lesson.subject_slug ?? lesson.subject_title,
      unit: lesson.unit_slug ?? lesson.unit_title,
      score: quality.score,
      issues: quality.issues.slice(0, 4).join(", "),
    }))
  );

  if (!apply) {
    console.log("\nDry run only. No lessons were changed.");
    console.log("Apply with: node scripts/enhance-placeholder-lessons.mjs --limit=" + limit + " --apply");
    return;
  }

  if (candidates.length === 0) {
    console.log("No eligible placeholder lessons found.");
    return;
  }

  const results = [];
  for (const { lesson } of candidates) {
    console.log("\nEnhancing:", lesson.lesson_id, lesson.lesson_title);
    const payload = await generateEnhancedLesson(lesson);
    const generatedQuality = scoreLessonQuality({ ...lesson, ...payload, exercise_count: payload.exercises.length });
    if (generatedQuality.score < threshold && !force) {
      throw new Error(`Generated content for ${lesson.lesson_id} scored ${generatedQuality.score}, below threshold ${threshold}.`);
    }
    const counts = await updateLessonWithPayload(client, lesson.lesson_id, payload, { replaceExercises: true });
    results.push({ lessonId: lesson.lesson_id, title: lesson.lesson_title, generatedScore: generatedQuality.score, ...counts });
    await sleep(Number(args.delayMs ?? 1000));
  }

  console.log("\nEnhancement results:");
  console.table(results);
});

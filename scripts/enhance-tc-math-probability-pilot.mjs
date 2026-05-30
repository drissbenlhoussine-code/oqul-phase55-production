import {
  buildDbPayloadFromEnhancedLesson,
  fetchLessonForViewer,
  fetchLessons,
  getPilotSourceLesson,
  parseArgs,
  printLessonSummary,
  scoreLessonQuality,
  updateLessonWithPayload,
  withDb,
} from "./lib/lesson-quality-tools.mjs";

const args = parseArgs();
const APPLY_DB = Boolean(args["apply-db"]);
const lessonIdArg = args["lesson-id"];

const { filePath, lesson: sourceLesson } = getPilotSourceLesson();
const payload = buildDbPayloadFromEnhancedLesson(sourceLesson);

function printPlan() {
  console.log("Pilot source:", filePath);
  console.log("Pilot registry id:", "TC-math-19-01");
  console.log("Pilot JSON lesson id:", sourceLesson.lessonId);
  console.log("Pilot title:", sourceLesson.title);
  console.log("Mode:", APPLY_DB ? "APPLY_DB" : "DRY_RUN");
  console.log("Payload summary:", {
    objectives: payload.objectives.length,
    explanationChars: payload.explanation.length,
    vocabulary: payload.vocabulary.length,
    examples: payload.examples.length,
    exercises: payload.exercises.length,
  });
}

async function resolvePilotLesson(client) {
  if (lessonIdArg) {
    const exact = await fetchLessons(client, { lessonId: lessonIdArg, limit: 2 });
    if (exact.length !== 1) {
      throw new Error(`Safety abort: --lesson-id matched ${exact.length} lessons.`);
    }
    return exact[0];
  }

  const searches = [];
  searches.push(
    await fetchLessons(client, {
      grade: "tc",
      subject: "math,advanced_math,advanced-math",
      unit: "probability",
      title: "probability",
      limit: 20,
    })
  );
  searches.push(await fetchLessons(client, { grade: "tc", title: "الاحتمالات", limit: 20 }));
  searches.push(await fetchLessons(client, { title: "الاحتمالات", limit: 20 }));
  const unique = new Map();
  for (const row of searches.flat()) unique.set(row.lesson_id, row);
  const candidates = [...unique.values()];

  const titleCandidates = candidates.filter((row) => {
    const title = String(row.lesson_title ?? "");
    const slug = String(row.lesson_slug ?? "");
    const grade = String(row.grade_slug ?? row.grade_title ?? "").toLowerCase();
    return (
      (grade === "tc" || title.includes("الجذع المشترك")) &&
      (title.includes("المفهوم") || title.includes("مفاهيم أساسية") || slug.includes("concept")) &&
      (title.includes("الاحتمالات") ||
        title.includes("Probability") ||
        title.includes("probability") ||
        slug.includes("probability") ||
        String(row.unit_title ?? "").includes("الاحتمالات") ||
        String(row.unit_slug ?? "").includes("probability"))
    );
  });

  const matches = titleCandidates.length ? titleCandidates : candidates;
  if (matches.length === 0) {
    throw new Error("Safety abort: no matching TC math probability lesson found in the database.");
  }
  if (matches.length > 1) {
    console.table(
      matches.map((row) => ({
        id: row.lesson_id,
        title: row.lesson_title,
        grade: row.grade_slug,
        subject: row.subject_slug,
        unit: row.unit_slug,
        exercises: row.exercise_count,
      }))
    );
    throw new Error("Safety abort: multiple candidate lessons found. Re-run with --lesson-id=<id>.");
  }
  return matches[0];
}

printPlan();

await withDb(async (client) => {
  const before = await resolvePilotLesson(client);
  printLessonSummary("Current DB content before update", before);

  const beforeQuality = scoreLessonQuality(before);
  console.log("Source payload quality:", scoreLessonQuality({ ...before, ...payload, exercise_count: payload.exercises.length }));

  if (!APPLY_DB) {
    console.log("\nDry run only. No database rows were changed.");
    console.log("Apply with: node scripts/enhance-tc-math-probability-pilot.mjs --apply-db");
    if (beforeQuality.score >= 90) {
      console.log("Note: current DB content already scores high; review before overwriting.");
    }
    return;
  }

  const counts = await updateLessonWithPayload(client, before.lesson_id, payload, { replaceExercises: true });
  const totalChanged = Object.values(counts).reduce((sum, count) => sum + count, 0);
  if (totalChanged <= 0) {
    throw new Error("Safety abort: update completed with 0 changed rows.");
  }

  console.log("\nRows changed:");
  console.table([counts]);

  const afterRows = await fetchLessons(client, { lessonId: before.lesson_id, limit: 2 });
  if (afterRows.length !== 1) throw new Error("Verification failed: updated lesson could not be read back.");
  printLessonSummary("Updated DB content after update", afterRows[0]);

  const viewerLesson = await fetchLessonForViewer(client, before.lesson_id);
  if (!viewerLesson?.content?.explanation) {
    throw new Error("Verification failed: curriculumRepo-shaped lesson content is missing.");
  }
  console.log("\nRepository-path verification:");
  console.log({
    lessonId: viewerLesson.id,
    title: viewerLesson.titleAr,
    contentChars: viewerLesson.content.explanation.length,
    exercises: viewerLesson.exercises.length,
    firstExercise: viewerLesson.exercises[0]?.question?.slice(0, 120) ?? null,
  });
});

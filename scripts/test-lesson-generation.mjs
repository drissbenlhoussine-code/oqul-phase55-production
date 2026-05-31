import {
  buildQualityReport,
  formatQualityReport,
  generateEnhancedLessonWithReport,
  loadLatestGeneratedLessonArtifact,
} from "./lib/ai-lesson-enhancer.mjs";
import { fetchLessons, parseArgs, withDb } from "./lib/lesson-quality-tools.mjs";

const args = parseArgs();
const defaultTitle = "الاحتمالات — مثال محلول";

await withDb(async (client) => {
  if (args["resume-from-local"] && !args["lesson-id"]) {
    throw new Error("Provide --lesson-id=<uuid> with --resume-from-local.");
  }

  const matches = await fetchLessons(client, {
    lessonId: args["lesson-id"],
    grade: args.grade ?? "tc",
    subject: args.subject ?? "advanced-math",
    title: args["lesson-id"] ? undefined : args.title ?? defaultTitle,
    limit: Number(args.limit ?? 10),
  });

  if (matches.length === 0) {
    throw new Error("No matching lesson found for generation test.");
  }

  const exactMatches = args["lesson-id"] ? matches : matches.filter((lesson) => String(lesson.lesson_title ?? "").includes(args.title ?? defaultTitle));
  const candidates = exactMatches.length ? exactMatches : matches;
  if (candidates.length > 1 && !args["lesson-id"]) {
    console.table(
      candidates.map((lesson) => ({
        id: lesson.lesson_id,
        title: lesson.lesson_title,
        grade: lesson.grade_slug,
        subject: lesson.subject_slug,
      }))
    );
    throw new Error("Multiple lessons matched. Re-run with --lesson-id=<uuid>.");
  }

  const lesson = candidates[0];
  console.log("Generation test target:");
  console.table([
    {
      id: lesson.lesson_id,
      title: lesson.lesson_title,
      grade: lesson.grade_slug,
      subject: lesson.subject_slug,
      unit: lesson.unit_slug,
    },
  ]);

  if (args["resume-from-local"]) {
    const { artifactPath, artifact } = await loadLatestGeneratedLessonArtifact(lesson.lesson_id);
    const generated = artifact.generated;
    const report = buildQualityReport(generated, lesson);
    console.log(`\nLoaded local artifact: ${artifactPath}`);
    console.log("\nGENERATED LESSON");
    console.log("----------------");
    console.log(JSON.stringify(generated, null, 2));
    console.log("\n" + formatQualityReport(report));
    console.log(`\nStatus: ${report.validationFailures.length || report.weakSections.length ? "generated but not safe" : "review quality gates passed"}`);
    console.log(`Safe to apply: ${!report.validationFailures.length && !report.weakSections.length && report.qualityScore >= Number(args.minimumScore ?? 75) && report.qualityScore >= Number(args.targetScore ?? 85) ? "yes" : "no"}`);
    console.log("\nNo Groq call was made. No database rows were changed.");
    return;
  }

  const result = await generateEnhancedLessonWithReport(lesson, {
    minimumScore: Number(args.minimumScore ?? 75),
    targetScore: Number(args.targetScore ?? 85),
    noRetry: Boolean(args["no-retry"]),
    saveArtifact: true,
  });
  const generated = result.payload;
  const report = result.report;

  console.log("\nGENERATED LESSON");
  console.log("----------------");
  console.log(JSON.stringify(generated, null, 2));
  console.log("\n" + formatQualityReport(report));
  console.log(`\nStatus: ${result.status}`);
  console.log(`Safe to apply: ${result.safeToApply ? "yes" : "no"}`);
  if (result.message) console.log(`Message: ${result.message}`);
  if (result.artifactPath) console.log(`Local artifact: ${result.artifactPath}`);
  if (!result.safeToApply) {
    console.log("Generated but not safe. Do not apply this lesson until all weak sections and validation failures are resolved.");
  }
  if (result.status === "blocked_by_rate_limit") {
    console.log("Generation incomplete because retry was rate-limited.");
  }
  console.log(`Resume command: node scripts/test-lesson-generation.mjs --lesson-id=${lesson.lesson_id} --resume-from-local`);
  console.log("\nNo database rows were changed.");
});

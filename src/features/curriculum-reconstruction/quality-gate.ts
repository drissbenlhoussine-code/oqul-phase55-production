import type { DeepLesson } from "./lesson-shape";

export function validateDeepLessonQuality(lesson: DeepLesson) {
  const issues: string[] = [];

  if (!lesson.title || lesson.title.includes("يحتاج مطابقة")) {
    issues.push("lesson_title_not_verified");
  }

  if (lesson.examples.length < 3) issues.push("not_enough_examples");
  if (lesson.interactiveQuestions.length < 3) issues.push("not_enough_interactive_questions");
  if (lesson.commonMistakes.length < 3) issues.push("not_enough_common_mistakes");
  if (lesson.remediation.length < 4) issues.push("not_enough_remediation_steps");

  const exerciseCount =
    lesson.exercises.easy.length +
    lesson.exercises.medium.length +
    lesson.exercises.hard.length +
    lesson.exercises.examStyle.length;

  if (exerciseCount < 12) issues.push("not_enough_exercises");
  if (!lesson.leilaTutorHooks?.opening) issues.push("missing_leila_hooks");

  return {
    ok: issues.length === 0,
    issues,
    score: Math.max(0, 100 - issues.length * 12),
  };
}
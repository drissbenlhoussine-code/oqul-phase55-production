export type ExerciseBlueprint = {
  difficulty: "easy" | "medium" | "hard" | "exam";
  format: "mcq" | "short_answer" | "step_by_step" | "oral" | "writing";
  cognitiveSkill:
    | "remember"
    | "understand"
    | "apply"
    | "analyze"
    | "evaluate"
    | "create";
  correctionMode: "instant" | "guided" | "teacher_like";
};

export function createExerciseBlueprints(layer: "primary" | "middle_school" | "secondary"): ExerciseBlueprint[] {
  if (layer === "primary") {
    return [
      { difficulty: "easy", format: "oral", cognitiveSkill: "understand", correctionMode: "guided" },
      { difficulty: "easy", format: "mcq", cognitiveSkill: "apply", correctionMode: "instant" },
      { difficulty: "medium", format: "short_answer", cognitiveSkill: "apply", correctionMode: "teacher_like" },
    ];
  }

  if (layer === "secondary") {
    return [
      { difficulty: "medium", format: "step_by_step", cognitiveSkill: "analyze", correctionMode: "guided" },
      { difficulty: "hard", format: "step_by_step", cognitiveSkill: "evaluate", correctionMode: "teacher_like" },
      { difficulty: "exam", format: "writing", cognitiveSkill: "create", correctionMode: "teacher_like" },
    ];
  }

  return [
    { difficulty: "easy", format: "mcq", cognitiveSkill: "understand", correctionMode: "instant" },
    { difficulty: "medium", format: "short_answer", cognitiveSkill: "apply", correctionMode: "guided" },
    { difficulty: "hard", format: "step_by_step", cognitiveSkill: "analyze", correctionMode: "teacher_like" },
  ];
}
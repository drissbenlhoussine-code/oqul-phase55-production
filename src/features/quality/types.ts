export type EducationLayer = "primary" | "middle_school" | "secondary";

export type QualitySignal = {
  childId?: string;
  layer: EducationLayer;
  grade?: string;
  subject?: string;
  lessonId?: string;
  answerCorrect?: boolean;
  responseTimeSeconds?: number;
  hintsUsed?: number;
  retryCount?: number;
  confidenceSelfRating?: 1 | 2 | 3 | 4 | 5;
  emotion?: "confident" | "neutral" | "confused" | "frustrated" | "excited";
};

export type QualityDecision = {
  masteryDelta: number;
  confidenceDelta: number;
  nextAction:
    | "continue"
    | "give_hint"
    | "simplify"
    | "repeat_with_example"
    | "review_prerequisite"
    | "increase_difficulty"
    | "celebrate";
  reason: string;
  leilaInstruction: string;
};
export type TutorState =
  | "INTRO"
  | "EXPLAIN"
  | "QUESTION"
  | "WAITING_ANSWER"
  | "ANALYZE_MISTAKE"
  | "REINFORCE"
  | "ADAPT"
  | "COMPLETE";

export type EmotionalSignal = "calm" | "excited" | "hesitant" | "frustrated" | "confident";

export type MasteryBand = "discover" | "practice" | "review" | "master";

export type LearningMission = {
  id: string;
  title: string;
  description: string;
  xpReward: number;
  estimatedMinutes: number;
  type: "lesson" | "review" | "quiz" | "confidence";
};

export type Phase40LearningSnapshot = {
  childId: string;
  masteryScore: number;
  confidenceScore: number;
  masteryBand: MasteryBand;
  emotionalSignal: EmotionalSignal;
  tutorState: TutorState;
  nextTeacherMove: string;
  missions: LearningMission[];
  parentInsight: string;
  safetyNote: string;
};

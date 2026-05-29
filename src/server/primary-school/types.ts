export type PrimaryGrade = "1AP" | "2AP" | "3AP" | "4AP" | "5AP" | "6AP";

export type PrimarySubject =
  | "math"
  | "arabic"
  | "french"
  | "science"
  | "islamic_education"
  | "social_studies";

export type PrimaryLanguage = "auto" | "darija" | "ar_fusha" | "fr";

export type PrimaryLesson = {
  id: string;
  grade: PrimaryGrade;
  subject: PrimarySubject;
  unit: string;
  titleAr: string;
  titleFr?: string;
  durationMinutes: number;
  objectives: string[];
  prerequisites: string[];
  competencies: string[];
  misconceptions: string[];
  microSteps: string[];
  exerciseTypes: Array<"oral_prompt" | "picture_choice" | "guided_practice" | "mini_game" | "quick_check">;
  parentSignal: string;
  masteryThreshold: number;
};

export type PrimaryLessonBlock = {
  kind: "warmup" | "visual_explain" | "voice_prompt" | "mini_game" | "guided_practice" | "encouragement" | "parent_note";
  title: string;
  body: string;
  expectedAnswer?: string;
  childFriendlyHint?: string;
};

export type PrimaryStudentProfile = {
  childId: string;
  childName?: string;
  grade: PrimaryGrade;
  targetLanguage: Exclude<PrimaryLanguage, "auto">;
  subjects: PrimarySubject[];
  totalLessons: number;
  priorityLessons: PrimaryLesson[];
  suggestedMicroLesson: PrimaryLessonBlock[];
  tutorPolicy: {
    persona: string;
    defaultLanguage: string;
    pacing: string[];
    reinforcement: string[];
  };
  uxMode: "primary_child_first";
  safetyNote: string;
};

export type DeepLessonStage = "primary" | "middle" | "secondary";

export type DeepLessonInput = {
  registryId: string;
  stage: DeepLessonStage;
  grade: string;
  gradeAr: string;
  subject: string;
  subjectAr: string;
  unitTitle: string;
  lessonTitle: string;
  verificationStatus: string;
};

export type DeepLesson = {
  registryId: string;
  title: string;
  grade: string;
  subject: string;
  unitTitle: string;
  languagePolicy: {
    defaultLanguage: "formal_arabic" | "darija" | "french";
    canSwitchTo: string[];
  };
  objectives: string[];
  prerequisiteCheck: string[];
  explanation: {
    hook: string;
    concept: string;
    stepByStep: string[];
    teacherNotes: string[];
  };
  examples: {
    level: "easy" | "medium" | "hard";
    prompt: string;
    solutionSteps: string[];
  }[];
  interactiveQuestions: {
    question: string;
    expectedAnswer: string;
    hint: string;
  }[];
  commonMistakes: {
    mistake: string;
    whyItHappens: string;
    correction: string;
  }[];
  remediation: {
    trigger: string;
    action: string;
    followUpQuestion: string;
  }[];
  exercises: {
    easy: string[];
    medium: string[];
    hard: string[];
    examStyle: string[];
  };
  miniAssessment: {
    question: string;
    answer: string;
  }[];
  summary: string[];
  leilaTutorHooks: {
    opening: string;
    ifCorrect: string;
    ifWrong: string;
    ifConfused: string;
    closing: string;
  };
};

export const deepLessonQualityRules = {
  noPlaceholderTitles: true,
  noCopiedSourceText: true,
  minimumExamples: 3,
  minimumInteractiveQuestions: 3,
  minimumCommonMistakes: 3,
  minimumExercises: 12,
  requiresLeilaHooks: true,
  requiresRemediation: true,
};
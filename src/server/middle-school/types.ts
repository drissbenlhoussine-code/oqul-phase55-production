export type MiddleSchoolGrade = "1AC" | "2AC" | "3AC";

export type MiddleSchoolSubject =
  | "math"
  | "physics_chemistry"
  | "life_earth_sciences"
  | "arabic"
  | "french"
  | "social_studies";

export type LearningLanguage = "auto" | "ar_fusha" | "darija" | "fr" | "en";

export type CompetencyDepth = "foundation" | "practice" | "mastery" | "exam_ready";

export type MiddleSchoolCompetency = {
  id: string;
  grade: MiddleSchoolGrade;
  subject: MiddleSchoolSubject;
  titleAr: string;
  titleFr?: string;
  skill: string;
  prerequisites: string[];
  misconceptions: string[];
  objectives: string[];
  lessonSeeds: string[];
  exerciseTypes: Array<"guided" | "interactive" | "socratic" | "mini_assessment" | "remediation">;
};

export type LessonEngineBlock = {
  kind: "objective" | "explanation" | "example" | "interactive_question" | "remediation" | "summary" | "mini_assessment";
  title: string;
  body: string;
  expectedAnswer?: string;
  adaptiveHint?: string;
};

export type Phase42StudentProfile = {
  childId: string;
  childName?: string;
  grade: MiddleSchoolGrade;
  language: LearningLanguage;
  targetLanguage: Exclude<LearningLanguage, "auto">;
  subjects: MiddleSchoolSubject[];
  priorityCompetencies: MiddleSchoolCompetency[];
  suggestedLesson: LessonEngineBlock[];
  tutorPolicy: {
    tone: string;
    defaultLanguage: string;
    languageSwitchingRule: string;
    teachingLoop: string[];
  };
  uxMode: "middle_school_smart";
  safetyNote: string;
};

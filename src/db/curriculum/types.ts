export interface Exercise {
  type: "mcq" | "true_false" | "fill_blank";
  question: string;
  options?: string[];
  correctAnswer: string;
  explanation: string;
  points: number;
}

export interface LessonData {
  slug: string;
  titleAr: string;
  objectives: string[];
  difficulty: "easy" | "medium" | "hard";
  durationMin: number;
  explanation: string;
  vocabulary: { word: string; definition: string }[];
  examples: { text: string; note?: string }[];
  summary: string;
  exercises: Exercise[];
}

export interface UnitData {
  slug: string;
  titleAr: string;
  orderIndex: number;
  lessons: LessonData[];
}

export interface SubjectData {
  slug: string;
  titleAr: string;
  icon: string;
  color: string;
  orderIndex: number;
  units: UnitData[];
}

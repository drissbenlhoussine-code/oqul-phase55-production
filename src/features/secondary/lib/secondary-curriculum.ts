import fs from "node:fs";
import path from "node:path";

export type SecondaryLesson = {
  lessonId: string;
  grade: string;
  gradeLabelAr: string;
  subject: string;
  subjectLabelAr: string;
  unit: string;
  title: string;
  lessonType: string;
  objectives: string[];
  competencies: string[];
  prerequisites: string[];
  misconceptions: string[];
  assessment: {
    quickCheck: number;
    guidedExercises: number;
    examStyleQuestions: number;
    masteryThreshold: number;
  };
  leilaMode: {
    defaultLanguage: string;
    canSwitchTo: string[];
    teachingStyle: string;
    tone: string;
  };
};

const DATA_DIR = path.join(process.cwd(), "src", "features", "secondary", "data");

export function getSecondaryLessons(grade?: string, subject?: string): SecondaryLesson[] {
  const lessons: SecondaryLesson[] = [];
  if (!fs.existsSync(DATA_DIR)) return lessons;

  const grades = grade ? [grade] : fs.readdirSync(DATA_DIR);

  for (const g of grades) {
    const gradeDir = path.join(DATA_DIR, g);
    if (!fs.existsSync(gradeDir)) continue;

    const files = subject ? [`${subject}.json`] : fs.readdirSync(gradeDir).filter((f) => f.endsWith(".json"));

    for (const file of files) {
      const filePath = path.join(gradeDir, file);
      if (!fs.existsSync(filePath)) continue;
      lessons.push(...JSON.parse(fs.readFileSync(filePath, "utf8")));
    }
  }

  return lessons;
}

export function getSecondarySummary() {
  const lessons = getSecondaryLessons();
  const byGrade: Record<string, number> = {};
  const bySubject: Record<string, number> = {};

  for (const lesson of lessons) {
    byGrade[lesson.grade] = (byGrade[lesson.grade] ?? 0) + 1;
    bySubject[lesson.subject] = (bySubject[lesson.subject] ?? 0) + 1;
  }

  return {
    totalLessons: lessons.length,
    grades: Object.keys(byGrade),
    subjects: Object.keys(bySubject),
    byGrade,
    bySubject,
  };
}
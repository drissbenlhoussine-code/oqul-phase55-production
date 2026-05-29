import { curriculumRepo } from "@/server/repositories/curriculum";

export class LearningService {
  async listSubjects(input: { gradeId?: string }) {
    if (!input.gradeId) return [];
    return curriculumRepo.getSubjects(input.gradeId);
  }

  async listUnitsWithLessons(input: { subjectId: string }) {
    return curriculumRepo.getUnitsWithLessons(input.subjectId);
  }

  async getLesson(lessonId: string) {
    return curriculumRepo.getLessonWithContent(lessonId);
  }

  async getGrades(cycleSlug?: string) {
    return curriculumRepo.getGrades(cycleSlug);
  }

  async submitExercise(input: {
    childId: string;
    exerciseId: string;
    answer: string;
    lessonId: string;
  }) {
    const lesson = await curriculumRepo.getLessonWithContent(input.lessonId);
    const exercise = lesson?.exercises.find((e) => e.id === input.exerciseId);
    if (!exercise) return { correct: false, feedback: "التمرين غير موجود" };

    const correct =
      input.answer.trim().toLowerCase() === exercise.correctAnswer.trim().toLowerCase();

    return {
      correct,
      correctAnswer: exercise.correctAnswer,
      explanation: exercise.explanation,
      points: correct ? exercise.points : 0,
      feedback: correct
        ? "أحسنت! إجابة صحيحة 🎉"
        : `الجواب الصحيح هو: ${exercise.correctAnswer}. ${exercise.explanation ?? ""}`,
    };
  }
}

export const learningService = new LearningService();

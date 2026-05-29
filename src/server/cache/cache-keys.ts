export const cacheKeys = {
  lesson: (lessonId: string) => `lesson:${lessonId}`,
  subjectLessons: (subjectId: string) => `subject:${subjectId}:lessons`,
  dashboard: (userId: string) => `dashboard:${userId}`,
  recommendation: (childId: string) => `recommendation:${childId}`,
  aiExplanation: (lessonId: string, promptVersion: string) =>
    `ai:explanation:${lessonId}:${promptVersion}`,
};

import { apiClient } from "@/lib/api/client";

export type DashboardSummary = {
  childName: string;
  level: string;
  xp: number;
  streakDays: number;
  completedLessons: number;
  weeklyProgress: number;
};

export type TutorMessage = {
  id: string;
  role: "user" | "assistant";
  content: string;
  createdAt: string;
};

export const productApi = {
  dashboard: {
    summary: () => apiClient.get<DashboardSummary>("/api/analytics/learning"),
  },
  learning: {
    subjects: () => apiClient.get("/api/learning/subjects"),
    lessons: (subjectId?: string) =>
      apiClient.get(`/api/learning/lessons${subjectId ? `?subjectId=${subjectId}` : ""}`),
    completeLesson: (lessonId: string) =>
      apiClient.post("/api/progress/complete-lesson", { lessonId }),
  },
  tutor: {
    ask: (message: string, lessonId?: string) =>
      apiClient.post<{ answer: string }>("/api/ai/leila", { message, lessonId }),
  },
};

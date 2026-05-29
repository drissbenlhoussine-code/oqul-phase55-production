import { progressRepo } from "@/server/repositories/progress";

export interface AIUsageLog {
  provider: string;
  model: string;
  tokens: number;
  latencyMs: number;
  success: boolean;
  userId?: string;
  feature?: "leila_text" | "leila_voice" | "quiz" | "lesson";
}

export async function logAIUsage(data: AIUsageLog) {
  // Always log to console for observability
  console.info("[AI_USAGE]", {
    provider: data.provider,
    model: data.model,
    tokens: data.tokens,
    latencyMs: data.latencyMs,
    success: data.success,
    userId: data.userId,
  });

  // Persist to DB if userId is provided
  if (data.userId) {
    try {
      await progressRepo.logAiUsage({
        userId: data.userId,
        feature: data.feature ?? "leila_text",
        tokens: data.tokens,
        provider: data.provider,
        model: data.model,
        success: data.success,
      });
    } catch (err) {
      // Don't let logging failure break the main flow
      console.error("[AI_USAGE] Failed to persist usage log:", err);
    }
  }
}

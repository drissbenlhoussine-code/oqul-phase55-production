import { buildLeilaPrompt } from "@/server/ai/prompt-builder";
import { getAIProvider } from "@/server/ai/provider-factory";
import { PROMPT_VERSIONS } from "./prompt-versioning";
import { logAIUsage } from "@/server/ai/usage/usage-logger";
import { moderateTutorInput } from "@/server/ai/moderation";
import { quotaService } from "@/server/services/quota-service";
import { AppError } from "@/server/errors/app-error";
import { ERROR_CODES } from "@/server/errors/error-codes";

export type AskLeilaInput = {
  userId: string;
  childId?: string;
  childName?: string;
  lessonTitle?: string;
  weakPoints?: string[];
  message: string;
};

export class TutorService {
  async askLeila(input: AskLeilaInput) {
    await quotaService.assertWithinQuota(input.userId, "leila_text");

    const moderation = await moderateTutorInput({
      text: input.message,
      userId: input.userId,
      locale: "ar",
    });

    if (!moderation.allowed) {
      throw new AppError(
        "لا يمكنني الإجابة على هذا الطلب. حاول صياغة سؤال تعليمي واضح.",
        ERROR_CODES.FORBIDDEN,
        403
      );
    }

    const provider = getAIProvider();
    const prompt = buildLeilaPrompt({
      childName: input.childName,
      lessonTitle: input.lessonTitle,
      weakPoints: input.weakPoints,
      message: input.message,
    });

    const startedAt = Date.now();

    try {
      const response = await provider.generateText({
        prompt,
        metadata: {
          promptVersion: PROMPT_VERSIONS.LEILA_TUTOR_V1,
          userId: input.userId,
          childId: input.childId,
        },
      });

      await logAIUsage({
        provider: response.provider,
        model: response.model,
        tokens: response.usage.totalTokens,
        latencyMs: Date.now() - startedAt,
        success: true,
        userId: input.userId,
      });

      return {
        answer: response.text,
        provider: response.provider,
        model: response.model,
        promptVersion: PROMPT_VERSIONS.LEILA_TUTOR_V1,
      };
    } catch (error) {
      await logAIUsage({
        provider: "unknown",
        model: "unknown",
        tokens: 0,
        latencyMs: Date.now() - startedAt,
        success: false,
        userId: input.userId,
      });

      throw error;
    }
  }
}

export const tutorService = new TutorService();

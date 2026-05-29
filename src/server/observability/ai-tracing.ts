import { endSpan, startSpan } from "./tracing";

export type AITraceInput = {
  requestId: string;
  provider: string;
  model: string;
  promptVersion?: string;
};

export function startAITrace(input: AITraceInput) {
  return startSpan("ai.execution", input.requestId, {
    provider: input.provider,
    model: input.model,
    promptVersion: input.promptVersion,
  });
}

export function finishAITrace(span: ReturnType<typeof startAITrace>) {
  return endSpan(span);
}

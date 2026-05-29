/**
 * prompt-builder.ts - unified prompt construction entry point.
 * All prompt logic now lives in personas/. This file delegates.
 */
import { buildLeilaSystemPrompt, type LeilaContext } from "./leila";

export { buildLeilaSystemPrompt };
export type { LeilaContext };

export function buildLeilaPrompt(ctx: LeilaContext & { message?: string }): string {
  return buildLeilaSystemPrompt(ctx);
}

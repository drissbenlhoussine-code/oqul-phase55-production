import type { ModerationInput, ModerationResult } from "./moderation-types";

const blockedPatterns = [
  /كلمة\s*السر/i,
  /ignore\s+previous\s+instructions/i,
  /system\s+prompt/i,
];

export async function moderateTutorInput(input: ModerationInput): Promise<ModerationResult> {
  const reasons: string[] = [];

  for (const pattern of blockedPatterns) {
    if (pattern.test(input.text)) {
      reasons.push("Potential prompt injection or unsafe instruction.");
    }
  }

  return {
    allowed: reasons.length === 0,
    severity: reasons.length === 0 ? "safe" : "medium",
    reasons,
  };
}

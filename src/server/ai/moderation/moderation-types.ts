export type ModerationSeverity = "safe" | "low" | "medium" | "high";

export type ModerationResult = {
  allowed: boolean;
  severity: ModerationSeverity;
  reasons: string[];
};

export type ModerationInput = {
  text: string;
  userId?: string;
  childAge?: number;
  locale?: "ar" | "fr" | "en";
};

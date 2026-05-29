export type ConfidenceProfile = {
  learnerId: string;
  confidenceLevel: number;
  frustrationLevel: number;
};

export function evolveConfidence(
  profile: ConfidenceProfile,
  successfulSession: boolean,
): ConfidenceProfile {
  return {
    ...profile,
    confidenceLevel: successfulSession
      ? Math.min(1, profile.confidenceLevel + 0.07)
      : Math.max(0, profile.confidenceLevel - 0.04),
    frustrationLevel: successfulSession
      ? Math.max(0, profile.frustrationLevel - 0.06)
      : Math.min(1, profile.frustrationLevel + 0.08),
  };
}

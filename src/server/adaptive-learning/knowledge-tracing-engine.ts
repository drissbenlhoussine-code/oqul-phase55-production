export type KnowledgeState = {
  skillId: string;
  mastery: number;
  confidence: number;
  misconceptionRisk: number;
};

export class KnowledgeTracingEngine {
  update(state: KnowledgeState, correct: boolean): KnowledgeState {
    return {
      ...state,
      mastery: Math.max(0, Math.min(1, state.mastery + (correct ? 0.08 : -0.04))),
      confidence: Math.max(0, Math.min(1, state.confidence + (correct ? 0.05 : -0.03))),
      misconceptionRisk: correct
        ? Math.max(0, state.misconceptionRisk - 0.05)
        : Math.min(1, state.misconceptionRisk + 0.08),
    };
  }
}

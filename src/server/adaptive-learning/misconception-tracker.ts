export type MisconceptionEvent = {
  skillId: string;
  pattern: string;
  frequency: number;
};

export class MisconceptionTracker {
  detect(events: MisconceptionEvent[]) {
    return events
      .filter((event) => event.frequency >= 3)
      .map((event) => ({
        skillId: event.skillId,
        misconception: event.pattern,
        remediationSuggested: true,
      }));
  }
}

export type DomainEventName =
  | "lesson.completed"
  | "exercise.submitted"
  | "ai.response.generated"
  | "quota.exceeded"
  | "streak.updated"
  | "recommendation.generated";

export type DomainEvent<TPayload = Record<string, unknown>> = {
  id: string;
  name: DomainEventName;
  payload: TPayload;
  occurredAt: string;
  actorId?: string;
  requestId?: string;
};

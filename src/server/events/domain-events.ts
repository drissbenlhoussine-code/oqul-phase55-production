export type DomainEventType =
  | "auth.registered"
  | "auth.logged_in"
  | "lesson.completed"
  | "exercise.submitted"
  | "ai.interaction.completed"
  | "quota.exceeded";

export type DomainEvent<TPayload extends Record<string, unknown> = Record<string, unknown>> = {
  id: string;
  type: DomainEventType;
  payload: TPayload;
  occurredAt: Date;
  requestId?: string;
};

export function createDomainEvent<TPayload extends Record<string, unknown>>(
  type: DomainEventType,
  payload: TPayload,
  requestId?: string
): DomainEvent<TPayload> {
  return {
    id: crypto.randomUUID(),
    type,
    payload,
    occurredAt: new Date(),
    requestId,
  };
}

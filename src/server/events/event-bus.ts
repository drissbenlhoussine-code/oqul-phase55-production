import type { DomainEvent, DomainEventName } from "./event-types";

type EventHandler<TPayload = Record<string, unknown>> = (
  event: DomainEvent<TPayload>
) => Promise<void> | void;

const handlers = new Map<DomainEventName, EventHandler[]>();

export function onDomainEvent(name: DomainEventName, handler: EventHandler) {
  const current = handlers.get(name) ?? [];
  handlers.set(name, [...current, handler]);
}

export async function emitDomainEvent<TPayload extends Record<string, unknown>>(
  name: DomainEventName,
  payload: TPayload,
  meta?: Pick<DomainEvent, "actorId" | "requestId">
) {
  const event: DomainEvent<TPayload> = {
    id: crypto.randomUUID(),
    name,
    payload,
    occurredAt: new Date().toISOString(),
    ...meta,
  };

  const currentHandlers = handlers.get(name) ?? [];
  await Promise.all(currentHandlers.map((handler) => handler(event)));

  return event;
}

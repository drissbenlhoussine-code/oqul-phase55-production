export type OutboxEvent<TPayload = unknown> = {
  id: string;
  type: string;
  payload: TPayload;
  createdAt: string;
  processedAt?: string;
};

const outbox: OutboxEvent[] = [];

export function addOutboxEvent<TPayload>(
  type: string,
  payload: TPayload,
  id = crypto.randomUUID()
): OutboxEvent<TPayload> {
  const event: OutboxEvent<TPayload> = {
    id,
    type,
    payload,
    createdAt: new Date().toISOString(),
  };

  outbox.push(event as OutboxEvent);

  return event;
}

export function markOutboxEventProcessed(id: string) {
  const event = outbox.find((item) => item.id === id);

  if (event) {
    event.processedAt = new Date().toISOString();
  }

  return event;
}

export function listPendingOutboxEvents() {
  return outbox.filter((event) => !event.processedAt);
}

import { randomUUID } from "node:crypto";
import { withPostgresTransaction } from "@/server/db/transaction";
import { insertOutboxEventInTransaction } from "./transactional-outbox";

export async function writeBusinessStateWithOutbox(input: {
  entityId?: string;
  entityType: string;
  eventType: string;
  payload: Record<string, unknown>;
}) {
  const entityId = input.entityId ?? randomUUID();

  return withPostgresTransaction(async (client) => {
    await client.query(
      `
      INSERT INTO reliability_entities (id, entity_type, payload)
      VALUES ($1, $2, $3::jsonb)
      ON CONFLICT (id) DO UPDATE
      SET payload = EXCLUDED.payload, updated_at = NOW()
      `,
      [entityId, input.entityType, JSON.stringify(input.payload)]
    );

    const event = await insertOutboxEventInTransaction(client, {
      eventType: input.eventType,
      aggregateId: entityId,
      payload: input.payload,
    });

    return { entityId, eventId: event.id };
  });
}

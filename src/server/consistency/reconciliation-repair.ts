import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";
import { recordEffectOnce } from "./effect-receipts";

export async function repairMissingEffectReceipts(limit = 50) {
  const pool = getPostgresPool();

  const missing = await pool.query(
    `
    SELECT o.id, o.event_type, o.aggregate_id, o.payload
    FROM outbox_events o
    LEFT JOIN effect_receipts e ON e.event_id = o.id
    WHERE o.status = 'processed'
      AND e.event_id IS NULL
    ORDER BY o.created_at ASC
    LIMIT $1
    `,
    [limit]
  );

  let repaired = 0;

  for (const event of missing.rows) {
    const effectKey = [
      "repair",
      event.event_type,
      event.aggregate_id,
      event.id,
    ].join(":");

    const receipt = await recordEffectOnce({
      effectKey,
      eventId: event.id,
      effectType: event.event_type,
      aggregateId: event.aggregate_id,
      payload: event.payload,
    });

    if (receipt.applied) {
      await pool.query(
        `
        INSERT INTO repaired_effects (id, event_id, repair_type)
        VALUES ($1, $2, $3)
        ON CONFLICT (id) DO NOTHING
        `,
        [randomUUID(), event.id, "missing-effect-receipt"]
      );
      repaired += 1;
    }
  }

  return {
    checked: missing.rowCount ?? 0,
    repaired,
  };
}

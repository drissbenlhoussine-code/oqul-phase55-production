import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export async function publishRevocationEvent(input: {
  subjectType: "trust-anchor" | "provider-key" | "delegation" | "worker" | "route";
  subjectId: string;
  reason: string;
  issuedBy: string;
}) {
  const pool = getPostgresPool();
  const eventId = randomUUID();

  await pool.query(
    `
    INSERT INTO authority_revocation_events (
      event_id,
      subject_type,
      subject_id,
      reason,
      issued_by
    )
    VALUES ($1, $2, $3, $4, $5)
    `,
    [eventId, input.subjectType, input.subjectId, input.reason, input.issuedBy]
  );

  return { eventId };
}

export async function processRevocationEvents(consumerId = "default-authority-consumer") {
  const pool = getPostgresPool();

  const offset = await pool.query(
    "SELECT last_event_created_at FROM authority_stream_offsets WHERE consumer_id = $1",
    [consumerId]
  );

  const lastSeen = offset.rows[0]?.last_event_created_at ?? null;

  const events = await pool.query(
    `
    SELECT *
    FROM authority_revocation_events
    WHERE ($1::timestamptz IS NULL OR created_at > $1)
      AND processed_at IS NULL
    ORDER BY created_at ASC
    LIMIT 100
    `,
    [lastSeen]
  );

  for (const event of events.rows) {
    if (event.subject_type === "worker") {
      await pool.query(
        "UPDATE worker_admissions SET revoked_at = NOW() WHERE worker_id = $1",
        [event.subject_id]
      );
    }

    if (event.subject_type === "provider-key") {
      await pool.query(
        "UPDATE provider_authority_keys SET active = FALSE, revoked_at = NOW() WHERE key_id = $1",
        [event.subject_id]
      );
    }

    if (event.subject_type === "delegation") {
      await pool.query(
        "UPDATE delegated_authorities SET active = FALSE, revoked_at = NOW() WHERE delegation_id = $1",
        [event.subject_id]
      );
    }

    await pool.query(
      "UPDATE authority_revocation_events SET processed_at = NOW() WHERE event_id = $1",
      [event.event_id]
    );
  }

  const newest = events.rows.at(-1)?.created_at ?? lastSeen;

  await pool.query(
    `
    INSERT INTO authority_stream_offsets (consumer_id, last_event_created_at)
    VALUES ($1, $2)
    ON CONFLICT (consumer_id)
    DO UPDATE SET
      last_event_created_at = EXCLUDED.last_event_created_at,
      updated_at = NOW()
    `,
    [consumerId, newest]
  );

  return {
    processed: events.rowCount ?? 0,
  };
}

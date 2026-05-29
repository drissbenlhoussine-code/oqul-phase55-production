import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";

export type ReconciliationResult = {
  runId: string;
  checkedEvents: number;
  missingReceipts: number;
};

export async function startReconciliationRun() {
  const pool = getPostgresPool();
  const id = randomUUID();

  await pool.query(
    `
    INSERT INTO reconciliation_runs (id, status)
    VALUES ($1, 'running')
    `,
    [id]
  );

  return id;
}

export async function finishReconciliationRun(input: {
  runId: string;
  checkedEvents: number;
  repairedEvents: number;
  error?: unknown;
}) {
  const pool = getPostgresPool();

  await pool.query(
    `
    UPDATE reconciliation_runs
    SET
      status = $2,
      finished_at = NOW(),
      checked_events = $3,
      repaired_events = $4,
      last_error = $5
    WHERE id = $1
    `,
    [
      input.runId,
      input.error ? "failed" : "completed",
      input.checkedEvents,
      input.repairedEvents,
      input.error instanceof Error ? input.error.message : input.error ? String(input.error) : null,
    ]
  );
}

export async function detectMissingEffectReceipts(limit = 100): Promise<ReconciliationResult> {
  const pool = getPostgresPool();
  const runId = await startReconciliationRun();

  const result = await pool.query(
    `
    SELECT o.id, o.aggregate_id
    FROM outbox_events o
    LEFT JOIN effect_receipts e ON e.event_id = o.id
    WHERE o.status = 'processed'
      AND e.event_id IS NULL
    ORDER BY o.created_at ASC
    LIMIT $1
    `,
    [limit]
  );

  await finishReconciliationRun({
    runId,
    checkedEvents: result.rowCount ?? 0,
    repairedEvents: 0,
  });

  return {
    runId,
    checkedEvents: result.rowCount ?? 0,
    missingReceipts: result.rowCount ?? 0,
  };
}

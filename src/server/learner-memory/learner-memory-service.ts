import { randomUUID } from "node:crypto";
import { getPostgresPool } from "@/server/db/postgres";
import {
  type LearnerMemorySignal,
  summarizeLearnerMemory,
} from "./learner-memory-engine";

export async function createLearnerMemorySnapshot(input: {
  studentId: string;
  memoryType?: string;
  signals: LearnerMemorySignal[];
}) {
  const pool = getPostgresPool();
  const snapshot = summarizeLearnerMemory(input.signals);
  const snapshotId = randomUUID();

  await pool.query(
    `
    INSERT INTO learner_memory_snapshots (
      snapshot_id,
      student_id,
      memory_type,
      summary,
      signals,
      confidence_score
    )
    VALUES ($1, $2, $3, $4, $5::jsonb, $6)
    `,
    [
      snapshotId,
      input.studentId,
      input.memoryType ?? "learning-summary",
      snapshot.summary,
      JSON.stringify(snapshot),
      snapshot.confidenceHint === "rising" ? 70 : 45,
    ]
  );

  return {
    snapshotId,
    ...snapshot,
  };
}

export async function getLatestLearnerMemory(studentId: string) {
  const pool = getPostgresPool();

  const result = await pool.query(
    `
    SELECT *
    FROM learner_memory_snapshots
    WHERE student_id = $1
    ORDER BY created_at DESC
    LIMIT 1
    `,
    [studentId]
  );

  return result.rows[0] ?? null;
}

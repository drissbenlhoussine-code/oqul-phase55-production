import { enqueueBullJob } from "./bullmq-adapter";

export async function moveToDeadLetterQueue<TPayload>(
  queueName: string,
  jobName: string,
  payload: TPayload,
  reason: string
) {
  await enqueueBullJob("dead-letter", `${queueName}:${jobName}`, {
    originalQueue: queueName,
    originalJob: jobName,
    payload,
    reason,
    failedAt: new Date().toISOString(),
  });
}

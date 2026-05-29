import { createBullWorker } from "./bullmq-adapter";

export function startJobWorker<TPayload>(
  queueName: string,
  processor: (payload: TPayload) => Promise<void>
) {
  const worker = createBullWorker(queueName, processor);

  worker.on("completed", (job) => {
    console.log("[OQUL_WORKER_COMPLETED]", {
      queueName,
      jobId: job.id,
    });
  });

  worker.on("failed", (job, error) => {
    console.error("[OQUL_WORKER_FAILED]", {
      queueName,
      jobId: job?.id,
      error: error.message,
    });
  });

  return worker;
}

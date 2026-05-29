import { Queue, Worker, type JobsOptions } from "bullmq";
import { getRedisClient } from "@/server/cache/redis-client";

export type BullMQJobOptions = JobsOptions & {
  idempotencyKey?: string;
};

function getConnection() {
  const connection = getRedisClient();

  if (!connection) {
    throw new Error("Redis connection is required for BullMQ queues.");
  }

  return connection;
}

export function createBullQueue(name: string) {
  return new Queue(name, {
    connection: getConnection(),
    defaultJobOptions: {
      attempts: 3,
      backoff: {
        type: "exponential",
        delay: 1000,
      },
      removeOnComplete: 100,
      removeOnFail: false,
    },
  });
}

export async function enqueueBullJob<TPayload>(
  queueName: string,
  jobName: string,
  payload: TPayload,
  options?: BullMQJobOptions
) {
  const queue = createBullQueue(queueName);

  return queue.add(jobName, payload, {
    ...options,
    jobId: options?.idempotencyKey,
  });
}

export function createBullWorker<TPayload>(
  queueName: string,
  processor: (payload: TPayload) => Promise<void>
) {
  return new Worker(
    queueName,
    async (job) => {
      await processor(job.data as TPayload);
    },
    {
      connection: getConnection(),
      concurrency: Number(process.env.WORKER_CONCURRENCY ?? 5),
    }
  );
}

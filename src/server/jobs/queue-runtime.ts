import {
  enqueueBullJob,
  createBullWorker,
} from "./bullmq-adapter";

export type QueueRuntimeMode = "bullmq";

export const QUEUE_RUNTIME_MODE: QueueRuntimeMode = "bullmq";

export const queueRuntime = {
  mode: QUEUE_RUNTIME_MODE,
  enqueue: enqueueBullJob,
  createWorker: createBullWorker,
};

/**
 * Development-only queue adapter.
 *
 * This file must never be used as the production queue runtime.
 * The official runtime is BullMQ via queue-runtime.ts.
 */

export type DevMemoryJob<TPayload = unknown> = {
  id: string;
  queueName: string;
  jobName: string;
  payload: TPayload;
  createdAt: string;
};

const devJobs: DevMemoryJob[] = [];

export async function enqueueDevMemoryJob<TPayload>(
  queueName: string,
  jobName: string,
  payload: TPayload
) {
  if (process.env.NODE_ENV === "production") {
    throw new Error("Dev memory queue cannot be used in production.");
  }

  const job: DevMemoryJob<TPayload> = {
    id: crypto.randomUUID(),
    queueName,
    jobName,
    payload,
    createdAt: new Date().toISOString(),
  };

  devJobs.push(job);

  return job;
}

export function listDevMemoryJobs() {
  return devJobs;
}

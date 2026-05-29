export type QueueCorrectnessResult = {
  duplicateJobIds: string[];
  totalJobs: number;
  uniqueJobs: number;
};

export function detectDuplicateJobIds(jobIds: string[]): QueueCorrectnessResult {
  const seen = new Set<string>();
  const duplicates = new Set<string>();

  for (const jobId of jobIds) {
    if (seen.has(jobId)) {
      duplicates.add(jobId);
    }
    seen.add(jobId);
  }

  return {
    duplicateJobIds: Array.from(duplicates),
    totalJobs: jobIds.length,
    uniqueJobs: seen.size,
  };
}

export function buildIdempotencyKey(parts: string[]) {
  return parts.join(":");
}

export async function runConcurrent<T>(
  count: number,
  operation: (index: number) => Promise<T>
): Promise<T[]> {
  return Promise.all(
    Array.from({ length: count }, (_, index) => operation(index))
  );
}

export function countAllowed(results: Array<{ allowed: boolean }>) {
  return results.filter((result) => result.allowed).length;
}

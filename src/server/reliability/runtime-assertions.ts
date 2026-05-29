export function assertAtMost(value: number, max: number, message: string) {
  if (value > max) {
    throw new Error(`${message}: expected <= ${max}, received ${value}`);
  }
}

export function assertNoDuplicateValues(values: string[], message: string) {
  const unique = new Set(values);

  if (unique.size !== values.length) {
    throw new Error(message);
  }
}

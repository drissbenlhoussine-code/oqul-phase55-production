export function isProviderTimeout(error: unknown) {
  return error instanceof Error && /timeout/i.test(error.message);
}

export function createProviderTimeout(provider: string) {
  return new Error(`${provider} provider timeout`);
}

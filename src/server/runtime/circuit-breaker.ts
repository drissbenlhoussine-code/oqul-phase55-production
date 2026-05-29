type CircuitState = "closed" | "open" | "half-open";

export class CircuitBreaker {
  private failures = 0;
  private state: CircuitState = "closed";
  private openedAt: number | null = null;

  constructor(
    private readonly threshold = 5,
    private readonly cooldownMs = 30_000
  ) {}

  async execute<T>(operation: () => Promise<T>): Promise<T> {
    if (this.state === "open") {
      const canTry = this.openedAt && Date.now() - this.openedAt > this.cooldownMs;
      if (!canTry) throw new Error("Circuit breaker is open");
      this.state = "half-open";
    }

    try {
      const result = await operation();
      this.failures = 0;
      this.state = "closed";
      this.openedAt = null;
      return result;
    } catch (error) {
      this.failures += 1;
      if (this.failures >= this.threshold) {
        this.state = "open";
        this.openedAt = Date.now();
      }
      throw error;
    }
  }
}

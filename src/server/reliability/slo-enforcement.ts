export type SloCheck = {
  name: string;
  actual: number;
  budget: number;
  passed: boolean;
};

export function enforceSlo(name: string, actual: number, budget: number): SloCheck {
  return {
    name,
    actual,
    budget,
    passed: actual <= budget,
  };
}

export function assertSlo(check: SloCheck) {
  if (!check.passed) {
    throw new Error(
      `SLO breach for ${check.name}: actual=${check.actual}, budget=${check.budget}`
    );
  }
}

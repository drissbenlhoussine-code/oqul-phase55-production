export type RecoveryBudgetCheck = {
  name: string;
  startedAt: number;
  recoveredAt: number;
  budgetMs: number;
  passed: boolean;
};

export function checkRecoveryBudget(
  name: string,
  startedAt: number,
  recoveredAt: number,
  budgetMs: number
): RecoveryBudgetCheck {
  return {
    name,
    startedAt,
    recoveredAt,
    budgetMs,
    passed: recoveredAt - startedAt <= budgetMs,
  };
}

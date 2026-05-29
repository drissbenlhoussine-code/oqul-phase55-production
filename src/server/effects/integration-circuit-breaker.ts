import { getPostgresPool } from "@/server/db/postgres";

export async function isIntegrationCircuitOpen(integration: string) {
  const pool = getPostgresPool();

  const result = await pool.query(
    "SELECT state FROM integration_circuit_breakers WHERE integration = $1",
    [integration]
  );

  return result.rows[0]?.state === "open";
}

export async function recordIntegrationFailure(input: {
  integration: string;
  openAfter?: number;
}) {
  const pool = getPostgresPool();
  const openAfter = input.openAfter ?? 5;

  await pool.query(
    `
    INSERT INTO integration_circuit_breakers (
      integration,
      state,
      failure_count,
      updated_at
    )
    VALUES ($1, 'closed', 1, NOW())
    ON CONFLICT (integration)
    DO UPDATE SET
      failure_count = integration_circuit_breakers.failure_count + 1,
      state = CASE
        WHEN integration_circuit_breakers.failure_count + 1 >= $2 THEN 'open'
        ELSE integration_circuit_breakers.state
      END,
      opened_at = CASE
        WHEN integration_circuit_breakers.failure_count + 1 >= $2 THEN NOW()
        ELSE integration_circuit_breakers.opened_at
      END,
      updated_at = NOW()
    `,
    [input.integration, openAfter]
  );
}

export async function closeIntegrationCircuit(integration: string) {
  const pool = getPostgresPool();

  await pool.query(
    `
    INSERT INTO integration_circuit_breakers (
      integration,
      state,
      failure_count,
      updated_at
    )
    VALUES ($1, 'closed', 0, NOW())
    ON CONFLICT (integration)
    DO UPDATE SET
      state = 'closed',
      failure_count = 0,
      opened_at = NULL,
      updated_at = NOW()
    `,
    [integration]
  );
}

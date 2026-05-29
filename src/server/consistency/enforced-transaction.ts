import type { PoolClient } from "pg";
import { withPostgresTransaction } from "@/server/db/transaction";

const transactionClients = new WeakSet<PoolClient>();

export async function withConsistencyTransaction<T>(
  operation: (client: PoolClient) => Promise<T>
): Promise<T> {
  return withPostgresTransaction(async (client) => {
    transactionClients.add(client);

    try {
      return await operation(client);
    } finally {
      transactionClients.delete(client);
    }
  });
}

export function assertConsistencyTransaction(client: PoolClient) {
  if (!transactionClients.has(client)) {
    throw new Error(
      "Consistency invariant violated: outbox writes must happen inside withConsistencyTransaction()."
    );
  }
}

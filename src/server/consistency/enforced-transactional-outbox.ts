import type { PoolClient } from "pg";
import { insertOutboxEventInTransaction } from "./transactional-outbox";
import { assertConsistencyTransaction } from "./enforced-transaction";

export async function insertEnforcedOutboxEvent(
  client: PoolClient,
  input: {
    id?: string;
    eventType: string;
    aggregateId: string;
    payload: unknown;
  }
) {
  assertConsistencyTransaction(client);
  return insertOutboxEventInTransaction(client, input);
}

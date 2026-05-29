export interface QueueAdapter {
  add<T>(queueName: string, payload: T): Promise<void>;
}

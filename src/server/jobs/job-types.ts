export type BackgroundJob<T = unknown> = {
  id: string;
  type: string;
  payload: T;
  createdAt: string;
};

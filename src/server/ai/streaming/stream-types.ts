export type AIStreamToken = {
  id: string;
  type: "token" | "done" | "error" | "metadata";
  content?: string;
  metadata?: Record<string, unknown>;
  createdAt: string;
};

export type AIStreamOptions = {
  requestId: string;
  userId?: string;
  provider?: string;
  model?: string;
  signal?: AbortSignal;
};

export type AIStreamResult = {
  stream: ReadableStream<Uint8Array>;
  requestId: string;
};

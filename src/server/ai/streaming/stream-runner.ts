import { createSSEStream, encodeSSE, streamResponse } from "./sse";

type StreamRunnerInput = {
  requestId: string;
  chunks: AsyncIterable<string> | string[];
  metadata?: Record<string, unknown>;
};

export async function runAIStream(input: StreamRunnerInput) {
  const stream = createSSEStream(async (controller) => {
    controller.enqueue(
      encodeSSE({
        id: input.requestId,
        type: "metadata",
        metadata: input.metadata ?? {},
        createdAt: new Date().toISOString(),
      })
    );

    for await (const chunk of input.chunks) {
      controller.enqueue(
        encodeSSE({
          id: crypto.randomUUID(),
          type: "token",
          content: chunk,
          createdAt: new Date().toISOString(),
        })
      );
    }

    controller.enqueue(
      encodeSSE({
        id: crypto.randomUUID(),
        type: "done",
        createdAt: new Date().toISOString(),
      })
    );
  });

  return streamResponse(stream);
}

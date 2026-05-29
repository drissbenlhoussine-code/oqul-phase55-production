import type { AIStreamToken } from "./stream-types";

const encoder = new TextEncoder();

export function encodeSSE(event: AIStreamToken) {
  return encoder.encode(`data: ${JSON.stringify(event)}\n\n`);
}

export function createSSEStream(
  producer: (controller: ReadableStreamDefaultController<Uint8Array>) => Promise<void>
) {
  return new ReadableStream<Uint8Array>({
    async start(controller) {
      try {
        await producer(controller);
      } catch (error) {
        controller.enqueue(
          encodeSSE({
            id: crypto.randomUUID(),
            type: "error",
            content: error instanceof Error ? error.message : "Unknown stream error",
            createdAt: new Date().toISOString(),
          })
        );
      } finally {
        controller.close();
      }
    },
  });
}

export function streamResponse(stream: ReadableStream<Uint8Array>) {
  return new Response(stream, {
    headers: {
      "Content-Type": "text/event-stream; charset=utf-8",
      "Cache-Control": "no-cache, no-transform",
      Connection: "keep-alive",
      "X-Accel-Buffering": "no",
    },
  });
}

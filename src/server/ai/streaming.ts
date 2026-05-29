export type AIStreamChunk = {
  text: string;
  done?: boolean;
};

export function createTextStream(chunks: AsyncIterable<AIStreamChunk>) {
  const encoder = new TextEncoder();

  return new ReadableStream({
    async start(controller) {
      for await (const chunk of chunks) {
        controller.enqueue(encoder.encode(chunk.text));
      }

      controller.close();
    },
  });
}

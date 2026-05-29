export type StreamMessage = {
  type: "token" | "done" | "error" | "metadata";
  content?: string;
  metadata?: Record<string, unknown>;
};

export async function readAIStream(
  response: Response,
  onMessage: (message: StreamMessage) => void
) {
  if (!response.body) throw new Error("Streaming response body is empty.");

  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });

    const events = buffer.split("\n\n");
    buffer = events.pop() ?? "";

    for (const event of events) {
      const line = event.split("\n").find((item) => item.startsWith("data: "));
      if (!line) continue;
      onMessage(JSON.parse(line.replace("data: ", "")));
    }
  }
}

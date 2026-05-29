import Groq from "groq-sdk";
import type { AIMessage, AIProvider, GenerateTextInput, GenerateTextResult } from "./base-provider";
import { CircuitBreaker } from "@/server/runtime/circuit-breaker";
import { withRetry } from "@/server/runtime/retry";
import { withTimeout } from "@/server/runtime/timeout";

const groqCircuitBreaker = new CircuitBreaker(5, 30_000);
const MODEL = "llama-3.3-70b-versatile";

function getClient() {
  const key = process.env.GROQ_API_KEY;
  if (!key) throw new Error("GROQ_API_KEY is required");
  return new Groq({ apiKey: key });
}

export class GroqProvider implements AIProvider {
  async generate(messages: AIMessage[]): Promise<string> {
    const groq = getClient();
    const result = await groqCircuitBreaker.execute(() =>
      withRetry(
        () =>
          withTimeout(
            groq.chat.completions.create({
              model: MODEL,
              messages: messages.map((m) => ({ role: m.role, content: m.content })),
              max_tokens: 1024,
              temperature: 0.7,
              stream: false,
            }),
            20_000,
            "Groq timed out"
          ),
        { retries: 2, delayMs: 300 }
      )
    );
    return result.choices[0]?.message?.content ?? "";
  }

  async generateText(input: GenerateTextInput): Promise<GenerateTextResult> {
    const groq = getClient();

    const messages = input.systemPrompt
      ? [
          { role: "system" as const, content: input.systemPrompt },
          { role: "user" as const, content: input.prompt },
        ]
      : [{ role: "user" as const, content: input.prompt }];

    const completion = await groqCircuitBreaker.execute(() =>
      withRetry(
        () =>
          withTimeout(
            groq.chat.completions.create({ model: MODEL, messages, max_tokens: 1024, temperature: 0.7, stream: false }),
            20_000,
            "Groq timed out"
          ),
        { retries: 2, delayMs: 300 }
      )
    );

    const text = completion.choices[0]?.message?.content ?? "";
    const usage = completion.usage;

    return {
      text,
      provider: "groq",
      model: MODEL,
      usage: {
        inputTokens: usage?.prompt_tokens ?? 0,
        outputTokens: usage?.completion_tokens ?? 0,
        totalTokens: usage?.total_tokens ?? 0,
      },
    };
  }

  async *stream(messages: AIMessage[], systemPrompt?: string): AsyncGenerator<string> {
    const groq = getClient();

    const fullMessages = systemPrompt
      ? [{ role: "system" as const, content: systemPrompt }, ...messages.map((m) => ({ role: m.role, content: m.content }))]
      : messages.map((m) => ({ role: m.role, content: m.content }));

    const streamCompletion = await groq.chat.completions.create({
      model: MODEL,
      messages: fullMessages,
      max_tokens: 1024,
      temperature: 0.7,
      stream: true,
    });

    for await (const chunk of streamCompletion) {
      const delta = chunk.choices[0]?.delta?.content ?? "";
      if (delta) yield delta;
    }
  }
}

export interface AIMessage {
  role: "system" | "user" | "assistant";
  content: string;
}

export interface GenerateTextInput {
  prompt: string;
  systemPrompt?: string;
  metadata?: Record<string, unknown>;
}

export interface GenerateTextResult {
  text: string;
  provider: string;
  model: string;
  usage: {
    inputTokens: number;
    outputTokens: number;
    totalTokens: number;
  };
}

export interface AIProvider {
  generate(messages: AIMessage[]): Promise<string>;
  generateText(input: GenerateTextInput): Promise<GenerateTextResult>;
  stream?(messages: AIMessage[], systemPrompt?: string): AsyncGenerator<string>;
}

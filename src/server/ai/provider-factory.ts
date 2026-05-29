import { GroqProvider } from "./providers/groq-provider";

export function getAIProvider() {
  return new GroqProvider();
}

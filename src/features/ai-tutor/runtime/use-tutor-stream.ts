"use client";

import { useCallback, useRef, useState } from "react";
import {
  createChildMessage,
  createStreamingLeilaMessage,
  type TutorMessage,
} from "./message-runtime";
import { readAIStream } from "./stream-client";

export interface UseTutorStreamOptions {
  childId: string;
  lessonId?: string;
}

export function useTutorStream({ childId, lessonId }: UseTutorStreamOptions) {
  const [messages, setMessages] = useState<TutorMessage[]>([]);
  const [isStreaming, setIsStreaming] = useState(false);
  const abortRef = useRef<AbortController | null>(null);

  const stop = useCallback(() => {
    abortRef.current?.abort();
    abortRef.current = null;
    setIsStreaming(false);
  }, []);

  const sendMessage = useCallback(
    async (content: string, extra?: { attemptCount?: number; mood?: "neutral" | "frustrated" | "excited" }) => {
      if (!childId) return;

      const childMessage = createChildMessage(content);
      const leilaMessage = createStreamingLeilaMessage();

      // Build conversation history for context
      setMessages((current) => {
        const updated = [...current, childMessage, leilaMessage];
        return updated;
      });
      setIsStreaming(true);

      const controller = new AbortController();
      abortRef.current = controller;

      // Build message history from current messages (before adding the new pair)
      const history = messages
        .filter((m) => m.status === "done")
        .map((m) => ({
          role: m.role === "child" ? ("user" as const) : ("assistant" as const),
          content: m.content,
        }));

      try {
        const response = await fetch("/api/ai/leila", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            // Multi-turn format: full history + new message
            messages: [...history, { role: "user" as const, content }],
            childId,
            lessonId,
            attemptCount: extra?.attemptCount,
            mood: extra?.mood,
          }),
          signal: controller.signal,
        });

        if (!response.ok) {
          const err = await response.json().catch(() => ({ message: "خطأ في الاتصال" }));
          throw new Error(err.message ?? err.error ?? "خطأ في الاتصال");
        }

        await readAIStream(response, (event) => {
          if (event.type === "token" && event.content) {
            setMessages((current) =>
              current.map((m) =>
                m.id === leilaMessage.id
                  ? { ...m, content: m.content + event.content }
                  : m
              )
            );
          }

          if (event.type === "done") {
            setMessages((current) =>
              current.map((m) =>
                m.id === leilaMessage.id ? { ...m, status: "done" } : m
              )
            );
          }

          if (event.type === "error") {
            setMessages((current) =>
              current.map((m) =>
                m.id === leilaMessage.id
                  ? { ...m, status: "error", content: event.content ?? "حدث خطأ" }
                  : m
              )
            );
          }
        });
      } catch (err) {
        const msg = err instanceof Error ? err.message : "سمح ليا، وقع خطأ. جرب مرة أخرى.";
        setMessages((current) =>
          current.map((m) =>
            m.id === leilaMessage.id
              ? { ...m, status: "error", content: msg }
              : m
          )
        );
      } finally {
        setIsStreaming(false);
        abortRef.current = null;
      }
    },
    [childId, lessonId, messages]
  );

  const reset = useCallback(() => {
    setMessages([]);
    stop();
  }, [stop]);

  return {
    messages,
    isStreaming,
    sendMessage,
    stop,
    reset,
  };
}

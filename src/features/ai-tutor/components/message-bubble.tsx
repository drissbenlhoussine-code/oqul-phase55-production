"use client";
import { Bot, User } from "lucide-react";
import { cn } from "@/lib/cn";

interface MessageBubbleProps {
  role: "child" | "leila" | "user" | "assistant";
  content: string;
  status?: "sending" | "streaming" | "done" | "error";
}

export function MessageBubble({ role, content, status }: MessageBubbleProps) {
  const isLeila = role === "leila" || role === "assistant";
  const isError = status === "error";
  const isEmpty = !content && status === "streaming";

  return (
    <div className={cn("flex items-start gap-3", !isLeila && "flex-row-reverse")}>
      <div className={cn(
        "w-8 h-8 rounded-xl flex items-center justify-center flex-shrink-0",
        isLeila ? "bg-primary text-white" : "bg-secondary"
      )}>
        {isLeila ? <Bot className="w-4 h-4" /> : <User className="w-4 h-4" />}
      </div>

      <div className={cn(
        "max-w-[78%] px-4 py-3 rounded-2xl text-sm leading-relaxed",
        isLeila && !isError
          ? "leila-bubble text-white rounded-tr-sm"
          : isError
          ? "bg-red-50 text-red-700 border border-red-200 rounded-tr-sm"
          : "user-bubble text-foreground rounded-tl-sm"
      )}>
        {isEmpty ? (
          <span className="flex items-center gap-2 opacity-70">
            <span className="dot-pulse" />
          </span>
        ) : (
          <span className="whitespace-pre-wrap">{content}</span>
        )}
      </div>
    </div>
  );
}

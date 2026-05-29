"use client";

import { useRef, useEffect, useState, useCallback } from "react";
import { Send, Sparkles, StopCircle, History, RefreshCcw, Mic, MicOff, Loader2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { MessageBubble } from "./components/message-bubble";
import { useTutorStream } from "./runtime/use-tutor-stream";
import { Spinner } from "@/components/ui/spinner";

interface TutorChatProps {
  childId:          string;
  lessonId?:        string;
  lessonTitle?:     string;
  initialGreeting?: string;
}

// Quick-action suggestions grouped by context

function useVoiceInput(onTranscript: (text: string) => void) {
  const mediaRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);
  const [recording, setRecording] = useState(false);
  const [loading, setLoading] = useState(false);

  async function startRecording() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream, { mimeType: "audio/webm" });
      chunksRef.current = [];
      recorder.ondataavailable = (event) => {
        if (event.data.size > 0) chunksRef.current.push(event.data);
      };
      recorder.onstop = async () => {
        stream.getTracks().forEach((track) => track.stop());
        setLoading(true);
        try {
          const blob = new Blob(chunksRef.current, { type: "audio/webm" });
          const form = new FormData();
          form.append("audio", blob, "voice.webm");
          const response = await fetch("/api/ai/transcribe", { method: "POST", body: form });
          const data = await response.json();
          if (data?.success && data?.text) onTranscript(data.text);
        } catch (error) {
          console.error("[Voice input]", error);
        } finally {
          setLoading(false);
        }
      };
      mediaRef.current = recorder;
      recorder.start();
      setRecording(true);
    } catch (error) {
      console.warn("[Voice input] Microphone not available", error);
    }
  }

  function stopRecording() {
    mediaRef.current?.stop();
    setRecording(false);
  }

  function toggle() {
    if (recording) stopRecording();
    else startRecording();
  }

  return { toggle, recording, loading };
}

const QUICK_ACTIONS = {
  lesson:   ["اشرح لي الدرس بطريقة أبسط", "عطيني مثال من حياتي", "فين غلطت في التمارين؟"],
  general:  ["واش نبدأ درس جديد؟", "ساعدني في الواجب", "عندي سؤال في الرياضيات"],
  stuck:    ["ما فهمت هاد الشيء", "شرح لي خطوة بخطوة", "ممكن مثال أسهل؟"],
};

export function TutorChat({ childId, lessonId, lessonTitle, initialGreeting }: TutorChatProps) {
  const { messages, isStreaming, sendMessage, stop, reset } = useTutorStream({ childId, lessonId });
  const inputRef  = useRef<HTMLInputElement>(null);
  const bottomRef = useRef<HTMLDivElement>(null);
  const [inputVal, setInputVal]         = useState("");
  const [showHistory, setShowHistory]   = useState(false);
  const [sessions, setSessions]         = useState<Array<{ id: string; title: string; updatedAt: string; lesson?: { titleAr: string } }>>([]);
  const [mood, setMood]                 = useState<"neutral" | "frustrated" | "excited">("neutral");
  const [attemptCount, setAttemptCount] = useState(0);
  const voice = useVoiceInput((text) => {
    setInputVal((prev) => prev ? `${prev} ${text}` : text);
    inputRef.current?.focus();
  });

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  // Detect mood from message content
  useEffect(() => {
    const last = messages[messages.length - 1];
    if (!last || last.role !== "child") return;
    const text = last.content.toLowerCase();
    if (text.includes("ما فهمت") || text.includes("صعب") || text.includes("ما قادر")) {
      setMood("frustrated");
      setAttemptCount((count) => count + 1);
    } else if (text.includes("شطارة") || text.includes("مزيان") || text.includes("فهمت")) {
      setMood("excited");
      setAttemptCount(0);
    }
  }, [messages]);

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const val = inputVal.trim();
    if (!val || isStreaming) return;
    setInputVal("");
    sendMessage(val, { attemptCount, mood });
  }

  const loadHistory = useCallback(async () => {
    const res = await fetch(`/api/ai/history?childId=${childId}`).then((r) => r.json());
    if (res.success) setSessions(res.data);
    setShowHistory(true);
  }, [childId]);

  const suggestions = lessonId ? QUICK_ACTIONS.lesson : QUICK_ACTIONS.general;
  const isEmpty     = messages.length === 0;

  const greetings: Record<string, string> = {
    neutral:    "سلام يا بطل! 🌟 أنا ليلى، شنو بغيتي نشرحوه اليوم؟",
    frustrated: "سلام! أنا هنا نساعدك — خو علي الصعوبة ونحلوها سوا 💙",
    excited:    "أهلاً! شايف أنك متحمس 🔥 — هيا نتعلمو أكثر!",
  };

  return (
    <section className="flex flex-col h-full rounded-2xl border bg-card shadow-sm overflow-hidden">
      {/* Header */}
      <div className="flex items-center gap-3 px-5 py-4 border-b border-border bg-gradient-to-l from-emerald-50 to-transparent">
        <div className="w-10 h-10 rounded-xl bg-primary flex items-center justify-center flex-shrink-0 shadow-sm">
          <Sparkles className="w-5 h-5 text-white" />
        </div>
        <div className="flex-1 min-w-0">
          <h2 className="font-bold text-foreground">ليلى</h2>
          <p className="text-xs text-muted-foreground flex items-center gap-1">
            <span className={`w-2 h-2 rounded-full inline-block transition-colors ${isStreaming ? "bg-amber-400 animate-pulse" : "bg-emerald-500"}`} />
            {isStreaming ? "تكتب..." : lessonTitle ? `سياق: ${lessonTitle}` : "مستعدة للمساعدة"}
          </p>
        </div>
        <div className="flex items-center gap-1">
          <button onClick={loadHistory} title="محادثات سابقة"
            className="p-2 rounded-lg hover:bg-secondary transition-colors text-muted-foreground hover:text-foreground">
            <History className="w-4 h-4" />
          </button>
          {messages.length > 0 && (
            <button onClick={() => { reset(); setAttemptCount(0); setMood("neutral"); }} title="محادثة جديدة"
              className="p-2 rounded-lg hover:bg-secondary transition-colors text-muted-foreground hover:text-foreground">
              <RefreshCcw className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>

      {/* History panel */}
      {showHistory && sessions.length > 0 && (
        <div className="border-b border-border bg-secondary/50 px-4 py-3">
          <p className="text-xs font-semibold text-muted-foreground mb-2">محادثات سابقة</p>
          <div className="flex gap-2 overflow-x-auto scrollbar-hide pb-1">
            {sessions.slice(0, 5).map((s) => (
              <button key={s.id} onClick={() => setShowHistory(false)}
                className="flex-shrink-0 bg-white border border-border rounded-lg px-3 py-2 text-xs text-right hover:border-primary transition-colors">
                <p className="font-medium truncate max-w-[120px]">{s.lesson?.titleAr ?? s.title}</p>
                <p className="text-muted-foreground">{new Date(s.updatedAt).toLocaleDateString("ar-MA")}</p>
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Messages */}
      <div className="flex-1 overflow-y-auto px-4 py-4 space-y-3 scrollbar-hide">
        {/* Welcome */}
        <div className="flex items-start gap-3">
          <div className="w-8 h-8 rounded-xl bg-primary flex items-center justify-center flex-shrink-0">
            <Sparkles className="w-4 h-4 text-white" />
          </div>
          <div className="leila-bubble text-white px-4 py-3 rounded-2xl rounded-tr-sm max-w-[78%] text-sm leading-relaxed">
            {initialGreeting ?? greetings[mood]}
          </div>
        </div>
        {messages.map((msg) => (
          <MessageBubble key={msg.id} role={msg.role} content={msg.content} status={msg.status} />
        ))}
        <div ref={bottomRef} />
      </div>

      {/* Quick suggestions */}
      {isEmpty && (
        <div className="px-4 pb-3 flex flex-wrap gap-2">
          {suggestions.map((s) => (
            <button key={s} onClick={() => { setInputVal(s); inputRef.current?.focus(); }}
              className="px-3 py-1.5 rounded-full border border-border text-xs hover:border-primary hover:text-primary hover:bg-primary/5 transition-all bg-card">
              {s}
            </button>
          ))}
        </div>
      )}

      {/* Input */}
      <form onSubmit={handleSubmit} className="flex gap-2 px-4 py-3 border-t border-border">
        <input
          ref={inputRef}
          value={inputVal}
          onChange={(e) => setInputVal(e.target.value)}
          placeholder="اسأل ليلى أي سؤال..."
          disabled={isStreaming}
          className="flex-1 rounded-xl border border-border bg-background px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-primary disabled:opacity-60 transition-shadow"
        />
        {!isStreaming && (
          <Button
            type="button"
            onClick={voice.toggle}
            variant="outline"
            size="icon"
            className="flex-shrink-0"
            title={voice.recording ? "إيقاف التسجيل" : "إملاء صوتي"}
            disabled={voice.loading}
          >
            {voice.loading ? <Loader2 className="w-4 h-4 animate-spin" /> : voice.recording ? <MicOff className="w-4 h-4 text-destructive" /> : <Mic className="w-4 h-4" />}
          </Button>
        )}
        {isStreaming ? (
          <Button type="button" onClick={stop} variant="outline" size="icon" className="flex-shrink-0">
            <StopCircle className="w-4 h-4 text-destructive" />
          </Button>
        ) : (
          <Button type="submit" size="icon" className="flex-shrink-0" disabled={!inputVal.trim()}>
            <Send className="w-4 h-4" />
          </Button>
        )}
      </form>
    </section>
  );
}

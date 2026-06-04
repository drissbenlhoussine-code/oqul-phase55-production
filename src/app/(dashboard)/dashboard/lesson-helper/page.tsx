"use client";
import { useState } from "react";
import { BookOpen, Send, RotateCcw, Copy, CheckCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/cn";

const STUDY_PROMPTS = [
  "اشرح قاعدة الكسور في الرياضيات مع أمثلة مغربية",
  "اشرح تركيب الجملة الفعلية في اللغة العربية",
  "كيف أحل معادلة من الدرجة الأولى؟",
  "لخص لي درس الكهرباء للثانوي مع تمارين",
  "ما هو مفهوم التفاضل والتكامل وكيف أطبقه؟",
];

export default function LessonHelperPage() {
  const [query,   setQuery]   = useState("");
  const [output,  setOutput]  = useState("");
  const [running, setRunning] = useState(false);
  const [copied,  setCopied]  = useState(false);

  async function generate() {
    if (!query.trim() || running) return;
    setOutput("");
    setRunning(true);
    try {
      const res = await fetch("/api/ai/pipeline", {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify({ input: query.trim(), flow: "lesson", model: "llama-3.3-70b-versatile" }),
      });
      if (!res.ok || !res.body) { setRunning(false); return; }

      const reader  = res.body.getReader();
      const decoder = new TextDecoder();
      let   buf     = "";
      let   live    = "";

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buf += decoder.decode(value, { stream: true });
        const lines = buf.split("\n");
        buf = lines.pop() ?? "";
        for (const line of lines) {
          if (!line.startsWith("data: ")) continue;
          try {
            const ev = JSON.parse(line.slice(6)) as Record<string, unknown>;
            const agentId = (ev.agent_id ?? ev.agentId) as string;
            if (ev.event === "agent_delta" && agentId === "writer") {
              live += ev.delta as string;
              setOutput(live);
            } else if (ev.event === "end") {
              setOutput((ev.final_output ?? ev.finalOutput ?? live) as string);
            }
          } catch { /* ignore */ }
        }
      }
    } catch { /* network error — silent */ }
    setRunning(false);
  }

  async function copy() {
    await navigator.clipboard.writeText(output);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  }

  const hasOutput = Boolean(output);

  return (
    <div className="mx-auto max-w-3xl space-y-6" dir="rtl">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-black flex items-center gap-3">
          <span className="w-10 h-10 rounded-2xl bg-gradient-to-br from-emerald-500 to-primary flex items-center justify-center text-white text-lg">
            📖
          </span>
          مولد الدروس الذكي
        </h1>
        <p className="mt-1 text-sm text-muted-foreground">
          اكتب موضوعاً أو سؤالاً دراسياً — ستحصل على شرح كامل مع أمثلة وتمارين من منظور المنهج المغربي
        </p>
      </div>

      {/* Quick prompts */}
      <div className="flex flex-wrap gap-2">
        {STUDY_PROMPTS.map((p) => (
          <button
            key={p}
            onClick={() => setQuery(p)}
            className="rounded-full border border-border px-3 py-1.5 text-xs text-muted-foreground hover:border-primary hover:text-primary transition-colors"
          >
            {p.length > 42 ? `${p.slice(0, 42)}…` : p}
          </button>
        ))}
      </div>

      {/* Input */}
      <div className="flex gap-3">
        <div className="relative flex-1">
          <BookOpen className="absolute right-4 top-3 h-4 w-4 text-muted-foreground" />
          <textarea
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); void generate(); } }}
            placeholder="ما الموضوع الذي تريد فهمه؟"
            rows={3}
            disabled={running}
            className="w-full resize-none rounded-2xl border border-border bg-background py-3 pl-4 pr-11 text-sm transition-shadow focus:outline-none focus:ring-2 focus:ring-primary disabled:opacity-60"
          />
        </div>
        <div className="flex flex-col gap-2">
          <Button
            onClick={() => void generate()}
            disabled={!query.trim() && !running}
            variant={running ? "outline" : "default"}
            className="h-auto rounded-2xl px-5 py-3"
          >
            {running ? (
              <span className="flex items-center gap-2">
                <span className="h-2 w-2 animate-ping rounded-full bg-primary" />
                يكتب...
              </span>
            ) : (
              <span className="flex items-center gap-2">
                <Send className="h-4 w-4" />
                اشرح
              </span>
            )}
          </Button>
          {hasOutput && (
            <Button
              onClick={() => { setOutput(""); setQuery(""); }}
              variant="ghost"
              size="sm"
              className="rounded-xl"
            >
              <RotateCcw className="h-4 w-4" />
            </Button>
          )}
        </div>
      </div>

      {/* Output */}
      {(hasOutput || running) && (
        <div className="overflow-hidden rounded-2xl border border-primary/20 bg-primary/5">
          <div className="flex items-center justify-between border-b border-primary/10 px-5 py-3">
            <div className="flex items-center gap-2">
              <CheckCircle className="h-4 w-4 text-primary" />
              <span className="text-sm font-semibold text-primary">الشرح</span>
            </div>
            {hasOutput && (
              <button
                onClick={() => void copy()}
                className="flex items-center gap-1.5 text-xs text-muted-foreground transition-colors hover:text-foreground"
              >
                <Copy className="h-3.5 w-3.5" />
                {copied ? "تم النسخ ✓" : "نسخ"}
              </button>
            )}
          </div>
          <div
            className={cn(
              "min-h-32 max-h-[500px] overflow-y-auto px-5 py-4 text-sm leading-8 whitespace-pre-wrap",
              !output && "text-muted-foreground"
            )}
          >
            {output || "يُعدّ الشرح…"}
          </div>
        </div>
      )}

      {/* Empty state */}
      {!hasOutput && !running && (
        <div className="py-12 text-center text-muted-foreground">
          <div className="mb-4 text-5xl">📖</div>
          <p className="font-semibold">مولد الدروس الذكي</p>
          <p className="mx-auto mt-2 max-w-sm text-sm leading-7">
            اكتب موضوعاً من المنهج — ستحصل على شرح مفصل مع أمثلة مغربية وتمارين وخلاصة.
            لا يُحفظ شيء في قاعدة البيانات.
          </p>
        </div>
      )}
    </div>
  );
}

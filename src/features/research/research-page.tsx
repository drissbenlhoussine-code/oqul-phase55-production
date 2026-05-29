"use client";
/**
 * ResearchPage — Phase 36 Merge
 * Path: src/features/research/research-page.tsx
 *
 * Beautiful UI for the multi-agent research pipeline.
 * Shows each agent's progress live as SSE events stream in.
 */
import { useState, useRef, useCallback } from "react";
import { Search, Sparkles, Copy, RotateCcw, ChevronDown, ChevronUp, CheckCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn }     from "@/lib/cn";

// ── Types ──────────────────────────────────────────────────────────────────────

type FlowId = "research" | "full" | "analysis" | "quick" | "lesson";
type AgentStatus = "waiting" | "running" | "done";

interface AgentState {
  id:      string;
  label:   string;
  status:  AgentStatus;
  output:  string;
  durationMs?: number;
}

interface Flow {
  id:    FlowId;
  label: string;
  desc:  string;
  agents: string[];
}

// ── Config ─────────────────────────────────────────────────────────────────────

const FLOWS: Flow[] = [
  { id: "research",  label: "بحث",        desc: "بحث عميق في الموضوع",         agents: ["orchestrator", "researcher", "writer"] },
  { id: "full",      label: "متكامل",     desc: "بحث + تحليل + كتابة",        agents: ["orchestrator", "researcher", "analyst", "writer"] },
  { id: "analysis",  label: "تحليل",      desc: "تحليل نقدي ومقارنة",         agents: ["orchestrator", "analyst", "writer"] },
  { id: "lesson",    label: "تعليمي",     desc: "من منظور المنهج المغربي",     agents: ["orchestrator", "pedagogue", "writer"] },
  { id: "quick",     label: "سريع",       desc: "إجابة مباشرة وسريعة",        agents: ["orchestrator", "writer"] },
];

const AGENT_LABELS: Record<string, string> = {
  orchestrator:      "🎯 المنسق",
  researcher:        "🔍 الباحث",
  analyst:           "📊 المحلل",
  pedagogue: "📚 خبير المنهج",
  writer:            "✍️ الكاتب",
};

const AGENT_COLORS: Record<AgentStatus, string> = {
  waiting: "border-border text-muted-foreground bg-muted/30",
  running: "border-primary text-primary bg-primary/5 animate-pulse",
  done:    "border-emerald-500 text-emerald-700 bg-emerald-50",
};

// ── Sub-components ─────────────────────────────────────────────────────────────

function AgentCard({ agent, expanded, onToggle }: {
  agent:    AgentState;
  expanded: boolean;
  onToggle: () => void;
}) {
  return (
    <div className={cn(
      "rounded-2xl border transition-all duration-300",
      AGENT_COLORS[agent.status]
    )}>
      <button
        onClick={onToggle}
        className="w-full flex items-center justify-between px-4 py-3 text-right"
      >
        <div className="flex items-center gap-3">
          <span className="text-sm font-semibold">{AGENT_LABELS[agent.id] ?? agent.id}</span>
          {agent.status === "running" && (
            <span className="w-2 h-2 rounded-full bg-primary animate-ping" />
          )}
          {agent.status === "done" && agent.durationMs && (
            <span className="text-xs opacity-60">{(agent.durationMs / 1000).toFixed(1)}s</span>
          )}
        </div>
        {agent.output && (agent.status === "done"
          ? expanded ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />
          : null
        )}
      </button>

      {/* Streaming output */}
      {(agent.status === "running" || (expanded && agent.status === "done")) && agent.output && (
        <div className="px-4 pb-4">
          <div className="text-sm leading-7 whitespace-pre-wrap opacity-80 max-h-60 overflow-y-auto scrollbar-hide">
            {agent.output}
            {agent.status === "running" && <span className="animate-pulse">▊</span>}
          </div>
        </div>
      )}
    </div>
  );
}

function FinalAnswer({ text }: { text: string }) {
  const [copied, setCopied] = useState(false);

  async function copy() {
    await navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  }

  return (
    <div className="rounded-2xl border border-primary/20 bg-primary/5 overflow-hidden">
      <div className="flex items-center justify-between px-5 py-3 border-b border-primary/10">
        <div className="flex items-center gap-2">
          <CheckCircle className="w-4 h-4 text-primary" />
          <span className="text-sm font-semibold text-primary">النتيجة النهائية</span>
        </div>
        <button onClick={copy}
          className="flex items-center gap-1.5 text-xs text-muted-foreground hover:text-foreground transition-colors">
          <Copy className="w-3.5 h-3.5" />
          {copied ? "تم النسخ ✓" : "نسخ"}
        </button>
      </div>
      <div className="px-5 py-4 text-sm leading-8 whitespace-pre-wrap max-h-[500px] overflow-y-auto scrollbar-hide">
        {text}
      </div>
    </div>
  );
}

// ── Main component ─────────────────────────────────────────────────────────────

export function ResearchPage() {
  const [query,      setQuery]      = useState("");
  const [flow,       setFlow]       = useState<FlowId>("research");
  const [agents,     setAgents]     = useState<AgentState[]>([]);
  const [finalOutput, setFinalOutput] = useState("");
  const [running,    setRunning]    = useState(false);
  const [expanded,   setExpanded]   = useState<Record<string, boolean>>({});
  const [totalMs,    setTotalMs]    = useState<number | null>(null);
  const abortRef = useRef<AbortController | null>(null);

  const run = useCallback(async () => {
    if (!query.trim() || running) return;

    // Reset
    const selectedFlow = FLOWS.find((f) => f.id === flow)!;
    const initialAgents: AgentState[] = selectedFlow.agents.map((id) => ({
      id, label: AGENT_LABELS[id] ?? id, status: "waiting", output: "",
    }));
    setAgents(initialAgents);
    setFinalOutput("");
    setTotalMs(null);
    setExpanded({});
    setRunning(true);

    abortRef.current = new AbortController();

    try {
      const res = await fetch("/api/ai/pipeline", {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify({ input: query.trim(), flow, model: "llama-3.3-70b-versatile" }),
        signal:  abortRef.current.signal,
      });

      if (!res.ok) {
        const err = await res.json();
        console.error("[Research]", err.message);
        setRunning(false);
        return;
      }

      const reader  = res.body!.getReader();
      const decoder = new TextDecoder();
      let   buf     = "";

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buf += decoder.decode(value, { stream: true });
        const lines = buf.split("\n");
        buf = lines.pop() ?? "";

        for (const line of lines) {
          if (!line.startsWith("data: ")) continue;
          try {
            const event = JSON.parse(line.slice(6)) as Record<string, unknown>;
            const e = event.event as string;

            if (e === "agent_start") {
              const id = (event.agent_id ?? event.agentId) as string;
              setAgents((prev) => prev.map((a) =>
                a.id === id ? { ...a, status: "running" } : a
              ));
            } else if (e === "agent_delta") {
              const id    = event.agent_id as string;
              const delta = event.delta as string;
              setAgents((prev) => prev.map((a) =>
                a.id === id ? { ...a, output: a.output + delta } : a
              ));
            } else if (e === "agent_done") {
              const id  = event.agent_id as string;
              const dur = (event.duration_ms ?? event.durationMs) as number;
              setAgents((prev) => prev.map((a) =>
                a.id === id ? { ...a, status: "done", durationMs: dur } : a
              ));
            } else if (e === "end") {
              setFinalOutput(((event.final_output ?? event.finalOutput) as string) ?? "");
              setTotalMs(((event.total_ms ?? event.totalMs) as number) ?? null);
            }
          } catch { /* ignore malformed events */ }
        }
      }
    } catch (err) {
      if ((err as Error).name !== "AbortError") console.error("[Research]", err);
    } finally {
      setRunning(false);
    }
  }, [query, flow, running]);

  function handleStop() {
    abortRef.current?.abort();
    setRunning(false);
  }

  function handleReset() {
    handleStop();
    setAgents([]);
    setFinalOutput("");
    setQuery("");
    setTotalMs(null);
  }

  const hasResults = agents.length > 0;

  return (
    <div className="max-w-3xl mx-auto space-y-6 animate-fade-in" dir="rtl">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-black flex items-center gap-3">
          <span className="w-10 h-10 rounded-2xl bg-gradient-to-br from-violet-500 to-primary flex items-center justify-center text-white text-lg">🔬</span>
          البحث الذكي
        </h1>
        <p className="text-sm text-muted-foreground mt-1">
          نظام متعدد الوكلاء — كل وكيل متخصص يعمل بالتسلسل لإنتاج إجابة شاملة ودقيقة
        </p>
      </div>

      {/* Flow selector */}
      <div className="flex gap-2 flex-wrap">
        {FLOWS.map((f) => (
          <button
            key={f.id}
            onClick={() => setFlow(f.id)}
            className={cn(
              "px-4 py-2 rounded-xl text-sm font-medium transition-all border",
              flow === f.id
                ? "bg-primary text-white border-primary shadow-sm"
                : "border-border hover:border-primary hover:text-primary bg-card"
            )}
          >
            {f.label}
            <span className="mr-2 text-xs opacity-60">{f.desc}</span>
          </button>
        ))}
      </div>

      {/* Query input */}
      <div className="flex gap-3">
        <div className="flex-1 relative">
          <Search className="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
          <textarea
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); run(); } }}
            placeholder="اكتب سؤالك أو موضوعك للبحث..."
            rows={2}
            disabled={running}
            className="w-full rounded-2xl border border-border bg-background pr-11 pl-4 py-3 text-sm resize-none focus:outline-none focus:ring-2 focus:ring-primary disabled:opacity-60 transition-shadow"
          />
        </div>
        <div className="flex flex-col gap-2">
          <Button
            onClick={running ? handleStop : run}
            disabled={!query.trim() && !running}
            variant={running ? "outline" : "default"}
            className="rounded-2xl h-auto py-3 px-5"
          >
            {running ? "إيقاف" : "ابحث"}
          </Button>
          {hasResults && (
            <Button onClick={handleReset} variant="ghost" size="sm" className="rounded-xl">
              <RotateCcw className="w-4 h-4" />
            </Button>
          )}
        </div>
      </div>

      {/* Agents progress */}
      {hasResults && (
        <div className="space-y-3">
          <div className="flex items-center justify-between">
            <p className="text-sm font-semibold">تقدم الوكلاء</p>
            {totalMs && (
              <span className="text-xs text-muted-foreground">
                اكتمل في {(totalMs / 1000).toFixed(1)} ثانية
              </span>
            )}
          </div>
          {agents.map((a) => (
            <AgentCard
              key={a.id}
              agent={a}
              expanded={!!expanded[a.id]}
              onToggle={() => setExpanded((prev) => ({ ...prev, [a.id]: !prev[a.id] }))}
            />
          ))}
        </div>
      )}

      {/* Final answer */}
      {finalOutput && <FinalAnswer text={finalOutput} />}

      {/* Empty state */}
      {!hasResults && (
        <div className="text-center py-16 text-muted-foreground">
          <div className="text-5xl mb-4">🔬</div>
          <p className="font-semibold mb-2">اكتشف المعرفة مع نظام الوكلاء</p>
          <p className="text-sm max-w-sm mx-auto leading-7">
            اطرح أي سؤال أكاديمي أو تعليمي — سيعمل فريق من الوكلاء الذكيين بالتسلسل لإنتاج إجابة شاملة ودقيقة.
          </p>
          <div className="mt-6 flex flex-wrap gap-2 justify-center">
            {["ما هي الكسور الاعتيادية؟", "اشرح تركيب الجملة الفعلية", "ما هو دور النيل في الحضارة المصرية؟"].map((s) => (
              <button key={s} onClick={() => setQuery(s)}
                className="px-4 py-2 rounded-full border border-border text-sm hover:border-primary hover:text-primary transition-colors">
                {s}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

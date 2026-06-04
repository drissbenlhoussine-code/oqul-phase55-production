"use client";
import { useState, useRef, useCallback } from "react";
import { Search, Copy, RotateCcw, ChevronDown, ChevronUp, CheckCircle, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn }     from "@/lib/cn";

// ── Types ──────────────────────────────────────────────────────────────────────

type FlowId     = "edu" | "research" | "full" | "analysis" | "quick" | "lesson";
type AgentStatus = "waiting" | "running" | "done";

interface AgentState {
  id:          string;
  nameAr:      string;
  roleAr:      string;
  status:      AgentStatus;
  output:      string;
  durationMs?: number;
}

// ── Agent display config — matches backend config.ts ──────────────────────────

const AGENT_META: Record<string, { nameAr: string; roleAr: string; color: string }> = {
  orchestrator: { nameAr: "منظم الخطة",    roleAr: "يفهم الطلب ويضع خطة العمل",                      color: "indigo"  },
  researcher:   { nameAr: "الباحث",         roleAr: "يجمع المعطيات ويبني الأساس المعرفي",              color: "blue"    },
  analyst:      { nameAr: "المحلل",          roleAr: "يستخرج الأنماط والأسباب والحلول",                 color: "violet"  },
  pedagogue:    { nameAr: "الشارح",          roleAr: "يبسّط الشرح لمستوى الطالب المغربي",               color: "pink"    },
  checker:      { nameAr: "المدقق",          roleAr: "يتحقق من دقة المعلومات وجودتها",                  color: "amber"   },
  exercise_gen: { nameAr: "مولد التمارين",   roleAr: "ينتج التمارين وخطة المراجعة",                    color: "cyan"    },
  writer:       { nameAr: "الكاتب النهائي",  roleAr: "ينتج جوابًا منظمًا وعمليًا",                     color: "emerald" },
};

// ── Flow selector ──────────────────────────────────────────────────────────────

interface FlowOption {
  id:     FlowId;
  label:  string;
  desc:   string;
  agents: string[];
}

const FLOWS: FlowOption[] = [
  {
    id:     "edu",
    label:  "بحث تعليمي",
    desc:   "ملخص + شرح + تمارين + خطة مراجعة",
    agents: ["orchestrator", "researcher", "analyst", "pedagogue", "checker", "exercise_gen"],
  },
  {
    id:     "research",
    label:  "بحث وملخص",
    desc:   "بحث عميق ثم تلخيص منظم",
    agents: ["orchestrator", "researcher", "writer"],
  },
  {
    id:     "analysis",
    label:  "تحليل",
    desc:   "تحليل نقدي ومقارنة",
    agents: ["orchestrator", "analyst", "writer"],
  },
  {
    id:     "quick",
    label:  "سريع",
    desc:   "إجابة مباشرة وسريعة",
    agents: ["orchestrator", "writer"],
  },
];

// ── Color map for status rings ─────────────────────────────────────────────────

const STATUS_RING: Record<AgentStatus, string> = {
  waiting: "border-border bg-muted/20 text-muted-foreground",
  running: "border-primary bg-primary/5 text-primary",
  done:    "border-emerald-400 bg-emerald-50 text-emerald-800",
};

// ── Status label ───────────────────────────────────────────────────────────────

const STATUS_LABEL: Record<AgentStatus, string> = {
  waiting: "ينتظر",
  running: "يعمل",
  done:    "اكتمل",
};

// ── Agent card ─────────────────────────────────────────────────────────────────

function AgentCard({
  agent, expanded, onToggle,
}: {
  agent:    AgentState;
  expanded: boolean;
  onToggle: () => void;
}) {
  return (
    <div className={cn(
      "rounded-2xl border transition-all duration-300",
      STATUS_RING[agent.status]
    )}>
      <button
        onClick={onToggle}
        disabled={!agent.output}
        className="w-full flex items-center justify-between px-4 py-3 text-right disabled:cursor-default"
        type="button"
      >
        <div className="flex items-center gap-3 min-w-0">
          <span className="text-sm font-semibold truncate">{agent.nameAr}</span>
          <span className={cn(
            "shrink-0 text-[10px] px-2 py-0.5 rounded-full font-medium",
            agent.status === "waiting" && "bg-muted text-muted-foreground",
            agent.status === "running" && "bg-primary/15 text-primary animate-pulse",
            agent.status === "done"    && "bg-emerald-100 text-emerald-700",
          )}>
            {STATUS_LABEL[agent.status]}
          </span>
          {agent.status === "running" && (
            <span className="w-2 h-2 shrink-0 rounded-full bg-primary animate-ping" />
          )}
          {agent.status === "done" && agent.durationMs && (
            <span className="text-xs opacity-50 shrink-0">{(agent.durationMs / 1000).toFixed(1)}s</span>
          )}
        </div>
        {agent.output && (
          expanded
            ? <ChevronUp className="w-4 h-4 shrink-0" />
            : <ChevronDown className="w-4 h-4 shrink-0" />
        )}
      </button>

      {/* Role description — always visible when waiting */}
      {agent.status === "waiting" && (
        <p className="px-4 pb-3 text-xs text-muted-foreground leading-5">{agent.roleAr}</p>
      )}

      {/* Streaming output */}
      {agent.status === "running" && agent.output && (
        <div className="px-4 pb-4">
          <div className="text-sm leading-7 whitespace-pre-wrap opacity-80 max-h-48 overflow-y-auto">
            {agent.output}
            <span className="animate-pulse">▊</span>
          </div>
        </div>
      )}

      {/* Collapsed preview when done */}
      {agent.status === "done" && !expanded && agent.output && (
        <p className="px-4 pb-3 text-xs text-muted-foreground truncate">{agent.output.slice(0, 120)}…</p>
      )}

      {/* Full output when expanded */}
      {agent.status === "done" && expanded && agent.output && (
        <div className="px-4 pb-4">
          <div className="text-sm leading-7 whitespace-pre-wrap max-h-72 overflow-y-auto">
            {agent.output}
          </div>
        </div>
      )}
    </div>
  );
}

// ── Final output ───────────────────────────────────────────────────────────────

function FinalOutput({ text }: { text: string }) {
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
          <span className="text-sm font-semibold text-primary">نتيجة الفريق</span>
        </div>
        <button
          onClick={() => void copy()}
          className="flex items-center gap-1.5 text-xs text-muted-foreground hover:text-foreground transition-colors"
          type="button"
        >
          <Copy className="w-3.5 h-3.5" />
          {copied ? "تم النسخ ✓" : "نسخ"}
        </button>
      </div>
      <div className="px-5 py-4 text-sm leading-8 whitespace-pre-wrap max-h-[600px] overflow-y-auto">
        {text}
      </div>
    </div>
  );
}

// ── Main component ─────────────────────────────────────────────────────────────

export function ResearchPage() {
  const [query,      setQuery]       = useState("");
  const [flow,       setFlow]        = useState<FlowId>("edu");
  const [agents,     setAgents]      = useState<AgentState[]>(() => buildAgentPreview("edu"));
  const [finalOutput, setFinalOutput] = useState("");
  const [running,    setRunning]     = useState(false);
  const [error,      setError]       = useState("");
  const [expanded,   setExpanded]    = useState<Record<string, boolean>>({});
  const [totalMs,    setTotalMs]     = useState<number | null>(null);
  const abortRef = useRef<AbortController | null>(null);

  // Build a "waiting" preview for the selected flow's agents
  function buildAgentPreview(flowId: FlowId): AgentState[] {
    const agentIds = FLOWS.find((f) => f.id === flowId)?.agents ?? ["orchestrator", "writer"];
    return agentIds.map((id) => ({
      id,
      nameAr: AGENT_META[id]?.nameAr ?? id,
      roleAr: AGENT_META[id]?.roleAr ?? "",
      status: "waiting",
      output: "",
    }));
  }

  function selectFlow(f: FlowId) {
    if (running) return;
    setFlow(f);
    setAgents(buildAgentPreview(f));
    setFinalOutput("");
    setError("");
    setTotalMs(null);
    setExpanded({});
  }

  const run = useCallback(async () => {
    if (!query.trim() || running) return;

    // Reset to waiting state for the selected flow
    setAgents(buildAgentPreview(flow));
    setFinalOutput("");
    setError("");
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
        const err = await res.json().catch(() => ({})) as { message?: string };
        setError(err.message ?? "حدث خطأ غير متوقع. تحقق من الاتصال وحاول مرة أخرى.");
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
            const ev = JSON.parse(line.slice(6)) as Record<string, unknown>;
            const e  = ev.event as string;
            const id = (ev.agentId ?? ev.agent_id) as string;

            if (e === "agent_start") {
              setAgents((prev) => prev.map((a) =>
                a.id === id ? { ...a, status: "running" } : a
              ));
            } else if (e === "agent_delta") {
              const delta = ev.delta as string;
              setAgents((prev) => prev.map((a) =>
                a.id === id ? { ...a, output: a.output + delta } : a
              ));
            } else if (e === "agent_done") {
              const dur = (ev.durationMs ?? ev.duration_ms) as number;
              setAgents((prev) => prev.map((a) =>
                a.id === id ? { ...a, status: "done", durationMs: dur } : a
              ));
            } else if (e === "end") {
              setFinalOutput(((ev.finalOutput ?? ev.final_output) as string) ?? "");
              setTotalMs((ev.totalMs ?? ev.total_ms) as number ?? null);
            } else if (e === "error") {
              setError((ev.message as string) ?? "حدث خطأ أثناء تشغيل الوكلاء.");
            }
          } catch { /* ignore malformed events */ }
        }
      }
    } catch (err) {
      if ((err as Error).name !== "AbortError") {
        setError("تعذّر الاتصال بالخادم. تحقق من الاتصال بالإنترنت وأعد المحاولة.");
      }
    } finally {
      setRunning(false);
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [query, flow, running]);

  function handleStop() {
    abortRef.current?.abort();
    setRunning(false);
  }

  function handleReset() {
    handleStop();
    setAgents(buildAgentPreview(flow));
    setFinalOutput("");
    setError("");
    setQuery("");
    setTotalMs(null);
    setExpanded({});
  }

  const hasRun = agents.some((a) => a.status !== "waiting");

  return (
    <div className="max-w-3xl mx-auto space-y-6" dir="rtl">

      {/* ── Header ── */}
      <div>
        <h1 className="text-2xl font-black flex items-center gap-3">
          <span className="w-10 h-10 rounded-2xl bg-gradient-to-br from-violet-500 to-primary flex items-center justify-center text-white text-lg">
            🔬
          </span>
          البحث الذكي متعدد الوكلاء
        </h1>
        <p className="text-sm text-muted-foreground mt-1">
          للبحث والتحليل والمقارنة وحل المشكلات — فريق متكامل من الوكلاء يعملون بالتسلسل
        </p>
      </div>

      {/* ── Flow selector ── */}
      <div className="flex gap-2 flex-wrap">
        {FLOWS.map((f) => (
          <button
            key={f.id}
            onClick={() => selectFlow(f.id)}
            disabled={running}
            type="button"
            className={cn(
              "px-4 py-2 rounded-xl text-sm font-medium transition-all border",
              flow === f.id
                ? "bg-primary text-white border-primary shadow-sm"
                : "border-border hover:border-primary hover:text-primary bg-card disabled:opacity-50"
            )}
          >
            {f.label}
            <span className="mr-2 text-xs opacity-60">{f.desc}</span>
          </button>
        ))}
      </div>

      {/* ── Agent cards — always visible ── */}
      <div className="space-y-2">
        <div className="flex items-center justify-between">
          <p className="text-xs font-semibold uppercase tracking-widest text-muted-foreground/60">
            الوكلاء
          </p>
          {hasRun && totalMs && (
            <span className="text-xs text-muted-foreground">
              اكتمل في {(totalMs / 1000).toFixed(1)} ث
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

      {/* ── Query input ── */}
      <div className="flex gap-3">
        <div className="flex-1 relative">
          <Search className="absolute right-4 top-3 w-4 h-4 text-muted-foreground" />
          <textarea
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); void run(); } }}
            placeholder="اكتب سؤالك أو موضوعك الدراسي..."
            rows={2}
            disabled={running}
            className="w-full rounded-2xl border border-border bg-background pr-11 pl-4 py-3 text-sm resize-none focus:outline-none focus:ring-2 focus:ring-primary disabled:opacity-60 transition-shadow"
          />
        </div>
        <div className="flex flex-col gap-2">
          <Button
            onClick={running ? handleStop : () => void run()}
            disabled={!running && !query.trim()}
            variant={running ? "outline" : "default"}
            className="rounded-2xl h-auto py-3 px-5"
          >
            {running
              ? <span className="flex items-center gap-2"><span className="h-2 w-2 rounded-full bg-primary animate-ping" />إيقاف</span>
              : "ابحث"
            }
          </Button>
          {hasRun && (
            <Button onClick={handleReset} variant="ghost" size="sm" className="rounded-xl">
              <RotateCcw className="w-4 h-4" />
            </Button>
          )}
        </div>
      </div>

      {/* ── Error state ── */}
      {error && (
        <div className="flex items-start gap-3 rounded-2xl border border-red-200 bg-red-50 px-4 py-3">
          <AlertCircle className="w-4 h-4 text-red-500 mt-0.5 shrink-0" />
          <p className="text-sm text-red-700 leading-6">{error}</p>
        </div>
      )}

      {/* ── Final output ── */}
      {finalOutput && <FinalOutput text={finalOutput} />}

      {/* ── Empty state ── */}
      {!hasRun && !error && (
        <div className="text-center py-10 text-muted-foreground">
          <p className="text-sm">اكتب سؤالاً بحثياً أو مشكلة دراسية أو طلب مقارنة — سيعمل الفريق أعلاه بالتسلسل وتتابع كل وكيل مباشرةً.</p>
          <div className="mt-4 flex flex-wrap gap-2 justify-center">
            {[
              "قارن بين الفيزياء الكلاسيكية والكميّة",
              "ما أسباب ضعفي في الرياضيات وكيف أحسّن؟",
              "ساعدني على التحضير لامتحان العلوم",
            ].map((s) => (
              <button
                key={s}
                onClick={() => setQuery(s)}
                type="button"
                className="px-3 py-1.5 rounded-full border border-border text-xs hover:border-primary hover:text-primary transition-colors"
              >
                {s}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

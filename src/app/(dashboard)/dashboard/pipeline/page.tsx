"use client";

import { useMemo, useState } from "react";
import { Send, Download, RotateCcw, Sparkles, Brain, CheckCircle2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { PIPELINE_FLOWS, AGENTS, PIPELINE_MODELS, type AgentId, type PipelineFlowId } from "@/server/ai/pipeline/config";

type AgentOutput = { agentId: AgentId; output: string; durationMs?: number };
type RunState = {
  status: "idle" | "running" | "done" | "error";
  currentAgent: AgentId | null;
  outputs: AgentOutput[];
  deltas: Partial<Record<AgentId, string>>;
  finalOutput: string;
  error?: string;
};

const starterPrompts = [
  "حوّل درس الجملة الاسمية للسنة الرابعة ابتدائي إلى شرح تفاعلي مع تمارين",
  "حلل نقاط ضعف طفل في الرياضيات واقترح خطة أسبوعية للأهل",
  "صمّم درسًا مغربيًا عن الكسور مع مثال من السوق وتمارين متدرجة",
  "اكتب خطة محتوى لشهر كامل في اللغة العربية للسنة الثالثة ابتدائي",
];

function AgentCard({ agentId, active, done, text, durationMs }: {
  agentId: AgentId;
  active: boolean;
  done: boolean;
  text: string;
  durationMs?: number;
}) {
  const agent = AGENTS[agentId];
  return (
    <div className={`rounded-2xl border p-4 transition-all ${active ? "border-primary bg-primary/5 shadow-sm" : done ? "border-emerald-200 bg-emerald-50/60" : "border-border bg-card"}`}>
      <div className="flex items-center gap-3">
        <div className="flex h-10 w-10 items-center justify-center rounded-xl text-lg" style={{ backgroundColor: `${agent.color}18`, color: agent.color }}>
          {done ? <CheckCircle2 className="h-5 w-5" /> : agent.icon}
        </div>
        <div className="min-w-0 flex-1">
          <div className="font-bold text-foreground">{agent.nameAr}</div>
          <div className="text-xs text-muted-foreground">{agent.roleAr}</div>
        </div>
        {durationMs ? <span className="text-xs text-muted-foreground">{Math.round(durationMs / 1000)}s</span> : null}
      </div>
      {(text || active) && (
        <div className="mt-3 max-h-48 overflow-auto whitespace-pre-wrap rounded-xl bg-background/80 p-3 text-sm leading-7 text-foreground">
          {text || "يفكر الآن..."}
        </div>
      )}
    </div>
  );
}

export default function PipelinePage() {
  const [input, setInput] = useState(starterPrompts[0]);
  const [flow, setFlow] = useState<PipelineFlowId>("lesson");
  const [model, setModel] = useState<string>(PIPELINE_MODELS[0].id);
  const [run, setRun] = useState<RunState>({ status: "idle", currentAgent: null, outputs: [], deltas: {}, finalOutput: "" });

  const selectedFlow = useMemo(() => PIPELINE_FLOWS.find((f) => f.id === flow) ?? PIPELINE_FLOWS[0], [flow]);

  async function startPipeline() {
    if (!input.trim() || run.status === "running") return;
    setRun({ status: "running", currentAgent: null, outputs: [], deltas: {}, finalOutput: "" });

    try {
      const response = await fetch("/api/ai/pipeline", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input, flow, model }),
      });

      if (!response.ok || !response.body) {
        const json = await response.json().catch(() => null);
        throw new Error(json?.message ?? "تعذر تشغيل عقول المتعدد");
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const events = buffer.split("\n\n");
        buffer = events.pop() ?? "";

        for (const raw of events) {
          const line = raw.split("\n").find((l) => l.startsWith("data: "));
          if (!line) continue;
          const data = JSON.parse(line.slice(6));

          if (data.event === "agent_start") {
            setRun((r) => ({ ...r, currentAgent: data.agentId }));
          } else if (data.event === "agent_delta") {
            setRun((r) => ({
              ...r,
              deltas: { ...r.deltas, [data.agentId]: `${r.deltas[data.agentId as AgentId] ?? ""}${data.delta}` },
            }));
          } else if (data.event === "agent_done") {
            setRun((r) => ({
              ...r,
              outputs: [...r.outputs, { agentId: data.agentId, output: data.output, durationMs: data.durationMs }],
              deltas: { ...r.deltas, [data.agentId]: "" },
            }));
          } else if (data.event === "end") {
            setRun((r) => ({ ...r, status: "done", currentAgent: null, finalOutput: data.finalOutput ?? "" }));
          } else if (data.event === "error") {
            setRun((r) => ({ ...r, status: "error", currentAgent: null, error: data.message }));
          }
        }
      }
    } catch (error) {
      setRun((r) => ({ ...r, status: "error", currentAgent: null, error: error instanceof Error ? error.message : "حدث خطأ" }));
    }
  }

  function downloadMarkdown() {
    const content = `# نتيجة عقول المتعدد\n\n## الطلب\n${input}\n\n## النتيجة\n${run.finalOutput || run.outputs.map((o) => o.output).join("\n\n---\n\n")}`;
    const blob = new Blob([content], { type: "text/markdown;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "oqul-pipeline-result.md";
    a.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div className="mx-auto max-w-7xl space-y-6" dir="rtl">
      <div className="rounded-3xl bg-gradient-to-br from-primary/10 via-background to-emerald-500/10 p-6 md:p-8 border border-border">
        <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
          <div>
            <div className="mb-2 inline-flex items-center gap-2 rounded-full bg-primary/10 px-3 py-1 text-sm font-medium text-primary">
              <Brain className="h-4 w-4" /> ميزة v13 الأسطورية مدمجة الآن
            </div>
            <h1 className="text-3xl font-black tracking-tight text-foreground md:text-4xl">عقول المتعدد</h1>
            <p className="mt-2 max-w-2xl text-muted-foreground">
              منظومة وكلاء ذكية: منسق، باحث، محلل، خبير تربوي، وكاتب نهائي. صممت لتوليد دروس، تحليل مشاكل التعلم، وبناء محتوى مغربي أفضل.
            </p>
          </div>
          <Sparkles className="hidden h-16 w-16 text-primary md:block" />
        </div>
      </div>

      <div className="grid gap-6 lg:grid-cols-[420px_1fr]">
        <Card className="h-fit rounded-3xl">
          <CardContent className="space-y-5 p-5">
            <div>
              <label className="mb-2 block text-sm font-bold">نوع المعالجة</label>
              <div className="grid grid-cols-1 gap-2">
                {PIPELINE_FLOWS.map((f) => (
                  <button
                    key={f.id}
                    onClick={() => setFlow(f.id)}
                    className={`rounded-2xl border p-3 text-right transition ${flow === f.id ? "border-primary bg-primary/10" : "border-border hover:bg-secondary"}`}
                    type="button"
                  >
                    <div className="flex items-center gap-2 font-bold"><span>{f.icon}</span>{f.nameAr}</div>
                    <div className="mt-1 text-xs text-muted-foreground">{f.descriptionAr}</div>
                  </button>
                ))}
              </div>
            </div>

            <div>
              <label className="mb-2 block text-sm font-bold">النموذج</label>
              <select value={model} onChange={(e) => setModel(e.target.value)} className="h-11 w-full rounded-xl border border-input bg-background px-3 text-sm">
                {PIPELINE_MODELS.map((m) => <option key={m.id} value={m.id}>{m.label} — {m.id}</option>)}
              </select>
            </div>

            <div>
              <label className="mb-2 block text-sm font-bold">طلبك</label>
              <Textarea value={input} onChange={(e) => setInput(e.target.value)} className="min-h-40 resize-y" placeholder="اكتب ما تريد من عقول المتعدد..." />
            </div>

            <div className="flex flex-wrap gap-2">
              {starterPrompts.map((p) => (
                <button key={p} onClick={() => setInput(p)} className="rounded-full bg-secondary px-3 py-1.5 text-xs text-muted-foreground hover:text-foreground" type="button">
                  {p.slice(0, 38)}...
                </button>
              ))}
            </div>

            <div className="flex gap-2">
              <Button onClick={startPipeline} disabled={run.status === "running" || !input.trim()} className="flex-1">
                <Send className="h-4 w-4" /> تشغيل الوكلاء
              </Button>
              <Button variant="outline" onClick={() => setRun({ status: "idle", currentAgent: null, outputs: [], deltas: {}, finalOutput: "" })}>
                <RotateCcw className="h-4 w-4" />
              </Button>
            </div>
          </CardContent>
        </Card>

        <div className="space-y-4">
          <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
            {selectedFlow.agents.map((agentId) => {
              const output = run.outputs.find((o) => o.agentId === agentId);
              const delta = run.deltas[agentId] ?? "";
              return (
                <AgentCard
                  key={agentId}
                  agentId={agentId}
                  active={run.currentAgent === agentId}
                  done={Boolean(output)}
                  text={output?.output ?? delta}
                  durationMs={output?.durationMs}
                />
              );
            })}
          </div>

          <Card className="rounded-3xl">
            <CardContent className="p-5">
              <div className="mb-4 flex items-center justify-between gap-2">
                <div>
                  <h2 className="text-xl font-black">النتيجة النهائية</h2>
                  <p className="text-sm text-muted-foreground">هنا تظهر خلاصة الكاتب النهائي بعد مرور الطلب على الوكلاء.</p>
                </div>
                <Button variant="outline" onClick={downloadMarkdown} disabled={!run.finalOutput && run.outputs.length === 0}>
                  <Download className="h-4 w-4" /> تنزيل
                </Button>
              </div>
              {run.error ? <div className="rounded-2xl border border-red-200 bg-red-50 p-4 text-red-700">{run.error}</div> : null}
              <div className="min-h-64 whitespace-pre-wrap rounded-2xl bg-secondary/60 p-5 leading-8 text-foreground">
                {run.finalOutput || (run.status === "running" ? "الوكلاء يعملون الآن..." : "اكتب طلبك وشغّل عقول المتعدد.")}
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}

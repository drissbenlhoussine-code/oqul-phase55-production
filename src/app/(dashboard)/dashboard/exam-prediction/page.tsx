"use client";
import { useState, useEffect } from "react";
import { Send, RotateCcw, Copy, CheckCircle, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn }     from "@/lib/cn";
import type { GradeLevel } from "@/components/layout/sidebar";

// ── Grade detection (mirrors layout.tsx) ──────────────────────────────────────

function detectGradeLevel(slug: string | undefined): GradeLevel {
  if (!slug) return "unknown";
  const s = slug.toLowerCase().trim();
  if (s === "ap" || s.startsWith("ap") || /^\dap/.test(s)) return "primary";
  if (
    s === "ac" || /^\dac/.test(s) || s.startsWith("ac") ||
    s.includes("college") || s.includes("collège") || s.includes("middle") ||
    s.includes("اعدادي") || s.includes("الإعدادي")
  ) return "middle";
  if (
    s === "tc" || s.startsWith("tc") ||
    s.includes("common-core") || s.includes("trunk-common") ||
    s.includes("bac") || s.includes("lycee") || s.includes("lycée") ||
    s.includes("secondary") || s.includes("ثانوي") || s.includes("الجذع")
  ) return "secondary";
  return "unknown";
}

// ── Subject lists ──────────────────────────────────────────────────────────────

const SUBJECTS_MIDDLE = [
  "الرياضيات", "اللغة العربية", "الفيزياء والكيمياء",
  "علوم الحياة والأرض", "التاريخ والجغرافيا", "التربية الإسلامية", "اللغة الفرنسية",
];

const SUBJECTS_SECONDARY = [
  "الرياضيات", "الفيزياء والكيمياء", "علوم الحياة والأرض",
  "اللغة العربية", "الفلسفة", "التاريخ والجغرافيا",
  "علوم اقتصادية واجتماعية", "اللغة الفرنسية",
];

// ── Grade context prefix injected into pipeline input ─────────────────────────

const GRADE_CONTEXT: Record<GradeLevel, string> = {
  middle:    "المستوى: إعدادي (collège) — المغرب. الفروض والاختبارات إعدادية.\n\n",
  secondary: "المستوى: ثانوي / جذع مشترك / باكالوريا — المغرب. امتحانات وفروض أكثر تقدماً.\n\n",
  primary:   "",
  unknown:   "",
};

// ── Structured output template ─────────────────────────────────────────────────

const PLAN_TEMPLATE = `أنتج خطة استعداد كاملة للامتحان/الفرض تشمل بالترتيب:

## نقاط الضعف المحتملة
(المفاهيم التي يخطئ فيها الطلاب عادةً في هذه المادة بهذا المستوى)

## خطة مراجعة قصيرة
(مقسمة على محاور أو أيام — عملية وقابلة للتطبيق)

## تمارين مقترحة
(ثلاثة تمارين متدرجة الصعوبة مع الحلول الكاملة)

## نصائح للفرض والامتحان
(إدارة الوقت، أسلوب الإجابة، الأخطاء الشائعة، ما يجب تجنبه)

## مستوى الصعوبة المناسب للمرحلة
(ما الذي يُتوقع من الطالب في هذا المستوى بالتحديد)`;

// ── Page ───────────────────────────────────────────────────────────────────────

export default function ExamPredictionPage() {
  const [subject,    setSubject]    = useState("");
  const [concern,    setConcern]    = useState("");
  const [output,     setOutput]     = useState("");
  const [running,    setRunning]    = useState(false);
  const [copied,     setCopied]     = useState(false);
  const [error,      setError]      = useState("");
  const [gradeLevel, setGradeLevel] = useState<GradeLevel>("unknown");

  useEffect(() => {
    fetch("/api/children")
      .then((r) => r.json())
      .then((d) => {
        if (d.success && d.data?.length) {
          setGradeLevel(detectGradeLevel(d.data[0]?.grade?.slug));
        }
      })
      .catch(() => {});
  }, []);

  const subjects = gradeLevel === "secondary" ? SUBJECTS_SECONDARY : SUBJECTS_MIDDLE;
  const gradePrefix  = GRADE_CONTEXT[gradeLevel];
  const levelLabel   = gradeLevel === "secondary"
    ? "الثانوي والباكالوريا"
    : gradeLevel === "middle"
    ? "الإعدادي"
    : "";

  async function generate() {
    if (!subject.trim() || running) return;
    setOutput("");
    setError("");
    setRunning(true);

    const input = [
      gradePrefix,
      `استعداد لامتحان/فرض مادة: ${subject}`,
      concern.trim() ? `\nملاحظة الطالب: ${concern.trim()}` : "",
      `\n\n${PLAN_TEMPLATE}`,
    ].join("");

    try {
      const res = await fetch("/api/ai/pipeline", {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify({ input, flow: "analysis", model: "llama-3.3-70b-versatile" }),
      });

      if (!res.ok) {
        const err = await res.json().catch(() => ({})) as { message?: string };
        setError(err.message ?? "حدث خطأ غير متوقع. حاول مرة أخرى.");
        setRunning(false);
        return;
      }

      const reader  = res.body!.getReader();
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
            const ev      = JSON.parse(line.slice(6)) as Record<string, unknown>;
            const agentId = (ev.agentId ?? ev.agent_id) as string;
            if (ev.event === "agent_delta" && agentId === "writer") {
              live += ev.delta as string;
              setOutput(live);
            } else if (ev.event === "end") {
              setOutput(((ev.finalOutput ?? ev.final_output) as string) ?? live);
            } else if (ev.event === "error") {
              setError((ev.message as string) ?? "حدث خطأ أثناء تشغيل الوكلاء.");
            }
          } catch { /* ignore */ }
        }
      }
    } catch {
      setError("تعذّر الاتصال بالخادم. تحقق من الاتصال بالإنترنت وأعد المحاولة.");
    } finally {
      setRunning(false);
    }
  }

  async function copy() {
    await navigator.clipboard.writeText(output);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  }

  const hasOutput = Boolean(output);

  return (
    <div className="mx-auto max-w-3xl space-y-6" dir="rtl">

      {/* ── Header ── */}
      <div>
        <h1 className="text-2xl font-black flex items-center gap-3">
          <span className="w-10 h-10 rounded-2xl bg-gradient-to-br from-orange-500 to-primary flex items-center justify-center text-white text-lg">
            🎯
          </span>
          استعداد للامتحان
          {levelLabel && (
            <span className="text-sm font-medium text-muted-foreground bg-secondary px-2 py-0.5 rounded-lg">
              {levelLabel}
            </span>
          )}
        </h1>
        <p className="mt-1 text-sm text-muted-foreground">
          اختر المادة وسيُعدّ لك خطة مراجعة مخصصة مع تمارين ونصائح حسب مستواك
        </p>
      </div>

      {/* ── Subject picker ── */}
      <div className="space-y-2">
        <p className="text-[10px] font-semibold uppercase tracking-widest text-muted-foreground/60">اختر المادة</p>
        <div className="flex flex-wrap gap-2">
          {subjects.map((s) => (
            <button
              key={s}
              onClick={() => setSubject(s)}
              type="button"
              className={cn(
                "px-3 py-1.5 rounded-xl text-sm border transition-colors",
                subject === s
                  ? "bg-primary text-white border-primary"
                  : "border-border hover:border-primary hover:text-primary"
              )}
            >
              {s}
            </button>
          ))}
        </div>
      </div>

      {/* ── Optional concern ── */}
      <div className="space-y-2">
        <p className="text-[10px] font-semibold uppercase tracking-widest text-muted-foreground/60">ملاحظة إضافية (اختياري)</p>
        <textarea
          value={concern}
          onChange={(e) => setConcern(e.target.value)}
          onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); void generate(); } }}
          placeholder="مثال: أجد صعوبة في المعادلات، الامتحان بعد أسبوع، أريد التركيز على الجزء الثاني..."
          rows={2}
          disabled={running}
          className="w-full resize-none rounded-2xl border border-border bg-background px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary disabled:opacity-60 transition-shadow"
        />
      </div>

      {/* ── Actions ── */}
      <div className="flex gap-3">
        <Button
          onClick={() => void generate()}
          disabled={!subject.trim() || running}
          variant={running ? "outline" : "default"}
          className="rounded-2xl px-6 py-3 h-auto"
        >
          {running ? (
            <span className="flex items-center gap-2">
              <span className="h-2 w-2 animate-ping rounded-full bg-primary" />
              يُعدّ الخطة...
            </span>
          ) : (
            <span className="flex items-center gap-2">
              <Send className="h-4 w-4" />
              أعدّ لي خطة المراجعة
            </span>
          )}
        </Button>
        {hasOutput && (
          <Button
            onClick={() => { setOutput(""); setConcern(""); setSubject(""); setError(""); }}
            variant="ghost" size="sm" className="rounded-xl"
          >
            <RotateCcw className="h-4 w-4" />
          </Button>
        )}
      </div>

      {/* ── Error ── */}
      {error && (
        <div className="flex items-start gap-3 rounded-2xl border border-red-200 bg-red-50 px-4 py-3">
          <AlertCircle className="w-4 h-4 text-red-500 mt-0.5 shrink-0" />
          <p className="text-sm text-red-700 leading-6">{error}</p>
        </div>
      )}

      {/* ── Output ── */}
      {(hasOutput || running) && (
        <div className="overflow-hidden rounded-2xl border border-primary/20 bg-primary/5">
          <div className="flex items-center justify-between border-b border-primary/10 px-5 py-3">
            <div className="flex items-center gap-2">
              <CheckCircle className="h-4 w-4 text-primary" />
              <span className="text-sm font-semibold text-primary">خطة الاستعداد</span>
            </div>
            {hasOutput && (
              <button
                onClick={() => void copy()}
                type="button"
                className="flex items-center gap-1.5 text-xs text-muted-foreground hover:text-foreground transition-colors"
              >
                <Copy className="h-3.5 w-3.5" />
                {copied ? "تم النسخ ✓" : "نسخ"}
              </button>
            )}
          </div>
          <div className={cn(
            "min-h-32 max-h-[600px] overflow-y-auto px-5 py-4 text-sm leading-8 whitespace-pre-wrap",
            !output && "text-muted-foreground"
          )}>
            {output || "يُعدّ الخطة…"}
          </div>
        </div>
      )}

      {/* ── Empty state ── */}
      {!hasOutput && !running && !error && (
        <div className="py-12 text-center text-muted-foreground">
          <div className="mb-4 text-5xl">🎯</div>
          <p className="font-semibold">استعداد ذكي للامتحان</p>
          <p className="mx-auto mt-2 max-w-sm text-sm leading-7">
            اختر المادة أعلاه للحصول على خطة مراجعة مخصصة مع تمارين ونصائح للامتحان.
            لا يُحفظ شيء في قاعدة البيانات.
          </p>
        </div>
      )}

    </div>
  );
}

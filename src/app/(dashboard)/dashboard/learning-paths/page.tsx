"use client";
import { useState } from "react";
import { Target, Sparkles, ChevronLeft, RotateCcw, ExternalLink, BookOpen, MessageCircle, GraduationCap, AlertTriangle, TrendingUp, CheckCircle2, Clock } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/cn";
import Link from "next/link";

// ── Types mirroring API response ───────────────────────────────────────────────

type DayPlan = { day: string; action: string; tool: string; durationMinutes: number };
type LearningPathResult = {
  risk: "high" | "medium" | "low";
  pace: string;
  subject: string;
  detectedWeakness: string | null;
  weeklyPlan: DayPlan[];
  recommendations: string[];
  nextActions: string[];
  toolConnections: { leila: string; lessonHelper: string; examPrep: string };
};

// ── Static data ────────────────────────────────────────────────────────────────

const SUBJECTS = [
  { value: "math",          label: "الرياضيات",          emoji: "📐" },
  { value: "physics",       label: "الفيزياء والكيمياء", emoji: "⚗️" },
  { value: "arabic",        label: "اللغة العربية",       emoji: "📝" },
  { value: "french",        label: "اللغة الفرنسية",      emoji: "🇫🇷" },
  { value: "philosophy",    label: "الفلسفة",              emoji: "🧠" },
  { value: "history",       label: "التاريخ والجغرافيا",  emoji: "🗺️" },
  { value: "svt",           label: "علوم الحياة والأرض",  emoji: "🔬" },
  { value: "english",       label: "اللغة الإنجليزية",    emoji: "🇬🇧" },
];

const GRADES = [
  { value: "TC",   label: "جذع مشترك" },
  { value: "1BAC", label: "الأولى باكالوريا" },
  { value: "2BAC", label: "الثانية باكالوريا" },
  { value: "3AC",  label: "الثالثة إعدادي" },
  { value: "2AC",  label: "الثانية إعدادي" },
  { value: "1AC",  label: "الأولى إعدادي" },
];

const WEAKNESS_CHIPS = [
  "المعادلات والجبر", "الهندسة والبرهان", "قواعد اللغة والإعراب",
  "التعبير الكتابي", "فهم النصوص", "قوانين الفيزياء",
  "المنهجية والخطوات", "الوحدات والتطبيق", "بناء المقالة الفلسفية",
  "الروابط السببية في التاريخ", "الرسوم العلمية",
];

const TOOL_LINKS: Record<string, { href: string; icon: React.ElementType; color: string }> = {
  "ليلى":             { href: "/dashboard/leila",          icon: MessageCircle, color: "text-violet-600 bg-violet-50 border-violet-200" },
  "مولد الدروس":      { href: "/dashboard/lesson-helper",  icon: BookOpen,      color: "text-emerald-600 bg-emerald-50 border-emerald-200" },
  "استعداد للامتحان": { href: "/dashboard/secondary-school", icon: GraduationCap, color: "text-blue-600 bg-blue-50 border-blue-200" },
};

function getCsrfToken(): string {
  if (typeof document === "undefined") return "";
  const m = document.cookie.match(/oqul_csrf=([^;]+)/);
  return m ? decodeURIComponent(m[1]) : "";
}

// ── Risk badge ─────────────────────────────────────────────────────────────────

function RiskBadge({ risk }: { risk: "high" | "medium" | "low" }) {
  const map = {
    high:   { label: "يحتاج دعماً مكثفاً",  icon: AlertTriangle, cls: "bg-red-50    border-red-200   text-red-700"    },
    medium: { label: "أداء متوسط — تحسين ممكن", icon: TrendingUp,   cls: "bg-amber-50  border-amber-200 text-amber-700"  },
    low:    { label: "مستوى جيد — تسريع",     icon: CheckCircle2, cls: "bg-green-50  border-green-200 text-green-700"  },
  };
  const { label, icon: Icon, cls } = map[risk];
  return (
    <span className={cn("inline-flex items-center gap-1.5 rounded-full border px-3 py-1 text-xs font-medium", cls)}>
      <Icon className="h-3.5 w-3.5" />
      {label}
    </span>
  );
}

// ── Day card ───────────────────────────────────────────────────────────────────

function DayCard({ plan, index }: { plan: DayPlan; index: number }) {
  const toolInfo = TOOL_LINKS[plan.tool];
  return (
    <div className="flex gap-3 rounded-2xl border border-border bg-background p-4 hover:border-primary/30 transition-colors">
      <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-primary/10 text-xs font-bold text-primary">
        {index + 1}
      </div>
      <div className="flex-1 min-w-0">
        <div className="flex items-center justify-between gap-2 flex-wrap">
          <span className="text-xs font-semibold text-muted-foreground">{plan.day}</span>
          <div className="flex items-center gap-1.5">
            <Clock className="h-3 w-3 text-muted-foreground" />
            <span className="text-xs text-muted-foreground">{plan.durationMinutes} دق</span>
          </div>
        </div>
        <p className="mt-1 text-sm leading-6">{plan.action}</p>
        {toolInfo ? (
          <Link
            href={toolInfo.href}
            className={cn("mt-2 inline-flex items-center gap-1 rounded-lg border px-2 py-0.5 text-xs font-medium transition-opacity hover:opacity-80", toolInfo.color)}
          >
            <toolInfo.icon className="h-3 w-3" />
            {plan.tool}
          </Link>
        ) : (
          <span className="mt-2 inline-flex items-center gap-1 rounded-lg border bg-secondary px-2 py-0.5 text-xs text-muted-foreground">
            {plan.tool}
          </span>
        )}
      </div>
    </div>
  );
}

// ── Page ───────────────────────────────────────────────────────────────────────

export default function LearningPathsPage() {
  const [subject,    setSubject]    = useState("");
  const [grade,      setGrade]      = useState("");
  const [weakness,   setWeakness]   = useState("");
  const [score,      setScore]      = useState("");
  const [loading,    setLoading]    = useState(false);
  const [result,     setResult]     = useState<LearningPathResult | null>(null);
  const [error,      setError]      = useState("");

  async function generate() {
    if (!subject || loading) return;
    setError("");
    setLoading(true);
    setResult(null);

    const weakPoints = weakness
      .split(/[،,\n]+/)
      .map((s) => s.trim())
      .filter(Boolean);

    const body = {
      subject,
      grade:        grade   || undefined,
      weakPoints:   weakPoints.length ? weakPoints : undefined,
      averageScore: score   ? Number(score)  : undefined,
    };

    try {
      const res = await fetch("/api/phase55/learning-path", {
        method:  "POST",
        headers: {
          "Content-Type":  "application/json",
          "X-CSRF-Token":  getCsrfToken(),
        },
        body: JSON.stringify(body),
      });

      if (res.status === 403) {
        // CSRF cookie missing — retry once after page refresh hint
        setError("جلسة منتهية. أعد تحميل الصفحة ثم حاول مجدداً.");
        setLoading(false);
        return;
      }

      const data = await res.json().catch(() => ({})) as { ok?: boolean; path?: LearningPathResult; error?: string };
      if (!data.ok || !data.path) {
        setError(data.error ?? "حدث خطأ. حاول مجدداً.");
        setLoading(false);
        return;
      }
      setResult(data.path);
    } catch {
      setError("تعذر الاتصال. تحقق من الشبكة وحاول مجدداً.");
    }
    setLoading(false);
  }

  function reset() {
    setResult(null);
    setError("");
  }

  const subjectLabel = SUBJECTS.find((s) => s.value === subject)?.label ?? subject;

  return (
    <div className="mx-auto max-w-3xl space-y-6" dir="rtl">

      {/* Header */}
      <div>
        <h1 className="flex items-center gap-3 text-2xl font-black">
          <span className="flex h-10 w-10 items-center justify-center rounded-2xl bg-gradient-to-br from-primary to-violet-500 text-white text-lg">
            🗺️
          </span>
          مسارات التعلم الشخصية
        </h1>
        <p className="mt-1 text-sm text-muted-foreground">
          خطة دراسية أسبوعية مخصصة لك — حسب المادة، المستوى، ونقاط الضعف
        </p>
      </div>

      {/* Form — only shown when no result */}
      {!result && (
        <div className="space-y-5 rounded-3xl border border-border bg-background p-6">

          {/* Subject selector */}
          <div>
            <label className="mb-2 block text-sm font-semibold">المادة الدراسية *</label>
            <div className="flex flex-wrap gap-2">
              {SUBJECTS.map((s) => (
                <button
                  key={s.value}
                  onClick={() => setSubject(s.value)}
                  className={cn(
                    "flex items-center gap-1.5 rounded-xl border px-3 py-2 text-sm transition-all",
                    subject === s.value
                      ? "border-primary bg-primary/10 text-primary font-semibold"
                      : "border-border text-muted-foreground hover:border-primary/50 hover:text-foreground"
                  )}
                >
                  <span>{s.emoji}</span>
                  {s.label}
                </button>
              ))}
            </div>
          </div>

          {/* Grade selector */}
          <div>
            <label className="mb-2 block text-sm font-semibold">المستوى الدراسي</label>
            <div className="flex flex-wrap gap-2">
              {GRADES.map((g) => (
                <button
                  key={g.value}
                  onClick={() => setGrade(g.value === grade ? "" : g.value)}
                  className={cn(
                    "rounded-xl border px-3 py-2 text-sm transition-all",
                    grade === g.value
                      ? "border-primary bg-primary/10 text-primary font-semibold"
                      : "border-border text-muted-foreground hover:border-primary/50 hover:text-foreground"
                  )}
                >
                  {g.label}
                </button>
              ))}
            </div>
          </div>

          {/* Weakness chips + free text */}
          <div>
            <label className="mb-2 block text-sm font-semibold">نقاط الضعف أو الأهداف</label>
            <div className="mb-2 flex flex-wrap gap-1.5">
              {WEAKNESS_CHIPS.map((chip) => {
                const active = weakness.includes(chip);
                return (
                  <button
                    key={chip}
                    onClick={() => {
                      setWeakness((prev) => {
                        const parts = prev.split("،").map((p) => p.trim()).filter(Boolean);
                        return active
                          ? parts.filter((p) => p !== chip).join("، ")
                          : [...parts, chip].join("، ");
                      });
                    }}
                    className={cn(
                      "rounded-full border px-2.5 py-1 text-xs transition-all",
                      active
                        ? "border-primary bg-primary/10 text-primary"
                        : "border-border text-muted-foreground hover:border-primary/40"
                    )}
                  >
                    {chip}
                  </button>
                );
              })}
            </div>
            <textarea
              value={weakness}
              onChange={(e) => setWeakness(e.target.value)}
              placeholder="أو اكتب بحرية: مثلاً 'معادلات تفاضلية، البرهان الهندسي'"
              rows={2}
              className="w-full resize-none rounded-xl border border-border bg-background px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-primary"
            />
          </div>

          {/* Optional score */}
          <div>
            <label className="mb-2 block text-sm font-semibold">
              آخر معدل في هذه المادة
              <span className="mr-2 text-xs font-normal text-muted-foreground">(اختياري — يساعد في تحديد المستوى)</span>
            </label>
            <div className="flex items-center gap-2">
              <input
                type="number"
                min="0"
                max="20"
                value={score}
                onChange={(e) => setScore(e.target.value)}
                placeholder="من 0 إلى 20"
                className="w-32 rounded-xl border border-border bg-background px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary"
              />
              <span className="text-sm text-muted-foreground">/ 20</span>
            </div>
          </div>

          {error && (
            <p className="rounded-xl bg-red-50 border border-red-200 px-4 py-2 text-sm text-red-700">
              {error}
            </p>
          )}

          <Button
            onClick={() => void generate()}
            disabled={!subject || loading}
            className="w-full rounded-2xl py-6 text-base font-semibold"
          >
            {loading ? (
              <span className="flex items-center gap-2">
                <span className="h-2 w-2 animate-ping rounded-full bg-white/80" />
                يُعد المسار…
              </span>
            ) : (
              <span className="flex items-center gap-2">
                <Sparkles className="h-5 w-5" />
                أنشئ مساري الشخصي
              </span>
            )}
          </Button>
        </div>
      )}

      {/* Results */}
      {result && (
        <div className="space-y-5">

          {/* Summary header */}
          <div className="flex items-start justify-between gap-4 rounded-3xl border border-border bg-background p-5">
            <div>
              <h2 className="text-lg font-bold">
                مسار {subjectLabel}
                {result.detectedWeakness && (
                  <span className="mr-2 text-sm font-normal text-muted-foreground">
                    — التركيز: {result.detectedWeakness}
                  </span>
                )}
              </h2>
              <div className="mt-2">
                <RiskBadge risk={result.risk} />
              </div>
            </div>
            <Button
              onClick={reset}
              variant="outline"
              size="sm"
              className="shrink-0 rounded-xl gap-1.5"
            >
              <RotateCcw className="h-4 w-4" />
              مسار جديد
            </Button>
          </div>

          {/* Weekly plan */}
          <section>
            <h3 className="mb-3 flex items-center gap-2 text-base font-bold">
              <Target className="h-4 w-4 text-primary" />
              الخطة الأسبوعية ({result.weeklyPlan.length} أيام)
            </h3>
            <div className="space-y-2">
              {result.weeklyPlan.map((day, i) => (
                <DayCard key={i} plan={day} index={i} />
              ))}
            </div>
          </section>

          {/* Recommendations */}
          <section className="rounded-2xl border border-amber-200 bg-amber-50 p-5">
            <h3 className="mb-3 flex items-center gap-2 text-sm font-bold text-amber-800">
              <Sparkles className="h-4 w-4" />
              توصيات شخصية
            </h3>
            <ul className="space-y-2">
              {result.recommendations.map((rec, i) => (
                <li key={i} className="flex items-start gap-2 text-sm text-amber-900">
                  <ChevronLeft className="mt-0.5 h-4 w-4 shrink-0 text-amber-500" />
                  {rec}
                </li>
              ))}
            </ul>
          </section>

          {/* Next actions */}
          {result.nextActions.length > 0 && (
            <section className="rounded-2xl border border-primary/20 bg-primary/5 p-5">
              <h3 className="mb-3 text-sm font-bold text-primary">ابدأ الآن</h3>
              <ul className="space-y-1.5">
                {result.nextActions.map((action, i) => (
                  <li key={i} className="flex items-start gap-2 text-sm">
                    <span className="mt-0.5 h-5 w-5 shrink-0 rounded-full bg-primary/20 text-center text-xs font-bold leading-5 text-primary">
                      {i + 1}
                    </span>
                    {action}
                  </li>
                ))}
              </ul>
            </section>
          )}

          {/* Tool connections */}
          <section>
            <h3 className="mb-3 text-sm font-bold">الأدوات المستخدمة في هذا المسار</h3>
            <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
              {(
                [
                  { key: "leila",        label: "اسألي ليلى",    href: "/dashboard/leila",           icon: MessageCircle, desc: result.toolConnections.leila,        color: "border-violet-200 bg-violet-50" },
                  { key: "lessonHelper", label: "مولد الدروس",   href: "/dashboard/lesson-helper",   icon: BookOpen,      desc: result.toolConnections.lessonHelper,  color: "border-emerald-200 bg-emerald-50" },
                  { key: "examPrep",     label: "الثانوي والباك", href: "/dashboard/secondary-school", icon: GraduationCap, desc: result.toolConnections.examPrep,      color: "border-blue-200 bg-blue-50" },
                ] as const
              ).map((tool) => (
                <Link
                  key={tool.key}
                  href={tool.href}
                  className={cn(
                    "flex flex-col gap-2 rounded-2xl border p-4 transition-opacity hover:opacity-80",
                    tool.color
                  )}
                >
                  <div className="flex items-center gap-2">
                    <tool.icon className="h-4 w-4" />
                    <span className="text-sm font-semibold">{tool.label}</span>
                    <ExternalLink className="h-3 w-3 mr-auto text-muted-foreground" />
                  </div>
                  <p className="text-xs leading-5 text-muted-foreground">{tool.desc}</p>
                </Link>
              ))}
            </div>
          </section>

        </div>
      )}

      {/* Empty state */}
      {!result && !loading && (
        <div className="py-8 text-center text-muted-foreground">
          <div className="mb-3 text-5xl">🗺️</div>
          <p className="font-semibold">خطة مخصصة لكل طالب</p>
          <p className="mx-auto mt-2 max-w-sm text-sm leading-7">
            اختر المادة ومستواك ونقاط ضعفك — ستحصل على خطة أسبوعية مفصلة مع أدوات تعليمية موجهة.
          </p>
        </div>
      )}

    </div>
  );
}

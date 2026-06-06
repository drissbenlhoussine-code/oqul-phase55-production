"use client";
import { useState, useEffect } from "react";
import { Send, RotateCcw, Copy, CheckCircle, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn }     from "@/lib/cn";

// ── Grade level (more granular than sidebar GradeLevel) ───────────────────────

type ExamGradeLevel = "primary" | "middle" | "tc" | "bac1" | "bac2" | "unknown";

function detectExamGradeLevel(slug: string | undefined): ExamGradeLevel {
  if (!slug) return "unknown";
  const s = slug.toLowerCase().trim();
  if (s === "ap" || s.startsWith("ap") || /^\dap/.test(s)) return "primary";

  // Secondary — most specific first
  if (s.includes("2bac") || s.startsWith("2bac") || /2.*bac/.test(s) || s === "tronc-commun-2" || s.includes("deuxième") || s.includes("ثانية باك"))
    return "bac2";
  if (s.includes("1bac") || s.startsWith("1bac") || /1.*bac/.test(s) || s.includes("première bac") || s.includes("أولى باك"))
    return "bac1";
  if (s === "tc" || s.startsWith("tc") || s.includes("tronc") || s.includes("common-core") || s.includes("trunk-common") || s.includes("جذع"))
    return "tc";
  if (s.includes("bac") || s.includes("lycee") || s.includes("lycée") || s.includes("secondary") || s.includes("ثانوي"))
    return "bac1"; // fallback secondary → bac1

  if (
    s === "ac" || /^\dac/.test(s) || s.startsWith("ac") ||
    s.includes("college") || s.includes("collège") || s.includes("middle") ||
    s.includes("اعدادي") || s.includes("الإعدادي")
  ) return "middle";

  return "unknown";
}

// ── Exam type labels per level ────────────────────────────────────────────────

const EXAM_TYPE: Record<ExamGradeLevel, string> = {
  middle:  "الفرض والامتحان الموحد الإقليمي",
  tc:      "الفرض والامتحان الموحد الإقليمي (جذع مشترك)",
  bac1:    "الفرض والامتحان الموحد الجهوي (السنة الأولى باك)",
  bac2:    "الفرض والامتحان الوطني الموحد (الباكالوريا)",
  primary: "",
  unknown: "",
};

const LEVEL_LABEL: Record<ExamGradeLevel, string> = {
  middle:  "الإعدادي",
  tc:      "الجذع المشترك",
  bac1:    "السنة الأولى باك",
  bac2:    "الباكالوريا (2BAC)",
  primary: "",
  unknown: "",
};

// ── Subjects per level ────────────────────────────────────────────────────────

const SUBJECTS: Record<ExamGradeLevel, string[]> = {
  middle: [
    "الرياضيات", "اللغة العربية", "الفيزياء والكيمياء",
    "علوم الحياة والأرض", "التاريخ والجغرافيا", "التربية الإسلامية", "اللغة الفرنسية",
  ],
  tc: [
    "الرياضيات", "الفيزياء والكيمياء", "علوم الحياة والأرض",
    "اللغة العربية", "التاريخ والجغرافيا", "اللغة الفرنسية",
  ],
  bac1: [
    "الرياضيات", "الفيزياء والكيمياء", "علوم الحياة والأرض",
    "اللغة العربية", "الفلسفة", "التاريخ والجغرافيا",
    "علوم اقتصادية واجتماعية", "اللغة الفرنسية",
  ],
  bac2: [
    "الرياضيات", "الفيزياء والكيمياء", "علوم الحياة والأرض",
    "اللغة العربية", "الفلسفة", "التاريخ والجغرافيا",
    "علوم اقتصادية واجتماعية", "اللغة الفرنسية",
  ],
  primary: [],
  unknown: [
    "الرياضيات", "اللغة العربية", "الفيزياء والكيمياء",
    "علوم الحياة والأرض", "التاريخ والجغرافيا",
  ],
};

// ── Topics per level × subject ────────────────────────────────────────────────

type TopicMap = Record<string, Record<string, string[]>>;

const TOPICS: Partial<TopicMap> = {
  middle: {
    "الرياضيات":        ["كسور وأعداد عشرية", "معادلات وتفاوتات", "هندسة مستوية", "نسب ومئويات", "إحصاء وتمثيلات", "أعداد صحيحة وعمليات"],
    "الفيزياء والكيمياء": ["المادة وتحولاتها", "الكهرباء الساكنة", "الضوء والأبصار", "المحاليل والتفاعلات", "الميكانيك"],
    "علوم الحياة والأرض": ["الخلية والكائنات الحية", "الهضم والتغذية", "الحركة والعضلات", "التوالد", "الجيولوجيا والصخور"],
    "اللغة العربية":    ["النصوص الأدبية", "قواعد اللغة", "التعبير والإنشاء", "البلاغة"],
    "التاريخ والجغرافيا": ["الحضارات القديمة", "الجغرافيا الاقتصادية", "تاريخ المغرب", "البيئة والتنمية"],
  },
  tc: {
    "الرياضيات":        ["الدوال العددية", "المشتقات", "المثلثية", "هندسة فضائية", "حساب المتجهات", "الإحصاء والاحتمالات"],
    "الفيزياء والكيمياء": ["الكيمياء العضوية المدخل", "الكهرباء والدوائر", "ميكانيك نيوتن", "الذرة والعنصر الكيميائي"],
    "علوم الحياة والأرض": ["الوراثة والخلية", "وحدة الكائنات الحية", "علم الأعصاب المدخل", "الجيولوجيا الخارجية"],
    "اللغة العربية":    ["الأجناس الأدبية", "النقد الأدبي", "قواعد متقدمة", "التعبير الكتابي"],
  },
  bac1: {
    "الرياضيات":        ["التفاضل والتكامل", "المتتاليات", "اللوغاريتم والأسي", "الاحتمالات", "المتجهات والفضاء"],
    "الفيزياء والكيمياء": ["الميكانيك الكلاسيكي", "الكهرومغناطيسية", "الكيمياء العضوية", "الضوئيات"],
    "علوم الحياة والأرض": ["الجهاز العصبي والهرموني", "المناعة", "الجيولوجيا الداخلية", "علم الوراثة"],
    "الفلسفة":          ["الإنسان والتفكير", "المعرفة والحقيقة", "الوجود والزمان", "السياسة والمجتمع"],
    "التاريخ والجغرافيا": ["الحرب العالمية والعلاقات الدولية", "التنمية والتفاوتات", "العولمة", "جغرافيا المغرب"],
  },
  bac2: {
    "الرياضيات":        ["الأعداد المركبة", "التكامل المتقدم", "المعادلات التفاضلية", "الاحتمالات المتقدمة", "الفضاء الإقليدي"],
    "الفيزياء والكيمياء": ["ميكانيك الموائع وتحليل الحركة", "الكيمياء العضوية المتقدمة", "الكهرومغناطيسية المتقدمة", "فيزياء النواة"],
    "علوم الحياة والأرض": ["أساليب الاستدلال العلمي", "الجينوم وتنظيم التعبير الجيني", "الجيولوجيا والبنية الداخلية"],
    "الفلسفة":          ["نظرية المعرفة", "فلسفة الفن", "الأخلاق والسياسة", "الوجودية والحرية"],
    "التاريخ والجغرافيا": ["العلاقات الدولية بعد الحرب الباردة", "الجغرافيا الاقتصادية العالمية", "قضايا المغرب المعاصر"],
  },
};

// ── Grade context injected into prompt ────────────────────────────────────────

const GRADE_CONTEXT: Record<ExamGradeLevel, string> = {
  middle:  "المستوى: إعدادي (collège) — المغرب. نوع التقييم: الفرض المحروس والامتحان الموحد الإقليمي.\n",
  tc:      "المستوى: جذع مشترك (tronc commun) — ثانوي المغرب. نوع التقييم: الفرض المحروس والامتحان الموحد الإقليمي.\n",
  bac1:    "المستوى: السنة الأولى بكالوريا (1ère Bac) — المغرب. نوع التقييم: الفرض المحروس والامتحان الموحد الجهوي.\n",
  bac2:    "المستوى: الثانية بكالوريا (2ème Bac) — المغرب. نوع التقييم: الامتحان الوطني الموحد (الباكالوريا).\n",
  primary: "",
  unknown: "",
};

// ── Plan template ─────────────────────────────────────────────────────────────

function buildPlanTemplate(
  level:       ExamGradeLevel,
  subject:     string,
  topic:       string,
  examType:    string,
  weakAreas:   string[],
  avgScore:    number | null,
) {
  const weakSection = weakAreas.length > 0
    ? `نقاط الضعف المرصودة فعلياً من تاريخ الطالب: ${weakAreas.join("، ")}\n`
    : "";

  const scoreSection = avgScore !== null
    ? `معدل الطالب الحالي: ${avgScore}% — ${avgScore < 50 ? "يحتاج تركيزاً مكثفاً على الأساسيات" : avgScore < 70 ? "مستوى متوسط، التركيز على التمارين المتوسطة" : "مستوى جيد، التركيز على التمارين المتقدمة والأخطاء الدقيقة"}.\n`
    : "";

  const topicLine = topic ? `المحور / الوحدة المختارة: ${topic}\n` : "";

  return `${GRADE_CONTEXT[level]}المادة: ${subject}
${topicLine}نوع الامتحان المستهدف: ${examType}
${weakSection}${scoreSection}
أنتج خطة استعداد شاملة ومخصصة تشمل بالترتيب:

## نقاط الضعف المحتملة
${weakAreas.length > 0
  ? "ابدأ بالنقاط المرصودة أعلاه، ثم أضف المفاهيم التي يخطئ فيها الطلاب عادةً في هذه المادة بهذا المستوى."
  : "المفاهيم التي يخطئ فيها الطلاب عادةً في هذه المادة بهذا المستوى."}

## خطة مراجعة قصيرة
مقسمة على محاور أو أيام — عملية وقابلة للتطبيق. خصصها لمستوى ${LEVEL_LABEL[level]}.

## تمارين مخصصة للامتحان
ثلاثة تمارين متدرجة الصعوبة تحاكي أسلوب ${examType}، مع الحلول الكاملة.
${avgScore !== null && avgScore < 50 ? "ابدأ بتمرين أساسي جداً ثم توسط ثم متقدم." : avgScore !== null && avgScore >= 70 ? "ركز على التمارين المتوسطة والمتقدمة مع تمرين تركيبي." : "تدرج من سهل إلى متوسط إلى متقدم."}

## نصائح للفرض والامتحان
إدارة الوقت حسب أسلوب ${examType}، ترتيب الإجابات، الأخطاء الشائعة، ما يجب تجنبه.

## مستوى التوقعات لـ${LEVEL_LABEL[level]}
ما الذي يُتوقع تحديداً من طالب ${LEVEL_LABEL[level]} في ${subject}${topic ? ` — محور ${topic}` : ""}.`;
}

// ── Types ─────────────────────────────────────────────────────────────────────

interface ProgressItem { status: string; lesson?: { titleAr?: string } }

// ── Page ───────────────────────────────────────────────────────────────────────

export default function ExamPredictionPage() {
  const [subject,    setSubject]    = useState("");
  const [topic,      setTopic]      = useState("");
  const [concern,    setConcern]    = useState("");
  const [output,     setOutput]     = useState("");
  const [running,    setRunning]    = useState(false);
  const [copied,     setCopied]     = useState(false);
  const [error,      setError]      = useState("");

  const [level,      setLevel]      = useState<ExamGradeLevel>("unknown");
  const [avgScore,   setAvgScore]   = useState<number | null>(null);
  const [weakAreas,  setWeakAreas]  = useState<string[]>([]);

  useEffect(() => {
    async function load() {
      try {
        const cr = await fetch("/api/children").then(r => r.json()).catch(() => ({ success: false }));
        if (!cr.success || !cr.data?.[0]) return;
        const child = cr.data[0] as { id: string; grade?: { slug?: string } };
        const detectedLevel = detectExamGradeLevel(child.grade?.slug);
        setLevel(detectedLevel);

        const [sumRes, progRes] = await Promise.all([
          fetch(`/api/analytics/learning?childId=${child.id}`).then(r => r.json()).catch(() => ({})),
          fetch(`/api/progress?childId=${child.id}`).then(r => r.json()).catch(() => ({})),
        ]);

        if (sumRes.success && sumRes.data?.averageScore != null) {
          setAvgScore(sumRes.data.averageScore as number);
        }
        if (progRes.success && Array.isArray(progRes.data)) {
          const weak = (progRes.data as ProgressItem[])
            .filter(p => p.status === "needs_review" && p.lesson?.titleAr)
            .map(p => p.lesson!.titleAr as string)
            .slice(0, 5);
          setWeakAreas(weak);
        }
      } catch { /* silent */ }
    }
    void load();
  }, []);

  const subjects      = SUBJECTS[level] ?? SUBJECTS.unknown;
  const topicOptions: string[] = (subject ? TOPICS[level as keyof typeof TOPICS]?.[subject] : undefined) ?? [];
  const examType      = EXAM_TYPE[level];
  const levelLabel    = LEVEL_LABEL[level];

  function pickSubject(s: string) {
    setSubject(s);
    setTopic("");
    setOutput("");
    setError("");
  }

  async function generate() {
    if (!subject.trim() || running) return;
    setOutput("");
    setError("");
    setRunning(true);

    const input = buildPlanTemplate(level, subject, topic, examType, weakAreas, avgScore)
      + (concern.trim() ? `\n\nملاحظة إضافية من الطالب: ${concern.trim()}` : "");

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

  function reset() {
    setOutput("");
    setConcern("");
    setSubject("");
    setTopic("");
    setError("");
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
          {examType
            ? `خطة مراجعة مخصصة لـ${examType} — تمارين على أسلوب الامتحان الحقيقي`
            : "اختر المادة وسيُعدّ لك خطة مراجعة مخصصة مع تمارين ونصائح حسب مستواك"}
        </p>
      </div>

      {/* ── Progress context badges ── */}
      {(weakAreas.length > 0 || avgScore !== null) && (
        <div className="flex flex-wrap gap-2 text-xs">
          {avgScore !== null && (
            <span className={cn(
              "px-2.5 py-1 rounded-full border font-medium",
              avgScore >= 70 ? "bg-emerald-50 border-emerald-200 text-emerald-700"
                : avgScore >= 50 ? "bg-amber-50 border-amber-200 text-amber-700"
                : "bg-red-50 border-red-200 text-red-700"
            )}>
              معدلك {avgScore}%
            </span>
          )}
          {weakAreas.map((w) => (
            <span key={w} className="px-2.5 py-1 rounded-full bg-orange-50 border border-orange-200 text-orange-700">
              ⚠ {w}
            </span>
          ))}
        </div>
      )}

      {/* ── Subject picker ── */}
      <div className="space-y-2">
        <p className="text-[10px] font-semibold uppercase tracking-widest text-muted-foreground/60">اختر المادة</p>
        <div className="flex flex-wrap gap-2">
          {subjects.map((s) => (
            <button
              key={s}
              onClick={() => pickSubject(s)}
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

      {/* ── Topic chips (appear after subject selected) ── */}
      {topicOptions.length > 0 && (
        <div className="space-y-2">
          <p className="text-[10px] font-semibold uppercase tracking-widest text-muted-foreground/60">
            المحور / الوحدة (اختياري)
          </p>
          <div className="flex flex-wrap gap-2">
            {topicOptions.map((t) => (
              <button
                key={t}
                onClick={() => setTopic(prev => prev === t ? "" : t)}
                type="button"
                className={cn(
                  "px-3 py-1.5 rounded-xl text-sm border transition-colors",
                  topic === t
                    ? "bg-orange-500 text-white border-orange-500"
                    : "border-border hover:border-orange-400 hover:text-orange-600"
                )}
              >
                {t}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* ── Optional concern ── */}
      <div className="space-y-2">
        <p className="text-[10px] font-semibold uppercase tracking-widest text-muted-foreground/60">ملاحظة إضافية (اختياري)</p>
        <textarea
          value={concern}
          onChange={(e) => setConcern(e.target.value)}
          onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); void generate(); } }}
          placeholder="مثال: الامتحان بعد أسبوع، أجد صعوبة في التمارين المركبة، أريد التركيز على الجزء الثاني..."
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
          <Button onClick={reset} variant="ghost" size="sm" className="rounded-xl">
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
              {subject && (
                <span className="text-xs text-muted-foreground">— {subject}{topic ? ` / ${topic}` : ""}</span>
              )}
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
            اختر المادة أعلاه للحصول على خطة مراجعة مخصصة مع تمارين على أسلوب
            {examType ? ` ${examType}` : " الامتحان الحقيقي"}.
            لا يُحفظ شيء في قاعدة البيانات.
          </p>
        </div>
      )}

    </div>
  );
}

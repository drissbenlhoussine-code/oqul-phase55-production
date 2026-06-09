import Link from "next/link";
import { getSecondarySummary } from "@/features/secondary/lib/secondary-curriculum";

// ── Subject sections with BAC topics and CTAs ──────────────────────────────────

const SUBJECTS = [
  {
    key:     "math",
    emoji:   "📐",
    label:   "الرياضيات",
    color:   "border-blue-200 bg-blue-50",
    titleColor: "text-blue-800",
    topics:  [
      "الحساب المثلثي والوظائف",
      "الاشتقاق والتكامل",
      "الجبر الخطي والمصفوفات",
      "المعادلات التفاضلية",
      "الإحصاء والاحتمالات",
      "الهندسة الفضائية",
    ],
    leilaHint: "الرياضيات",
  },
  {
    key:     "physics",
    emoji:   "⚗️",
    label:   "الفيزياء والكيمياء",
    color:   "border-violet-200 bg-violet-50",
    titleColor: "text-violet-800",
    topics:  [
      "الحركة وقوانين نيوتن",
      "الكهرباء والمغناطيسية",
      "الضوء والموجات",
      "التحولات الكيميائية",
      "الطاقة وتحولاتها",
      "الترموديناميك",
    ],
    leilaHint: "الفيزياء والكيمياء",
  },
  {
    key:     "philosophy",
    emoji:   "🧠",
    label:   "الفلسفة",
    color:   "border-amber-200 bg-amber-50",
    titleColor: "text-amber-800",
    topics:  [
      "بناء المقالة الفلسفية",
      "الإشكالية والأطروحة والنقيضة",
      "نظرية المعرفة",
      "الأخلاق والقيم",
      "الفلسفة السياسية",
      "الوجود والحرية والهوية",
    ],
    leilaHint: "الفلسفة وبناء المقالة",
  },
  {
    key:     "arabic",
    emoji:   "📝",
    label:   "اللغة العربية",
    color:   "border-emerald-200 bg-emerald-50",
    titleColor: "text-emerald-800",
    topics:  [
      "تحليل النصوص الأدبية",
      "النحو والصرف والإعراب",
      "التعبير الكتابي والإنشاء",
      "الأساليب البيانية",
      "الأدب المغربي الحديث",
      "النصوص الفكرية والفلسفية",
    ],
    leilaHint: "اللغة العربية والإعراب",
  },
  {
    key:     "french",
    emoji:   "🇫🇷",
    label:   "اللغة الفرنسية",
    color:   "border-red-200 bg-red-50",
    titleColor: "text-red-800",
    topics:  [
      "Compréhension de texte",
      "Expression écrite (rédaction)",
      "Grammaire et conjugaison",
      "Textes littéraires",
      "Langue de spécialité",
      "Argumentation et dissertation",
    ],
    leilaHint: "la langue française et la grammaire",
  },
  {
    key:     "svt",
    emoji:   "🔬",
    label:   "علوم الحياة والأرض",
    color:   "border-teal-200 bg-teal-50",
    titleColor: "text-teal-800",
    topics:  [
      "الوراثة والتكاثر",
      "علم الأعصاب والتنسيق",
      "التغذية والتمثيل الغذائي",
      "الجيولوجيا وبنية الأرض",
      "علم المناعة",
      "تطور الأنواع",
    ],
    leilaHint: "علوم الحياة والأرض",
  },
];

const GRADES = [
  { key: "TC",   label: "جذع مشترك",          note: "بناء الأسس + استيعاب المنهج الثانوي" },
  { key: "1BAC", label: "الأولى باكالوريا",    note: "الفروض الجهوية + تعمق في كل مادة" },
  { key: "2BAC", label: "الثانية باكالوريا",   note: "الباكالوريا الوطنية + امتحانات حقيقية" },
];

const METHODOLOGY_STEPS = [
  { step: "1", title: "اشرح لي", desc: "اطلب من ليلى أو مولد الدروس شرح أي مفهوم بعمق", href: "/dashboard/leila",         btnLabel: "اسألي ليلى" },
  { step: "2", title: "تدرّب",   desc: "احصل على تمارين بمستوى الفرض أو الباكالوريا",    href: "/dashboard/lesson-helper",  btnLabel: "مولد الدروس" },
  { step: "3", title: "راجع",    desc: "بحث وتحليل معمق لأي موضوع أو مسألة صعبة",       href: "/dashboard/research",       btnLabel: "البحث الذكي" },
  { step: "4", title: "خطط",     desc: "خطة أسبوعية مخصصة حسب مادتك ونقاط ضعفك",       href: "/dashboard/learning-paths", btnLabel: "مسار شخصي" },
];

// ── Page ────────────────────────────────────────────────────────────────────────

export default function SecondarySchoolDashboardPage() {
  const summary = getSecondarySummary();

  return (
    <main className="mx-auto max-w-6xl space-y-8 p-6" dir="rtl">

      {/* Hero */}
      <section className="rounded-3xl border bg-gradient-to-br from-background to-muted/30 p-8 shadow-sm">
        <p className="text-sm font-medium text-muted-foreground">الثانوي والباكالوريا</p>
        <h1 className="mt-2 text-3xl font-bold tracking-tight">مركز الثانوي والباكالوريا</h1>
        <p className="mt-3 max-w-3xl text-muted-foreground leading-7">
          منصة تعليمية كاملة للمرحلة الثانوية — شرح عميق، تمارين بأسلوب الفروض والباكالوريا،
          خطط مراجعة ذكية، ودعم مخصص لجميع مواد المنهج المغربي.
        </p>
        <div className="mt-5 flex flex-wrap gap-2">
          {GRADES.map((g) => (
            <span key={g.key} className="rounded-xl bg-primary/10 px-3 py-1 text-sm font-medium text-primary">
              {g.label}
            </span>
          ))}
        </div>
      </section>

      {/* Stats */}
      <section className="grid gap-4 md:grid-cols-3">
        <div className="rounded-2xl border bg-background p-5">
          <p className="text-sm text-muted-foreground">الدروس المنظمة</p>
          <p className="mt-2 text-3xl font-bold">{summary.totalLessons}</p>
          <p className="mt-1 text-xs text-muted-foreground">عبر جميع المستويات والمواد</p>
        </div>
        <div className="rounded-2xl border bg-background p-5">
          <p className="text-sm text-muted-foreground">المستويات الدراسية</p>
          <p className="mt-2 text-3xl font-bold">{summary.grades.length}</p>
          <p className="mt-1 text-xs text-muted-foreground">جذع مشترك، أولى، وثانية باكالوريا</p>
        </div>
        <div className="rounded-2xl border bg-background p-5">
          <p className="text-sm text-muted-foreground">المواد الدراسية</p>
          <p className="mt-2 text-3xl font-bold">{summary.subjects.length}</p>
          <p className="mt-1 text-xs text-muted-foreground">من الرياضيات إلى الفلسفة</p>
        </div>
      </section>

      {/* Methodology */}
      <section>
        <h2 className="mb-4 text-xl font-bold">منهجية الدراسة للباكالوريا</h2>
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
          {METHODOLOGY_STEPS.map((m) => (
            <div key={m.step} className="flex flex-col gap-3 rounded-2xl border bg-background p-5">
              <div className="flex h-9 w-9 items-center justify-center rounded-full bg-primary/10 text-sm font-bold text-primary">
                {m.step}
              </div>
              <div>
                <p className="font-semibold">{m.title}</p>
                <p className="mt-1 text-xs leading-5 text-muted-foreground">{m.desc}</p>
              </div>
              <Link
                href={m.href}
                className="mt-auto inline-flex items-center justify-center rounded-xl bg-primary/10 px-3 py-2 text-xs font-medium text-primary transition-colors hover:bg-primary hover:text-white"
              >
                {m.btnLabel} ←
              </Link>
            </div>
          ))}
        </div>
      </section>

      {/* Subject sections */}
      <section>
        <h2 className="mb-4 text-xl font-bold">المواد الدراسية والمحاور الأساسية</h2>
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {SUBJECTS.map((subj) => (
            <div key={subj.key} className={`rounded-2xl border p-5 ${subj.color}`}>
              <div className="mb-3 flex items-center gap-2">
                <span className="text-xl">{subj.emoji}</span>
                <h3 className={`font-bold ${subj.titleColor}`}>{subj.label}</h3>
              </div>
              <ul className="mb-4 space-y-1.5">
                {subj.topics.map((topic) => (
                  <li key={topic} className="flex items-start gap-1.5 text-xs text-muted-foreground">
                    <span className="mt-0.5 text-primary">•</span>
                    {topic}
                  </li>
                ))}
              </ul>
              <div className="flex gap-2">
                <Link
                  href="/dashboard/leila"
                  className="flex-1 rounded-xl border border-current/20 bg-white/60 px-2 py-1.5 text-center text-xs font-medium transition-opacity hover:opacity-80"
                >
                  اسألي ليلى
                </Link>
                <Link
                  href="/dashboard/lesson-helper"
                  className="flex-1 rounded-xl border border-current/20 bg-white/60 px-2 py-1.5 text-center text-xs font-medium transition-opacity hover:opacity-80"
                >
                  درس كامل
                </Link>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Grade breakdown */}
      <section>
        <h2 className="mb-4 text-xl font-bold">حسب المستوى الدراسي</h2>
        <div className="grid gap-4 md:grid-cols-3">
          {GRADES.map((g) => {
            const count = summary.byGrade[g.key] ?? 0;
            return (
              <div key={g.key} className="rounded-2xl border bg-background p-5">
                <p className="text-xs font-semibold uppercase tracking-widest text-muted-foreground">{g.key}</p>
                <p className="mt-1 text-lg font-bold">{g.label}</p>
                <p className="mt-1 text-xs leading-5 text-muted-foreground">{g.note}</p>
                <p className="mt-3 text-2xl font-bold text-primary">{count}</p>
                <p className="text-xs text-muted-foreground">درس منظم</p>
                <Link
                  href="/dashboard/learning-paths"
                  className="mt-4 block rounded-xl bg-primary/10 px-3 py-2 text-center text-xs font-medium text-primary transition-colors hover:bg-primary hover:text-white"
                >
                  خطة مراجعة لـ {g.label} ←
                </Link>
              </div>
            );
          })}
        </div>
      </section>

      {/* BAC exam strategy callout */}
      <section className="rounded-3xl border border-amber-200 bg-amber-50 p-6">
        <div className="flex items-start gap-4">
          <span className="text-3xl">🎯</span>
          <div className="flex-1">
            <h2 className="font-bold text-amber-900">استراتيجية الباكالوريا</h2>
            <p className="mt-2 text-sm leading-7 text-amber-800">
              المصحح يُقيّم <strong>المنهجية</strong> قبل النتيجة — طالب بمنهجية صحيحة يأخذ 14/20
              حتى لو أخطأ في الحساب. استعمل الأدوات أعلاه لبناء منهجية قوية في كل مادة.
            </p>
            <div className="mt-4 flex flex-wrap gap-2 text-xs text-amber-800">
              {[
                "اكتب كل خطوة مع تبريرها",
                "اذكر القانون قبل التطبيق",
                "تحقق من الوحدات دائماً",
                "لا تترك سؤالاً فارغاً",
                "صغ الإشكالية بجملة استفهامية",
              ].map((tip) => (
                <span key={tip} className="rounded-lg border border-amber-300 bg-amber-100 px-2.5 py-1">
                  {tip}
                </span>
              ))}
            </div>
          </div>
        </div>
      </section>

    </main>
  );
}

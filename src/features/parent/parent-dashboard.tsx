"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { BarChart3, BookOpen, Flame, Trophy, AlertTriangle, ArrowLeft, CheckCircle, TrendingUp, TrendingDown, Minus } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Spinner } from "@/components/ui/spinner";
import { getLevelInfo } from "@/lib/gamification-level";

interface Child { id: string; name: string; xp: number; streak: number; grade?: { titleAr: string }; }
interface Summary { completedLessons: number; averageScore: number; weakPointCount: number; streakDays: number; xp: number; }
interface Rec { type: string; lessonId?: string; title: string; reason: string; }
interface ProgressItem {
  id: string; status: string; score?: number; completedAt?: string | null;
  lesson: { titleAr: string; unit: { subject: { titleAr: string; color?: string } } };
}

// ── Date helpers ──────────────────────────────────────────────────────────────
function daysAgo(n: number): Date {
  const d = new Date();
  d.setDate(d.getDate() - n);
  d.setHours(0, 0, 0, 0);
  return d;
}

function countCompleted(items: ProgressItem[], from: Date, to: Date): number {
  return items.filter((p) => {
    if (p.status !== "completed" || !p.completedAt) return false;
    const d = new Date(p.completedAt);
    return d >= from && d < to;
  }).length;
}

// ── Weekly comparison bar ─────────────────────────────────────────────────────
function WeeklyComparison({ lessons, childName }: { lessons: ProgressItem[]; childName: string }) {
  const now      = new Date(); now.setHours(23, 59, 59, 999);
  const todayStart = daysAgo(0);
  const weekStart  = daysAgo(6);
  const prevStart  = daysAgo(13);

  const thisWeek  = countCompleted(lessons, weekStart, now);
  const lastWeek  = countCompleted(lessons, prevStart, weekStart);
  const todayCount = countCompleted(lessons, todayStart, now);

  const delta  = thisWeek - lastWeek;
  const pct    = lastWeek === 0 ? null : Math.round(Math.abs(delta / lastWeek) * 100);
  const up     = delta > 0;
  const flat   = delta === 0;
  const TrendIcon = flat ? Minus : up ? TrendingUp : TrendingDown;
  const trendColor = flat ? "text-muted-foreground" : up ? "text-emerald-600" : "text-amber-600";
  const trendBg   = flat ? "bg-secondary"            : up ? "bg-emerald-50"   : "bg-amber-50";

  return (
    <div className="space-y-3">
      {/* Today activity notification */}
      {todayCount > 0 && (
        <div className="flex items-center gap-2.5 rounded-xl bg-emerald-50 border border-emerald-100 px-4 py-2.5">
          <span className="text-lg flex-shrink-0">🎉</span>
          <p className="text-sm font-semibold text-emerald-800">
            {childName} أكمل <strong>{todayCount} {todayCount === 1 ? "درس" : "دروس"}</strong> اليوم
          </p>
        </div>
      )}

      {/* Week-over-week comparison */}
      {(thisWeek > 0 || lastWeek > 0) && (
        <div className={`flex items-center justify-between gap-3 rounded-xl border px-4 py-3 ${trendBg}`}>
          <div className="flex items-center gap-4 text-sm">
            <div className="text-center">
              <p className="font-black text-xl text-foreground">{thisWeek}</p>
              <p className="text-xs text-muted-foreground">هذا الأسبوع</p>
            </div>
            <div className="text-muted-foreground text-xs">vs</div>
            <div className="text-center opacity-70">
              <p className="font-bold text-lg text-foreground">{lastWeek}</p>
              <p className="text-xs text-muted-foreground">الأسبوع الماضي</p>
            </div>
          </div>
          <div className={`flex items-center gap-1 font-bold text-sm ${trendColor}`}>
            <TrendIcon className="w-4 h-4" />
            {flat ? "نفس الوتيرة" : `${pct != null ? `${pct}%` : ""} ${up ? "↑" : "↓"}`}
          </div>
        </div>
      )}
    </div>
  );
}

// ── Unit completion badges ────────────────────────────────────────────────────
function UnitBadges({ lessons }: { lessons: ProgressItem[] }) {
  const unitMap = new Map<string, { subject: string; count: number }>();
  for (const p of lessons) {
    if (p.status !== "completed") continue;
    const subject = p.lesson?.unit?.subject?.titleAr ?? "";
    const key = subject;
    if (!unitMap.has(key)) unitMap.set(key, { subject, count: 0 });
    unitMap.get(key)!.count++;
  }

  const earned = Array.from(unitMap.values()).filter((u) => u.count >= 5);
  if (earned.length === 0) return null;

  return (
    <div>
      <h3 className="font-semibold text-sm mb-2 flex items-center gap-1.5">
        <Trophy className="w-4 h-4 text-amber-500" /> شارات الإنجاز
      </h3>
      <div className="flex flex-wrap gap-2">
        {earned.map((u) => (
          <div key={u.subject} className="flex items-center gap-1.5 rounded-full bg-amber-50 border border-amber-200 px-3 py-1.5">
            <span className="text-base">🏅</span>
            <span className="text-xs font-semibold text-amber-800">{u.count}+ دروس في {u.subject}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

// ── Recent lessons list ───────────────────────────────────────────────────────
function RecentLessons({ lessons }: { lessons: ProgressItem[] }) {
  const done = lessons
    .filter((p) => p.status === "completed")
    .sort((a, b) => (b.completedAt ?? "").localeCompare(a.completedAt ?? ""))
    .slice(0, 6);

  if (done.length === 0) return (
    <div className="rounded-xl bg-secondary/50 p-4 text-center text-sm text-muted-foreground">
      لم يُكمل طفلك أي درس بعد — شجّعه على أول خطوة 👋
    </div>
  );

  return (
    <div className="space-y-2">
      {done.map((item) => (
        <div key={item.id} className="flex items-center gap-3 rounded-xl border bg-card p-3">
          <div className="w-8 h-8 rounded-lg bg-emerald-50 flex items-center justify-center flex-shrink-0">
            <CheckCircle className="w-4 h-4 text-emerald-600" />
          </div>
          <div className="flex-1 min-w-0">
            <p className="text-sm font-medium truncate">{item.lesson?.titleAr}</p>
            <p className="text-xs text-muted-foreground truncate">{item.lesson?.unit?.subject?.titleAr}</p>
          </div>
          {item.score != null && (
            <span className="text-sm font-bold text-emerald-600 flex-shrink-0">{Math.round(item.score)}%</span>
          )}
        </div>
      ))}
    </div>
  );
}

// ── Main component ────────────────────────────────────────────────────────────
export function ParentDashboard() {
  const [children, setChildren]   = useState<Child[]>([]);
  const [summaries, setSummaries] = useState<Record<string, Summary>>({});
  const [recs, setRecs]           = useState<Record<string, Rec[]>>({});
  const [progress, setProgress]   = useState<Record<string, ProgressItem[]>>({});
  const [loading, setLoading]     = useState(true);

  useEffect(() => {
    fetch("/api/children")
      .then((r) => r.json())
      .then(async (d) => {
        if (!d.success) return;
        const kids: Child[] = d.data;
        setChildren(kids);

        const results = await Promise.all(kids.map(async (c) => {
          const [s, r, p] = await Promise.all([
            fetch(`/api/analytics/learning?childId=${c.id}`).then((x) => x.json()).catch(() => ({ data: null })),
            fetch(`/api/recommendations?childId=${c.id}`).then((x) => x.json()).catch(() => ({ data: [] })),
            fetch(`/api/progress?childId=${c.id}`).then((x) => x.json()).catch(() => ({ success: false, data: [] })),
          ]);
          return { id: c.id, summary: s.data, recs: r.data ?? [], progress: p.success ? (p.data ?? []) : [] };
        }));

        const sMap: Record<string, Summary>        = {};
        const rMap: Record<string, Rec[]>          = {};
        const pMap: Record<string, ProgressItem[]> = {};
        for (const r of results) { sMap[r.id] = r.summary; rMap[r.id] = r.recs; pMap[r.id] = r.progress; }
        setSummaries(sMap); setRecs(rMap); setProgress(pMap);
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div className="flex justify-center py-20"><Spinner className="w-8 h-8 text-primary" /></div>;

  return (
    <div className="max-w-4xl mx-auto space-y-6 animate-fade-in">
      <div>
        <h1 className="text-2xl font-bold flex items-center gap-2">👨‍👩‍👦 لوحة ولي الأمر</h1>
        <p className="text-muted-foreground text-sm">متابعة شاملة لتقدم أطفالك</p>
      </div>

      {children.length === 0 ? (
        <Card>
          <CardContent className="py-12 text-center space-y-3">
            <p className="text-4xl">👶</p>
            <p className="font-semibold">لم تُضف أي طفل بعد</p>
            <Link href="/onboarding">
              <button className="mt-2 rounded-xl bg-primary px-5 py-2 text-sm font-semibold text-white hover:bg-primary/90 transition-colors">
                أضف طفلاً الآن
              </button>
            </Link>
          </CardContent>
        </Card>
      ) : (
        children.map((child) => {
          const s   = summaries[child.id];
          const r   = recs[child.id] ?? [];
          const p   = progress[child.id] ?? [];
          const lvl = getLevelInfo(child.xp);

          return (
            <Card key={child.id} className="overflow-hidden">
              {/* Child header */}
              <div className="bg-gradient-to-l from-emerald-600 to-emerald-700 p-5 text-white">
                <div className="flex items-center justify-between gap-4">
                  <div className="flex items-center gap-3">
                    <div className="w-12 h-12 rounded-2xl bg-white/20 flex items-center justify-center text-2xl">🧒</div>
                    <div>
                      <h2 className="font-bold text-lg">{child.name}</h2>
                      <p className="text-emerald-200 text-sm">{child.grade?.titleAr ?? "لم يُحدد المستوى"}</p>
                    </div>
                  </div>
                  <div className="text-right">
                    <p className="text-emerald-200 text-xs">المستوى {lvl.level}</p>
                    <p className="font-bold">{lvl.title}</p>
                  </div>
                </div>
                <div className="mt-4">
                  <div className="flex justify-between text-xs text-emerald-200 mb-1">
                    <span>{child.xp} نقطة</span>
                    <span>{lvl.xpToNext} للمستوى التالي</span>
                  </div>
                  <div className="h-2 bg-white/20 rounded-full overflow-hidden">
                    <div className="h-full bg-amber-400 rounded-full transition-all" style={{ width: `${lvl.progress}%` }} />
                  </div>
                </div>
              </div>

              <CardContent className="p-5 space-y-5">
                {/* Weekly comparison + today notification */}
                <WeeklyComparison lessons={p} childName={child.name} />

                {/* All-time stats */}
                {s && (
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                    {[
                      { icon: BookOpen,      label: "إجمالي الدروس",  value: s.completedLessons,  color: "text-blue-600 bg-blue-50" },
                      { icon: BarChart3,     label: "متوسط النتيجة",  value: `${s.averageScore}%`, color: s.averageScore >= 70 ? "text-emerald-600 bg-emerald-50" : "text-amber-600 bg-amber-50" },
                      { icon: Flame,         label: "أيام متتالية",   value: `${child.streak} يوم`, color: "text-orange-600 bg-orange-50" },
                      { icon: AlertTriangle, label: "نقاط ضعيفة",    value: s.weakPointCount,    color: s.weakPointCount > 0 ? "text-red-600 bg-red-50" : "text-emerald-600 bg-emerald-50" },
                    ].map(({ icon: Icon, label, value, color }) => (
                      <div key={label} className={`p-3 rounded-xl ${color.split(" ")[1]} flex items-center gap-2`}>
                        <Icon className={`w-5 h-5 ${color.split(" ")[0]} flex-shrink-0`} />
                        <div>
                          <p className="font-bold text-sm text-foreground">{value}</p>
                          <p className="text-xs text-muted-foreground">{label}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                )}

                {/* Unit achievement badges */}
                <UnitBadges lessons={p} />

                {/* Recently completed lessons */}
                <div>
                  <h3 className="font-semibold text-sm mb-2 flex items-center gap-1.5">
                    <CheckCircle className="w-4 h-4 text-emerald-600" />
                    آخر الدروس المكتملة
                  </h3>
                  <RecentLessons lessons={p} />
                </div>

                {/* Recommendations */}
                {r.length > 0 && (
                  <div>
                    <h3 className="font-semibold text-sm mb-2 flex items-center gap-1.5">
                      <Trophy className="w-4 h-4 text-amber-500" /> توصيات هذا الأسبوع
                    </h3>
                    <div className="space-y-2">
                      {r.slice(0, 3).map((rec, i) => (
                        <Link key={i} href={rec.lessonId ? `/dashboard/lessons/${rec.lessonId}` : "/dashboard/lessons"}>
                          <div className="flex items-center gap-2 p-2.5 rounded-lg hover:bg-secondary transition-colors">
                            <span className="text-lg">{rec.type === "review" ? "🔄" : rec.type === "quiz" ? "✏️" : "📚"}</span>
                            <div className="flex-1 min-w-0">
                              <p className="text-sm font-medium truncate">{rec.title}</p>
                              <p className="text-xs text-muted-foreground truncate">{rec.reason}</p>
                            </div>
                            <ArrowLeft className="w-3.5 h-3.5 text-muted-foreground flex-shrink-0" />
                          </div>
                        </Link>
                      ))}
                    </div>
                  </div>
                )}

                {/* Performance insight */}
                {s && (
                  <div className={`p-3 rounded-xl text-sm border ${
                    s.averageScore >= 75 ? "bg-emerald-50 border-emerald-200 text-emerald-800"
                    : s.averageScore >= 50 ? "bg-amber-50 border-amber-200 text-amber-800"
                    : "bg-red-50 border-red-200 text-red-800"
                  }`}>
                    {s.averageScore >= 75
                      ? `${child.name} يُبلي بلاءً حسنًا! معدل ${s.averageScore}% ممتاز. استمروا هكذا! 🌟`
                      : s.averageScore >= 50
                      ? `${child.name} يتحسن. نوصي بمراجعة الدروس الصعبة مع ليلى يوميًا.`
                      : `${child.name} يحتاج دعمًا. المعدل ${s.averageScore}% — ننصح بجلسة يومية منتظمة.`}
                  </div>
                )}
              </CardContent>
            </Card>
          );
        })
      )}
    </div>
  );
}

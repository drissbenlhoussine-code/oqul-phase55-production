"use client";
/**
 * StudentDashboard — Phase 32
 * Replaces: src/features/dashboard/student-dashboard.tsx
 *
 * Changes:
 * - Replaced <Spinner> with <DashboardSkeleton> on first load
 * - Added fetch error state with retry
 * - Improved empty-state copy
 * - No logic changes
 */
import { useEffect, useState } from "react";
import Link from "next/link";
import { BookOpen, Sparkles, BarChart3, ArrowLeft, Trophy, AlertCircle, RefreshCcw } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { DashboardSkeleton } from "./dashboard-skeleton";
import { DailyGreeting }     from "./daily-greeting";
import { DailyLoop }         from "@/features/learning/daily-loop";
import { LeilaWelcome }      from "@/features/engagement/leila-welcome";
import { MilestoneAlert }    from "@/features/engagement/milestone-alert";
import { GettingStarted }    from "@/features/engagement/getting-started";
import { LearningWorldCard } from "@/features/learning-experience/learning-world-card";
import { MiddleSchoolIntelligenceCard } from "@/features/middle-school/middle-school-intelligence-card";

interface Child        { id: string; name: string; xp: number; streak: number; grade?: { titleAr: string }; }
interface Summary      { completedLessons: number; averageScore: number; weakPointCount: number; streakDays: number; xp: number; }
interface Rec          { type: string; lessonId?: string; title: string; reason: string; }
interface ProgressItem { status: string; lesson?: { titleAr: string }; }

export function StudentDashboard() {
  const [child,    setChild]    = useState<Child | null>(null);
  const [summary,  setSummary]  = useState<Summary | null>(null);
  const [recs,     setRecs]     = useState<Rec[]>([]);
  const [progress, setProgress] = useState<ProgressItem[]>([]);
  const [loading,  setLoading]  = useState(true);
  const [error,    setError]    = useState(false);

  const safeJson = (url: string) =>
    fetch(url, { signal: AbortSignal.timeout(8000) })
      .then((r) => r.json())
      .catch(() => ({ success: false, data: null }));

  async function load() {
    setLoading(true);
    setError(false);
    try {
      const d = await safeJson("/api/children");
      if (!d.success || !d.data?.[0]) { setLoading(false); return; }
      const c = d.data[0] as Child;
      setChild(c);

      const [sumRes, recRes, adaptiveRes, progRes] = await Promise.all([
        safeJson(`/api/analytics/learning?childId=${c.id}`),
        safeJson(`/api/recommendations?childId=${c.id}`),
        safeJson(`/api/adaptive?childId=${c.id}`),
        safeJson(`/api/progress?childId=${c.id}`),
      ]);

      if (sumRes.success)  setSummary(sumRes.data);
      if (progRes.success) setProgress(progRes.data ?? []);

      if (adaptiveRes.success && adaptiveRes.data?.actions?.length > 0) {
        setRecs(adaptiveRes.data.actions.map((a: { type: string; lessonId?: string; lessonTitle?: string; topic?: string; reason: string; }) => ({
          type:     a.type === "review_lesson" ? "review" : a.type === "practice_quiz" ? "quiz" : "lesson",
          lessonId: a.lessonId,
          title:    a.lessonTitle ?? a.topic ?? "توصية ليلى",
          reason:   a.reason,
        })));
      } else if (recRes.success) {
        setRecs(recRes.data ?? []);
      }
    } catch {
      setError(true);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => { load(); }, []);

  // ── Loading ────────────────────────────────────────────────────────────────
  if (loading) return <DashboardSkeleton />;

  // ── Error ──────────────────────────────────────────────────────────────────
  if (error) return (
    <div className="max-w-3xl mx-auto">
      <Card>
        <CardContent className="py-16 text-center space-y-4">
          <div className="text-5xl">😕</div>
          <p className="font-semibold text-lg">تعذّر تحميل لوحة التحكم</p>
          <p className="text-sm text-muted-foreground">تحقق من اتصالك بالإنترنت وحاول مجدداً.</p>
          <button
            onClick={load}
            className="inline-flex items-center gap-2 rounded-xl bg-primary px-5 py-2.5 text-sm font-semibold text-white hover:bg-primary/90 transition"
          >
            <RefreshCcw className="h-4 w-4" />
            أعد المحاولة
          </button>
        </CardContent>
      </Card>
    </div>
  );

  const needsReview    = progress.filter((p) => p.status === "needs_review");
  const completedToday = progress.filter((p) => p.status === "completed").length;
  const recIcons: Record<string, string> = { lesson: "📚", review: "🔄", quiz: "✏️" };

  return (
    <div className="max-w-3xl mx-auto space-y-4 animate-fade-in">

      {child && (
        <LeilaWelcome
          childName={child.name}
          streak={child.streak}
          avgScore={summary?.averageScore}
          completedToday={completedToday}
        />
      )}

      <DailyGreeting
        childName={child?.name}
        xp={child?.xp}
        streak={child?.streak}
        completedToday={completedToday}
      />

      {child && <LearningWorldCard childId={child.id} />}

      {child && <MiddleSchoolIntelligenceCard childId={child.id} />}

      {child && progress.length === 0 ? (
        <GettingStarted childName={child.name} gradeName={child.grade?.titleAr} />
      ) : child ? (
        <DailyLoop childId={child.id} streak={child.streak} />
      ) : null}

      {needsReview.length > 0 && (
        <div className="flex items-start gap-3 bg-amber-50 border border-amber-200 rounded-xl p-4">
          <AlertCircle className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" />
          <div className="flex-1 min-w-0">
            <p className="text-sm font-semibold text-amber-800">
              {needsReview.length} درس {needsReview.length === 1 ? "يحتاج" : "يحتاجون"} مراجعة
            </p>
            <p className="text-xs text-amber-700 mt-0.5">ليلى تنصح بمراجعتها لتثبيت المعلومات</p>
          </div>
          <Link href="/dashboard/lessons">
            <button className="text-xs text-amber-700 font-semibold hover:underline flex-shrink-0">راجع الآن</button>
          </Link>
        </div>
      )}

      <div className="grid grid-cols-3 gap-3">
        {[
          { href: "/dashboard/lessons", icon: BookOpen, label: "الدروس",  sub: `${summary?.completedLessons ?? 0} مكتمل`,    color: "bg-emerald-50 text-emerald-700" },
          { href: "/dashboard/leila",   icon: Sparkles,  label: "ليلى",    sub: "اسألني أي شيء",                              color: "bg-blue-50 text-blue-700" },
          { href: "/dashboard/progress",icon: BarChart3,  label: "تقدمي",  sub: `${summary?.averageScore ?? 0}% معدل`,        color: "bg-amber-50 text-amber-700" },
        ].map(({ href, icon: Icon, label, sub, color }) => (
          <Link key={href} href={href}>
            <Card className="hover:shadow-md transition-all hover:-translate-y-0.5 cursor-pointer h-full">
              <CardContent className="p-4 text-center space-y-2">
                <div className={`w-10 h-10 rounded-xl flex items-center justify-center mx-auto ${color}`}>
                  <Icon className="w-5 h-5" />
                </div>
                <p className="text-sm font-semibold">{label}</p>
                <p className="text-xs text-muted-foreground">{sub}</p>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>

      {recs.length > 0 && (
        <div>
          <h2 className="font-semibold text-sm mb-2 flex items-center gap-2">
            <Trophy className="w-4 h-4 text-amber-500" />
            ليلى توصيك بـ:
          </h2>
          <div className="space-y-2">
            {recs.slice(0, 3).map((rec, i) => (
              <Link key={i} href={rec.lessonId ? `/dashboard/lessons/${rec.lessonId}` : "/dashboard/lessons"}>
                <Card className="hover:shadow-md transition-all hover:-translate-y-0.5 cursor-pointer">
                  <CardContent className="p-4 flex items-center gap-3">
                    <span className="text-xl flex-shrink-0">{recIcons[rec.type] ?? "📖"}</span>
                    <div className="flex-1 min-w-0">
                      <p className="text-sm font-medium truncate">{rec.title}</p>
                      <p className="text-xs text-muted-foreground truncate">{rec.reason}</p>
                    </div>
                    <ArrowLeft className="w-4 h-4 text-muted-foreground flex-shrink-0" />
                  </CardContent>
                </Card>
              </Link>
            ))}
          </div>
        </div>
      )}

      {!child && !loading && (
        <Card>
          <CardContent className="py-16 text-center space-y-4">
            <div className="text-6xl">🎒</div>
            <p className="font-semibold text-xl">أهلاً بك في عقول!</p>
            <p className="text-muted-foreground text-sm max-w-xs mx-auto leading-7">
              ابدأ بإضافة طفلك ليبدأ رحلته التعليمية مع أستاذة ليلى.
            </p>
            <Link href="/onboarding">
              <button className="bg-primary text-white px-7 py-3 rounded-xl text-sm font-semibold hover:bg-primary/90 transition-colors">
                أضف طفلك الآن 👶
              </button>
            </Link>
          </CardContent>
        </Card>
      )}

      {child && (
        <MilestoneAlert
          streak={child.streak}
          xp={child.xp}
          completed={summary?.completedLessons ?? 0}
        />
      )}
    </div>
  );
}

"use client";
import { useEffect, useState } from "react";
import { BookOpen, CheckCircle, BarChart3, Flame } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Spinner } from "@/components/ui/spinner";
import { getLevelInfo } from "@/lib/gamification-level";
import { StreakCalendar } from "@/features/gamification/streak-calendar";
import { MasteryMap } from "@/features/gamification/mastery-map";

interface Child { id: string; name: string; xp: number; streak: number; }
interface ProgressItem {
  id: string; status: string; score?: number;
  lesson: { titleAr: string; unit: { subject: { titleAr: string; color: string; icon: string } } };
}
interface ChildBadge { id: string; badge: { titleAr: string; icon: string }; earnedAt: string; }

export default function ProgressPage() {
  const [child,    setChild]    = useState<Child | null>(null);
  const [progress, setProgress] = useState<ProgressItem[]>([]);
  const [badges,   setBadges]   = useState<ChildBadge[]>([]);
  const [loading,  setLoading]  = useState(true);

  useEffect(() => {
    const safeJson = (url: string) =>
      fetch(url, { signal: AbortSignal.timeout(8000) })
        .then((r) => r.json())
        .catch(() => ({ success: false }));

    safeJson("/api/children").then(async (d) => {
      if (!d.success || !d.data?.[0]) return;
      const c: Child = d.data[0];
      setChild(c);
      const [pr, bg] = await Promise.all([
        safeJson(`/api/progress?childId=${c.id}`),
        safeJson(`/api/children/badges?childId=${c.id}`),
      ]);
      if (pr.success) setProgress(pr.data);
      if (bg.success) setBadges(bg.data);
    }).finally(() => setLoading(false));
  }, []);

  if (loading) return <div className="flex justify-center py-20"><Spinner className="w-8 h-8 text-primary" /></div>;

  const lvl       = child ? getLevelInfo(child.xp) : null;
  const completed = progress.filter((p) => p.status === "completed").length;
  const scores    = progress.filter((p) => p.score != null).map((p) => p.score!);
  const avgScore  = scores.length ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : 0;

  // Build mastery data per subject
  const subjectMap = new Map<string, { subject: ProgressItem["lesson"]["unit"]["subject"]; completed: number; total: number; scores: number[] }>();
  for (const item of progress) {
    const sub = item.lesson?.unit?.subject;
    if (!sub) continue;
    if (!subjectMap.has(sub.titleAr)) subjectMap.set(sub.titleAr, { subject: sub, completed: 0, total: 0, scores: [] });
    const entry = subjectMap.get(sub.titleAr)!;
    entry.total++;
    if (item.status === "completed") { entry.completed++; if (item.score != null) entry.scores.push(item.score); }
  }
  const masteryData = Array.from(subjectMap.values()).map(({ subject, completed, total, scores }) => ({
    subject: { titleAr: subject.titleAr, color: subject.color ?? "#059669", icon: subject.icon ?? "📚" },
    completedLessons: completed, totalLessons: total,
    avgScore: scores.length ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : 0,
    weakPointCount: 0,
  }));

  const statusMap  = { completed: "مكتمل", in_progress: "قيد التقدم", not_started: "لم يبدأ", needs_review: "مراجعة" };
  const variantMap: Record<string, "success" | "warning" | "default" | "secondary"> = {
    completed: "success", in_progress: "default", not_started: "secondary", needs_review: "warning",
  };

  return (
    <div className="max-w-4xl mx-auto space-y-5 animate-fade-in">
      <div>
        <h1 className="text-2xl font-bold">
          {child ? `تقدم ${child.name}` : "التقدم"}
        </h1>
        <p className="text-muted-foreground text-sm">
          {child ? `متابعة إنجازات ${child.name} ومستواه` : "تتبع تقدم طفلك"}
        </p>
      </div>

      {/* Level card */}
      {lvl && child && (
        <Card className="bg-gradient-to-l from-emerald-600 to-emerald-700 text-white border-0 shadow-md">
          <CardContent className="p-5">
            <div className="flex items-center justify-between mb-3">
              <div>
                <p className="text-emerald-200 text-xs">المستوى {lvl.level}</p>
                <p className="text-xl font-bold">{lvl.title}</p>
              </div>
              <div className="text-right">
                <p className="text-3xl font-black">{child.xp}</p>
                <p className="text-emerald-200 text-xs">نقطة مكتسبة</p>
              </div>
            </div>
            <div className="space-y-1">
              <div className="flex justify-between text-xs text-emerald-200">
                <span>التقدم للمستوى التالي</span><span>{lvl.xpToNext} نقطة</span>
              </div>
              <div className="h-2.5 bg-white/20 rounded-full overflow-hidden">
                <div className="h-full bg-amber-400 rounded-full transition-all duration-700" style={{ width: `${lvl.progress}%` }} />
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Stats row */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        {[
          { icon: CheckCircle, label: "مكتملة",   value: completed,                    color: "text-emerald-600 bg-emerald-50" },
          { icon: BookOpen,    label: "الكل",      value: progress.length,              color: "text-blue-600 bg-blue-50" },
          { icon: BarChart3,   label: "المعدل",    value: `${avgScore}%`,               color: "text-amber-600 bg-amber-50" },
          { icon: Flame,       label: "السلسلة",   value: `${child?.streak ?? 0} يوم`,  color: "text-orange-600 bg-orange-50" },
        ].map(({ icon: Icon, label, value, color }) => (
          <Card key={label}>
            <CardContent className="p-4 flex items-center gap-3">
              <div className={`w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 ${color}`}>
                <Icon className="w-4 h-4" />
              </div>
              <div><p className="font-bold">{value}</p><p className="text-xs text-muted-foreground">{label}</p></div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Streak calendar + Mastery map */}
      <div className="grid md:grid-cols-2 gap-4">
        <StreakCalendar streak={child?.streak ?? 0} xp={child?.xp ?? 0} />
        <MasteryMap data={masteryData} />
      </div>

      {/* Badges */}
      {badges.length > 0 && (
        <Card>
          <CardHeader><CardTitle className="text-base">🏅 الإنجازات ({badges.length})</CardTitle></CardHeader>
          <CardContent>
            <div className="flex flex-wrap gap-2">
              {badges.map((cb) => (
                <div key={cb.id} className="flex items-center gap-2 bg-amber-50 border border-amber-200 px-3 py-2 rounded-xl">
                  <span className="text-lg">{cb.badge.icon}</span>
                  <span className="text-sm font-medium text-amber-800">{cb.badge.titleAr}</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Lesson list */}
      <div className="space-y-2">
        <h2 className="font-semibold text-sm text-muted-foreground">سجل الدروس</h2>
        {progress.length === 0 ? (
          <Card><CardContent className="py-8 text-center text-muted-foreground text-sm">لم تبدأ أي درس بعد</CardContent></Card>
        ) : (
          progress.slice(0, 15).map((item) => (
            <Card key={item.id}>
              <CardContent className="p-4 flex items-center justify-between gap-3">
                <div className="flex items-center gap-3 min-w-0">
                  <div className="w-8 h-8 rounded-lg bg-primary/10 flex items-center justify-center flex-shrink-0">
                    <BookOpen className="w-4 h-4 text-primary" />
                  </div>
                  <div className="min-w-0">
                    <p className="text-sm font-medium truncate">{item.lesson?.titleAr}</p>
                    <p className="text-xs text-muted-foreground truncate">{item.lesson?.unit?.subject?.titleAr}</p>
                  </div>
                </div>
                <div className="flex items-center gap-2 flex-shrink-0">
                  {item.score != null && <span className="text-sm font-bold text-primary">{Math.round(item.score)}%</span>}
                  <Badge variant={variantMap[item.status] ?? "secondary"}>
                    {statusMap[item.status as keyof typeof statusMap] ?? item.status}
                  </Badge>
                </div>
              </CardContent>
            </Card>
          ))
        )}
      </div>
    </div>
  );
}

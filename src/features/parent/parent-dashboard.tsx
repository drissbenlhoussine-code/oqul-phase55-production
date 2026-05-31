"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { BarChart3, BookOpen, Clock, Star, Flame, Trophy, AlertTriangle, ArrowLeft } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Spinner } from "@/components/ui/spinner";
import { getLevelInfo } from "@/lib/gamification-level";

interface Child { id: string; name: string; xp: number; streak: number; grade?: { titleAr: string }; }
interface Summary { completedLessons: number; averageScore: number; weakPointCount: number; streakDays: number; xp: number; }
interface Rec { type: string; lessonId?: string; title: string; reason: string; }

export function ParentDashboard() {
  const [children, setChildren]     = useState<Child[]>([]);
  const [summaries, setSummaries]   = useState<Record<string, Summary>>({});
  const [recs, setRecs]             = useState<Record<string, Rec[]>>({});
  const [loading, setLoading]       = useState(true);

  useEffect(() => {
    fetch("/api/children")
      .then((r) => r.json())
      .then(async (d) => {
        if (!d.success) return;
        const kids: Child[] = d.data;
        setChildren(kids);

        const results = await Promise.all(kids.map(async (c) => {
          const [s, r] = await Promise.all([
            fetch(`/api/analytics/learning?childId=${c.id}`).then((x) => x.json()),
            fetch(`/api/recommendations?childId=${c.id}`).then((x) => x.json()),
          ]);
          return { id: c.id, summary: s.data, recs: r.data ?? [] };
        }));

        const sMap: Record<string, Summary> = {};
        const rMap: Record<string, Rec[]>   = {};
        for (const r of results) { sMap[r.id] = r.summary; rMap[r.id] = r.recs; }
        setSummaries(sMap); setRecs(rMap);
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
        <Card><CardContent className="py-12 text-center"><p className="text-muted-foreground">لم تُضف أي طفل بعد</p></CardContent></Card>
      ) : (
        children.map((child) => {
          const s    = summaries[child.id];
          const r    = recs[child.id] ?? [];
          const lvl  = getLevelInfo(child.xp);

          return (
            <Card key={child.id} className="overflow-hidden">
              {/* Child header */}
              <div className="bg-gradient-to-l from-emerald-600 to-emerald-700 p-5 text-white">
                <div className="flex items-center justify-between gap-4">
                  <div className="flex items-center gap-3">
                    <div className="w-12 h-12 rounded-2xl bg-white/20 flex items-center justify-center text-2xl">👦</div>
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

                {/* XP bar */}
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
                {/* Stats */}
                {s && (
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                    {[
                      { icon: BookOpen, label: "دروس مكتملة", value: s.completedLessons,  color: "text-blue-600 bg-blue-50" },
                      { icon: BarChart3, label: "متوسط النتيجة", value: `${s.averageScore}%`, color: s.averageScore >= 70 ? "text-emerald-600 bg-emerald-50" : "text-amber-600 bg-amber-50" },
                      { icon: Flame,    label: "أيام متتالية",  value: `${child.streak} يوم`, color: "text-orange-600 bg-orange-50" },
                      { icon: AlertTriangle, label: "نقاط ضعيفة", value: s.weakPointCount, color: s.weakPointCount > 0 ? "text-red-600 bg-red-50" : "text-emerald-600 bg-emerald-50" },
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

                {/* Recommendations */}
                {r.length > 0 && (
                  <div>
                    <h3 className="font-semibold text-sm mb-2 flex items-center gap-1.5"><Trophy className="w-4 h-4 text-amber-500" /> توصيات هذا الأسبوع</h3>
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
                  <div className={`p-3 rounded-xl text-sm border ${s.averageScore >= 75 ? "bg-emerald-50 border-emerald-200 text-emerald-800" : s.averageScore >= 50 ? "bg-amber-50 border-amber-200 text-amber-800" : "bg-red-50 border-red-200 text-red-800"}`}>
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

"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Sparkles, Flame, BookOpen, Trophy } from "lucide-react";
import { getLevelInfo } from "@/lib/gamification-level";

interface GreetingProps {
  childName?: string;
  xp?: number;
  streak?: number;
  completedToday?: number;
}

function getTimeGreeting(): string {
  const h = new Date().getHours();
  if (h < 12) return "صباح النور";
  if (h < 17) return "مساء الخير";
  return "مساء النور";
}

function getLeilaMessage(streak: number, completedToday: number, avgScore: number): string {
  if (completedToday === 0 && streak > 0) {
    return `سلام! لا تنسى تحافظ على سلسلتك — ${streak} أيام متتالية! درس واحد كافٍ اليوم 💪`;
  }
  if (completedToday > 0) {
    return `ممتاز! كملتي ${completedToday} درس اليوم. باقي اليوم عندك وقت لمزيد 🌟`;
  }
  if (avgScore < 60) {
    return `واش نبدأ بمراجعة الدروس اللي فيها صعوبة؟ ليلى هنا تساعدك! 🤝`;
  }
  return `مرحباً! أنا مستعدة لمساعدتك في أي درس تختاره اليوم 📚`;
}

export function DailyGreeting({ childName, xp = 0, streak = 0, completedToday = 0 }: GreetingProps) {
  const [mounted, setMounted] = useState(false);
  const [intelligence, setIntelligence] = useState<{
    message?: string; pace?: string; maxMinutes?: number;
  } | null>(null);

  useEffect(() => setMounted(true), []);

  useEffect(() => {
    if (!mounted) return;
    // Fetch cognitive intelligence async — non-blocking
    fetch("/api/children")
      .then((r) => r.json())
      .then(async (d) => {
        if (!d.success || !d.data?.[0]) return;
        const res = await fetch("/api/ai/living-leila", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ childId: d.data[0].id }),
        }).then((r) => r.json()).catch(() => null);
        if (res?.success) {
          setIntelligence({
            message:    res.data?.sessionRecommendation?.message,
            pace:       res.data?.sessionRecommendation?.pace,
            maxMinutes: res.data?.sessionRecommendation?.maxMinutes,
          });
        }
      }).catch(() => {});
  }, [mounted]);

  if (!mounted) return null;

  const greeting  = getTimeGreeting();
  const lvl       = getLevelInfo(xp);
  const message   = getLeilaMessage(streak, completedToday, 70);

  return (
    <div className="rounded-2xl bg-gradient-to-l from-emerald-600 via-emerald-700 to-emerald-800 p-6 text-white shadow-lg">
      <div className="flex items-start justify-between gap-4">
        <div className="space-y-1 flex-1 min-w-0">
          <p className="text-emerald-200 text-sm">{greeting} ☀️</p>
          <h1 className="text-2xl font-bold truncate">
            {childName ? `${childName}!` : "أهلاً بك!"}
          </h1>
          <p className="text-emerald-100 text-sm font-medium">
            {lvl.title} · المستوى {lvl.level}
          </p>
        </div>
        <div className="w-14 h-14 rounded-2xl bg-white/20 flex items-center justify-center flex-shrink-0">
          <Sparkles className="w-7 h-7 text-white" />
        </div>
      </div>

      {/* XP Progress */}
      <div className="mt-4 space-y-1.5">
        <div className="flex justify-between text-xs text-emerald-200">
          <span>{xp} XP</span>
          <span>{lvl.xpToNext} للمستوى {lvl.level + 1}</span>
        </div>
        <div className="h-2 bg-white/20 rounded-full overflow-hidden">
          <div
            className="h-full bg-amber-400 rounded-full transition-all duration-700"
            style={{ width: `${lvl.progress}%` }}
          />
        </div>
      </div>

      {/* Leila message */}
      <div className="mt-4 bg-white/15 rounded-xl p-3 text-sm">
        <p className="text-white/90">ليلى: {message}</p>
      </div>

      {/* Quick stats */}
      <div className="mt-4 flex gap-2 flex-wrap">
        {streak > 0 && (
          <span className="flex items-center gap-1 bg-white/20 px-3 py-1.5 rounded-full text-xs font-medium">
            <Flame className="w-3.5 h-3.5 text-orange-300" /> {streak} أيام متتالية
          </span>
        )}
        {completedToday > 0 && (
          <span className="flex items-center gap-1 bg-white/20 px-3 py-1.5 rounded-full text-xs font-medium">
            <BookOpen className="w-3.5 h-3.5 text-blue-300" /> {completedToday} درس اليوم
          </span>
        )}
        <Link href="/dashboard/progress">
          <span className="flex items-center gap-1 bg-white/20 hover:bg-white/30 transition-colors px-3 py-1.5 rounded-full text-xs font-medium cursor-pointer">
            <Trophy className="w-3.5 h-3.5 text-amber-300" /> إنجازاتي
          </span>
        </Link>
      </div>
    </div>
  );
}

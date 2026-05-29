"use client";

import { useMemo } from "react";

interface StreakCalendarProps {
  streak:    number;
  xp:        number;
  className?: string;
}

export function StreakCalendar({ streak, xp, className = "" }: StreakCalendarProps) {
  // Build last 21 days (3 weeks)
  const days = useMemo(() => {
    const result = [];
    const today  = new Date();
    for (let i = 20; i >= 0; i--) {
      const d     = new Date(today);
      d.setDate(today.getDate() - i);
      const isActive = i < streak; // streak days are "active"
      const isToday  = i === 0;
      result.push({ date: d, isActive, isToday, dayNum: d.getDate(), dayName: d.toLocaleDateString("ar-MA", { weekday: "short" }) });
    }
    return result;
  }, [streak]);

  const WEEKDAYS = ["أ", "ا", "ث", "ر", "خ", "ج", "س"];

  return (
    <div className={`rounded-2xl border bg-card p-5 space-y-4 ${className}`}>
      <div className="flex items-center justify-between">
        <div>
          <h3 className="font-bold">سجل الأيام 🔥</h3>
          <p className="text-xs text-muted-foreground">{streak} أيام متتالية</p>
        </div>
        <div className="text-left">
          <p className="text-2xl font-black text-primary">{streak}</p>
          <p className="text-xs text-muted-foreground">يوم</p>
        </div>
      </div>

      {/* Calendar grid — 3 rows of 7 */}
      <div className="grid grid-cols-7 gap-1.5">
        {WEEKDAYS.map((d) => (
          <div key={d} className="text-center text-xs text-muted-foreground font-medium py-0.5">{d}</div>
        ))}
        {days.map((d, i) => (
          <div
            key={i}
            title={d.date.toLocaleDateString("ar-MA")}
            className={`
              aspect-square rounded-lg flex items-center justify-center text-xs font-bold transition-all
              ${d.isToday
                ? "ring-2 ring-primary ring-offset-1"
                : ""}
              ${d.isActive
                ? "bg-primary text-white shadow-sm"
                : "bg-secondary text-muted-foreground"}
            `}
          >
            {d.isActive ? "✓" : d.dayNum}
          </div>
        ))}
      </div>

      {/* Milestone next */}
      {streak > 0 && streak < 30 && (
        <div className="bg-amber-50 rounded-xl px-3 py-2 flex items-center gap-2">
          <span className="text-lg">{streak >= 7 ? "🏆" : streak >= 3 ? "🔥" : "⭐"}</span>
          <div className="flex-1 min-w-0">
            <p className="text-xs font-semibold text-amber-800">
              {streak < 3 ? `${3 - streak} أيام للشارة الأولى!` :
               streak < 7 ? `${7 - streak} أيام لشارة الأسبوع!` :
               streak < 30 ? `${30 - streak} يوم لشارة الشهر 👑` : ""}
            </p>
            <div className="mt-1 h-1.5 bg-amber-100 rounded-full overflow-hidden">
              <div
                className="h-full bg-amber-400 rounded-full transition-all"
                style={{ width: `${streak < 3 ? (streak/3)*100 : streak < 7 ? (streak/7)*100 : (streak/30)*100}%` }}
              />
            </div>
          </div>
        </div>
      )}

      {streak === 0 && (
        <div className="text-center py-2 space-y-1">
          <p className="text-2xl">🌱</p>
          <p className="text-sm text-muted-foreground">ابدأ اليوم وابنِ سلسلتك!</p>
        </div>
      )}
    </div>
  );
}

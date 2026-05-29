"use client";

/**
 * Daily Learning Loop
 * The most critical retention feature — gives the child ONE clear thing to do today.
 * Shown prominently on the dashboard every day.
 *
 * Design principles:
 * - One clear action (not a list)
 * - Estimated time is always short (5-10 min)
 * - Celebrates streak momentum
 * - Changes daily to feel fresh
 */

import { useEffect, useState } from "react";
import Link from "next/link";
import { Clock, Flame, Star, ChevronLeft, CheckCircle } from "lucide-react";
import { Spinner } from "@/components/ui/spinner";

interface DailyAction {
  type:        "lesson" | "review" | "quiz" | "leila";
  lessonId?:   string;
  title:       string;
  description: string;
  estimatedMin: number;
  xpReward:    number;
  urgency:     "high" | "medium" | "low";
  emoji:       string;
}

interface DailyLoopProps {
  childId: string;
  streak:  number;
}

export function DailyLoop({ childId, streak }: DailyLoopProps) {
  const [action,  setAction]  = useState<DailyAction | null>(null);
  const [done,    setDone]    = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Get today's recommended action from adaptive engine
    fetch(`/api/adaptive?childId=${childId}`)
      .then((r) => r.json())
      .then((d) => {
        if (!d.success || !d.data?.actions?.length) return;

        const actions = d.data.actions;
        const first   = actions[0];

        // Map adaptive engine action to daily action
        const daily: DailyAction = {
          type:         first.type === "review_lesson" ? "review" :
                        first.type === "practice_quiz" ? "quiz" :
                        first.type === "ask_leila"     ? "leila" : "lesson",
          lessonId:     first.lessonId,
          title:        first.lessonTitle ?? first.topic ?? "درس اليوم",
          description:  first.reason,
          estimatedMin: first.type === "review_lesson" ? 5 : first.type === "ask_leila" ? 3 : 10,
          xpReward:     first.urgency === "high" ? 40 : first.urgency === "medium" ? 25 : 15,
          urgency:      first.urgency ?? "medium",
          emoji:        first.type === "review_lesson" ? "🔄" :
                        first.type === "practice_quiz" ? "✏️" :
                        first.type === "ask_leila"     ? "🤖" : "📚",
        };
        setAction(daily);
      })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [childId]);

  if (loading) return (
    <div className="rounded-2xl border bg-card p-5 flex items-center gap-3">
      <Spinner className="w-5 h-5 text-primary" />
      <p className="text-sm text-muted-foreground">ليلى تختار درس اليوم...</p>
    </div>
  );

  if (!action) return null;

  const href = action.lessonId
    ? (action.type === "leila"
        ? `/dashboard/leila?lessonId=${action.lessonId}`
        : `/dashboard/lessons/${action.lessonId}`)
    : action.type === "leila"
    ? "/dashboard/leila"
    : "/dashboard/lessons";

  const urgencyColors = {
    high:   "from-red-500 to-orange-500",
    medium: "from-primary to-emerald-600",
    low:    "from-blue-500 to-blue-700",
  };

  if (done) {
    return (
      <div className="rounded-2xl bg-emerald-50 border-2 border-emerald-200 p-5">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 rounded-2xl bg-emerald-100 flex items-center justify-center">
            <CheckCircle className="w-6 h-6 text-emerald-600" />
          </div>
          <div>
            <p className="font-bold text-emerald-800">أحسنت! أكملت درس اليوم 🎉</p>
            <p className="text-sm text-emerald-600">+{action.xpReward} XP مكتسبة — استمر غداً!</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <Link href={href} onClick={() => setDone(true)}>
      <div className={`rounded-2xl bg-gradient-to-l ${urgencyColors[action.urgency]} p-5 text-white cursor-pointer hover:opacity-95 transition-opacity shadow-md`}>
        {/* Header */}
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2">
            <span className="text-xs font-semibold bg-white/20 px-2.5 py-1 rounded-full">
              درس اليوم ✨
            </span>
            {action.urgency === "high" && (
              <span className="text-xs bg-white/20 px-2 py-1 rounded-full">مهم جداً</span>
            )}
          </div>
          <div className="flex items-center gap-1 text-sm font-medium bg-white/20 px-3 py-1 rounded-full">
            <Star className="w-4 h-4 text-amber-300" />
            <span>+{action.xpReward} XP</span>
          </div>
        </div>

        {/* Main content */}
        <div className="flex items-center gap-4">
          <div className="w-14 h-14 rounded-2xl bg-white/20 flex items-center justify-center text-3xl flex-shrink-0">
            {action.emoji}
          </div>
          <div className="flex-1 min-w-0">
            <h3 className="font-bold text-lg leading-tight truncate">{action.title}</h3>
            <p className="text-white/80 text-sm mt-0.5 line-clamp-2">{action.description}</p>
          </div>
          <ChevronLeft className="w-6 h-6 text-white/70 flex-shrink-0" />
        </div>

        {/* Footer */}
        <div className="flex items-center justify-between mt-4 pt-3 border-t border-white/20">
          <div className="flex items-center gap-1.5 text-sm text-white/80">
            <Clock className="w-4 h-4" />
            <span>~{action.estimatedMin} دقائق فقط</span>
          </div>
          {streak > 0 && (
            <div className="flex items-center gap-1.5 text-sm font-medium">
              <Flame className="w-4 h-4 text-amber-300" />
              <span>{streak} يوم متتالي</span>
            </div>
          )}
        </div>
      </div>
    </Link>
  );
}

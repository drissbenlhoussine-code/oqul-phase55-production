"use client";

import { Flame, Star, Trophy } from "lucide-react";
import { getLevelInfo } from "@/lib/gamification-level";

interface HabitBarProps {
  streak: number;
  xp:     number;
}

export function HabitBar({ streak, xp }: HabitBarProps) {
  const lvl = getLevelInfo(xp);

  return (
    <div className="flex items-center gap-3 text-sm">
      {/* Streak */}
      <div className={`flex items-center gap-1.5 px-2.5 py-1 rounded-full font-semibold ${
        streak > 0 ? "bg-orange-100 text-orange-700" : "bg-secondary text-muted-foreground"
      }`}>
        <Flame className="w-4 h-4" />
        <span>{streak}</span>
      </div>

      {/* XP */}
      <div className="flex items-center gap-1.5 bg-amber-50 text-amber-700 px-2.5 py-1 rounded-full font-semibold">
        <Star className="w-4 h-4" />
        <span>{xp}</span>
      </div>

      {/* Level */}
      <div className="hidden md:flex items-center gap-1.5 bg-primary/10 text-primary px-2.5 py-1 rounded-full font-semibold">
        <Trophy className="w-4 h-4" />
        <span>Lv.{lvl.level}</span>
      </div>
    </div>
  );
}

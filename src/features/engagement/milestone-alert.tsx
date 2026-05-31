"use client";

/**
 * MilestoneAlert — a subtle, non-blocking notification that tells the child
 * they're CLOSE to something. Creates urgency to keep going.
 *
 * "Just 2 more lessons to unlock the Week Warrior badge! 🏆"
 * "You're 30 XP away from Level 4! ⭐"
 */

import { useEffect, useState } from "react";
import Link from "next/link";
import { X, Trophy, Star, Flame } from "lucide-react";
import { getLevelInfo } from "@/lib/gamification-level";

interface MilestoneAlertProps {
  streak:    number;
  xp:        number;
  completed: number;
}

interface Milestone {
  icon:    React.ReactNode;
  title:   string;
  action:  string;
  href:    string;
  urgent:  boolean;
}

export function MilestoneAlert({ streak, xp, completed }: MilestoneAlertProps) {
  const [dismissed, setDismissed] = useState(false);
  const [visible, setVisible]     = useState(false);
  const lvl = getLevelInfo(xp);

  useEffect(() => {
    const t = setTimeout(() => setVisible(true), 2000); // show after 2s
    return () => clearTimeout(t);
  }, []);

  // Find the most urgent upcoming milestone
  const milestone: Milestone | null = (() => {
    // XP to next level
    if (lvl.xpToNext <= 50) {
      return {
        icon:    <Star className="w-5 h-5 text-amber-500" />,
        title:   `${lvl.xpToNext} نقطة للمستوى ${lvl.level + 1}!`,
        action:  "درس واحد يكفي ⚡",
        href:    "/dashboard/lessons",
        urgent:  lvl.xpToNext <= 20,
      };
    }

    // Streak milestones
    if (streak === 2) {
      return {
        icon:    <Flame className="w-5 h-5 text-orange-500" />,
        title:   "يوم واحد للشارة الأولى 🔥",
        action:  "درس اليوم = شارة جديدة",
        href:    "/dashboard/lessons",
        urgent:  true,
      };
    }
    if (streak === 6) {
      return {
        icon:    <Trophy className="w-5 h-5 text-amber-600" />,
        title:   "يوم واحد لشارة الأسبوع! 🏆",
        action:  "لا تكسر السلسلة الآن!",
        href:    "/dashboard/lessons",
        urgent:  true,
      };
    }

    // Lessons milestone
    if (completed === 9) {
      return {
        icon:    <Trophy className="w-5 h-5 text-purple-500" />,
        title:   "درس واحد لشارة '10 دروس'! 📚",
        action:  "أكملها الآن",
        href:    "/dashboard/lessons",
        urgent:  false,
      };
    }

    return null;
  })();

  if (!milestone || dismissed || !visible) return null;

  return (
    <div className={`fixed bottom-6 right-6 z-40 max-w-xs transition-all duration-500 ${visible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-4"}`}>
      <div className={`bg-white rounded-2xl shadow-xl border-2 ${milestone.urgent ? "border-amber-300" : "border-border"} p-4`}>
        <div className="flex items-start gap-3">
          <div className={`w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0 ${milestone.urgent ? "bg-amber-50" : "bg-secondary"}`}>
            {milestone.icon}
          </div>
          <div className="flex-1 min-w-0">
            <p className="font-bold text-sm">{milestone.title}</p>
            <p className="text-xs text-muted-foreground">{milestone.action}</p>
          </div>
          <button onClick={() => setDismissed(true)} className="text-muted-foreground hover:text-foreground">
            <X className="w-4 h-4" />
          </button>
        </div>
        <Link href={milestone.href}>
          <button
            onClick={() => setDismissed(true)}
            className={`w-full mt-3 py-2 rounded-xl text-sm font-bold transition-colors ${
              milestone.urgent
                ? "bg-amber-500 text-white hover:bg-amber-600"
                : "bg-primary text-white hover:bg-primary/90"
            }`}
          >
            ابدأ الآن! →
          </button>
        </Link>
      </div>
    </div>
  );
}

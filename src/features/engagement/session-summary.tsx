"use client";

/**
 * SessionSummary — the satisfying end-of-session recap.
 * Shown when navigating away from dashboard after completing something.
 * Like Duolingo's "You're on fire!" screen.
 */

import { useEffect, useState } from "react";
import Link from "next/link";
import { Trophy, BookOpen, Star, Flame, ArrowLeft } from "lucide-react";
import { getLevelInfo } from "@/lib/gamification-level";

interface SessionSummaryProps {
  childName:         string;
  lessonsCompleted:  number;
  xpEarned:          number;
  currentXP:         number;
  streak:            number;
  newBadges:         string[];
  onClose:           () => void;
}

export function SessionSummary({
  childName, lessonsCompleted, xpEarned, currentXP,
  streak, newBadges, onClose,
}: SessionSummaryProps) {
  const [visible, setVisible] = useState(false);
  const lvl = getLevelInfo(currentXP);

  useEffect(() => {
    const t = setTimeout(() => setVisible(true), 100);
    return () => clearTimeout(t);
  }, []);

  const encouragements = [
    `شطارة ${childName}! 🌟`,
    `راك تحسن بزاف! 🚀`,
    `عندك مستقبل نيشان! 💫`,
    `برافو عليك! 🎉`,
  ];
  const encouragement = encouragements[Math.floor(Math.random() * encouragements.length)];

  return (
    <div className={`fixed inset-0 z-50 flex items-end md:items-center justify-center transition-all duration-400 ${visible ? "opacity-100" : "opacity-0"}`}>
      <div className="absolute inset-0 bg-black/50 backdrop-blur-sm" onClick={onClose} />

      <div className={`relative z-10 w-full max-w-sm mx-4 mb-4 md:mb-0 transition-all duration-500 ${visible ? "translate-y-0" : "translate-y-8"}`}>
        <div className="bg-white rounded-3xl shadow-2xl overflow-hidden">
          {/* Header gradient */}
          <div className="bg-gradient-to-br from-emerald-500 to-emerald-700 p-6 text-white text-center">
            <p className="text-4xl mb-2">🎓</p>
            <h2 className="text-2xl font-bold">{encouragement}</h2>
            <p className="text-emerald-100 text-sm mt-1">جلسة اليوم منتهية</p>
          </div>

          {/* Stats */}
          <div className="p-5 space-y-3">
            {lessonsCompleted > 0 && (
              <div className="flex items-center gap-3 bg-blue-50 rounded-2xl p-3">
                <div className="w-10 h-10 rounded-xl bg-blue-100 flex items-center justify-center">
                  <BookOpen className="w-5 h-5 text-blue-600" />
                </div>
                <div>
                  <p className="font-bold text-blue-800">{lessonsCompleted} درس مكتمل</p>
                  <p className="text-xs text-blue-600">تعلمت أشياء جديدة اليوم!</p>
                </div>
              </div>
            )}

            {xpEarned > 0 && (
              <div className="flex items-center gap-3 bg-amber-50 rounded-2xl p-3">
                <div className="w-10 h-10 rounded-xl bg-amber-100 flex items-center justify-center">
                  <Star className="w-5 h-5 text-amber-600" />
                </div>
                <div className="flex-1">
                  <p className="font-bold text-amber-800">+{xpEarned} XP مكتسبة</p>
                  <div className="mt-1 h-1.5 bg-amber-100 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-amber-400 rounded-full transition-all duration-1000"
                      style={{ width: `${lvl.progress}%` }}
                    />
                  </div>
                  <p className="text-xs text-amber-600 mt-0.5">المستوى {lvl.level}: {lvl.title}</p>
                </div>
              </div>
            )}

            {streak > 0 && (
              <div className="flex items-center gap-3 bg-orange-50 rounded-2xl p-3">
                <div className="w-10 h-10 rounded-xl bg-orange-100 flex items-center justify-center">
                  <Flame className="w-5 h-5 text-orange-600" />
                </div>
                <div>
                  <p className="font-bold text-orange-800">🔥 {streak} أيام متتالية</p>
                  <p className="text-xs text-orange-600">
                    {streak < 3 ? `${3 - streak} أيام للشارة الأولى` :
                     streak < 7 ? `${7 - streak} أيام لشارة الأسبوع` :
                     "مستمر رائع — لا تقطع السلسلة!"}
                  </p>
                </div>
              </div>
            )}

            {newBadges.length > 0 && (
              <div className="bg-purple-50 rounded-2xl p-3">
                <p className="text-sm font-bold text-purple-800 mb-2 flex items-center gap-1">
                  <Trophy className="w-4 h-4" /> شارات جديدة!
                </p>
                <div className="flex flex-wrap gap-1.5">
                  {newBadges.map((b) => (
                    <span key={b} className="bg-purple-100 text-purple-800 text-xs font-bold px-2.5 py-1 rounded-full">🏅 {b}</span>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* CTA */}
          <div className="px-5 pb-5 space-y-2">
            <button
              onClick={onClose}
              className="w-full bg-primary text-white py-3 rounded-2xl font-bold hover:bg-primary/90 transition-colors"
            >
              تابع التعلم! 🚀
            </button>
            <Link href="/dashboard">
              <button onClick={onClose} className="w-full text-muted-foreground text-sm py-2 hover:text-foreground transition-colors flex items-center justify-center gap-1">
                <ArrowLeft className="w-4 h-4" /> العودة للرئيسية
              </button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

"use client";

/**
 * GettingStarted — shown to new users with no progress.
 * Replaces the empty DailyLoop to give a clear first action.
 */

import Link from "next/link";
import { Sparkles, ChevronLeft, BookOpen } from "lucide-react";
import { useEffect, useState } from "react";

interface GettingStartedProps {
  childName?: string;
  gradeName?: string;
}

export function GettingStarted({ childName, gradeName }: GettingStartedProps) {
  const [visible, setVisible] = useState(false);
  useEffect(() => { setTimeout(() => setVisible(true), 200); }, []);

  return (
    <div className={`transition-all duration-500 ${visible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-3"}`}>
      {/* Leila intro message */}
      <div className="flex items-start gap-3 mb-4">
        <div className="w-10 h-10 rounded-2xl bg-gradient-to-br from-primary to-emerald-600 flex items-center justify-center flex-shrink-0 shadow-md">
          <Sparkles className="w-5 h-5 text-white" />
        </div>
        <div className="bg-gradient-to-br from-emerald-600 to-emerald-700 text-white rounded-2xl rounded-tr-sm px-4 py-3 shadow-sm">
          <p className="text-sm leading-relaxed">
            مرحباً {childName ? <strong>{childName}</strong> : "بك"}! 🌟 أنا ليلى، هنا باش نساعدك تتعلم مزيان!
            {gradeName && <span className="block mt-1 text-emerald-200 text-xs">مستواك: {gradeName}</span>}
          </p>
        </div>
      </div>

      {/* First action card */}
      <Link href="/dashboard/lessons">
        <div className="rounded-2xl bg-gradient-to-l from-primary to-emerald-600 p-5 text-white cursor-pointer hover:opacity-95 transition-opacity shadow-md">
          <div className="flex items-center justify-between mb-3">
            <span className="text-xs font-semibold bg-white/20 px-2.5 py-1 rounded-full">ابدأ من هنا ✨</span>
            <span className="text-xs bg-white/20 px-2.5 py-1 rounded-full">+25 XP</span>
          </div>
          <div className="flex items-center gap-4">
            <div className="w-14 h-14 rounded-2xl bg-white/20 flex items-center justify-center text-3xl flex-shrink-0">
              📚
            </div>
            <div className="flex-1 min-w-0">
              <h3 className="font-bold text-lg">اختار درسك الأول!</h3>
              <p className="text-white/80 text-sm mt-0.5">ليلى جاهزة تشرح ليك — 10 دقائق فقط 😊</p>
            </div>
            <ChevronLeft className="w-6 h-6 text-white/70 flex-shrink-0" />
          </div>
          <div className="mt-4 pt-3 border-t border-white/20 text-sm text-white/80 flex items-center gap-2">
            <BookOpen className="w-4 h-4" />
            <span>اختر المادة اللي تبغي تبدأ بها</span>
          </div>
        </div>
      </Link>
    </div>
  );
}

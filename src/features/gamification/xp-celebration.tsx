"use client";

import { useEffect, useState } from "react";
import { getLevelInfo } from "@/lib/gamification-level";

interface XPCelebrationProps {
  xpEarned:  number;
  newXP:     number;
  newBadges: string[];
  streak:    number;
  passed:    boolean;
  score:     number;
  onClose:   () => void;
}

export function XPCelebration({ xpEarned, newXP, newBadges, streak, passed, score, onClose }: XPCelebrationProps) {
  const [visible, setVisible]     = useState(false);
  const [particles, setParticles] = useState<{ x: number; y: number; emoji: string; id: number }[]>([]);

  const lvl       = getLevelInfo(newXP);
  const isPerfect = score === 100;

  useEffect(() => {
    setTimeout(() => setVisible(true), 50);
    const emojis = isPerfect ? ["🌟","💯","✨","🎉","🏆"] : passed ? ["🌟","✨","🎉","👏","⭐"] : ["💪","🤔","📚","🔄","✏️"];
    setParticles(Array.from({ length: 12 }, (_, i) => ({ id: i, x: Math.random() * 90 + 5, y: Math.random() * 60 + 10, emoji: emojis[i % emojis.length] })));
    const t = setTimeout(() => { setVisible(false); setTimeout(onClose, 400); }, 4500);
    return () => clearTimeout(t);
  }, [passed, isPerfect, onClose]);

  return (
    <div className={`fixed inset-0 z-50 flex items-center justify-center transition-all duration-400 ${visible ? "opacity-100" : "opacity-0 pointer-events-none"}`}>
      <div className="absolute inset-0 bg-black/60 backdrop-blur-sm" onClick={() => { setVisible(false); setTimeout(onClose, 300); }} />
      {particles.map((p) => (
        <div key={p.id} className="absolute text-3xl animate-bounce pointer-events-none select-none" style={{ left: `${p.x}%`, top: `${p.y}%`, animationDelay: `${p.id * 0.1}s`, animationDuration: "1.5s" }}>
          {p.emoji}
        </div>
      ))}
      <div className={`relative z-10 w-full max-w-sm mx-4 transition-all duration-500 ${visible ? "scale-100 translate-y-0" : "scale-90 translate-y-8"}`}>
        <div className={`rounded-3xl p-7 text-center shadow-2xl border-2 ${isPerfect ? "bg-amber-50 border-amber-300" : passed ? "bg-emerald-50 border-emerald-300" : "bg-blue-50 border-blue-300"}`}>
          <div className="text-7xl mb-3 animate-pulse-soft">{isPerfect ? "🏆" : passed ? "🎉" : "💪"}</div>
          <h2 className="text-2xl font-bold mb-1">{isPerfect ? "علامة كاملة!" : passed ? "أحسنت!" : "حاول مجدداً!"}</h2>
          <p className="text-4xl font-black text-primary mb-4">{score}%</p>
          {passed && (
            <div className="bg-white rounded-2xl p-4 mb-4 space-y-3 shadow-sm">
              <div className="flex items-center justify-center gap-2">
                <span className="text-2xl">⭐</span>
                <span className="text-2xl font-bold text-amber-600">+{xpEarned} XP</span>
              </div>
              <div className="space-y-1">
                <div className="flex justify-between text-xs text-gray-500">
                  <span>المستوى {lvl.level}: {lvl.title}</span>
                  <span>{lvl.xpToNext} للمستوى التالي</span>
                </div>
                <div className="h-3 bg-gray-100 rounded-full overflow-hidden">
                  <div className="h-full bg-gradient-to-r from-primary to-emerald-400 rounded-full transition-all duration-1000" style={{ width: `${lvl.progress}%` }} />
                </div>
              </div>
              {streak > 0 && (
                <div className="flex items-center justify-center gap-2 text-sm font-medium text-orange-600">
                  <span>🔥</span><span>{streak} أيام متتالية!</span>
                </div>
              )}
            </div>
          )}
          {newBadges.length > 0 && (
            <div className="mb-4 space-y-2">
              <p className="text-sm font-semibold text-gray-600">شارات جديدة! 🏅</p>
              <div className="flex flex-wrap gap-2 justify-center">
                {newBadges.map((b) => (
                  <span key={b} className="bg-amber-100 text-amber-800 px-3 py-1.5 rounded-full text-sm font-bold border border-amber-200">🏅 {b}</span>
                ))}
              </div>
            </div>
          )}
          <button onClick={() => { setVisible(false); setTimeout(onClose, 300); }}
            className={`w-full py-3 rounded-2xl font-bold text-white transition-colors ${isPerfect ? "bg-amber-500 hover:bg-amber-600" : passed ? "bg-primary hover:bg-primary/90" : "bg-blue-500 hover:bg-blue-600"}`}>
            {passed ? "متابعة! 🚀" : "حاول مرة أخرى 💪"}
          </button>
        </div>
      </div>
    </div>
  );
}

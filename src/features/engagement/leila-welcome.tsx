"use client";

/**
 * LeilaWelcome — the emotional hook that opens every session.
 * Shows a personalized message from Leila based on:
 * - How long since last visit
 * - Streak status
 * - Recent performance
 * - Time of day
 *
 * This is the equivalent of Duolingo's owl — the character that makes you feel
 * like someone is waiting for you.
 */

import { useEffect, useState } from "react";
import { Sparkles } from "lucide-react";

interface WelcomeProps {
  childName:    string;
  streak:       number;
  lastVisitDaysAgo?: number;
  avgScore?:    number;
  completedToday?: number;
}

function buildMessage(props: WelcomeProps): string {
  const { childName, streak, lastVisitDaysAgo = 0, avgScore = 0, completedToday = 0 } = props;
  const h = new Date().getHours();
  const timeGreet = h < 12 ? "صباح النور" : h < 17 ? "مرحباً" : "مساء الخير";

  // Long absence
  if (lastVisitDaysAgo >= 3) {
    return `${timeGreet} ${childName}! وحشتني والله 🥺 غبيت ${lastVisitDaysAgo} أيام — اليوم نرجعو للمسيرة سوا!`;
  }

  // Broken streak
  if (lastVisitDaysAgo === 1 && streak === 0) {
    return `${timeGreet} ${childName}! غداً تبدأ سلسلة جديدة — ابدأ الآن ودير ولو درس واحد صغير 💪`;
  }

  // Strong streak
  if (streak >= 7) {
    return `${timeGreet} ${childName}! 🔥 ${streak} أيام متتالية — هاد رقم ما كيوقفوش إلا الأبطال! نكملو؟`;
  }

  if (streak >= 3) {
    return `${timeGreet} ${childName}! راك غادي مزيان — ${streak} أيام و${3 - streak % 3 === 0 ? "غادي تفوز بشارة جديدة قريبًا" : "مشي بزاف للشارة القادمة"} 🌟`;
  }

  // Already studied today
  if (completedToday > 0) {
    return `${timeGreet} ${childName}! ديجا دارتي ${completedToday} درس اليوم 🎉 كاين مزيد؟ نعاونك!`;
  }

  // Needs encouragement (low scores)
  if (avgScore > 0 && avgScore < 60) {
    return `${timeGreet} ${childName}! اليوم فرصة باش نحسنو شوية — ليلى معاك خطوة بخطوة 💙`;
  }

  // Doing well
  if (avgScore >= 80) {
    return `${timeGreet} ${childName}! معدلك ${avgScore}% — هاد شي مزيان بزاف! واصل هكذا 🏆`;
  }

  // Default warm greeting
  const greetings = [
    `${timeGreet} ${childName}! ليلى جاهزة — شنو نتعلمو اليوم؟ 📚`,
    `${timeGreet} ${childName}! نبدأو؟ كل درس كيحسب 🌟`,
    `${timeGreet} ${childName}! واشرانك؟ جاهز/ة نتعلمو شي جديد؟ ✨`,
  ];
  return greetings[Math.floor(Math.random() * greetings.length)];
}

export function LeilaWelcome(props: WelcomeProps) {
  const [visible, setVisible] = useState(false);
  const [message] = useState(() => buildMessage(props));

  useEffect(() => {
    const t = setTimeout(() => setVisible(true), 150);
    return () => clearTimeout(t);
  }, []);

  return (
    <div className={`transition-all duration-500 ${visible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-2"}`}>
      <div className="flex items-start gap-3">
        {/* Leila avatar */}
        <div className="w-10 h-10 rounded-2xl bg-gradient-to-br from-primary to-emerald-600 flex items-center justify-center flex-shrink-0 shadow-md">
          <Sparkles className="w-5 h-5 text-white" />
        </div>

        {/* Speech bubble */}
        <div className="bg-gradient-to-br from-emerald-600 to-emerald-700 text-white rounded-2xl rounded-tr-sm px-4 py-3 max-w-sm shadow-sm">
          <p className="text-sm leading-relaxed">{message}</p>
        </div>
      </div>
    </div>
  );
}

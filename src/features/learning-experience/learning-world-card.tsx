"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Sparkles, Star, Trophy, Compass } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";

type Mission = {
  id: string;
  title: string;
  description: string;
  xpReward: number;
  estimatedMinutes: number;
  type: "lesson" | "review" | "quiz" | "confidence";
};

type Phase40Snapshot = {
  masteryScore: number;
  confidenceScore: number;
  masteryBand: "discover" | "practice" | "review" | "master";
  emotionalSignal: string;
  nextTeacherMove: string;
  missions: Mission[];
};

const bandCopy: Record<Phase40Snapshot["masteryBand"], string> = {
  discover: "نبدأ بهدوء",
  review: "نثبت الفهم",
  practice: "نتدرّب بذكاء",
  master: "تحدي الأبطال",
};

const missionEmoji: Record<Mission["type"], string> = {
  lesson: "📚",
  review: "🔄",
  quiz: "⚡",
  confidence: "💪",
};

export function LearningWorldCard({ childId }: { childId: string }) {
  const [snapshot, setSnapshot] = useState<Phase40Snapshot | null>(null);

  useEffect(() => {
    let alive = true;
    fetch(`/api/learning/phase40?childId=${childId}`)
      .then((r) => r.json())
      .then((json) => {
        if (alive && json.success) setSnapshot(json.data);
      })
      .catch(() => undefined);

    return () => { alive = false; };
  }, [childId]);

  if (!snapshot) return null;

  return (
    <Card className="overflow-hidden border-emerald-100 bg-gradient-to-br from-emerald-50 via-white to-amber-50 shadow-sm">
      <CardContent className="p-4 space-y-4">
        <div className="flex items-start justify-between gap-3">
          <div>
            <div className="inline-flex items-center gap-2 rounded-full bg-white/80 px-3 py-1 text-xs font-semibold text-emerald-700 shadow-sm">
              <Compass className="h-3.5 w-3.5" />
              عالم التعلّم Phase40
            </div>
            <h2 className="mt-3 text-lg font-bold text-slate-900">{bandCopy[snapshot.masteryBand]}</h2>
            <p className="mt-1 text-sm leading-7 text-slate-600">{snapshot.nextTeacherMove}</p>
          </div>
          <div className="rounded-2xl bg-white p-3 text-center shadow-sm">
            <Sparkles className="mx-auto h-5 w-5 text-amber-500" />
            <p className="mt-1 text-xs text-slate-500">الثقة</p>
            <p className="text-lg font-bold">{snapshot.confidenceScore}%</p>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-2 text-center">
          <div className="rounded-2xl bg-white/80 p-3">
            <Star className="mx-auto h-4 w-4 text-emerald-600" />
            <p className="mt-1 text-xs text-slate-500">الإتقان</p>
            <p className="font-bold">{snapshot.masteryScore}%</p>
          </div>
          <div className="rounded-2xl bg-white/80 p-3">
            <Trophy className="mx-auto h-4 w-4 text-amber-600" />
            <p className="mt-1 text-xs text-slate-500">الحالة</p>
            <p className="font-bold">{snapshot.emotionalSignal}</p>
          </div>
        </div>

        <div className="space-y-2">
          {snapshot.missions.map((mission) => (
            <Link key={mission.id} href="/dashboard/leila" className="block rounded-2xl bg-white/90 p-3 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md">
              <div className="flex items-center gap-3">
                <span className="text-xl">{missionEmoji[mission.type]}</span>
                <div className="min-w-0 flex-1">
                  <p className="truncate text-sm font-semibold text-slate-900">{mission.title}</p>
                  <p className="truncate text-xs text-slate-500">{mission.description}</p>
                </div>
                <span className="rounded-full bg-amber-100 px-2 py-1 text-xs font-bold text-amber-700">+{mission.xpReward} XP</span>
              </div>
            </Link>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}

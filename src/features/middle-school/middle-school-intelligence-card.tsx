"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { BookOpen, Brain, Languages, Target, ArrowLeft } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";

type Competency = {
  id: string;
  titleAr: string;
  skill: string;
  misconceptions: string[];
  objectives: string[];
};

type Phase42Profile = {
  grade: "1AC" | "2AC" | "3AC";
  targetLanguage: "ar_fusha" | "darija" | "fr" | "en";
  priorityCompetencies: Competency[];
  tutorPolicy: {
    tone: string;
    defaultLanguage: string;
    languageSwitchingRule: string;
    teachingLoop: string[];
  };
};

const gradeLabel: Record<Phase42Profile["grade"], string> = {
  "1AC": "الأولى إعدادي",
  "2AC": "الثانية إعدادي",
  "3AC": "الثالثة إعدادي",
};

const langLabel: Record<Phase42Profile["targetLanguage"], string> = {
  ar_fusha: "فصحى سلسة",
  darija: "دارجة مغربية",
  fr: "Français",
  en: "English",
};

export function MiddleSchoolIntelligenceCard({ childId }: { childId: string }) {
  const [profile, setProfile] = useState<Phase42Profile | null>(null);

  useEffect(() => {
    let alive = true;
    fetch(`/api/learning/phase42?childId=${childId}`)
      .then((r) => r.json())
      .then((json) => {
        if (alive && json.success) setProfile(json.data);
      })
      .catch(() => undefined);
    return () => { alive = false; };
  }, [childId]);

  if (!profile) return null;

  const main = profile.priorityCompetencies[0];

  return (
    <Card className="overflow-hidden border-indigo-100 bg-gradient-to-br from-slate-950 via-indigo-950 to-slate-900 text-white shadow-sm">
      <CardContent className="space-y-4 p-5">
        <div className="flex items-start justify-between gap-4">
          <div>
            <div className="inline-flex items-center gap-2 rounded-full bg-white/10 px-3 py-1 text-xs font-semibold text-indigo-100">
              <Brain className="h-3.5 w-3.5" />
              Phase42 Middle School Intelligence
            </div>
            <h2 className="mt-3 text-xl font-bold">{gradeLabel[profile.grade]} — مسار ذكي للإعدادي</h2>
            <p className="mt-1 text-sm leading-7 text-indigo-100">ليلى تبدأ بالفصحى السلسة، وتغير اللغة فورًا حسب طلب التلميذ.</p>
          </div>
          <div className="rounded-2xl bg-white/10 p-3 text-center">
            <Languages className="mx-auto h-5 w-5" />
            <p className="mt-1 text-xs text-indigo-100">اللغة</p>
            <p className="text-sm font-bold">{langLabel[profile.targetLanguage]}</p>
          </div>
        </div>

        {main && (
          <div className="rounded-3xl bg-white p-4 text-slate-950">
            <div className="flex items-start gap-3">
              <Target className="mt-1 h-5 w-5 text-indigo-700" />
              <div>
                <p className="text-sm font-bold">أولوية التعلّم الآن</p>
                <h3 className="mt-1 font-semibold">{main.titleAr}</h3>
                <p className="mt-1 text-sm leading-7 text-slate-600">{main.skill}</p>
              </div>
            </div>
          </div>
        )}

        <div className="grid gap-2 sm:grid-cols-2">
          {profile.tutorPolicy.teachingLoop.slice(0, 4).map((step, index) => (
            <div key={step} className="rounded-2xl bg-white/10 p-3 text-sm text-indigo-50">
              <span className="font-bold text-white">{index + 1}. </span>{step}
            </div>
          ))}
        </div>

        <Link href="/dashboard/middle-school" className="inline-flex items-center gap-2 rounded-2xl bg-white px-4 py-2 text-sm font-bold text-indigo-950 transition hover:-translate-y-0.5">
          <BookOpen className="h-4 w-4" />
          افتح مركز الإعدادي
          <ArrowLeft className="h-4 w-4" />
        </Link>
      </CardContent>
    </Card>
  );
}

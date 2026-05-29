"use client";

import { useState } from "react";
import { BookOpen, ChevronLeft } from "lucide-react";

export interface OnboardingData {
  childName: string;
  level: number;
  subject: string;
}

type Step = 1 | 2 | 3;

const levels = [
  { value: 1, label: "المستوى الأول", age: "6–7 سنوات", emoji: "🌱" },
  { value: 2, label: "المستوى الثاني", age: "7–8 سنوات", emoji: "🌿" },
  { value: 3, label: "المستوى الثالث", age: "8–9 سنوات", emoji: "🌳" },
  { value: 4, label: "المستوى الرابع", age: "9–10 سنوات", emoji: "🌲" },
  { value: 5, label: "المستوى الخامس", age: "10–11 سنة", emoji: "🏔️" },
  { value: 6, label: "المستوى السادس", age: "11–12 سنة", emoji: "⭐" },
];

const subjects = [
  { id: "arabic", label: "اللغة العربية", icon: "ع", color: "bg-orange-100 text-orange-700 border-orange-200" },
  { id: "math", label: "الرياضيات", icon: "∑", color: "bg-emerald-100 text-emerald-700 border-emerald-200" },
  { id: "french", label: "الفرنسية", icon: "Fr", color: "bg-violet-100 text-violet-700 border-violet-200" },
];

export function OnboardingFlow({ onComplete }: { onComplete?: (data: OnboardingData) => void }) {
  const [step, setStep] = useState<Step>(1);
  const [done, setDone] = useState(false);
  const [data, setData] = useState<OnboardingData>({ childName: "", level: 2, subject: "arabic" });

  const canContinue = step === 1 ? data.childName.trim().length >= 2 : true;

  function next() {
    if (step < 3) {
      setStep((current) => (current + 1) as Step);
      return;
    }
    setDone(true);
    onComplete?.(data);
  }

  if (done) {
    const subject = subjects.find((item) => item.id === data.subject)?.label ?? "أول مادة";
    return (
      <div className="mx-auto max-w-md rounded-3xl bg-white p-8 text-center shadow-xl" dir="rtl">
        <div className="mx-auto flex h-24 w-24 items-center justify-center rounded-full bg-gradient-to-br from-orange-500 to-amber-400 text-5xl shadow-xl">👩‍🏫</div>
        <h2 className="mt-6 text-3xl font-black text-slate-900">يلا نبدأ يا {data.childName}! 🌟</h2>
        <p className="mt-3 leading-8 text-slate-500">ليلى جاهزة معك في {subject} — المستوى {data.level}.</p>
        <div className="mt-6 rounded-2xl bg-orange-50 p-5 text-right leading-8 text-slate-700">
          أنا هنا معك كل يوم. لا يهم إذا أخطأنا، المهم نتعلم بثقة ونفرح بكل خطوة صغيرة. 💛
          <p className="mt-2 text-sm font-bold text-orange-600">— أستاذة ليلى</p>
        </div>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-md rounded-3xl bg-white p-8 shadow-xl" dir="rtl">
      <div className="mb-6 flex items-center gap-2">
        <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-orange-500 to-amber-400"><BookOpen className="h-5 w-5 text-white" /></div>
        <span className="text-lg font-black text-slate-900">Oqul</span>
      </div>

      <div className="mb-8 flex gap-2">
        {[1, 2, 3].map((item) => <div key={item} className={`h-2 flex-1 rounded-full ${item <= step ? "bg-orange-500" : "bg-slate-200"}`} />)}
      </div>

      <div className="min-h-[360px]">
        {step === 1 && (
          <div className="space-y-6">
            <div className="flex h-20 w-20 items-center justify-center rounded-3xl bg-orange-100 text-4xl">👋</div>
            <div><h2 className="text-3xl font-black text-slate-900">ما اسم طفلك؟</h2><p className="mt-2 text-slate-500">ليلى ستستخدم هذا الاسم عند التحدث معه.</p></div>
            <input value={data.childName} onChange={(event) => setData((current) => ({ ...current, childName: event.target.value }))} placeholder="مثلًا: يوسف، أمينة…" className="w-full rounded-2xl border border-slate-200 bg-white px-5 py-4 text-lg font-bold outline-none focus:border-orange-400 focus:ring-2 focus:ring-orange-100" dir="rtl" />
          </div>
        )}

        {step === 2 && (
          <div className="space-y-6">
            <div><h2 className="text-3xl font-black text-slate-900">في أي مستوى دراسي؟</h2><p className="mt-2 text-slate-500">سنختار المحتوى المناسب لعمر طفلك.</p></div>
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
              {levels.map((level) => (
                <button key={level.value} onClick={() => setData((current) => ({ ...current, level: level.value }))} className={`rounded-2xl border p-4 text-center ${data.level === level.value ? "border-orange-400 bg-orange-50 ring-2 ring-orange-200" : "border-slate-200 bg-white"}`}>
                  <span className="text-3xl">{level.emoji}</span><span className="mt-2 block font-bold">{level.label}</span><span className="text-xs text-slate-500">{level.age}</span>
                </button>
              ))}
            </div>
          </div>
        )}

        {step === 3 && (
          <div className="space-y-6">
            <div><h2 className="text-3xl font-black text-slate-900">من أين نبدأ؟</h2><p className="mt-2 text-slate-500">اختر المادة الأولى.</p></div>
            {subjects.map((subject) => (
              <button key={subject.id} onClick={() => setData((current) => ({ ...current, subject: subject.id }))} className={`mb-3 flex w-full items-center gap-4 rounded-2xl border-2 p-5 text-right ${data.subject === subject.id ? "border-orange-400 bg-orange-50" : "border-slate-200 bg-white"}`}>
                <div className={`flex h-14 w-14 items-center justify-center rounded-2xl border text-xl font-black ${subject.color}`}>{subject.icon}</div>
                <span className="text-lg font-bold text-slate-900">{subject.label}</span>
                {data.subject === subject.id && <span className="mr-auto text-orange-500">✓</span>}
              </button>
            ))}
          </div>
        )}
      </div>

      <div className="mt-8 flex items-center gap-3">
        {step > 1 && <button onClick={() => setStep((current) => (current - 1) as Step)} className="flex h-12 w-12 items-center justify-center rounded-2xl border border-slate-200 text-slate-500"><ChevronLeft className="h-5 w-5" /></button>}
        <button onClick={next} disabled={!canContinue} className={`flex-1 rounded-2xl py-3.5 text-base font-bold text-white ${canContinue ? "bg-orange-500" : "bg-slate-200 text-slate-400"}`}>
          {step === 3 ? "خلّيني نبدأ! 🚀" : "التالي"}
        </button>
      </div>
    </div>
  );
}

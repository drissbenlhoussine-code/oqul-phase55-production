"use client";

import { useEffect, useMemo, useState } from "react";
import {
  BookOpen,
  Flame,
  MessageCircle,
  Sparkles,
  Star,
  Users,
} from "lucide-react";

const subjects = [
  { id: "arabic", icon: "ع", label: "اللغة العربية", color: "bg-orange-100 text-orange-700" },
  { id: "math", icon: "∑", label: "الرياضيات", color: "bg-emerald-100 text-emerald-700" },
  { id: "french", icon: "Fr", label: "الفرنسية", color: "bg-violet-100 text-violet-700" },
  { id: "science", icon: "⚗", label: "العلوم", color: "bg-amber-100 text-amber-700" },
];

const leilaMessages = [
  "أحسنت! أنت تتعلم بسرعة رائعة اليوم 🌟",
  "واصل هكذا، أنا فخورة بك جدًا 💫",
  "درس اليوم ممتع، نبدأ خطوة صغيرة؟ 📚",
  "تذكر، كل سؤال فرصة جديدة للتعلم ✨",
];

function LeilaAvatar({ speaking = false }: { speaking?: boolean }) {
  return (
    <div
      className={[
        "flex h-14 w-14 shrink-0 items-center justify-center rounded-full",
        "bg-gradient-to-br from-orange-500 to-amber-400 text-3xl shadow-lg",
        speaking ? "animate-pulse ring-4 ring-amber-200" : "",
      ].join(" ")}
    >
      👩‍🏫
    </div>
  );
}

function SubjectCard({ subject, index }: { subject: (typeof subjects)[number]; index: number }) {
  const progress = Math.min(92, 42 + index * 10);

  return (
    <div className="rounded-3xl bg-white p-4 shadow-sm ring-1 ring-slate-100 transition hover:-translate-y-1 hover:shadow-lg">
      <div className={`mb-3 flex h-12 w-12 items-center justify-center rounded-2xl text-xl font-black ${subject.color}`}>
        {subject.icon}
      </div>
      <p className="font-bold text-slate-900">{subject.label}</p>
      <div className="mt-3 h-2 overflow-hidden rounded-full bg-slate-100">
        <div className="h-full rounded-full bg-orange-500" style={{ width: `${progress}%` }} />
      </div>
      <p className="mt-2 text-xs text-slate-500">{progress}% مكتمل</p>
    </div>
  );
}

function ChildHome() {
  const [messageIndex, setMessageIndex] = useState(0);
  const [speaking, setSpeaking] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      setMessageIndex((current) => (current + 1) % leilaMessages.length);
      setSpeaking(true);
      setTimeout(() => setSpeaking(false), 1500);
    }, 4200);

    return () => clearInterval(interval);
  }, []);

  return (
    <main className="min-h-screen bg-[#F7F0E3]" dir="rtl">
      <section className="relative overflow-hidden rounded-b-[2rem] bg-gradient-to-br from-[#1A1025] to-[#2D1B4E] px-5 py-6 text-white">
        <div className="relative z-10 mx-auto max-w-6xl">
          <div className="mb-6 flex items-center justify-between">
            <span className="inline-flex items-center gap-1 rounded-full bg-amber-400/15 px-3 py-1 text-sm text-amber-100">
              <Flame className="h-4 w-4" />
              7 أيام
            </span>
            <span className="rounded-full bg-white/10 px-3 py-1 text-sm text-amber-100">⭐ 340 نقطة</span>
          </div>

          <div className="mb-5">
            <p className="text-sm text-white/60">مرحبًا بك يا</p>
            <h1 className="mt-1 text-4xl font-black">يوسف 👋</h1>
          </div>

          <div className="flex flex-col gap-4 rounded-3xl border border-white/15 bg-white/10 p-4 backdrop-blur md:flex-row md:items-center">
            <LeilaAvatar speaking={speaking} />
            <div className="flex-1">
              <p className="text-xs font-bold uppercase tracking-widest text-amber-200">أستاذة ليلى</p>
              <p className="mt-1 leading-8 text-white/90">{leilaMessages[messageIndex]}</p>
            </div>
            <button className="inline-flex items-center justify-center gap-2 rounded-2xl bg-orange-500 px-5 py-3 font-bold text-white shadow-lg">
              <MessageCircle className="h-4 w-4" />
              دردش
            </button>
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-6xl space-y-6 px-5 py-6">
        <div className="rounded-3xl bg-gradient-to-br from-orange-500 to-orange-400 p-6 text-white shadow-lg">
          <p className="text-sm text-white/80">تحدي اليوم • الرياضيات</p>
          <h2 className="mt-2 text-2xl font-black">الجمع والطرح حتى 100</h2>
          <div className="mt-5 flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
            <div className="flex gap-3 text-sm text-white/85">
              <span>⏱ 10 دقائق</span>
              <span>+50 نقطة</span>
            </div>
            <button className="rounded-2xl bg-white px-6 py-3 font-bold text-orange-600">ابدأ الآن</button>
          </div>
        </div>

        <div>
          <h2 className="mb-3 text-xl font-black text-slate-900">خريطة التعلم 🗺️</h2>
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {subjects.map((subject, index) => (
              <SubjectCard key={subject.id} subject={subject} index={index} />
            ))}
          </div>
        </div>

        <div className="rounded-3xl bg-white p-5 shadow-sm">
          <h2 className="mb-4 text-xl font-black text-slate-900">تقدمك هذا الأسبوع 📊</h2>
          <div className="grid gap-3 sm:grid-cols-3">
            <div className="rounded-2xl bg-slate-50 p-4"><p className="text-sm text-slate-500">دروس مكتملة</p><p className="text-2xl font-black">18</p></div>
            <div className="rounded-2xl bg-slate-50 p-4"><p className="text-sm text-slate-500">نقاط مكتسبة</p><p className="text-2xl font-black">340</p></div>
            <div className="rounded-2xl bg-slate-50 p-4"><p className="text-sm text-slate-500">وقت التعلم</p><p className="text-2xl font-black">4.2 س</p></div>
          </div>
        </div>
      </section>
    </main>
  );
}

function ParentHome() {
  return (
    <main className="min-h-screen bg-[#F8F5F0] px-5 py-6" dir="rtl">
      <section className="mx-auto max-w-5xl space-y-5">
        <div className="rounded-[2rem] bg-gradient-to-br from-emerald-700 to-emerald-600 p-6 text-white shadow-lg">
          <p className="text-sm text-white/70">لوحة ولي الأمر</p>
          <h1 className="mt-2 text-3xl font-black">أهلًا، الأستاذ محمد 👋</h1>
          <p className="mt-3 leading-8 text-white/80">ملخص بسيط لما تعلمه الطفل، وما تقترحه ليلى لليوم القادم.</p>
        </div>

        <div className="grid gap-4 md:grid-cols-3">
          <div className="rounded-3xl bg-white p-5 text-center shadow-sm">
            <Star className="mx-auto h-7 w-7 text-amber-500" />
            <p className="mt-2 text-3xl font-black text-amber-600">340</p>
            <p className="text-sm text-slate-500">نقطة</p>
          </div>
          <div className="rounded-3xl bg-white p-5 text-center shadow-sm">
            <Flame className="mx-auto h-7 w-7 text-orange-500" />
            <p className="mt-2 text-3xl font-black text-orange-600">7</p>
            <p className="text-sm text-slate-500">أيام متتالية</p>
          </div>
          <div className="rounded-3xl bg-white p-5 text-center shadow-sm">
            <BookOpen className="mx-auto h-7 w-7 text-emerald-600" />
            <p className="mt-2 text-3xl font-black text-emerald-700">18</p>
            <p className="text-sm text-slate-500">درس مكتمل</p>
          </div>
        </div>

        <div className="rounded-3xl bg-white p-6 shadow-sm">
          <div className="mb-4 flex items-center gap-3">
            <LeilaAvatar />
            <div>
              <h2 className="font-black text-slate-900">اقتراح أستاذة ليلى</h2>
              <p className="text-sm text-slate-500">بناءً على أداء يوسف هذا الأسبوع</p>
            </div>
          </div>
          <p className="rounded-2xl border-r-4 border-orange-500 bg-orange-50 p-4 leading-8 text-slate-800">
            يوسف يحتاج تمرينًا إضافيًا على الكسور، أقترح 10 دقائق يوميًا قبل النوم. أداؤه في الرياضيات تحسن بنسبة 23% هذا الأسبوع 🌟
          </p>
        </div>
      </section>
    </main>
  );
}

function Landing({ onNavigate }: { onNavigate: (view: "child" | "parent") => void }) {
  return (
    <main className="min-h-screen bg-[#1A1025] px-5 py-6 text-white" dir="rtl">
      <section className="mx-auto max-w-6xl">
        <nav className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-gradient-to-br from-orange-500 to-amber-400 text-2xl">📚</div>
            <span className="text-2xl font-black">Oqul</span>
          </div>
          <div className="flex gap-2">
            <button onClick={() => onNavigate("parent")} className="rounded-2xl border border-white/20 px-4 py-2">لوحة الأهل</button>
            <button onClick={() => onNavigate("child")} className="rounded-2xl bg-orange-500 px-4 py-2 font-bold">للأطفال 🎮</button>
          </div>
        </nav>

        <div className="py-20 text-center">
          <div className="mb-7 inline-flex rounded-full border border-orange-400/30 bg-orange-400/10 px-4 py-2 text-sm text-orange-200">
            🇲🇦 المنهج المغربي الرسمي
          </div>
          <h1 className="text-5xl font-black leading-tight md:text-7xl">
            تعلم مع
            <br />
            <span className="bg-gradient-to-br from-orange-400 to-amber-300 bg-clip-text text-transparent">أستاذة ليلى</span>
          </h1>
          <p className="mx-auto mt-6 max-w-2xl text-lg leading-8 text-white/65">
            تعليم ذكي وتفاعلي للأطفال المغاربة من المستوى الأول إلى السادس، بتجربة دافئة تشجع الطفل على التعلم يوميًا.
          </p>
          <div className="mt-10 flex flex-wrap justify-center gap-4">
            <button onClick={() => onNavigate("child")} className="rounded-3xl bg-orange-500 px-8 py-4 text-lg font-bold shadow-xl">ابدأ التعلم مجانًا 🚀</button>
            <button onClick={() => onNavigate("parent")} className="rounded-3xl border border-white/20 px-8 py-4 text-lg">لوحة الأهل 📊</button>
          </div>
        </div>

        <div className="grid gap-4 md:grid-cols-4">
          {[
            ["🤖", "ذكاء تعليمي", "ليلى ترافق الطفل خطوة بخطوة"],
            ["📚", "منهج مغربي", "من الأول إلى السادس ابتدائي"],
            ["🎮", "تعلم ممتع", "تحديات ومغامرات قصيرة"],
            ["📊", "ثقة الأهل", "ملخصات واضحة وبسيطة"],
          ].map(([icon, title, desc]) => (
            <div key={title} className="rounded-3xl border border-white/10 bg-white/5 p-5 text-center backdrop-blur">
              <div className="text-4xl">{icon}</div>
              <h3 className="mt-3 font-black">{title}</h3>
              <p className="mt-2 text-sm leading-7 text-white/55">{desc}</p>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}

export function OqulVisualSystem() {
  const [view, setView] = useState<"landing" | "child" | "parent">("landing");

  const content = useMemo(() => {
    if (view === "child") return <ChildHome />;
    if (view === "parent") return <ParentHome />;
    return <Landing onNavigate={setView} />;
  }, [view]);

  return (
    <div>
      {view !== "landing" && (
        <button
          onClick={() => setView("landing")}
          className="fixed bottom-5 left-1/2 z-50 -translate-x-1/2 rounded-full bg-slate-950 px-5 py-3 text-sm font-bold text-white shadow-xl"
        >
          ← الصفحة الرئيسية
        </button>
      )}
      {content}
    </div>
  );
}

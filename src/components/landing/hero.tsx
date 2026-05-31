"use client";
import Link from "next/link";
import { ArrowLeft, CheckCircle } from "lucide-react";

const TRUST_BADGES = [
  { icon: "🇲🇦", text: "المنهج المغربي الرسمي" },
  { icon: "🔒",  text: "آمن للأطفال" },
  { icon: "🎓",  text: "من الابتدائي إلى الثانوي التأهيلي" },
  { icon: "🎁",  text: "7 أيام مجانية" },
];

const BENEFITS = [
  "متابعة واضحة لتقدم طفلك",
  "دروس وتمارين منظمة حسب المنهج",
  "تجربة مجانية 7 أيام — بدون بطاقة بنكية",
];

export function Hero() {
  return (
    <section className="relative overflow-hidden bg-gradient-to-br from-[#0F172A] via-[#1E1B4B] to-[#0F172A] pb-24 pt-16 text-white">
      {/* Ambient glow */}
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <div className="absolute -right-40 -top-40 h-[600px] w-[600px] rounded-full bg-primary/20 blur-[120px]" />
        <div className="absolute -left-40 bottom-0 h-[500px] w-[500px] rounded-full bg-amber-500/10 blur-[120px]" />
      </div>

      <div className="container relative z-10">
        <div className="mx-auto max-w-3xl text-center">

          {/* Main headline */}
          <h1 className="text-5xl font-black leading-tight tracking-tight md:text-7xl">
            أستاذة{" "}
            <span className="relative">
              <span className="bg-gradient-to-r from-amber-400 to-orange-500 bg-clip-text text-transparent">
                ليلى
              </span>
            </span>
            <br />
            معلمة ذكية لطفلك في البيت
          </h1>

          <p className="mx-auto mt-6 max-w-xl text-lg leading-9 text-white/65">
            تساعد طفلك على فهم الدروس، إنجاز التمارين، ومراجعة نقاط الضعف خطوة بخطوة — حسب المنهج المغربي وبأسلوب بسيط.
          </p>

          {/* CTAs */}
          <div className="mt-10 flex flex-wrap items-center justify-center gap-4">
            <Link href="/register">
              <button className="group flex items-center gap-2 rounded-2xl bg-gradient-to-r from-primary to-emerald-500 px-8 py-4 text-base font-bold text-white shadow-lg shadow-primary/30 transition-all hover:-translate-y-0.5 hover:shadow-xl hover:shadow-primary/40">
                ابدأ 7 أيام مجاناً
                <ArrowLeft className="h-5 w-5 transition-transform group-hover:-translate-x-1" />
              </button>
            </Link>
          </div>

          {/* Benefits row */}
          <div className="mt-10 flex flex-col items-center gap-3 sm:flex-row sm:justify-center">
            {BENEFITS.map((b) => (
              <span key={b} className="flex items-center gap-2 text-sm text-white/70">
                <CheckCircle className="h-4 w-4 shrink-0 text-emerald-400" />
                {b}
              </span>
            ))}
          </div>

          {/* Trust badges */}
          <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
            {TRUST_BADGES.map((b) => (
              <span
                key={b.text}
                className="flex items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1.5 text-xs text-white/60"
              >
                {b.icon} {b.text}
              </span>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

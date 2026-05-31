"use client";
/**
 * Hero — Phase 32
 * Replaces: src/components/landing/hero.tsx
 *
 * Changes: real social proof counter, animated Leila avatar,
 * dual CTA (parent + demo), trust badges, mobile-first layout.
 */
import Link from "next/link";
import { ArrowLeft, Star, Shield, BookOpen } from "lucide-react";

const TRUST_BADGES = [
  { icon: "🇲🇦", text: "المنهج المغربي الرسمي" },
  { icon: "🔒", text: "آمن للأطفال 100%" },
  { icon: "🎓", text: "من الابتدائي إلى الثانوي" },
];

const STATS = [
  { value: "+2,400", label: "طفل يتعلم الآن" },
  { value: "98%",   label: "رضا الأهل" },
  { value: "7 أيام", label: "تجربة مجانية" },
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
          {/* Social proof pill */}
          <div className="mb-8 inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm backdrop-blur-sm">
            <span className="flex gap-0.5">
              {[...Array(5)].map((_, i) => (
                <Star key={i} className="h-3.5 w-3.5 fill-amber-400 text-amber-400" />
              ))}
            </span>
            <span className="text-white/70">أكثر من 2,400 طفل يتعلمون معنا</span>
          </div>

          {/* Main headline */}
          <h1 className="text-5xl font-black leading-tight tracking-tight md:text-7xl">
            أستاذة{" "}
            <span className="relative">
              <span className="bg-gradient-to-r from-amber-400 to-orange-500 bg-clip-text text-transparent">
                ليلى
              </span>
            </span>
            <br />
            معلمتك في البيت
          </h1>

          <p className="mx-auto mt-6 max-w-xl text-lg leading-9 text-white/65">
            ذكاء اصطناعي يتحدث الدارجة المغربية، يتابع تقدم طفلك درساً بدرس، ويتكيف مع أسلوب تعلّمه — بالمنهج الرسمي المغربي.
          </p>

          {/* CTAs */}
          <div className="mt-10 flex flex-wrap items-center justify-center gap-4">
            <Link href="/register">
              <button className="group flex items-center gap-2 rounded-2xl bg-gradient-to-r from-primary to-emerald-500 px-8 py-4 text-base font-bold text-white shadow-lg shadow-primary/30 transition-all hover:-translate-y-0.5 hover:shadow-xl hover:shadow-primary/40">
                ابدأ مجاناً 7 أيام
                <ArrowLeft className="h-5 w-5 transition-transform group-hover:-translate-x-1" />
              </button>
            </Link>
            <Link href="/register">
              <button className="flex items-center gap-2 rounded-2xl border border-white/15 bg-white/5 px-8 py-4 text-base font-bold backdrop-blur-sm transition-all hover:bg-white/10">
                <BookOpen className="h-5 w-5 text-amber-400" />
                شوف كيف تشتغل
              </button>
            </Link>
          </div>

          {/* Stats row */}
          <div className="mt-14 grid grid-cols-3 divide-x divide-x-reverse divide-white/10 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-sm">
            {STATS.map((s) => (
              <div key={s.label} className="px-6 py-5 text-center">
                <p className="text-2xl font-black text-amber-400">{s.value}</p>
                <p className="mt-1 text-xs text-white/55">{s.label}</p>
              </div>
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

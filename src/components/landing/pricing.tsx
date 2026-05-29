"use client";
/**
 * PricingSection — Phase 32
 * New file: src/components/landing/pricing.tsx
 *
 * Landing-page pricing section with toggle monthly/yearly,
 * plan cards, and school CTA. Connects to /register.
 */
import { useState } from "react";
import Link from "next/link";
import { Check, Zap, Users, Building2 } from "lucide-react";

const PLANS = [
  {
    id: "free",
    name: "مجاني",
    price: { monthly: 0, yearly: 0 },
    description: "للبداية والاكتشاف",
    icon: "🌱",
    features: ["طفل واحد", "30 دقيقة يومياً", "المستوى الأول", "5 جلسات مع ليلى / شهر"],
    cta: "ابدأ مجاناً",
    href: "/register",
    highlight: false,
  },
  {
    id: "plus",
    name: "بلس",
    price: { monthly: 49, yearly: 39 },
    description: "الأكثر شيوعاً للعائلة",
    icon: "⭐",
    features: ["طفلان", "تعلم غير محدود", "المستويات 1–3", "30 جلسة مع ليلى / شهر", "تقارير أسبوعية"],
    cta: "جرّب 7 أيام مجاناً",
    href: "/register?plan=plus",
    highlight: false,
  },
  {
    id: "premium",
    name: "بريميوم",
    price: { monthly: 99, yearly: 79 },
    description: "التجربة الكاملة مع ليلى",
    icon: "🏆",
    badge: "الأفضل قيمة",
    features: [
      "3 أطفال",
      "كل المستويات 1–6",
      "ليلى كاملة بذاكرة تكيفية",
      "تحديات مخصصة يومية",
      "تقارير تفصيلية بالذكاء الاصطناعي",
      "دعم أولوية",
    ],
    cta: "جرّب 7 أيام مجاناً",
    href: "/register?plan=premium",
    highlight: true,
  },
  {
    id: "family",
    name: "عائلي",
    price: { monthly: 149, yearly: 119 },
    description: "لعائلات أكبر",
    icon: "👨‍👩‍👧‍👦",
    features: ["حتى 5 أطفال", "كل مميزات بريميوم", "لوحة تحكم عائلية موحدة", "دعم مباشر"],
    cta: "جرّب 7 أيام مجاناً",
    href: "/register?plan=family",
    highlight: false,
  },
];

export function PricingSection() {
  const [yearly, setYearly] = useState(false);

  return (
    <section id="pricing" className="py-24">
      <div className="container">
        {/* Heading */}
        <div className="text-center">
          <span className="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-semibold text-primary">
            <Zap className="h-4 w-4" />
            أسعار شفافة بالكامل
          </span>
          <h2 className="mt-4 text-4xl font-black md:text-5xl">اختر الخطة المناسبة</h2>
          <p className="mx-auto mt-4 max-w-xl text-muted-foreground">
            ابدأ مجاناً. لا بطاقة بنكية. ألغِ في أي وقت.
          </p>
        </div>

        {/* Toggle */}
        <div className="mt-8 flex items-center justify-center gap-4">
          <span className={`text-sm font-semibold ${!yearly ? "text-foreground" : "text-muted-foreground"}`}>شهري</span>
          <button
            onClick={() => setYearly((y) => !y)}
            className={`relative h-7 w-14 rounded-full transition-colors ${yearly ? "bg-primary" : "bg-muted"}`}
          >
            <span className={`absolute top-0.5 h-6 w-6 rounded-full bg-white shadow transition-all ${yearly ? "right-0.5" : "left-0.5"}`} />
          </button>
          <span className={`text-sm font-semibold ${yearly ? "text-foreground" : "text-muted-foreground"}`}>
            سنوي <span className="rounded-full bg-emerald-100 px-2 py-0.5 text-xs text-emerald-700 font-bold">وفّر 20%</span>
          </span>
        </div>

        {/* Plan cards */}
        <div className="mt-12 grid gap-6 md:grid-cols-2 lg:grid-cols-4">
          {PLANS.map((plan) => (
            <div
              key={plan.id}
              className={`relative flex flex-col rounded-3xl border p-6 transition-all ${
                plan.highlight
                  ? "border-primary bg-gradient-to-br from-primary/5 to-emerald-50 shadow-xl shadow-primary/10 ring-2 ring-primary"
                  : "border-border bg-card hover:shadow-md"
              }`}
            >
              {plan.badge && (
                <span className="absolute -top-3.5 left-1/2 -translate-x-1/2 whitespace-nowrap rounded-full bg-primary px-4 py-1 text-xs font-bold text-white">
                  {plan.badge}
                </span>
              )}

              <div className="text-3xl">{plan.icon}</div>
              <h3 className="mt-3 text-xl font-black">{plan.name}</h3>
              <p className="text-sm text-muted-foreground">{plan.description}</p>

              {/* Price */}
              <div className="mt-4 flex items-end gap-1">
                {plan.price.monthly === 0 ? (
                  <span className="text-4xl font-black">مجاني</span>
                ) : (
                  <>
                    <span className="text-4xl font-black">
                      {yearly ? plan.price.yearly : plan.price.monthly}
                    </span>
                    <span className="mb-1.5 text-sm text-muted-foreground">درهم / شهر</span>
                  </>
                )}
              </div>
              {yearly && plan.price.monthly > 0 && (
                <p className="text-xs text-muted-foreground line-through">{plan.price.monthly} درهم / شهر</p>
              )}

              {/* Features */}
              <ul className="mt-6 flex-1 space-y-2.5">
                {plan.features.map((f) => (
                  <li key={f} className="flex items-start gap-2 text-sm">
                    <Check className="mt-0.5 h-4 w-4 shrink-0 text-primary" />
                    {f}
                  </li>
                ))}
              </ul>

              <Link href={plan.href} className="mt-8 block">
                <button
                  className={`w-full rounded-2xl py-3.5 text-sm font-bold transition-all ${
                    plan.highlight
                      ? "bg-primary text-white hover:bg-primary/90 shadow-md shadow-primary/20"
                      : "border border-border bg-background hover:bg-muted"
                  }`}
                >
                  {plan.cta}
                </button>
              </Link>
            </div>
          ))}
        </div>

        {/* School CTA */}
        <div className="mt-10 flex flex-col items-center gap-5 rounded-3xl border bg-muted/40 p-8 text-center md:flex-row md:text-right">
          <div className="flex h-16 w-16 shrink-0 items-center justify-center rounded-2xl bg-slate-200 text-3xl">
            <Building2 className="h-8 w-8 text-slate-600" />
          </div>
          <div className="flex-1">
            <h3 className="text-lg font-black">للمدارس والمؤسسات التعليمية</h3>
            <p className="mt-1 text-sm text-muted-foreground">
              رخصة مدرسية بـ 10 دراهم لكل طالب شهرياً. لوحة إدارية مخصصة. مناسب لـ DigiSchool.
            </p>
          </div>
          <a
            href="mailto:schools@oqul.ma"
            className="shrink-0 rounded-2xl border border-border bg-white px-6 py-3 text-sm font-bold transition hover:bg-muted"
          >
            تواصل معنا
          </a>
        </div>
      </div>
    </section>
  );
}

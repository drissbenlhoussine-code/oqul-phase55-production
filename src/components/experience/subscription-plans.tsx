"use client";

import { useState } from "react";
import { Check, School, Sparkles, Users } from "lucide-react";

type PlanId = "free" | "plus" | "premium" | "family";

const plans = [
  { id: "free" as const, name: "مجاني", price: 0, features: ["طفل واحد", "30 دقيقة يوميًا", "المستوى الأول", "5 جلسات مع ليلى شهريًا"] },
  { id: "plus" as const, name: "بلس", price: 49, features: ["طفلان", "تعلم غير محدود", "المستويات 1 إلى 3", "تقارير أسبوعية"] },
  { id: "premium" as const, name: "بريميوم", price: 99, popular: true, features: ["3 أطفال", "كل المستويات 1–6", "ليلى الكاملة", "تحديات يومية", "تقارير AI"] },
  { id: "family" as const, name: "عائلي", price: 149, features: ["حتى 5 أطفال", "كل مميزات بريميوم", "لوحة عائلية", "دعم أولوية"] },
];

export function SubscriptionPlans() {
  const [selected, setSelected] = useState<PlanId>("premium");

  return (
    <section className="mx-auto max-w-6xl px-4 py-12" dir="rtl">
      <div className="mb-10 text-center">
        <span className="inline-flex items-center gap-2 rounded-full bg-orange-50 px-4 py-2 text-sm font-medium text-orange-700"><Sparkles className="h-4 w-4" /> خطط بسيطة وشفافة</span>
        <h2 className="mt-4 text-4xl font-black text-slate-900">اختر الخطة المناسبة</h2>
        <p className="mt-3 text-slate-500">ابدأ مجانًا. لا بطاقة بنكية. لا التزامات.</p>
      </div>
      <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
        {plans.map((plan) => {
          const isPremium = plan.id === "premium";
          return (
            <button key={plan.id} onClick={() => setSelected(plan.id)} className={`relative flex flex-col rounded-3xl p-6 text-right transition ${isPremium ? "bg-gradient-to-br from-orange-500 to-amber-500 text-white shadow-xl ring-2 ring-orange-400" : "bg-white shadow-sm ring-1 ring-slate-100"} ${selected === plan.id && !isPremium ? "ring-2 ring-orange-400" : ""}`}>
              {plan.popular && <span className="absolute -top-3 left-1/2 -translate-x-1/2 rounded-full bg-slate-900 px-4 py-1 text-xs font-bold text-white">الأكثر شيوعًا</span>}
              <div className="mb-5 flex items-center justify-between">
                <div className={`flex h-10 w-10 items-center justify-center rounded-2xl ${isPremium ? "bg-white/20" : "bg-orange-50 text-orange-700"}`}>{plan.id === "family" ? <Users className="h-5 w-5" /> : <Sparkles className="h-5 w-5" />}</div>
                {selected === plan.id && !isPremium && <div className="flex h-6 w-6 items-center justify-center rounded-full bg-orange-500 text-white"><Check className="h-4 w-4" /></div>}
              </div>
              <h3 className="text-lg font-black">{plan.name}</h3>
              <p className="mt-2"><span className="text-3xl font-black">{plan.price === 0 ? "مجاني" : plan.price}</span>{plan.price > 0 && <span className="text-sm opacity-70"> درهم / شهريًا</span>}</p>
              <ul className="mt-5 flex-1 space-y-2">
                {plan.features.map((feature) => <li key={feature} className="flex gap-2 text-sm leading-6"><Check className="mt-0.5 h-4 w-4 shrink-0" /> {feature}</li>)}
              </ul>
              <span className={`mt-6 rounded-2xl py-3 text-center text-sm font-bold ${isPremium ? "bg-white text-orange-600" : "bg-orange-500 text-white"}`}>{plan.price === 0 ? "ابدأ مجانًا" : "اشترك الآن"}</span>
            </button>
          );
        })}
      </div>
      <div className="mt-8 flex flex-col items-center gap-4 rounded-3xl border border-slate-200 bg-white p-6 text-center shadow-sm md:flex-row md:text-right">
        <div className="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-slate-100"><School className="h-7 w-7 text-slate-600" /></div>
        <div className="flex-1"><h3 className="font-black text-slate-900">للمدارس والمؤسسات</h3><p className="mt-1 text-sm text-slate-500">ترخيص خاص بأسعار مخفضة، ولوحة إدارية مخصصة.</p></div>
      </div>
    </section>
  );
}

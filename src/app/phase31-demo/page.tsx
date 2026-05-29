"use client";

import { notFound } from "next/navigation";
import { useState } from "react";
import { OnboardingFlow } from "@/components/experience/onboarding-flow";
import { SubscriptionPlans } from "@/components/experience/subscription-plans";

type Tab = "onboarding" | "plans";

function OriginalPage() {
  const [tab, setTab] = useState<Tab>("onboarding");

  return (
    <main className="min-h-screen bg-[#F7F0E3]" dir="rtl">
      <div className="bg-gradient-to-br from-[#1A1025] to-[#2D1B4E] px-5 py-6 text-white">
        <div className="mx-auto max-w-4xl">
          <h1 className="text-xl font-black">Oqul — Launch Experience</h1>
          <p className="text-sm text-white/60">Onboarding + Pricing preview</p>
          <div className="mt-5 flex gap-2">
            <button onClick={() => setTab("onboarding")} className={`rounded-2xl px-4 py-2 text-sm font-bold ${tab === "onboarding" ? "bg-orange-500 text-white" : "bg-white/10 text-white/70"}`}>🚀 Onboarding</button>
            <button onClick={() => setTab("plans")} className={`rounded-2xl px-4 py-2 text-sm font-bold ${tab === "plans" ? "bg-orange-500 text-white" : "bg-white/10 text-white/70"}`}>💎 الاشتراكات</button>
          </div>
        </div>
      </div>
      <div className="mx-auto max-w-4xl px-4 py-10">
        {tab === "onboarding" ? <OnboardingFlow onComplete={(data) => console.log("Onboarding complete:", data)} /> : <SubscriptionPlans />}
      </div>
    </main>
  );
}


export default function Page() {
  if (process.env.NODE_ENV === "production") notFound();
  return <OriginalPage />;
}

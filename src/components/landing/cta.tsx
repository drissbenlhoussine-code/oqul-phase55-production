import { ArrowLeft, Sparkles } from "lucide-react";
import Link from "next/link";
import { Button } from "@/components/ui/button";

export function CTA() {
  return (
    <section className="py-24">
      <div className="container">
        <div className="relative overflow-hidden rounded-[2.5rem] bg-brand-indigo p-10 text-center text-white shadow-glow md:p-16">
          <div className="absolute inset-0 bg-brand-radial" />
          <div className="absolute inset-0 moroccan-pattern opacity-70" />
          <div className="relative mx-auto max-w-3xl">
            <Sparkles className="mx-auto h-12 w-12 text-secondary" />
            <h2 className="mt-6 text-4xl font-black leading-tight md:text-6xl">ابدأ رحلة طفلك التعليمية اليوم</h2>
            <p className="mt-5 text-xl leading-9 text-white/75">
              تجربة موجهة، ذكية، ومناسبة للبيت المغربي. ابدأ مجانًا وراقب التقدم خطوة بخطوة.
            </p>
            <Link href="/register" className="inline-flex">
              <Button size="lg" variant="secondary" className="mt-9 text-lg">
                ابدأ 7 أيام مجاناً <ArrowLeft className="h-5 w-5" />
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

import Link from "next/link";
import { Check, Clock } from "lucide-react";

const INCLUDES = [
  "جميع المستويات: الابتدائي، الإعدادي، والثانوي التأهيلي",
  "جميع المواد المتوفرة",
  "دروس وتمارين حسب المنهج المغربي",
  "أستاذة ليلى للمساعدة خطوة بخطوة",
  "تتبع تقدم الطفل",
  "تقارير مبسطة لولي الأمر",
  "حساب ولي الأمر + حساب الطفل",
];

const COMING_SOON = [
  "ليلى بالصوت",
  "شرح صوتي للدروس",
  "محادثة صوتية مع ليلى",
  "تقارير أعمق لولي الأمر",
];

export function PricingSection() {
  return (
    <section id="pricing" className="py-24">
      <div className="container">
        {/* Heading */}
        <div className="text-center">
          <h2 className="text-4xl font-black md:text-5xl">خطة واحدة. كل شيء مشمول.</h2>
          <p className="mx-auto mt-4 max-w-md text-muted-foreground">
            لا تعقيد في الأسعار. لا خطط مربكة. كل ما يحتاجه طفلك للتعلم من البيت.
          </p>
        </div>

        <div className="mt-14 mx-auto max-w-lg">
          {/* Main plan card */}
          <div className="relative rounded-3xl border-2 border-primary bg-gradient-to-br from-primary/5 to-emerald-50 p-8 shadow-xl shadow-primary/10 ring-2 ring-primary">
            {/* Badge */}
            <span className="absolute -top-4 left-1/2 -translate-x-1/2 whitespace-nowrap rounded-full bg-primary px-5 py-1.5 text-sm font-bold text-white shadow-md">
              🎁 جرّب 7 أيام مجاناً
            </span>

            <div className="text-center">
              <p className="text-sm font-semibold uppercase tracking-widest text-primary">الخطة الكاملة</p>
              <h3 className="mt-1 text-3xl font-black">عقول الكامل</h3>
              <p className="mt-2 text-muted-foreground">كل ما يحتاجه طفلك للتعلم من البيت.</p>

              {/* Price */}
              <div className="mt-6 flex items-end justify-center gap-2">
                <span className="text-7xl font-black text-foreground leading-none">20</span>
                <span className="mb-2 text-xl font-semibold text-muted-foreground">درهم / شهر</span>
              </div>
            </div>

            {/* Feature list */}
            <ul className="mt-8 space-y-3">
              {INCLUDES.map((f) => (
                <li key={f} className="flex items-start gap-3 text-sm">
                  <Check className="mt-0.5 h-5 w-5 shrink-0 text-primary" />
                  <span>{f}</span>
                </li>
              ))}
            </ul>

            {/* CTA */}
            <Link href="/register" className="mt-8 block">
              <button className="w-full rounded-2xl bg-primary py-4 text-base font-bold text-white shadow-md shadow-primary/20 transition-all hover:bg-primary/90 hover:shadow-lg hover:shadow-primary/30">
                ابدأ 7 أيام مجاناً
              </button>
            </Link>

            {/* Fine print */}
            <p className="mt-4 text-center text-xs text-muted-foreground">
              بدون بطاقة بنكية. يمكنك الإلغاء في أي وقت.
            </p>
          </div>

          {/* Coming soon card */}
          <div className="mt-6 rounded-3xl border border-dashed border-border bg-muted/30 p-6">
            <div className="flex items-start gap-4">
              <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-muted">
                <Clock className="h-5 w-5 text-muted-foreground" />
              </div>
              <div className="flex-1">
                <div className="flex items-center gap-2">
                  <h4 className="font-bold">قريباً: عقول بلس</h4>
                  <span className="rounded-full bg-amber-100 px-2.5 py-0.5 text-xs font-semibold text-amber-700">
                    قريباً
                  </span>
                </div>
                <p className="mt-1 text-sm text-muted-foreground">سيضيف مستقبلاً:</p>
                <ul className="mt-2 space-y-1.5">
                  {COMING_SOON.map((f) => (
                    <li key={f} className="flex items-center gap-2 text-sm text-muted-foreground">
                      <span className="h-1.5 w-1.5 shrink-0 rounded-full bg-muted-foreground/40" />
                      {f}
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

/**
 * /faq — الأسئلة الشائعة
 * New file: src/app/faq/page.tsx
 */
import Link from "next/link";
import { Brain } from "lucide-react";

export const metadata = {
  title: "الأسئلة الشائعة — عقول",
  description: "إجابات على أكثر الأسئلة شيوعاً حول منصة عقول التعليمية",
};

const FAQS = [
  {
    q: "ما الفرق بين عقول والدروس الخصوصية التقليدية؟",
    a: "عقول لا يهدف لاستبدال المعلم البشري، بل يكمّله. أستاذة ليلى متاحة 24/7، تتكيف مع مستوى كل طفل، وتتذكر نقاط ضعفه لتركز عليها — وهذا صعب تحقيقه في الدروس الخصوصية التقليدية.",
  },
  {
    q: "هل المحتوى يتوافق مع المنهج المغربي الرسمي؟",
    a: "نعم. عقول يغطي المنهج الرسمي للمملكة المغربية من الابتدائي إلى الثانوي التأهيلي، بما في ذلك اللغة العربية، الرياضيات، الفرنسية، والتربية الإسلامية.",
  },
  {
    q: "هل أستاذة ليلى آمنة للأطفال؟",
    a: "تماماً. ليلى مضبوطة بقواعد صارمة للمحتوى الآمن، لا تستطيع الحديث عن مواضيع غير تعليمية، ولا تجمع أي معلومات شخصية من الأطفال. جميع المحادثات مراقبة.",
  },
  {
    q: "كيف يمكنني متابعة تقدم ابني؟",
    a: "لوحة التحكم الخاصة بولي الأمر تُظهر تقارير أسبوعية مفصلة: الدروس المكتملة، معدل الأداء، نقاط القوة والضعف، ووقت التعلم اليومي.",
  },
  {
    q: "ماذا يحدث بعد انتهاء التجربة المجانية؟",
    a: "بعد انتهاء الأيام السبع المجانية، يمكنك الاشتراك في عقول الكامل بـ 20 درهماً في الشهر. لا يتم خصم أي مبلغ تلقائياً — يجب أن تختار الاشتراك بنفسك.",
  },
  {
    q: "هل يعمل عقول على الهاتف؟",
    a: "نعم، عقول يعمل على جميع الأجهزة — الحاسوب، الهاتف الذكي، والتابلت — عبر المتصفح مباشرة. لا يحتاج لتحميل تطبيق.",
  },
  {
    q: "هل يمكنني إلغاء الاشتراك في أي وقت؟",
    a: "نعم، يمكنك إلغاء اشتراكك في أي وقت من إعدادات الحساب. لا توجد رسوم إلغاء.",
  },
  {
    q: "هل عقول متاح بالأمازيغية؟",
    a: "أستاذة ليلى تتحدث الدارجة المغربية بشكل أساسي. نعمل حالياً على إضافة دعم أفضل للأمازيغية في الإصدارات القادمة.",
  },
];

export default function FAQPage() {
  return (
    <main className="min-h-screen bg-background" dir="rtl">
      {/* Header */}
      <div className="border-b bg-muted/30 px-5 py-10 text-center">
        <Link href="/" className="inline-flex items-center gap-2 mb-6">
          <span className="grid h-9 w-9 place-items-center rounded-xl bg-primary text-primary-foreground">
            <Brain className="h-5 w-5" />
          </span>
          <span className="text-xl font-black">عقول</span>
        </Link>
        <h1 className="text-3xl font-black">الأسئلة الشائعة</h1>
        <p className="mt-2 text-muted-foreground text-sm">إجابات على ما يدور في ذهنك</p>
      </div>

      <div className="mx-auto max-w-2xl px-5 py-12 space-y-4">
        {FAQS.map((item, i) => (
          <details
            key={i}
            className="group rounded-2xl border bg-card px-6 py-5 open:shadow-sm transition-all"
          >
            <summary className="flex cursor-pointer items-center justify-between gap-4 font-bold text-base list-none">
              {item.q}
              <span className="shrink-0 text-xl text-muted-foreground transition-transform group-open:rotate-45">+</span>
            </summary>
            <p className="mt-4 text-sm leading-8 text-muted-foreground">{item.a}</p>
          </details>
        ))}

        {/* CTA */}
        <div className="rounded-2xl bg-primary/5 border border-primary/20 p-6 text-center mt-8">
          <p className="font-bold text-lg mb-2">لم تجد إجابتك؟</p>
          <p className="text-sm text-muted-foreground mb-4">فريق الدعم جاهز للمساعدة</p>
          <a
            href="mailto:support@oqul.ma"
            className="inline-flex items-center gap-2 rounded-2xl bg-primary px-6 py-3 text-sm font-bold text-white hover:bg-primary/90 transition"
          >
            راسلنا مباشرة
          </a>
        </div>

        <div className="text-center mt-4">
          <Link href="/" className="text-sm text-muted-foreground hover:text-foreground transition">
            العودة للرئيسية
          </Link>
        </div>
      </div>
    </main>
  );
}

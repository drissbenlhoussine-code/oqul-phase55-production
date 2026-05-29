/**
 * /terms — شروط الاستخدام
 */
import Link from "next/link";

export const metadata = {
  title: "شروط الاستخدام — Oqul",
  description: "شروط وأحكام استخدام تطبيق Oqul التعليمي",
};

export default function TermsPage() {
  return (
    <main className="min-h-screen bg-[#F7F0E3]" dir="rtl">
      <div className="bg-gradient-to-br from-[#1A1025] to-[#2D1B4E] px-5 py-8 text-center">
        <Link href="/" className="inline-flex items-center gap-2 mb-6">
          <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-orange-500 to-amber-400 text-lg">
            📚
          </div>
          <span className="text-xl font-black text-white">Oqul</span>
        </Link>
        <h1 className="text-3xl font-black text-white">شروط الاستخدام</h1>
        <p className="mt-2 text-white/60 text-sm">آخر تحديث: مايو 2026</p>
      </div>

      <div className="mx-auto max-w-2xl px-5 py-12 space-y-8">

        <section className="rounded-3xl bg-emerald-50 border border-emerald-200 p-6">
          <h2 className="text-lg font-black text-emerald-800 mb-3">📋 ملخص سريع</h2>
          <p className="text-emerald-700 leading-8 text-sm">
            Oqul منصة تعليمية للأطفال المغاربة. باستخدامك للتطبيق، توافق على هذه الشروط.
            التسجيل مخصص لأولياء الأمور فقط.
          </p>
        </section>

        <TermsSection title="1. من يمكنه استخدام Oqul؟">
          <ul className="space-y-2 text-sm">
            <li className="flex gap-2"><span className="text-emerald-500 mt-1">•</span><span>يجب أن يكون المسجّل ولياً للأمر أو وصياً قانونياً على الطفل المستخدم.</span></li>
            <li className="flex gap-2"><span className="text-emerald-500 mt-1">•</span><span>الأطفال يستخدمون التطبيق تحت إشراف وليّ أمرهم.</span></li>
            <li className="flex gap-2"><span className="text-emerald-500 mt-1">•</span><span>يجب تقديم معلومات صحيحة عند التسجيل.</span></li>
          </ul>
        </TermsSection>

        <TermsSection title="2. ماذا يمكنك فعله؟">
          <ul className="space-y-2 text-sm">
            <li className="flex gap-2"><span className="text-emerald-500 mt-1">•</span><span>استخدام التطبيق لأغراض تعليمية شخصية وغير تجارية.</span></li>
            <li className="flex gap-2"><span className="text-emerald-500 mt-1">•</span><span>إنشاء ملفات لأطفالك وتتبع تقدمهم.</span></li>
            <li className="flex gap-2"><span className="text-emerald-500 mt-1">•</span><span>الوصول لجميع المحتوى المتاح ضمن خطتك.</span></li>
          </ul>
        </TermsSection>

        <TermsSection title="3. ما الذي لا يجوز؟">
          <ul className="space-y-2 text-sm">
            <li className="flex gap-2"><span className="text-red-400 mt-1">•</span><span>مشاركة حسابك مع أشخاص آخرين من خارج العائلة.</span></li>
            <li className="flex gap-2"><span className="text-red-400 mt-1">•</span><span>محاولة اختراق أنظمتنا أو استخراج المحتوى التعليمي.</span></li>
            <li className="flex gap-2"><span className="text-red-400 mt-1">•</span><span>إساءة استخدام أستاذة ليلى أو توجيه محتوى غير لائق إليها.</span></li>
          </ul>
        </TermsSection>

        <TermsSection title="4. الاشتراكات والدفع">
          <ul className="space-y-2 text-sm">
            <li className="flex gap-2"><span className="text-emerald-500 mt-1">•</span><span>الخطة المجانية متاحة دائماً مع محدودية في الميزات.</span></li>
            <li className="flex gap-2"><span className="text-emerald-500 mt-1">•</span><span>يمكن إلغاء الاشتراك في أي وقت.</span></li>
            <li className="flex gap-2"><span className="text-emerald-500 mt-1">•</span><span>لا يوجد استرداد للمبالغ عن فترات الاشتراك المستخدمة.</span></li>
          </ul>
        </TermsSection>

        <TermsSection title="5. المحتوى التعليمي">
          <p className="text-sm leading-8">
            جميع المحتوى التعليمي في Oqul محمي بحقوق الملكية الفكرية. لا يجوز نسخه أو توزيعه
            لأغراض تجارية. المحتوى الذي ينتجه الذكاء الاصطناعي لأغراض تعليمية فقط.
          </p>
        </TermsSection>

        <TermsSection title="6. تعديل الشروط">
          <p className="text-sm leading-8">
            نحتفظ بحق تعديل هذه الشروط. سنخطرك بأي تغييرات جوهرية عبر البريد الإلكتروني.
            استمرارك في استخدام التطبيق بعد التعديل يعني موافقتك على الشروط الجديدة.
          </p>
        </TermsSection>

        <TermsSection title="7. التواصل">
          <p className="text-sm leading-8">
            لأي استفسار قانوني:
            <br />
            📧 <a href="mailto:legal@oqul.ma" className="text-emerald-600 hover:underline">legal@oqul.ma</a>
          </p>
        </TermsSection>

        <div className="text-center pt-4">
          <Link href="/privacy" className="text-sm text-emerald-600 hover:underline mx-4">سياسة الخصوصية</Link>
          <Link href="/"        className="text-sm text-slate-500 hover:underline mx-4">العودة للرئيسية</Link>
        </div>
      </div>
    </main>
  );
}

function TermsSection({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="rounded-3xl bg-white p-6 shadow-sm">
      <h2 className="text-base font-black text-slate-900 mb-4">{title}</h2>
      <div className="text-slate-700 leading-8">{children}</div>
    </section>
  );
}

/**
 * /privacy — سياسة الخصوصية
 * مطابقة لمتطلبات حماية بيانات الأطفال
 */
import Link from "next/link";

export const metadata = {
  title: "سياسة الخصوصية — Oqul",
  description: "كيف نحمي بيانات أطفالك في تطبيق Oqul",
};

export default function PrivacyPage() {
  return (
    <main className="min-h-screen bg-[#F7F0E3]" dir="rtl">
      {/* Header */}
      <div className="bg-gradient-to-br from-[#1A1025] to-[#2D1B4E] px-5 py-8 text-center">
        <Link href="/" className="inline-flex items-center gap-2 mb-6">
          <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-orange-500 to-amber-400 text-lg">
            📚
          </div>
          <span className="text-xl font-black text-white">Oqul</span>
        </Link>
        <h1 className="text-3xl font-black text-white">سياسة الخصوصية</h1>
        <p className="mt-2 text-white/60 text-sm">آخر تحديث: مايو 2026</p>
      </div>

      {/* Content */}
      <div className="mx-auto max-w-2xl px-5 py-12 space-y-8">

        <section className="rounded-3xl bg-orange-50 border border-orange-200 p-6">
          <h2 className="text-lg font-black text-orange-800 mb-3">🧒 حماية بيانات الأطفال أولويتنا</h2>
          <p className="text-orange-700 leading-8 text-sm">
            Oqul مصمم للأطفال المغاربة. نأخذ حماية خصوصية الأطفال بجدية بالغة ونلتزم بالمعايير الدولية لحماية بيانات القاصرين.
          </p>
        </section>

        <PolicySection title="1. ما البيانات التي نجمعها؟">
          <ul className="space-y-2 text-sm">
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span><strong>بيانات ولي الأمر:</strong> الاسم الكامل، البريد الإلكتروني، كلمة المرور (مشفرة).</span></li>
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span><strong>بيانات الطفل:</strong> الاسم الأول فقط، المستوى الدراسي، التقدم التعليمي، نقاط الخبرة.</span></li>
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span><strong>بيانات الاستخدام:</strong> وقت التعلم، الدروس المكتملة، نتائج الاختبارات.</span></li>
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span><strong>بيانات تقنية:</strong> عنوان IP، نوع المتصفح، للأغراض الأمنية فقط.</span></li>
          </ul>
        </PolicySection>

        <PolicySection title="2. كيف نستخدم البيانات؟">
          <ul className="space-y-2 text-sm">
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span>تخصيص تجربة التعلم مع أستاذة ليلى.</span></li>
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span>تتبع التقدم التعليمي وتقديم تقارير لولي الأمر.</span></li>
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span>تحسين المنهج الدراسي.</span></li>
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span><strong>لا نبيع بياناتك لأي طرف ثالث.</strong></span></li>
          </ul>
        </PolicySection>

        <PolicySection title="3. أمان البيانات">
          <p className="text-sm leading-8">
            نستخدم تشفيراً من الدرجة البنكية (bcrypt + JWT). كلمات المرور لا تُخزّن بصيغتها الأصلية أبداً.
            جميع الاتصالات مشفرة بـ HTTPS. لا يمكن لأحد من فريقنا الاطلاع على كلمة مرورك.
          </p>
        </PolicySection>

        <PolicySection title="4. بيانات الأطفال — ضمانات خاصة">
          <ul className="space-y-2 text-sm">
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span>لا نجمع معلومات شخصية مفصّلة عن الأطفال (لا صور، لا عناوين، لا أرقام هواتف).</span></li>
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span>ليلى (الذكاء الاصطناعي) مضبوطة بقواعد صارمة للمحتوى الآمن للأطفال.</span></li>
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span>لا توجد إعلانات مستهدفة للأطفال.</span></li>
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span>ولي الأمر يتحكم بالكامل في بيانات طفله.</span></li>
          </ul>
        </PolicySection>

        <PolicySection title="5. حقوقك">
          <ul className="space-y-2 text-sm">
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span><strong>الاطلاع:</strong> يمكنك طلب نسخة من بياناتك في أي وقت.</span></li>
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span><strong>التصحيح:</strong> يمكنك تعديل بياناتك من لوحة التحكم.</span></li>
            <li className="flex gap-2"><span className="text-orange-500 mt-1">•</span><span><strong>الحذف:</strong> يمكنك طلب حذف حسابك وجميع البيانات المرتبطة به.</span></li>
          </ul>
        </PolicySection>

        <PolicySection title="6. التواصل معنا">
          <p className="text-sm leading-8">
            لأي استفسار حول خصوصيتك:
            <br />
            📧 <a href="mailto:privacy@oqul.ma" className="text-orange-600 hover:underline">privacy@oqul.ma</a>
          </p>
        </PolicySection>

        <div className="text-center pt-4">
          <Link href="/terms" className="text-sm text-orange-600 hover:underline mx-4">شروط الاستخدام</Link>
          <Link href="/"     className="text-sm text-slate-500 hover:underline mx-4">العودة للرئيسية</Link>
        </div>
      </div>
    </main>
  );
}

function PolicySection({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="rounded-3xl bg-white p-6 shadow-sm">
      <h2 className="text-base font-black text-slate-900 mb-4">{title}</h2>
      <div className="text-slate-700 leading-8">{children}</div>
    </section>
  );
}

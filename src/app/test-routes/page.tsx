import { notFound } from "next/navigation";

import Link from "next/link";

const routes = [
  { href: "/", label: "الصفحة الرئيسية" },
  { href: "/login", label: "تسجيل الدخول" },
  { href: "/register", label: "إنشاء حساب" },
  { href: "/forgot-password", label: "نسيت كلمة المرور" },
  { href: "/faq", label: "الأسئلة الشائعة" },
  { href: "/privacy", label: "سياسة الخصوصية" },
  { href: "/terms", label: "شروط الاستخدام" },
  { href: "/visual-demo", label: "العرض المرئي" },
  { href: "/phase31-demo", label: "Phase 31 Demo" },
];

function OriginalPage() {
  return (
    <main className="min-h-screen bg-background p-6">
      <div className="container max-w-3xl py-12">
        <h1 className="text-3xl font-black">اختبار روابط عقول</h1>
        <p className="mt-3 text-muted-foreground">
          هذه الصفحة للتأكد أن المسارات العامة والأزرار الأساسية تعمل بعد الدمج النهائي.
        </p>
        <div className="mt-8 grid gap-3 sm:grid-cols-2">
          {routes.map((route) => (
            <Link
              key={route.href}
              href={route.href}
              className="rounded-2xl border bg-card p-4 font-bold transition hover:border-primary hover:text-primary"
            >
              {route.label}
              <span className="mt-1 block text-xs font-normal text-muted-foreground">{route.href}</span>
            </Link>
          ))}
        </div>
      </div>
    </main>
  );
}


export default function Page() {
  if (process.env.NODE_ENV === "production") notFound();
  return <OriginalPage />;
}

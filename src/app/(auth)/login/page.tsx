"use client";
/**
 * Login Page — Phase 34 Fix
 * Path: src/app/(auth)/login/page.tsx
 *
 * Fixes:
 *  1. Added "نسيت كلمة المرور؟" link next to password label
 *  2. Added ?verified=1 and ?error= banners from email verification redirect
 *  3. Removed public demo hint (security)
 *  4. Wrapped in Suspense (required for useSearchParams in Next.js 15)
 *
 * All login logic unchanged.
 */
import { useState, Suspense } from "react";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { Star } from "lucide-react";
import { Button }      from "@/components/ui/button";
import { Input }       from "@/components/ui/input";
import { Label }       from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { useToast }    from "@/components/ui/toast";
import { Spinner }     from "@/components/ui/spinner";

function LoginForm() {
  const router    = useRouter();
  const params    = useSearchParams();
  const { toast } = useToast();
  const [loading, setLoading] = useState(false);
  const [form, setForm] = useState({ email: "", password: "" });

  const verified = params.get("verified");
  const error    = params.get("error");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch("/api/auth/login", {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify(form),
      });
      const data = await res.json();
      if (!data.success) throw new Error(data.message);
      toast("مرحباً بعودتك! 👋", "success");
      router.push("/dashboard");
      router.refresh();
    } catch (err: unknown) {
      toast(err instanceof Error ? err.message : "حدث خطأ", "error");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-emerald-50 to-amber-50 p-4">
      <div className="w-full max-w-md">

        <div className="text-center mb-8">
          <div className="w-14 h-14 rounded-2xl bg-primary mx-auto mb-4 flex items-center justify-center">
            <Star className="w-8 h-8 text-white" />
          </div>
          <h1 className="text-2xl font-bold">عقول</h1>
        </div>

        {/* Email verified success banner */}
        {verified && (
          <div className="mb-4 rounded-xl bg-emerald-50 border border-emerald-200 px-4 py-3 text-sm text-emerald-800 text-center">
            ✅ تم تأكيد بريدك الإلكتروني. سجّل دخولك الآن!
          </div>
        )}

        {/* Error banners from verify-email redirect */}
        {error === "token_expired" && (
          <div className="mb-4 rounded-xl bg-amber-50 border border-amber-200 px-4 py-3 text-sm text-amber-800 text-center">
            انتهت صلاحية رابط التأكيد. سجّل دخولك وسنرسل لك رابطاً جديداً.
          </div>
        )}
        {error === "invalid_token" && (
          <div className="mb-4 rounded-xl bg-red-50 border border-red-200 px-4 py-3 text-sm text-red-700 text-center">
            رابط غير صالح. تواصل معنا إذا استمرت المشكلة.
          </div>
        )}

        <Card>
          <CardHeader>
            <CardTitle>تسجيل الدخول</CardTitle>
            <CardDescription>أدخل بيانات حسابك للمتابعة</CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="email">البريد الإلكتروني</Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="example@gmail.com"
                  autoComplete="email"
                  required
                  value={form.email}
                  onChange={(e) => setForm({ ...form, email: e.target.value })}
                />
              </div>
              <div className="space-y-2">
                {/* Password row with forgot-password link */}
                <div className="flex items-center justify-between">
                  <Label htmlFor="password">كلمة المرور</Label>
                  <Link
                    href="/forgot-password"
                    className="text-xs text-primary hover:underline transition-colors"
                  >
                    نسيت كلمة المرور؟
                  </Link>
                </div>
                <Input
                  id="password"
                  type="password"
                  placeholder="••••••••"
                  autoComplete="current-password"
                  required
                  value={form.password}
                  onChange={(e) => setForm({ ...form, password: e.target.value })}
                />
              </div>
              <Button type="submit" className="w-full" disabled={loading}>
                {loading ? <Spinner className="w-4 h-4" /> : "دخول"}
              </Button>
            </form>

            <p className="text-center text-sm text-muted-foreground mt-4">
              ليس لديك حساب؟{" "}
              <Link href="/register" className="text-primary hover:underline font-medium">
                سجّل الآن
              </Link>
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

export default function LoginPage() {
  return (
    <Suspense>
      <LoginForm />
    </Suspense>
  );
}

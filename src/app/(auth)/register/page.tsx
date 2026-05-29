"use client";
import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { Star } from "lucide-react";
import { Button }      from "@/components/ui/button";
import { Input }       from "@/components/ui/input";
import { Label }       from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { useToast }   from "@/components/ui/toast";
import { Spinner }    from "@/components/ui/spinner";

export default function RegisterPage() {
  const router     = useRouter();
  const { toast }  = useToast();
  const [loading, setLoading] = useState(false);
  const [form, setForm] = useState({
    fullName:      "",
    email:         "",
    password:      "",
    termsAccepted: false,
  });

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (form.password.length < 8) { toast("كلمة المرور 8 أحرف على الأقل", "error"); return; }
    if (!form.termsAccepted)      { toast("يجب الموافقة على الشروط وسياسة الخصوصية", "error"); return; }

    setLoading(true);
    try {
      const res  = await fetch("/api/auth/register", {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify({ ...form, termsAccepted: true }),
      });
      const data = await res.json();
      if (!data.success) throw new Error(data.message);
      toast("تم إنشاء حسابك! تحقق من بريدك للتأكيد 📧", "success");
      router.push("/onboarding");
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
          <p className="text-sm text-muted-foreground mt-1">تجربة مجانية 7 أيام 🎁</p>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>إنشاء حساب جديد</CardTitle>
            <CardDescription>انضم لآلاف الأطفال المغاربة الذين يتعلمون مع ليلى</CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label>الاسم الكامل</Label>
                <Input
                  placeholder="محمد الأمين"
                  required
                  value={form.fullName}
                  onChange={(e) => setForm({ ...form, fullName: e.target.value })}
                />
              </div>

              <div className="space-y-2">
                <Label>البريد الإلكتروني</Label>
                <Input
                  type="email"
                  placeholder="example@gmail.com"
                  required
                  value={form.email}
                  onChange={(e) => setForm({ ...form, email: e.target.value })}
                />
              </div>

              <div className="space-y-2">
                <Label>كلمة المرور</Label>
                <Input
                  type="password"
                  placeholder="8 أحرف على الأقل"
                  required
                  value={form.password}
                  onChange={(e) => setForm({ ...form, password: e.target.value })}
                />
              </div>

              {/* Terms checkbox — Phase 31 */}
              <div className="flex items-start gap-3 rounded-xl bg-amber-50 border border-amber-200 p-3">
                <input
                  type="checkbox"
                  id="terms"
                  checked={form.termsAccepted}
                  onChange={(e) => setForm({ ...form, termsAccepted: e.target.checked })}
                  className="mt-0.5 h-4 w-4 rounded border-gray-300 accent-orange-500 cursor-pointer"
                  required
                />
                <label htmlFor="terms" className="text-sm text-slate-700 leading-6 cursor-pointer">
                  أوافق على{" "}
                  <Link href="/terms"   target="_blank" className="text-orange-600 hover:underline font-medium">شروط الاستخدام</Link>
                  {" "}و{" "}
                  <Link href="/privacy" target="_blank" className="text-orange-600 hover:underline font-medium">سياسة الخصوصية</Link>
                  ، وأقرّ بأنني ولي أمر الطفل المستخدم للتطبيق.
                </label>
              </div>

              <Button type="submit" className="w-full" disabled={loading || !form.termsAccepted}>
                {loading ? <Spinner className="w-4 h-4" /> : "ابدأ التجربة المجانية"}
              </Button>
            </form>

            <p className="text-center text-sm text-muted-foreground mt-4">
              لديك حساب؟{" "}
              <Link href="/login" className="text-primary hover:underline font-medium">سجّل الدخول</Link>
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

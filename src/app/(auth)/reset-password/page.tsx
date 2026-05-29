"use client";
import { useState, Suspense } from "react";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { Lock } from "lucide-react";
import { Button }  from "@/components/ui/button";
import { Input }   from "@/components/ui/input";
import { Label }   from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { useToast } from "@/components/ui/toast";
import { Spinner }  from "@/components/ui/spinner";

function ResetForm() {
  const router        = useRouter();
  const params        = useSearchParams();
  const { toast }     = useToast();
  const token         = params.get("token") ?? "";
  const [loading, setLoading]   = useState(false);
  const [password, setPassword] = useState("");
  const [confirm, setConfirm]   = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (password !== confirm) { toast("كلمتا المرور غير متطابقتين", "error"); return; }
    if (!token)               { toast("الرابط غير صالح", "error"); return; }

    setLoading(true);
    try {
      const res  = await fetch("/api/auth/reset-password", {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify({ token, password }),
      });
      const data = await res.json();
      if (!data.success) throw new Error(data.message);
      toast("تم تغيير كلمة المرور بنجاح! 🎉", "success");
      router.push("/login");
    } catch (err: unknown) {
      toast(err instanceof Error ? err.message : "حدث خطأ", "error");
    } finally {
      setLoading(false);
    }
  }

  if (!token) {
    return (
      <div className="text-center py-12">
        <p className="text-destructive font-medium">رابط غير صالح. اطلب رابطاً جديداً.</p>
        <Link href="/forgot-password" className="text-primary hover:underline text-sm mt-4 block">
          طلب رابط جديد
        </Link>
      </div>
    );
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle>كلمة مرور جديدة</CardTitle>
        <CardDescription>اختر كلمة مرور قوية لحسابك</CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="space-y-2">
            <Label>كلمة المرور الجديدة</Label>
            <Input
              type="password"
              placeholder="8 أحرف على الأقل"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className="space-y-2">
            <Label>تأكيد كلمة المرور</Label>
            <Input
              type="password"
              placeholder="أعد كتابة كلمة المرور"
              required
              value={confirm}
              onChange={(e) => setConfirm(e.target.value)}
            />
          </div>
          <Button type="submit" className="w-full" disabled={loading}>
            {loading ? <Spinner className="w-4 h-4" /> : "تغيير كلمة المرور"}
          </Button>
        </form>
      </CardContent>
    </Card>
  );
}

export default function ResetPasswordPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-emerald-50 to-amber-50 p-4">
      <div className="w-full max-w-md">
        <div className="text-center mb-8">
          <div className="w-14 h-14 rounded-2xl bg-primary mx-auto mb-4 flex items-center justify-center">
            <Lock className="w-8 h-8 text-white" />
          </div>
          <h1 className="text-2xl font-bold">إعادة تعيين كلمة المرور</h1>
        </div>
        <Suspense fallback={<div className="text-center py-8"><Spinner className="w-6 h-6 mx-auto" /></div>}>
          <ResetForm />
        </Suspense>
        <p className="text-center text-sm text-muted-foreground mt-4">
          <Link href="/login" className="text-primary hover:underline font-medium">
            العودة لتسجيل الدخول
          </Link>
        </p>
      </div>
    </div>
  );
}

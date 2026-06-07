"use client";

import { useState } from "react";
import Link from "next/link";
import { Key } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { useToast } from "@/components/ui/toast";
import { Spinner } from "@/components/ui/spinner";

type ForgotPasswordResponse = {
  success?: boolean;
  message?: string;
  code?: string;
};

async function readJsonSafely(response: Response): Promise<ForgotPasswordResponse> {
  const text = await response.text();

  if (!text.trim()) {
    return {
      success: false,
      code: "EMPTY_RESPONSE",
      message: "تعذر قراءة رد الخادم. حاول مرة أخرى بعد قليل.",
    };
  }

  try {
    return JSON.parse(text) as ForgotPasswordResponse;
  } catch {
    return {
      success: false,
      code: "INVALID_JSON_RESPONSE",
      message: "وصل رد غير متوقع من الخادم. حاول مرة أخرى بعد قليل.",
    };
  }
}

export default function ForgotPasswordPage() {
  const { toast } = useToast();
  const [loading, setLoading] = useState(false);
  const [sent, setSent] = useState(false);
  const [email, setEmail] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await fetch("/api/auth/forgot-password", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });
      const data = await readJsonSafely(res);

      if (!res.ok || !data.success) {
        throw new Error(data.message ?? "تعذر إرسال رابط الاسترداد الآن. حاول مرة أخرى بعد قليل.");
      }

      setSent(true);
    } catch (err: unknown) {
      toast(err instanceof Error ? err.message : "حدث خطأ غير متوقع", "error");
    } finally {
      setLoading(false);
    }
  }

  if (sent) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-emerald-50 to-amber-50 p-4">
        <div className="w-full max-w-md text-center">
          <div className="text-6xl mb-6">📧</div>
          <h1 className="text-2xl font-bold mb-3">تحقق من بريدك</h1>
          <p className="text-muted-foreground mb-6">
            أرسلنا رابط إعادة التعيين إلى <strong>{email}</strong>.
            الرابط صالح لساعة واحدة.
          </p>
          <Link href="/login" className="text-primary hover:underline text-sm font-medium">
            العودة لتسجيل الدخول
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-emerald-50 to-amber-50 p-4">
      <div className="w-full max-w-md">
        <div className="text-center mb-8">
          <div className="w-14 h-14 rounded-2xl bg-primary mx-auto mb-4 flex items-center justify-center">
            <Key className="w-8 h-8 text-white" />
          </div>
          <h1 className="text-2xl font-bold">نسيت كلمة المرور؟</h1>
          <p className="text-sm text-muted-foreground mt-1">سنرسل لك رابط الاسترداد</p>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>استرداد الحساب</CardTitle>
            <CardDescription>أدخل بريدك الإلكتروني المسجّل</CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label>البريد الإلكتروني</Label>
                <Input
                  type="email"
                  placeholder="example@gmail.com"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
              <Button type="submit" className="w-full" disabled={loading}>
                {loading ? <Spinner className="w-4 h-4" /> : "إرسال رابط الاسترداد"}
              </Button>
            </form>
            <p className="text-center text-sm text-muted-foreground mt-4">
              <Link href="/login" className="text-primary hover:underline font-medium">
                العودة لتسجيل الدخول
              </Link>
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

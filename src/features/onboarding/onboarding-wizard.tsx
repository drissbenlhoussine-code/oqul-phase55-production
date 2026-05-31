"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Star, BookOpen, User, ChevronLeft, CheckCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Spinner } from "@/components/ui/spinner";
import { useToast } from "@/components/ui/toast";

interface Grade { id: string; titleAr: string; color: string | null; ageMin?: number | null; ageMax?: number | null; }

interface OnboardingWizardProps {
  grades: Grade[];
}

type Step = "welcome" | "child-name" | "child-grade" | "done";

const STEP_ORDER: Step[] = ["welcome", "child-name", "child-grade", "done"];

export function OnboardingWizard({ grades }: OnboardingWizardProps) {
  const router = useRouter();
  const { toast } = useToast();
  const [step, setStep]         = useState<Step>("welcome");
  const [childName, setChildName] = useState("");
  const [gradeId, setGradeId]   = useState("");
  const [saving, setSaving]     = useState(false);

  const stepIdx   = STEP_ORDER.indexOf(step);
  const progress  = Math.round((stepIdx / (STEP_ORDER.length - 1)) * 100);
  const progressClass = progress === 0 ? "w-0" : progress <= 34 ? "w-1/3" : progress <= 68 ? "w-2/3" : "w-full";

  function next() {
    const idx = STEP_ORDER.indexOf(step);
    if (idx < STEP_ORDER.length - 1) setStep(STEP_ORDER[idx + 1]);
  }

  async function finish() {
    if (!childName.trim()) { toast("أدخل اسم الطفل", "error"); return; }
    setSaving(true);
    try {
      const res = await fetch("/api/children", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: childName.trim(), gradeId: gradeId || undefined }),
      });
      const data = await res.json();
      if (!data.success) throw new Error(data.message);
      setStep("done");
      setTimeout(() => router.push("/dashboard"), 1800);
    } catch (e) {
      toast(e instanceof Error ? e.message : "حدث خطأ", "error");
    } finally {
      setSaving(false);
    }
  }

  const primaryGrades  = grades.filter((g) => g.ageMin && g.ageMin <= 12);
  const middleGrades   = grades.filter((g) => g.ageMin && g.ageMin >= 12 && g.ageMin <= 15);
  const highGrades     = grades.filter((g) => g.ageMin && g.ageMin >= 15);

  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 via-white to-amber-50 flex items-center justify-center p-4">
      <div className="w-full max-w-lg space-y-6">

        {/* Logo */}
        <div className="text-center">
          <div className="w-16 h-16 rounded-2xl bg-primary mx-auto flex items-center justify-center shadow-lg">
            <Star className="w-9 h-9 text-white" />
          </div>
          <h1 className="text-2xl font-bold mt-3">عقول</h1>
        </div>

        {/* Progress bar */}
        {step !== "done" && (
          <div className="space-y-1">
            <div className="h-1.5 bg-border rounded-full overflow-hidden">
              <div className={`h-full bg-primary rounded-full transition-all duration-500 ${progressClass}`} />
            </div>
            <p className="text-xs text-muted-foreground text-center">خطوة {stepIdx + 1} من {STEP_ORDER.length - 1}</p>
          </div>
        )}

        {/* ── STEP: WELCOME ── */}
        {step === "welcome" && (
          <Card className="animate-fade-in shadow-xl border-0">
            <CardContent className="p-8 text-center space-y-6">
              <div className="text-6xl">👋</div>
              <div className="space-y-2">
                <h2 className="text-2xl font-bold">أهلاً بك في عقول!</h2>
                <p className="text-muted-foreground">
                  منصة تعليمية ذكية تساعد أطفالك على التعلم مع <span className="text-primary font-semibold">ليلى</span> — معلمتهم الذكية التي تتحدث الدارجة المغربية
                </p>
              </div>
              <div className="grid grid-cols-3 gap-3 text-center">
                {[
                  { icon: "📚", label: "المنهج الكامل", sub: "من الابتدائي للثانوي" },
                  { icon: "🤖", label: "ليلى AI", sub: "شرح بالدارجة" },
                  { icon: "🏆", label: "تحفيز ذكي", sub: "نقاط وشارات" },
                ].map((f) => (
                  <div key={f.label} className="bg-secondary rounded-xl p-3 space-y-1">
                    <div className="text-2xl">{f.icon}</div>
                    <p className="text-xs font-semibold">{f.label}</p>
                    <p className="text-xs text-muted-foreground">{f.sub}</p>
                  </div>
                ))}
              </div>
              <Button onClick={next} size="lg" className="w-full gap-2">
                لنبدأ! <ChevronLeft className="w-5 h-5" />
              </Button>
            </CardContent>
          </Card>
        )}

        {/* ── STEP: CHILD NAME ── */}
        {step === "child-name" && (
          <Card className="animate-fade-in shadow-xl border-0">
            <CardContent className="p-8 space-y-6">
              <div className="text-center space-y-2">
                <div className="w-14 h-14 rounded-2xl bg-blue-100 mx-auto flex items-center justify-center">
                  <User className="w-7 h-7 text-blue-600" />
                </div>
                <h2 className="text-xl font-bold">ما اسم طفلك؟</h2>
                <p className="text-muted-foreground text-sm">ليلى ستناديه بهذا الاسم دائمًا</p>
              </div>
              <input
                autoFocus
                value={childName}
                onChange={(e) => setChildName(e.target.value)}
                onKeyDown={(e) => { if (e.key === "Enter" && childName.trim()) next(); }}
                placeholder="مثال: يوسف، فاطمة، محمد..."
                className="w-full text-center text-xl font-semibold py-4 px-4 rounded-2xl border-2 border-border focus:border-primary focus:outline-none bg-background transition-colors"
              />
              {childName.trim() && (
                <p className="text-center text-sm text-muted-foreground animate-fade-in">
                  مرحباً <span className="font-bold text-primary">{childName}</span>! ليلى تتطلع لمساعدتك 🌟
                </p>
              )}
              <Button onClick={next} size="lg" className="w-full" disabled={!childName.trim()}>
                التالي <ChevronLeft className="w-5 h-5" />
              </Button>
            </CardContent>
          </Card>
        )}

        {/* ── STEP: CHILD GRADE ── */}
        {step === "child-grade" && (
          <Card className="animate-fade-in shadow-xl border-0">
            <CardContent className="p-6 space-y-5">
              <div className="text-center space-y-2">
                <div className="w-14 h-14 rounded-2xl bg-emerald-100 mx-auto flex items-center justify-center">
                  <BookOpen className="w-7 h-7 text-emerald-600" />
                </div>
                <h2 className="text-xl font-bold">في أي مستوى {childName}؟</h2>
                <p className="text-muted-foreground text-sm">سيساعد هذا ليلى في تقديم الشرح المناسب</p>
              </div>

              <div className="space-y-3">
                {primaryGrades.length > 0 && (
                  <div>
                    <p className="text-xs font-semibold text-muted-foreground mb-2 px-1">التعليم الابتدائي</p>
                    <div className="grid grid-cols-2 gap-2">
                      {primaryGrades.map((g) => (
                        <button key={g.id} onClick={() => setGradeId(g.id)}
                          className={`p-3 rounded-xl text-sm font-medium text-right transition-all border-2 ${gradeId === g.id ? "border-primary bg-primary/10 text-primary" : "border-border bg-secondary hover:border-primary/40"}`}>
                          {g.titleAr}
                          {g.ageMin && <span className="block text-xs opacity-60">{g.ageMin}-{g.ageMax} سنة</span>}
                        </button>
                      ))}
                    </div>
                  </div>
                )}
                {middleGrades.length > 0 && (
                  <div>
                    <p className="text-xs font-semibold text-muted-foreground mb-2 px-1">التعليم الإعدادي</p>
                    <div className="grid grid-cols-3 gap-2">
                      {middleGrades.map((g) => (
                        <button key={g.id} onClick={() => setGradeId(g.id)}
                          className={`p-3 rounded-xl text-sm font-medium text-right transition-all border-2 ${gradeId === g.id ? "border-primary bg-primary/10 text-primary" : "border-border bg-secondary hover:border-primary/40"}`}>
                          {g.titleAr}
                        </button>
                      ))}
                    </div>
                  </div>
                )}
                {highGrades.length > 0 && (
                  <div>
                    <p className="text-xs font-semibold text-muted-foreground mb-2 px-1">التعليم الثانوي</p>
                    <div className="grid grid-cols-3 gap-2">
                      {highGrades.map((g) => (
                        <button key={g.id} onClick={() => setGradeId(g.id)}
                          className={`p-3 rounded-xl text-sm font-medium text-right transition-all border-2 ${gradeId === g.id ? "border-primary bg-primary/10 text-primary" : "border-border bg-secondary hover:border-primary/40"}`}>
                          {g.titleAr}
                        </button>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              <div className="flex gap-3 pt-2">
                <Button variant="outline" onClick={() => setStep("child-name")} className="flex-1">رجوع</Button>
                <Button onClick={finish} className="flex-1 gap-2" disabled={saving}>
                  {saving ? <Spinner className="w-4 h-4" /> : <><CheckCircle className="w-4 h-4" /> ابدأ التعلم</>}
                </Button>
              </div>
              {!gradeId && (
                <p className="text-center text-xs text-muted-foreground">يمكنك تخطي هذه الخطوة وتحديده لاحقًا</p>
              )}
            </CardContent>
          </Card>
        )}

        {/* ── STEP: DONE ── */}
        {step === "done" && (
          <Card className="animate-fade-in shadow-xl border-0">
            <CardContent className="p-8 text-center space-y-5">
              <div className="text-6xl animate-pulse-soft">🎉</div>
              <h2 className="text-2xl font-bold">جاهزون للتعلم!</h2>
              <p className="text-muted-foreground">ليلى مستعدة لمساعدة <span className="font-bold text-primary">{childName}</span> الآن</p>
              <div className="flex justify-center">
                <Spinner className="w-6 h-6 text-primary" />
              </div>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
}

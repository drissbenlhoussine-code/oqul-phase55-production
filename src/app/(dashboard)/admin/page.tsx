"use client";
/**
 * Admin Curriculum Builder
 * AI-assisted lesson generation for scaling content production.
 * Only accessible to admin role users.
 */
import { useState } from "react";
import { Sparkles, BookOpen, CheckCircle, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Spinner } from "@/components/ui/spinner";
import { useToast } from "@/components/ui/toast";

interface GeneratedContent {
  explanation: string;
  vocabulary:  { word: string; definition: string }[];
  examples:    { text: string; note: string }[];
  summary:     string;
  exercises:   { type: string; question: string; options?: string[]; correctAnswer: string; explanation: string; points: number }[];
}

const SUBJECTS = ["arabic", "math", "french", "science", "islamic", "social"];
const GRADES   = Array.from({ length: 12 }, (_, i) => i + 1);

export default function AdminPage() {
  const { toast } = useToast();

  // Simple client-side check (real protection is server-side via withAdmin)
  const [isAdmin, setIsAdmin] = useState(true); // assume admin, server will 403 if not

  const [subject,    setSubject]    = useState("arabic");
  const [grade,      setGrade]      = useState(1);
  const [topic,      setTopic]      = useState("");
  const [objectives, setObjectives] = useState("");
  const [difficulty, setDifficulty] = useState<"easy"|"medium"|"hard">("easy");
  const [result,     setResult]     = useState<GeneratedContent | null>(null);
  const [loading,    setLoading]    = useState(false);
  const [error,      setError]      = useState<string | null>(null);

  async function generate() {
    if (!topic.trim()) { toast("أدخل موضوع الدرس", "error"); return; }
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const res = await fetch("/api/admin/generate-lesson", {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify({
          subject, grade, topic,
          objectives: objectives.split("\n").filter(Boolean),
          difficulty,
        }),
      });
      const data = await res.json().catch(() => null);
      if (!res.ok || !data?.success) {
        throw new Error(data?.message ?? "تعذر توليد الدرس. يرجى المحاولة لاحقاً.");
      }
      setResult(data.data);
      toast("تم توليد الدرس بنجاح! ✅", "success");
    } catch (e) {
      const message = e instanceof Error ? e.message : "تعذر توليد الدرس. يرجى المحاولة لاحقاً.";
      setError(message);
      toast(message, "error");
    } finally {
      setLoading(false);
    }
  }

  const subjectLabels: Record<string, string> = {
    arabic: "عربية", math: "رياضيات", french: "فرنسية",
    science: "علوم", islamic: "إسلامية", social: "اجتماعيات",
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6 animate-fade-in">
      <div>
        <h1 className="text-2xl font-bold flex items-center gap-2">
          <Sparkles className="w-6 h-6 text-primary" /> مولّد المحتوى التعليمي
        </h1>
        <p className="text-muted-foreground text-sm">أنشئ دروساً كاملة بمساعدة الذكاء الاصطناعي</p>
      </div>

      {/* Config */}
      <Card>
        <CardHeader><CardTitle className="text-base">إعدادات الدرس</CardTitle></CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="text-sm font-medium mb-1.5 block">المادة</label>
              <select value={subject} onChange={(e) => setSubject(e.target.value)}
                className="w-full rounded-xl border border-border bg-background px-3 py-2 text-sm">
                {Object.entries(subjectLabels).map(([v, l]) => (
                  <option key={v} value={v}>{l}</option>
                ))}
              </select>
            </div>
            <div>
              <label className="text-sm font-medium mb-1.5 block">المستوى</label>
              <select value={grade} onChange={(e) => setGrade(Number(e.target.value))}
                className="w-full rounded-xl border border-border bg-background px-3 py-2 text-sm">
                {GRADES.map((g) => <option key={g} value={g}>السنة {g}</option>)}
              </select>
            </div>
          </div>

          <div>
            <label className="text-sm font-medium mb-1.5 block">موضوع الدرس</label>
            <input value={topic} onChange={(e) => setTopic(e.target.value)}
              placeholder="مثال: الكسور العادية"
              className="w-full rounded-xl border border-border px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary" />
          </div>

          <div>
            <label className="text-sm font-medium mb-1.5 block">الأهداف (سطر لكل هدف)</label>
            <textarea value={objectives} onChange={(e) => setObjectives(e.target.value)}
              rows={3} placeholder="فهم مفهوم الكسر&#10;قراءة الكسور وكتابتها"
              className="w-full rounded-xl border border-border px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary resize-none" />
          </div>

          <div className="flex gap-2">
            {(["easy","medium","hard"] as const).map((d) => (
              <button key={d} onClick={() => setDifficulty(d)}
                className={`flex-1 py-2 rounded-xl text-sm font-medium border-2 transition-all ${
                  difficulty === d ? "border-primary bg-primary/10 text-primary" : "border-border"
                }`}>
                {d === "easy" ? "سهل" : d === "medium" ? "متوسط" : "صعب"}
              </button>
            ))}
          </div>

          <Button onClick={generate} className="w-full gap-2" disabled={loading}>
            {loading ? <><Spinner className="w-4 h-4" /> يُولّد الدرس...</> : <><Sparkles className="w-4 h-4" /> ولّد الدرس</>}
          </Button>

          {error && (
            <div className="flex items-start gap-2 rounded-xl border border-red-200 bg-red-50 p-3 text-sm text-red-700">
              <AlertCircle className="mt-0.5 h-4 w-4 flex-shrink-0" />
              <p>{error}</p>
            </div>
          )}
        </CardContent>
      </Card>

      {/* Result */}
      {result && (
        <div className="space-y-4 animate-fade-in">
          <Card className="border-emerald-200 bg-emerald-50">
            <CardHeader><CardTitle className="text-base flex items-center gap-2 text-emerald-800"><CheckCircle className="w-4 h-4" /> الشرح</CardTitle></CardHeader>
            <CardContent><p className="text-sm leading-loose whitespace-pre-wrap">{result.explanation}</p></CardContent>
          </Card>

          <Card>
            <CardHeader><CardTitle className="text-base">المفردات ({result.vocabulary?.length ?? 0})</CardTitle></CardHeader>
            <CardContent>
              <div className="space-y-2">
                {result.vocabulary?.map((v, i) => (
                  <div key={i} className="flex gap-3 p-2 bg-secondary rounded-lg">
                    <span className="font-bold text-primary text-sm min-w-[80px]">{v.word}</span>
                    <span className="text-sm text-muted-foreground">{v.definition}</span>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader><CardTitle className="text-base">التمارين ({result.exercises?.length ?? 0})</CardTitle></CardHeader>
            <CardContent>
              <div className="space-y-3">
                {result.exercises?.map((ex, i) => (
                  <div key={i} className="p-3 border rounded-xl">
                    <div className="flex items-center gap-2 mb-2">
                      <span className="text-xs bg-primary/10 text-primary px-2 py-0.5 rounded-full">{ex.type}</span>
                      <span className="text-xs text-muted-foreground">{ex.points} نقطة</span>
                    </div>
                    <p className="font-medium text-sm">{ex.question}</p>
                    {ex.options && <p className="text-xs text-muted-foreground mt-1">الخيارات: {ex.options.join(" | ")}</p>}
                    <p className="text-xs text-emerald-600 mt-1">✓ {ex.correctAnswer}</p>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          <Card className="border-blue-200 bg-blue-50">
            <CardContent className="p-4">
              <p className="text-xs font-medium text-blue-800">💡 ملاحظة: انسخ هذا المحتوى وأضفه لـ seed.ts أو استخدم Drizzle Studio لإضافته مباشرة.</p>
            </CardContent>
          </Card>
        </div>
      )}
    </div>
  );
}

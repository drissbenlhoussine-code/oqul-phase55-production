"use client";

import { useEffect, useMemo, useState } from "react";
import { AlertCircle, BarChart3, BookOpenCheck, CheckCircle2, RefreshCw } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { EmptyState } from "@/components/ui/empty-state";
import { Spinner } from "@/components/ui/spinner";

type LessonStatus = "excellent" | "needs_improvement" | "placeholder";

type GradeProgress = {
  grade: string;
  gradeSlug: string;
  totalLessons: number;
  completedLessons: number;
  remainingLessons: number;
  placeholderLessons: number;
  averageQuality: number;
  completionPercentage: number;
};

type LessonNeedingImprovement = {
  lessonId: string;
  title: string;
  subject: string;
  grade: string;
  gradeSlug: string;
  qualityScore: number;
  status: LessonStatus;
  reason: string;
};

type CurriculumProgressData = {
  summary: {
    totalLessons: number;
    completedLessons: number;
    remainingLessons: number;
    placeholderLessons: number;
    averageQualityScore: number;
    completionPercentage: number;
  };
  grades: GradeProgress[];
  lessonsNeedingImprovement: LessonNeedingImprovement[];
  generatedAt: string;
};

function statusLabel(status: LessonStatus) {
  if (status === "excellent") return "Excellent";
  if (status === "placeholder") return "Placeholder";
  return "Needs improvement";
}

function statusVariant(status: LessonStatus) {
  if (status === "excellent") return "success";
  if (status === "placeholder") return "destructive";
  return "warning";
}

function ProgressBar({ value }: { value: number }) {
  return (
    <div className="h-3 overflow-hidden rounded-full bg-slate-100">
      <div
        className="h-full rounded-full bg-emerald-500 transition-all"
        style={{ width: `${Math.max(0, Math.min(100, value))}%` }}
      />
    </div>
  );
}

export default function CurriculumProgressPage() {
  const [data, setData] = useState<CurriculumProgressData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  async function loadProgress() {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch("/api/admin/curriculum-progress", {
        headers: { Accept: "application/json" },
        cache: "no-store",
      });
      const body = await response.json().catch(() => null);
      if (!response.ok || !body?.success) {
        throw new Error(body?.message ?? "Could not load curriculum progress.");
      }
      setData(body.data);
    } catch (loadError) {
      setError(loadError instanceof Error ? loadError.message : "Could not load curriculum progress.");
      setData(null);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    void loadProgress();
  }, []);

  const topLessons = useMemo(() => data?.lessonsNeedingImprovement.slice(0, 20) ?? [], [data]);

  if (loading) {
    return (
      <div className="flex min-h-[50vh] items-center justify-center">
        <Spinner className="h-8 w-8" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="mx-auto max-w-4xl space-y-4">
        <Card className="border-red-200 bg-red-50">
          <CardContent className="flex items-start gap-3 p-5 text-red-700">
            <AlertCircle className="mt-0.5 h-5 w-5 flex-shrink-0" />
            <div className="space-y-3">
              <p className="font-semibold">Unable to load curriculum progress</p>
              <p className="text-sm">{error}</p>
              <Button type="button" variant="outline" onClick={loadProgress}>
                Try again
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    );
  }

  if (!data || data.summary.totalLessons === 0) {
    return (
      <EmptyState
        icon={<BookOpenCheck className="h-10 w-10 text-slate-400" />}
        title="No primary mathematics data found"
        description="The dashboard is read-only and will show progress once primary mathematics lessons exist in PostgreSQL."
      />
    );
  }

  return (
    <div className="mx-auto max-w-7xl space-y-6" dir="rtl">
      <div className="flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
        <div>
          <p className="text-sm font-semibold text-emerald-600">Admin → Curriculum Progress</p>
          <h1 className="mt-1 text-3xl font-black tracking-tight text-slate-950">لوحة تقدم جودة المنهاج</h1>
          <p className="mt-2 max-w-2xl text-sm leading-7 text-slate-600">
            متابعة read-only لجودة دروس الرياضيات في التعليم الابتدائي بدون Groq وبدون أي تعديل في قاعدة البيانات.
          </p>
        </div>
        <Button type="button" variant="outline" onClick={loadProgress} className="gap-2 self-start md:self-auto">
          <RefreshCw className="h-4 w-4" />
          تحديث
        </Button>
      </div>

      <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-5">
        <Card>
          <CardHeader className="pb-2"><CardTitle className="text-sm text-slate-500">Total lessons</CardTitle></CardHeader>
          <CardContent><p className="text-3xl font-black">{data.summary.totalLessons}</p></CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2"><CardTitle className="text-sm text-slate-500">Completed</CardTitle></CardHeader>
          <CardContent><p className="text-3xl font-black text-emerald-600">{data.summary.completedLessons}</p></CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2"><CardTitle className="text-sm text-slate-500">Remaining</CardTitle></CardHeader>
          <CardContent><p className="text-3xl font-black text-amber-600">{data.summary.remainingLessons}</p></CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2"><CardTitle className="text-sm text-slate-500">Placeholders</CardTitle></CardHeader>
          <CardContent><p className="text-3xl font-black text-red-600">{data.summary.placeholderLessons}</p></CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2"><CardTitle className="text-sm text-slate-500">Average quality</CardTitle></CardHeader>
          <CardContent><p className="text-3xl font-black">{data.summary.averageQualityScore}</p></CardContent>
        </Card>
      </div>

      <Card className="border-emerald-100 bg-gradient-to-br from-emerald-50 to-white">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <BarChart3 className="h-5 w-5 text-emerald-600" />
            Overall Primary Mathematics Progress
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <div className="flex items-center justify-between text-sm font-bold">
            <span>{data.summary.completedLessons}/{data.summary.totalLessons}</span>
            <span>{data.summary.completionPercentage}%</span>
          </div>
          <ProgressBar value={data.summary.completionPercentage} />
        </CardContent>
      </Card>

      <section className="grid gap-4 lg:grid-cols-2">
        {data.grades.map((grade) => (
          <Card key={grade.gradeSlug}>
            <CardHeader className="space-y-1">
              <div className="flex items-center justify-between gap-3">
                <CardTitle className="text-lg">{grade.grade}</CardTitle>
                <Badge variant={grade.completionPercentage === 100 ? "success" : "warning"}>
                  {grade.completedLessons}/{grade.totalLessons} — {grade.completionPercentage}%
                </Badge>
              </div>
              <p className="text-xs text-slate-500">
                Average quality: {grade.averageQuality} · Placeholders: {grade.placeholderLessons}
              </p>
            </CardHeader>
            <CardContent>
              <ProgressBar value={grade.completionPercentage} />
            </CardContent>
          </Card>
        ))}
      </section>

      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <AlertCircle className="h-5 w-5 text-amber-500" />
            Lessons Needing Improvement
          </CardTitle>
        </CardHeader>
        <CardContent>
          {topLessons.length === 0 ? (
            <div className="rounded-2xl bg-emerald-50 p-5 text-sm font-semibold text-emerald-700">
              <CheckCircle2 className="ml-2 inline h-5 w-5" />
              All primary mathematics lessons meet the completion definition.
            </div>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full min-w-[760px] text-right text-sm">
                <thead>
                  <tr className="border-b text-xs uppercase text-slate-500">
                    <th className="py-3 pl-3">Grade</th>
                    <th className="py-3 pl-3">Lesson title</th>
                    <th className="py-3 pl-3">Subject</th>
                    <th className="py-3 pl-3">Quality</th>
                    <th className="py-3 pl-3">Status</th>
                    <th className="py-3 pl-3">Reason</th>
                    <th className="py-3">Lesson ID</th>
                  </tr>
                </thead>
                <tbody>
                  {topLessons.map((lesson) => (
                    <tr key={lesson.lessonId} className="border-b last:border-0">
                      <td className="py-3 pl-3 font-semibold">{lesson.grade}</td>
                      <td className="py-3 pl-3">{lesson.title}</td>
                      <td className="py-3 pl-3">{lesson.subject}</td>
                      <td className="py-3 pl-3 font-bold">{lesson.qualityScore}</td>
                      <td className="py-3 pl-3">
                        <Badge variant={statusVariant(lesson.status)}>{statusLabel(lesson.status)}</Badge>
                      </td>
                      <td className="max-w-sm py-3 pl-3 text-xs leading-6 text-slate-600">{lesson.reason}</td>
                      <td className="py-3 font-mono text-xs text-slate-500" dir="ltr">{lesson.lessonId}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}

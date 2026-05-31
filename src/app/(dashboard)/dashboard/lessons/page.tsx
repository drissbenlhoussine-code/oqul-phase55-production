"use client";

import { useEffect, useMemo, useState } from "react";
import { BookOpen, Clock, ChevronLeft, CheckCircle, RefreshCw } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Spinner } from "@/components/ui/spinner";
import Link from "next/link";

interface Grade { id: string; titleAr: string; color?: string; }
interface Subject { id: string; titleAr: string; icon?: string; color?: string; }
interface Lesson { id: string; titleAr: string; difficulty: string; estimatedDurationMinutes: number; isPublished: boolean; }
interface Unit { id: string; titleAr: string; lessons: Lesson[]; }
interface ProgressItem { lessonId: string; status: string; score?: number; }
interface Child { id: string; name?: string; grade?: { id: string; titleAr?: string } | null; gradeId?: string | null; }

const ICON_MAP: Record<string, string> = {
  BookOpen: "📖", Calculator: "🔢", Globe: "🌍", Star: "⭐",
  Microscope: "🔬", Languages: "🗣️", Users: "👥", default: "📚",
};

async function getJson(url: string) {
  const res = await fetch(url, { cache: "no-store", signal: AbortSignal.timeout(8000) });
  const data = await res.json().catch(() => ({}));
  if (!res.ok || data.success === false) throw new Error(data.message || `تعذر تحميل ${url}`);
  return data.data ?? data;
}

export default function LessonsPage() {
  const [grades, setGrades] = useState<Grade[]>([]);
  const [subjects, setSubjects] = useState<Subject[]>([]);
  const [units, setUnits] = useState<Unit[]>([]);
  const [progress, setProgress] = useState<ProgressItem[]>([]);
  const [child, setChild] = useState<Child | null>(null);
  const [selectedGrade, setSelectedGrade] = useState<Grade | null>(null);
  const [selectedSubject, setSelectedSubject] = useState<Subject | null>(null);
  const [loading, setLoading] = useState(true);
  const [loadingUnits, setLoadingUnits] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function loadInitial() {
    setLoading(true);
    setError(null);
    try {
      const [gradeData, childData] = await Promise.all([
        getJson("/api/curriculum/grades"),
        getJson("/api/children").catch(() => []),
      ]);

      const allGrades: Grade[] = Array.isArray(gradeData) ? gradeData : [];
      const children: Child[] = Array.isArray(childData) ? childData : [];
      const firstChild = children[0] ?? null;
      setGrades(allGrades);
      setChild(firstChild);

      const childGradeId = firstChild?.grade?.id || firstChild?.gradeId || null;
      const initialGrade = allGrades.find((g) => g.id === childGradeId) ?? allGrades[0] ?? null;
      if (initialGrade) await selectGrade(initialGrade, firstChild?.id ?? null, true);
    } catch (e) {
      setError(e instanceof Error ? e.message : "تعذر تحميل الدروس");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => { loadInitial(); }, []);

  async function selectGrade(g: Grade, childId = child?.id ?? null, autoPickSubject = false) {
    setSelectedGrade(g);
    setSelectedSubject(null);
    setSubjects([]);
    setUnits([]);
    setLoadingUnits(true);
    setError(null);
    try {
      const [subjectData, progressData] = await Promise.all([
        getJson(`/api/curriculum/subjects?gradeId=${g.id}`),
        childId ? getJson(`/api/progress?childId=${childId}`).catch(() => []) : Promise.resolve([]),
      ]);
      const nextSubjects: Subject[] = Array.isArray(subjectData) ? subjectData : [];
      setSubjects(nextSubjects);
      setProgress(Array.isArray(progressData) ? progressData : []);
      if (autoPickSubject && nextSubjects[0]) await selectSubject(nextSubjects[0]);
    } catch (e) {
      setError(e instanceof Error ? e.message : "تعذر تحميل المواد");
    } finally {
      setLoadingUnits(false);
    }
  }

  async function selectSubject(s: Subject) {
    setSelectedSubject(s);
    setUnits([]);
    setLoadingUnits(true);
    setError(null);
    try {
      const unitData = await getJson(`/api/curriculum/units?subjectId=${s.id}`);
      setUnits(Array.isArray(unitData) ? unitData : []);
    } catch (e) {
      setError(e instanceof Error ? e.message : "تعذر تحميل وحدات الدروس");
    } finally {
      setLoadingUnits(false);
    }
  }

  const progressMap = useMemo(() => Object.fromEntries(progress.map((p) => [p.lessonId, p])), [progress]);
  const diffMap = { easy: "سهل", medium: "متوسط", hard: "صعب" } as Record<string, string>;
  const diffColor = { easy: "success", medium: "warning", hard: "destructive" } as Record<string, string>;
  const totalLessons = units.reduce((sum, unit) => sum + unit.lessons.length, 0);

  return (
    <div className="max-w-5xl mx-auto space-y-5 animate-fade-in">
      <div className="flex items-start justify-between gap-3 flex-wrap">
        <div>
          <h1 className="text-2xl font-bold">الدروس</h1>
          <p className="text-muted-foreground text-sm">
            المنهج الدراسي الكامل — {child ? `متابعة ${child.name ?? "الطفل"}` : "يمكنك تصفح الدروس ثم إضافة طفل لحفظ التقدم"}
          </p>
        </div>
        <Button variant="outline" size="sm" onClick={loadInitial} className="gap-2">
          <RefreshCw className="w-4 h-4" /> تحديث
        </Button>
      </div>

      {error && (
        <Card className="border-red-200 bg-red-50">
          <CardContent className="p-4 text-sm text-red-700 flex items-center justify-between gap-3">
            <span>{error}</span>
            <Button variant="outline" size="sm" onClick={loadInitial}>إعادة المحاولة</Button>
          </CardContent>
        </Card>
      )}

      {loading ? (
        <div className="flex justify-center py-12"><Spinner className="w-7 h-7 text-primary" /></div>
      ) : (
        <>
          <div>
            <p className="text-xs font-semibold text-muted-foreground mb-2 uppercase tracking-wide">المستوى الدراسي</p>
            <div className="flex flex-wrap gap-2">
              {grades.map((g) => (
                <button key={g.id} onClick={() => selectGrade(g)}
                  className={`px-4 py-2 rounded-xl text-sm font-medium transition-all border-2 ${
                    selectedGrade?.id === g.id ? "bg-primary text-white border-primary shadow-sm" : "bg-card border-border hover:border-primary/50"
                  }`}>
                  {g.titleAr}
                </button>
              ))}
            </div>
          </div>

          {subjects.length > 0 && (
            <div>
              <p className="text-xs font-semibold text-muted-foreground mb-2 uppercase tracking-wide">المادة</p>
              <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
                {subjects.map((s) => (
                  <button key={s.id} onClick={() => selectSubject(s)}
                    className={`p-4 rounded-2xl text-right transition-all border-2 space-y-2 ${
                      selectedSubject?.id === s.id ? "border-primary shadow-md bg-primary/5" : "bg-card border-border hover:border-primary/40 hover:shadow-sm"
                    }`}>
                    <div className="flex items-center justify-between">
                      <span className="text-2xl">{ICON_MAP[s.icon ?? "default"] ?? ICON_MAP.default}</span>
                      {selectedSubject?.id === s.id && <CheckCircle className="w-4 h-4 text-primary" />}
                    </div>
                    <p className="font-semibold text-sm">{s.titleAr}</p>
                  </button>
                ))}
              </div>
            </div>
          )}

          {loadingUnits && <div className="flex justify-center py-8"><Spinner className="w-6 h-6 text-primary" /></div>}

          {!loadingUnits && selectedSubject && units.length === 0 && (
            <Card>
              <CardContent className="py-12 text-center space-y-3">
                <p className="text-4xl">🛠️</p>
                <p className="font-semibold">لا توجد وحدات منشورة لهذه المادة بعد</p>
                <p className="text-sm text-muted-foreground">جرّب مادة أخرى أو أعد تشغيل seed.</p>
              </CardContent>
            </Card>
          )}

          {!loadingUnits && units.length > 0 && (
            <div className="text-sm text-muted-foreground">تم العثور على <b className="text-foreground">{totalLessons}</b> درسًا في هذه المادة.</div>
          )}

          {!loadingUnits && units.map((unit) => (
            <div key={unit.id}>
              <h2 className="font-semibold text-base mb-3 flex items-center gap-2">
                <BookOpen className="w-4 h-4 text-primary flex-shrink-0" />
                {unit.titleAr}
                <span className="text-xs text-muted-foreground font-normal">({unit.lessons.length} درس)</span>
              </h2>
              <div className="space-y-2">
                {unit.lessons.map((lesson) => {
                  const prog = progressMap[lesson.id];
                  const status = prog?.status;
                  return (
                    <Link key={lesson.id} href={`/dashboard/lessons/${lesson.id}`}>
                      <Card className={`hover:shadow-md transition-all hover:-translate-y-0.5 cursor-pointer ${status === "completed" ? "border-emerald-200" : ""}`}>
                        <CardContent className="p-4 flex items-center gap-4">
                          <div className={`w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0 ${
                            status === "completed" ? "bg-emerald-100" : status === "in_progress" ? "bg-blue-100" : status === "needs_review" ? "bg-amber-100" : "bg-secondary"
                          }`}>
                            {status === "completed" ? <CheckCircle className="w-5 h-5 text-emerald-600" /> : <BookOpen className={`w-5 h-5 ${status === "in_progress" ? "text-blue-600" : "text-muted-foreground"}`} />}
                          </div>
                          <div className="flex-1 min-w-0">
                            <p className="font-medium text-sm truncate">{lesson.titleAr}</p>
                            <div className="flex items-center gap-2 mt-1 flex-wrap">
                              <span className="flex items-center gap-1 text-xs text-muted-foreground"><Clock className="w-3 h-3" /> {lesson.estimatedDurationMinutes} دقيقة</span>
                              <Badge variant={diffColor[lesson.difficulty] as "success" | "warning" | "destructive"} className="text-[10px] py-0">{diffMap[lesson.difficulty] ?? lesson.difficulty}</Badge>
                              {prog?.score != null && <span className="text-xs font-bold text-emerald-600">{Math.round(prog.score)}%</span>}
                            </div>
                          </div>
                          <ChevronLeft className="w-4 h-4 text-muted-foreground flex-shrink-0" />
                        </CardContent>
                      </Card>
                    </Link>
                  );
                })}
              </div>
            </div>
          ))}

          {!selectedGrade && grades.length === 0 && (
            <Card>
              <CardContent className="py-12 text-center space-y-3">
                <p className="text-4xl">📚</p>
                <p className="font-semibold">لم يتم تحميل المستويات</p>
                <p className="text-sm text-muted-foreground">تأكد من تشغيل db:seed بنجاح.</p>
              </CardContent>
            </Card>
          )}
        </>
      )}
    </div>
  );
}

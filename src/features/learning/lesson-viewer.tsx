"use client";

import { useState, useEffect, useCallback, useRef } from "react";
import Link from "next/link";
import {
  ArrowRight, BookOpen, MessageCircle, CheckCircle,
  ChevronLeft, ChevronRight, Star, Trophy,
  Clock, RotateCcw, Sparkles, Lock,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Spinner } from "@/components/ui/spinner";
import { useToast } from "@/components/ui/toast";
import { getLevelInfo } from "@/lib/gamification-level";
import { XPCelebration } from "@/features/gamification/xp-celebration";
import { QuizQuestion } from "./quiz-question";

interface Exercise {
  id: string; type: string; question: string;
  options?: string[]; correctAnswer: string;
  explanation?: string | null; points: number;
}
interface Lesson {
  id: string; titleAr: string; difficulty: string;
  estimatedDurationMinutes: number; objectives: string[];
  content?: {
    explanation: string;
    vocabulary?: { word: string; definition: string }[];
    examples?: { text: string; note?: string }[];
    summary?: string;
  };
  exercises: Exercise[];
  unit: { titleAr: string; subject: { titleAr: string } };
}
interface QuizFeedback {
  exerciseId: string; correct: boolean;
  yourAnswer: string; correctAnswer: string;
  explanation: string | null; points: number;
}
interface QuizResult {
  score: number; passed: boolean; earnedPoints: number;
  totalPoints: number; feedback: QuizFeedback[];
  gamification?: {
    xpEarned: number; newXP: number;
    levelInfo: { level: number; title: string; xpToNext: number; progress: number };
    newBadges: string[]; streak: number;
  };
}

type Tab = "objectives" | "lesson" | "quiz" | "result";

export function LessonViewer({ lessonId, childId }: { lessonId: string; childId?: string }) {
  const { toast }      = useToast();
  const startTime      = useRef(Date.now());
  const [lesson, setLesson]             = useState<Lesson | null>(null);
  const [loading, setLoading]           = useState(true);
  const [tab, setTab]                   = useState<Tab>("objectives");
  const [answers, setAnswers]           = useState<Record<string, string>>({});
  const [quizResult, setResult]         = useState<QuizResult | null>(null);
  const [submitting, setSubmitting]     = useState(false);
  const [showCelebration, setCelebration] = useState(false);
  const [quizSubmitted, setQuizSubmitted] = useState(false);

  useEffect(() => {
    fetch(`/api/curriculum/lessons/${lessonId}`)
      .then((r) => r.json())
      .then((d) => { if (d.success) setLesson(d.data); })
      .catch(() => toast("تعذر تحميل الدرس", "error"))
      .finally(() => setLoading(false));
  }, [lessonId, toast]);

  // Mark in-progress
  useEffect(() => {
    if (tab === "lesson" && childId && lessonId) {
      fetch("/api/progress", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ childId, lessonId, status: "in_progress" }),
      }).catch(() => {});
    }
  }, [tab, childId, lessonId]);

  const submitQuiz = useCallback(async () => {
    if (!lesson) return;
    if (!childId) {
      toast("أضف طفلاً أولاً لحفظ التقدم وحل التمارين", "error");
      return;
    }
    setSubmitting(true);
    try {
      const timeSpentSecs = Math.round((Date.now() - startTime.current) / 1000);
      const res = await fetch("/api/progress/quiz", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ childId, lessonId, answers }),
      });
      const data = await res.json();
      if (!data.success) throw new Error(data.message);

      setResult(data.data);
      setQuizSubmitted(true);

      // Log time
      fetch("/api/progress", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ childId, lessonId, status: data.data.passed ? "completed" : "needs_review", score: data.data.score, timeSpentSecs }),
      }).catch(() => {});

      // Show celebration after brief delay (let them see the answers first)
      setTimeout(() => {
        if (data.data.gamification || data.data.passed !== undefined) {
          setCelebration(true);
        }
      }, 800);
    } catch (e) {
      toast(e instanceof Error ? e.message : "حدث خطأ", "error");
    } finally {
      setSubmitting(false);
    }
  }, [lesson, childId, lessonId, answers, toast]);

  if (loading) return <div className="flex justify-center py-20"><Spinner className="w-8 h-8 text-primary" /></div>;
  if (!lesson) return (
    <div className="text-center py-20 space-y-3">
      <p className="text-2xl">📚</p>
      <p className="text-muted-foreground">الدرس غير موجود</p>
      <Link href="/dashboard/lessons"><Button>العودة للدروس</Button></Link>
    </div>
  );

  const diffMap   = { easy: "سهل", medium: "متوسط", hard: "صعب" } as Record<string, string>;
  const diffColor = { easy: "success", medium: "warning", hard: "destructive" } as Record<string, string>;
  const answered  = Object.keys(answers).length;
  const total     = lesson.exercises.length;

  const tabs: { key: Tab; label: string; locked?: boolean }[] = [
    { key: "objectives", label: "الأهداف" },
    { key: "lesson",     label: "الشرح" },
    { key: "quiz",       label: `التمارين (${total})` },
  ];

  return (
    <div className="max-w-3xl mx-auto space-y-4 animate-fade-in">
      {/* Breadcrumb */}
      <div className="flex items-center gap-2 text-sm text-muted-foreground flex-wrap">
        <Link href="/dashboard/lessons" className="hover:text-primary flex items-center gap-1 transition-colors">
          <ArrowRight className="w-4 h-4" /> الدروس
        </Link>
        <span>/</span>
        <span className="text-foreground font-medium truncate">{lesson.unit.subject.titleAr}</span>
        <span>/</span>
        <span className="text-foreground font-medium truncate">{lesson.titleAr}</span>
      </div>

      {/* Header */}
      <div className="flex items-start justify-between gap-3 flex-wrap">
        <div>
          <h1 className="text-xl font-bold">{lesson.titleAr}</h1>
          <div className="flex items-center gap-2 mt-1.5 flex-wrap">
            <Badge variant={diffColor[lesson.difficulty] as "success" | "warning" | "destructive"}>
              {diffMap[lesson.difficulty]}
            </Badge>
            <span className="text-xs text-muted-foreground flex items-center gap-1">
              <Clock className="w-3 h-3" /> {lesson.estimatedDurationMinutes} دقيقة
            </span>
            <span className="text-xs text-muted-foreground">{lesson.unit.titleAr}</span>
          </div>
        </div>
        <Link href={`/dashboard/leila?lessonId=${lessonId}`}>
          <Button variant="outline" size="sm" className="gap-1.5 shrink-0">
            <Sparkles className="w-4 h-4 text-primary" /> اسأل ليلى
          </Button>
        </Link>
      </div>

      {/* Tabs */}
      {tab !== "result" && (
        <div className="flex border-b border-border">
          {tabs.map((t) => (
            <button key={t.key} onClick={() => setTab(t.key)}
              className={`px-4 py-2.5 text-sm font-medium border-b-2 transition-colors flex items-center gap-1.5 ${
                tab === t.key ? "border-primary text-primary" : "border-transparent text-muted-foreground hover:text-foreground"
              }`}>
              {t.label}
              {t.key === "quiz" && answered > 0 && !quizSubmitted && (
                <span className="w-4 h-4 rounded-full bg-primary text-white text-[10px] flex items-center justify-center">{answered}</span>
              )}
              {t.key === "quiz" && quizSubmitted && quizResult && (
                <span className={`text-xs font-bold ${quizResult.passed ? "text-emerald-600" : "text-amber-600"}`}>
                  {Math.round(quizResult.score)}%
                </span>
              )}
            </button>
          ))}
        </div>
      )}

      {/* OBJECTIVES */}
      {tab === "objectives" && (
        <div className="space-y-4 animate-fade-in">
          <Card>
            <CardHeader>
              <CardTitle className="text-base flex items-center gap-2">
                <Star className="w-4 h-4 text-amber-500" /> ماذا ستتعلم؟
              </CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="space-y-3">
                {lesson.objectives.map((obj, i) => (
                  <li key={i} className="flex items-start gap-3">
                    <span className="w-6 h-6 rounded-full bg-primary/10 text-primary text-xs flex items-center justify-center flex-shrink-0 font-bold mt-0.5">
                      {i + 1}
                    </span>
                    <span className="text-sm">{obj}</span>
                  </li>
                ))}
              </ul>
              <Button onClick={() => setTab("lesson")} className="w-full mt-5 gap-2">
                ابدأ الشرح <ChevronLeft className="w-4 h-4" />
              </Button>
            </CardContent>
          </Card>
        </div>
      )}

      {/* LESSON */}
      {tab === "lesson" && lesson.content && (
        <div className="space-y-4 animate-fade-in">
          <Card>
            <CardHeader>
              <CardTitle className="text-base flex items-center gap-2">
                <BookOpen className="w-4 h-4 text-primary" /> الشرح
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-sm leading-loose whitespace-pre-wrap">{lesson.content.explanation}</div>
            </CardContent>
          </Card>

          {lesson.content.vocabulary && lesson.content.vocabulary.length > 0 && (
            <Card>
              <CardHeader><CardTitle className="text-base">📖 المفردات</CardTitle></CardHeader>
              <CardContent>
                <div className="grid gap-2">
                  {lesson.content.vocabulary.map((v, i) => (
                    <div key={i} className="flex items-start gap-3 p-3 bg-emerald-50 rounded-xl border border-emerald-100">
                      <span className="font-bold text-emerald-700 text-sm min-w-[80px]">{v.word}</span>
                      <span className="text-sm text-muted-foreground">{v.definition}</span>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          )}

          {lesson.content.examples && lesson.content.examples.length > 0 && (
            <Card>
              <CardHeader><CardTitle className="text-base">💡 أمثلة</CardTitle></CardHeader>
              <CardContent>
                <div className="space-y-3">
                  {lesson.content.examples.map((ex, i) => (
                    <div key={i} className="p-3 border-r-4 border-primary bg-primary/5 rounded-lg">
                      <p className="font-medium text-sm">{ex.text}</p>
                      {ex.note && <p className="text-xs text-muted-foreground mt-1">{ex.note}</p>}
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          )}

          {lesson.content.summary && (
            <Card className="bg-amber-50 border-amber-200">
              <CardContent className="p-4">
                <p className="text-sm font-medium text-amber-800">📝 {lesson.content.summary}</p>
              </CardContent>
            </Card>
          )}

          <div className="flex gap-3">
            <Button variant="outline" onClick={() => setTab("objectives")} className="gap-1">
              <ChevronRight className="w-4 h-4" /> الأهداف
            </Button>
            <Button onClick={() => setTab("quiz")} className="flex-1 gap-1">
              ابدأ التمارين <ChevronLeft className="w-4 h-4" />
            </Button>
          </div>
        </div>
      )}

      {/* QUIZ */}
      {tab === "quiz" && (
        <div className="space-y-4 animate-fade-in">
          {!childId && (
            <Card className="border-amber-200 bg-amber-50">
              <CardContent className="p-4 text-sm text-amber-800">
                يمكنك مشاهدة الأسئلة الآن، لكن حفظ النقاط والتقدم يحتاج إضافة طفل من صفحة الإعداد الأولي.
              </CardContent>
            </Card>
          )}
          {/* Progress indicator */}
          {!quizSubmitted && (
            <div className="flex items-center justify-between">
              <p className="text-sm text-muted-foreground">{answered}/{total} إجابة</p>
              <div className="flex gap-1">
                {lesson.exercises.map((ex) => (
                  <span key={ex.id} className={`w-2.5 h-2.5 rounded-full transition-colors ${answers[ex.id] ? "bg-primary" : "bg-border"}`} />
                ))}
              </div>
            </div>
          )}

          {lesson.exercises.map((ex, idx) => (
            <QuizQuestion
              key={ex.id}
              index={idx}
              exercise={ex}
              submitted={quizSubmitted}
              value={answers[ex.id] ?? ""}
              onChange={(val) => setAnswers((prev) => ({ ...prev, [ex.id]: val }))}
            />
          ))}

          {!quizSubmitted && (
            <div className="flex gap-3">
              <Button variant="outline" onClick={() => setTab("lesson")} className="gap-1">
                <ChevronRight className="w-4 h-4" /> الشرح
              </Button>
              <Button
                onClick={submitQuiz}
                className="flex-1"
                disabled={submitting || answered === 0}
              >
                {submitting ? <Spinner className="w-4 h-4" /> : `تسليم الإجابات (${answered}/${total}) ✓`}
              </Button>
            </div>
          )}

          {quizSubmitted && quizResult && (
            <div className="flex gap-3 pt-2">
              <Button
                variant="outline"
                className="flex-1 gap-2"
                onClick={() => { setAnswers({}); setResult(null); setQuizSubmitted(false); }}
              >
                <RotateCcw className="w-4 h-4" /> إعادة المحاولة
              </Button>
              <Link href={`/dashboard/leila?lessonId=${lessonId}`} className="flex-1">
                <Button className="w-full gap-2">
                  <MessageCircle className="w-4 h-4" /> اسأل ليلى
                </Button>
              </Link>
            </div>
          )}

          {quizSubmitted && quizResult && (
            <Link href="/dashboard/lessons">
              <Button variant="ghost" className="w-full gap-2">
                <Trophy className="w-4 h-4" /> الدروس التالية
              </Button>
            </Link>
          )}
        </div>
      )}

      {/* XP Celebration */}
      {showCelebration && quizResult && (
        <XPCelebration
          xpEarned={quizResult.gamification?.xpEarned ?? 0}
          newXP={quizResult.gamification?.newXP ?? 0}
          newBadges={quizResult.gamification?.newBadges ?? []}
          streak={quizResult.gamification?.streak ?? 0}
          passed={quizResult.passed}
          score={quizResult.score}
          onClose={() => { setCelebration(false); setTab("result"); }}
        />
      )}
    </div>
  );
}

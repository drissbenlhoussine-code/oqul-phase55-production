"use client";
import { useEffect, useState, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import { TutorChat } from "@/features/ai-tutor/tutor-chat";
import { Spinner } from "@/components/ui/spinner";
import Link from "next/link";

function LeilaPageInner() {
  const searchParams = useSearchParams();
  const lessonId     = searchParams.get("lessonId") ?? undefined;

  const [childId, setChildId]       = useState<string | null>(null);
  const [lessonTitle, setLessonTitle] = useState<string | undefined>();
  const [loading, setLoading]       = useState(true);

  useEffect(() => {
    fetch("/api/children")
      .then((r) => r.json())
      .then(async (d) => {
        if (d.success && d.data?.[0]) setChildId(d.data[0].id);
        // Fetch lesson title if lessonId provided
        if (lessonId) {
          const lr = await fetch(`/api/curriculum/lessons/${lessonId}`).then((r) => r.json());
          if (lr.success) setLessonTitle(lr.data.titleAr);
        }
      })
      .finally(() => setLoading(false));
  }, [lessonId]);

  if (loading) return (
    <div className="flex justify-center items-center h-64">
      <Spinner className="w-8 h-8 text-primary" />
    </div>
  );

  if (!childId) return (
    <div className="max-w-md mx-auto text-center py-20 space-y-4">
      <p className="text-5xl">👶</p>
      <p className="font-semibold text-lg">أضف طفلاً أولاً</p>
      <p className="text-muted-foreground text-sm">تحتاج لإضافة طفل قبل التحدث مع ليلى</p>
      <Link href="/onboarding">
        <button className="bg-primary text-white px-6 py-2.5 rounded-xl text-sm font-medium hover:bg-primary/90 transition-colors">
          إضافة طفل
        </button>
      </Link>
    </div>
  );

  return (
    <div className="h-[calc(100vh-10rem)]">
      <TutorChat childId={childId} lessonId={lessonId} lessonTitle={lessonTitle} />
    </div>
  );
}

export default function LeilaPage() {
  return (
    <Suspense fallback={<div className="flex justify-center py-20"><Spinner className="w-8 h-8 text-primary" /></div>}>
      <LeilaPageInner />
    </Suspense>
  );
}

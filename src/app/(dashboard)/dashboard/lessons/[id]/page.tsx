"use client";

import { use, useEffect, useState } from "react";
import Link from "next/link";
import { LessonViewer } from "@/features/learning/lesson-viewer";
import { Spinner } from "@/components/ui/spinner";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function LessonPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = use(params);
  const [childId, setChildId] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/children", { signal: AbortSignal.timeout(8000) })
      .then((r) => r.json())
      .then((d) => { if (d.success && d.data?.[0]) setChildId(d.data[0].id); })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div className="flex justify-center py-20"><Spinner className="w-8 h-8 text-primary" /></div>;

  return (
    <div className="space-y-4">
      {!childId && (
        <Card className="border-amber-200 bg-amber-50">
          <CardContent className="p-4 flex items-center justify-between gap-3 flex-wrap">
            <div>
              <p className="font-semibold text-amber-900">تستطيع قراءة الدرس الآن</p>
              <p className="text-sm text-amber-800">للحصول على النقاط وحفظ التقدم، أضف طفلاً من الإعداد الأولي.</p>
            </div>
            <Link href="/onboarding"><Button size="sm">إضافة طفل</Button></Link>
          </CardContent>
        </Card>
      )}
      <LessonViewer lessonId={id} childId={childId ?? undefined} />
    </div>
  );
}

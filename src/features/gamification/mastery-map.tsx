"use client";

interface Subject {
  titleAr: string;
  color:   string;
  icon:    string;
}

interface MasteryData {
  subject:           Subject;
  completedLessons:  number;
  totalLessons:      number;
  avgScore:          number;
  weakPointCount:    number;
}

interface MasteryMapProps {
  data: MasteryData[];
}

function MasteryLevel(score: number): { label: string; color: string; bg: string } {
  if (score >= 90) return { label: "متقن",    color: "text-emerald-700", bg: "bg-emerald-100" };
  if (score >= 70) return { label: "جيد جداً", color: "text-blue-700",   bg: "bg-blue-100" };
  if (score >= 50) return { label: "جيد",      color: "text-amber-700",  bg: "bg-amber-100" };
  if (score >= 30) return { label: "يحتاج جهد", color: "text-orange-700", bg: "bg-orange-100" };
  return                   { label: "يحتاج مراجعة", color: "text-red-700", bg: "bg-red-100" };
}

export function MasteryMap({ data }: MasteryMapProps) {
  if (!data.length) return (
    <div className="rounded-2xl border bg-card p-5 text-center space-y-2">
      <p className="text-3xl">🗺️</p>
      <p className="text-sm text-muted-foreground">أكمل دروساً لترى خريطة إتقانك</p>
    </div>
  );

  return (
    <div className="rounded-2xl border bg-card p-5 space-y-4">
      <div>
        <h3 className="font-bold">خريطة الإتقان 🗺️</h3>
        <p className="text-xs text-muted-foreground">مستواك في كل مادة</p>
      </div>
      <div className="space-y-3">
        {data.map(({ subject, completedLessons, totalLessons, avgScore, weakPointCount }) => {
          const mastery  = MasteryLevel(avgScore);
          const progress = totalLessons > 0 ? Math.round((completedLessons / totalLessons) * 100) : 0;
          return (
            <div key={subject.titleAr} className="space-y-1.5">
              <div className="flex items-center justify-between gap-2">
                <div className="flex items-center gap-2 min-w-0">
                  <span className="text-base">{subject.icon}</span>
                  <span className="text-sm font-medium truncate">{subject.titleAr}</span>
                </div>
                <div className="flex items-center gap-2 flex-shrink-0">
                  {weakPointCount > 0 && (
                    <span className="text-xs text-orange-600">⚠️ {weakPointCount}</span>
                  )}
                  <span className={`text-xs font-semibold px-2 py-0.5 rounded-full ${mastery.bg} ${mastery.color}`}>
                    {mastery.label}
                  </span>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <div className="flex-1 h-2 bg-secondary rounded-full overflow-hidden">
                  <div
                    className="h-full rounded-full transition-all duration-700"
                    style={{ width: `${progress}%`, backgroundColor: subject.color }}
                  />
                </div>
                <span className="text-xs text-muted-foreground flex-shrink-0 w-16 text-left">
                  {completedLessons}/{totalLessons} درس
                </span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

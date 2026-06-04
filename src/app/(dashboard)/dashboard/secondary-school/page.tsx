import { getSecondarySummary } from "@/features/secondary/lib/secondary-curriculum";

export default function SecondarySchoolDashboardPage() {
  const summary = getSecondarySummary();

  return (
    <main className="mx-auto max-w-6xl space-y-8 p-6">
      <section className="rounded-3xl border bg-background p-8 shadow-sm">
        <p className="text-sm font-medium text-muted-foreground">الثانوي والباكالوريا</p>
        <h1 className="mt-2 text-3xl font-bold tracking-tight">مركز الثانوي والباكالوريا</h1>
        <p className="mt-3 max-w-3xl text-muted-foreground">
          طبقة تعليمية موجهة للثانوي: استدلال عميق، استعداد للامتحانات،
          خطط مراجعة ذكية، وتمارين بأسلوب الفروض والباكالوريا.
        </p>
      </section>

      <section className="grid gap-4 md:grid-cols-3">
        <div className="rounded-2xl border p-5">
          <p className="text-sm text-muted-foreground">عدد الدروس المنظمة</p>
          <p className="mt-2 text-3xl font-bold">{summary.totalLessons}</p>
        </div>
        <div className="rounded-2xl border p-5">
          <p className="text-sm text-muted-foreground">المستويات</p>
          <p className="mt-2 text-3xl font-bold">{summary.grades.length}</p>
        </div>
        <div className="rounded-2xl border p-5">
          <p className="text-sm text-muted-foreground">المواد</p>
          <p className="mt-2 text-3xl font-bold">{summary.subjects.length}</p>
        </div>
      </section>

      <section className="rounded-3xl border p-6">
        <h2 className="text-xl font-semibold">محركات الثانوي</h2>
        <div className="mt-4 grid gap-3 md:grid-cols-2">
          {[
            "حل خطوة بخطوة",
            "الاستعداد للباكالوريا",
            "ذكاء الامتحانات",
            "كشف الأخطاء الشائعة",
            "المراجعة التكيفية",
            "دعم العربية والفرنسية",
          ].map((item) => (
            <div key={item} className="rounded-2xl bg-muted/40 p-4">{item}</div>
          ))}
        </div>
      </section>
    </main>
  );
}

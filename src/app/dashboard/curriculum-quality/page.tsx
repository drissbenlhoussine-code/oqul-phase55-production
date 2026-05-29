async function getReport() {
  try {
    const res = await fetch(`${process.env.NEXT_PUBLIC_APP_URL ?? "http://localhost:3000"}/api/curriculum/quality-report`, {
      cache: "no-store",
    });
    if (!res.ok) return null;
    const data = await res.json();
    return data.report;
  } catch {
    return null;
  }
}

type WeakLesson = {
  id: string;
  score: number;
  grade: string;
  subject: string;
  title: string;
  issues?: string[];
};

export default async function CurriculumQualityPage() {
  const report = await getReport();

  if (!report) {
    return (
      <main className="mx-auto max-w-5xl p-6">
        <section className="rounded-3xl border p-8">
          <p className="text-sm text-muted-foreground">Oqul Phase50.4</p>
          <h1 className="mt-2 text-3xl font-bold">تقرير جودة المنهج غير موجود</h1>
          <p className="mt-4 text-muted-foreground">
            شغّل الأمر التالي أولًا:
          </p>
          <pre className="mt-4 rounded-2xl bg-muted p-4 text-sm">node scripts/audit-curriculum-quality.mjs</pre>
        </section>
      </main>
    );
  }

  const statuses = report.byStatus ?? {};
  const weakest: WeakLesson[] = report.weakestLessons ?? [];

  return (
    <main className="mx-auto max-w-6xl space-y-8 p-6">
      <section className="rounded-3xl border bg-background p-8 shadow-sm">
        <p className="text-sm font-medium text-muted-foreground">Oqul Phase50.4</p>
        <h1 className="mt-2 text-3xl font-bold tracking-tight">Curriculum Quality Assurance</h1>
        <p className="mt-3 max-w-3xl text-muted-foreground">
          هذه الصفحة تفحص جودة الدروس بعد الحقن: العمق، الأمثلة، التمارين، الأخطاء الشائعة، العلاج التربوي، وارتباط ليلى.
        </p>
      </section>

      <section className="grid gap-4 md:grid-cols-4">
        <div className="rounded-2xl border p-5">
          <p className="text-sm text-muted-foreground">عدد الدروس</p>
          <p className="mt-2 text-3xl font-bold">{report.totalLessons}</p>
        </div>
        <div className="rounded-2xl border p-5">
          <p className="text-sm text-muted-foreground">متوسط الجودة</p>
          <p className="mt-2 text-3xl font-bold">{report.averageScore}%</p>
        </div>
        <div className="rounded-2xl border p-5">
          <p className="text-sm text-muted-foreground">جيدة/ممتازة</p>
          <p className="mt-2 text-3xl font-bold">{(statuses.good ?? 0) + (statuses.excellent ?? 0)}</p>
        </div>
        <div className="rounded-2xl border p-5">
          <p className="text-sm text-muted-foreground">تحتاج مراجعة</p>
          <p className="mt-2 text-3xl font-bold">{(statuses.needs_review ?? 0) + (statuses.weak ?? 0)}</p>
        </div>
      </section>

      <section className="rounded-3xl border p-6">
        <h2 className="text-xl font-semibold">أضعف الدروس التي تحتاج تحسين</h2>
        <div className="mt-4 overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b text-right">
                <th className="p-3">النقطة</th>
                <th className="p-3">المستوى</th>
                <th className="p-3">المادة</th>
                <th className="p-3">الدرس</th>
                <th className="p-3">المشاكل</th>
              </tr>
            </thead>
            <tbody>
              {weakest.slice(0, 30).map((row) => (
                <tr key={row.id} className="border-b">
                  <td className="p-3 font-medium">{row.score}</td>
                  <td className="p-3">{row.grade}</td>
                  <td className="p-3">{row.subject}</td>
                  <td className="p-3">{row.title}</td>
                  <td className="p-3">{row.issues?.join(", ")}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </main>
  );
}

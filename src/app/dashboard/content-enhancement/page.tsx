async function getReport() {
  try {
    const res = await fetch(`${process.env.NEXT_PUBLIC_APP_URL ?? "http://localhost:3000"}/api/curriculum/enhancement-report`, { cache: "no-store" });
    if (!res.ok) return null;
    const data = await res.json();
    return data.report;
  } catch {
    return null;
  }
}

export default async function ContentEnhancementPage() {
  const report = await getReport();

  return (
    <main className="mx-auto max-w-5xl space-y-8 p-6">
      <section className="rounded-3xl border p-8">
        <p className="text-sm text-muted-foreground">Oqul Phase50.5</p>
        <h1 className="mt-2 text-3xl font-bold">Deep Content Enhancer</h1>
        <p className="mt-3 text-muted-foreground">
          هذه المرحلة تحسن الدروس الضعيفة والسطحية وتحولها إلى شروحات أعمق مع أمثلة وتمارين وعلاج تربوي.
        </p>
      </section>

      {report ? (
        <section className="grid gap-4 md:grid-cols-3">
          <div className="rounded-2xl border p-5"><p className="text-sm text-muted-foreground">الدروس المفحوصة</p><p className="mt-2 text-3xl font-bold">{report.scannedLessons}</p></div>
          <div className="rounded-2xl border p-5"><p className="text-sm text-muted-foreground">الدروس الضعيفة المختارة</p><p className="mt-2 text-3xl font-bold">{report.weakSelected}</p></div>
          <div className="rounded-2xl border p-5"><p className="text-sm text-muted-foreground">المحدثة</p><p className="mt-2 text-3xl font-bold">{report.updated}</p></div>
        </section>
      ) : (
        <section className="rounded-3xl border p-6">
          <h2 className="text-xl font-semibold">لا يوجد تقرير بعد</h2>
          <pre className="mt-4 rounded-2xl bg-muted p-4 text-sm">node scripts/enhance-weak-lessons.mjs --limit=100</pre>
        </section>
      )}
    </main>
  );
}
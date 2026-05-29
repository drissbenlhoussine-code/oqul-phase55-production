export default function QualityDepthDashboardPage() {
  const layers = [
    {
      title: "الابتدائي",
      description: "تعلم صوتي، قصير، بصري، محفز، مبني على اللعب.",
      items: ["micro-lessons", "mini-games", "darija-first", "emotional rewards"],
    },
    {
      title: "الإعدادي",
      description: "تعلم تكيفي، واضح، محفز، مناسب للاستقلالية.",
      items: ["misconception tracking", "guided practice", "mastery checks", "motivational challenges"],
    },
    {
      title: "الثانوي",
      description: "استدلال عميق، تحضير للامتحانات، حلول منظمة.",
      items: ["exam rubrics", "step-by-step reasoning", "bac plans", "scientific verification"],
    },
  ];

  return (
    <main className="mx-auto max-w-6xl space-y-8 p-6">
      <section className="rounded-3xl border bg-background p-8 shadow-sm">
        <p className="text-sm font-medium text-muted-foreground">Oqul Phase48</p>
        <h1 className="mt-2 text-3xl font-bold tracking-tight">Quality Depth لكل الطبقات</h1>
        <p className="mt-3 max-w-3xl text-muted-foreground">
          هذه المرحلة لا تضيف مستويات جديدة، بل تعمّق جودة التعلم داخل الابتدائي والإعدادي والثانوي.
        </p>
      </section>

      <section className="grid gap-4 md:grid-cols-3">
        {layers.map((layer) => (
          <article key={layer.title} className="rounded-3xl border p-6">
            <h2 className="text-xl font-semibold">{layer.title}</h2>
            <p className="mt-2 text-sm text-muted-foreground">{layer.description}</p>
            <div className="mt-4 space-y-2">
              {layer.items.map((item) => (
                <div key={item} className="rounded-2xl bg-muted/40 px-4 py-3 text-sm">
                  {item}
                </div>
              ))}
            </div>
          </article>
        ))}
      </section>
    </main>
  );
}
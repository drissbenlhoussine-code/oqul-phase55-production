import Link from "next/link";
import { BookOpen, Brain, Languages, LineChart, Target, type LucideIcon } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";

const subjects = [
  ["∑", "الرياضيات", "جبر، هندسة، معادلات، إحصاء"],
  ["⚡", "الفيزياء والكيمياء", "كهرباء، حركة، مادة، تفاعلات"],
  ["🧬", "علوم الحياة والأرض", "خلايا، بيئة، جيولوجيا، جسم الإنسان"],
  ["ض", "العربية", "نصوص، قواعد، تعبير، بلاغة"],
  ["Fr", "الفرنسية", "Grammaire, conjugaison, compréhension, rédaction"],
  ["🌍", "الاجتماعيات", "تاريخ، جغرافيا، مواطنة"],
];

export default function MiddleSchoolPage() {
  return (
    <div className="mx-auto max-w-5xl space-y-6 animate-fade-in">
      <section className="overflow-hidden rounded-3xl bg-gradient-to-br from-slate-950 via-indigo-950 to-slate-900 p-6 text-white shadow-sm">
        <div className="inline-flex items-center gap-2 rounded-full bg-white/10 px-3 py-1 text-xs font-semibold text-indigo-100">
          <Brain className="h-3.5 w-3.5" />
          Oqul Phase42
        </div>
        <h1 className="mt-4 text-3xl font-black tracking-tight">Middle School Intelligence Upgrade</h1>
        <p className="mt-3 max-w-2xl leading-8 text-indigo-100">
          مركز ذكي للإعدادي: Curriculum Intelligence، دروس منظمة، أسئلة سقراطية، تحليل أخطاء، وليلى بالفصحى السلسة مع تغيير اللغة حسب طلب التلميذ.
        </p>
        <div className="mt-5 flex flex-wrap gap-3 text-sm">
          <span className="rounded-full bg-white/10 px-3 py-1">الأولى إعدادي</span>
          <span className="rounded-full bg-white/10 px-3 py-1">الثانية إعدادي</span>
          <span className="rounded-full bg-white/10 px-3 py-1">الثالثة إعدادي</span>
        </div>
      </section>

      <div className="grid gap-4 md:grid-cols-3">
        {([
          [Target, "Competencies", "كفاءات، أهداف، متطلبات قبلية، وأخطاء شائعة."],
          [Languages, "Dynamic Language", "فصحى أولًا، ثم دارجة أو فرنسية أو إنجليزية عند الطلب."],
          [LineChart, "Adaptive Progression", "تقدم حسب الفهم، الثقة، ونوع الخطأ."],
        ] satisfies Array<[LucideIcon, string, string]>).map(([Icon, title, body]) => (
          <Card key={String(title)}>
            <CardContent className="space-y-2 p-5">
              <Icon className="h-5 w-5 text-indigo-700" />
              <h2 className="font-bold">{title}</h2>
              <p className="text-sm leading-7 text-muted-foreground">{body}</p>
            </CardContent>
          </Card>
        ))}
      </div>

      <section>
        <h2 className="mb-3 flex items-center gap-2 text-lg font-bold"><BookOpen className="h-5 w-5" /> المواد الأساسية</h2>
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {subjects.map(([icon, title, desc]) => (
            <Card key={title} className="transition hover:-translate-y-0.5 hover:shadow-md">
              <CardContent className="p-5">
                <div className="text-2xl font-black text-indigo-700">{icon}</div>
                <h3 className="mt-2 font-bold">{title}</h3>
                <p className="mt-1 text-sm leading-7 text-muted-foreground">{desc}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      <div className="rounded-3xl border bg-white p-5 shadow-sm">
        <h2 className="font-bold">Real Lesson Engine</h2>
        <p className="mt-2 leading-8 text-muted-foreground">
          كل درس في Phase42 يُبنى كمسار: هدف، شرح قصير، مثال، سؤال تفاعلي، علاج خطأ، تقييم مصغر، وملخص. هذا ليس dump للمحتوى، بل محرك تعلّم قابل للتوسع والمراجعة.
        </p>
        <Link href="/dashboard/leila" className="mt-4 inline-flex rounded-2xl bg-primary px-5 py-2.5 text-sm font-bold text-white">
          جرّب ليلى الآن
        </Link>
      </div>
    </div>
  );
}

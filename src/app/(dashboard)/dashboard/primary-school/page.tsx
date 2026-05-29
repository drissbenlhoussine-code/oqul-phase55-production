import Link from "next/link";
import { BookOpen, Brain, Heart, Mic, Sparkles } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { PrimarySchoolCard } from "@/features/primary-school/primary-school-card";

const grades = ["الأول ابتدائي", "الثاني ابتدائي", "الثالث ابتدائي", "الرابع ابتدائي", "الخامس ابتدائي", "السادس ابتدائي"];
const subjects = [
  ["🔢", "الرياضيات", "أعداد، عمليات، قياس، هندسة، مسائل قصيرة"],
  ["ض", "العربية", "قراءة، قواعد، تعبير، إملاء، فهم نص"],
  ["Fr", "الفرنسية", "Lecture, grammaire, conjugaison, production"],
  ["🔬", "النشاط العلمي", "صحة، نبات، حيوان، ماء، طاقة، تجارب آمنة"],
  ["☪", "التربية الإسلامية", "قيم، عبادات، سيرة، سلوك يومي"],
  ["🌍", "الاجتماعيات", "أسرة، مدرسة، حي، وطن، مواطنة"],
];

export default function PrimarySchoolPage() {
  return (
    <div className="mx-auto max-w-6xl space-y-6 animate-fade-in">
      <section className="overflow-hidden rounded-3xl bg-gradient-to-br from-amber-500 via-orange-500 to-rose-500 p-6 text-white shadow-sm">
        <div className="inline-flex items-center gap-2 rounded-full bg-white/15 px-3 py-1 text-xs font-semibold text-white">
          <Sparkles className="h-3.5 w-3.5" />
          Oqul Phase46 Primary Complete Layer
        </div>
        <h1 className="mt-4 text-3xl font-black tracking-tight">الابتدائي داخل Oqul — طفل أولًا</h1>
        <p className="mt-3 max-w-3xl leading-8 text-white/90">
          طبقة كاملة للابتدائي: 6 مستويات، 6 مواد، دروس قصيرة، صوت، دارجة مغربية دافئة، ألعاب صغيرة، تشجيع نفسي، وربط مباشر مع ليلى.
        </p>
        <div className="mt-5 flex flex-wrap gap-2 text-sm">
          {grades.map((grade) => <span key={grade} className="rounded-full bg-white/15 px-3 py-1">{grade}</span>)}
        </div>
      </section>

      <PrimarySchoolCard />

      <div className="grid gap-4 md:grid-cols-3">
        <Card>
          <CardContent className="space-y-2 p-5">
            <Heart className="h-5 w-5 text-rose-600" />
            <h2 className="font-bold">Emotional Tutoring</h2>
            <p className="text-sm leading-7 text-muted-foreground">الطفل يحتاج ثقة قبل الصعوبة. ليلى تكافئ المحاولة وتعيد الشرح بدون ضغط.</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="space-y-2 p-5">
            <Mic className="h-5 w-5 text-orange-600" />
            <h2 className="font-bold">Voice-first</h2>
            <p className="text-sm leading-7 text-muted-foreground">الأولوية للصوت والأسئلة القصيرة بدل القراءة الطويلة.</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="space-y-2 p-5">
            <Brain className="h-5 w-5 text-amber-700" />
            <h2 className="font-bold">Micro Learning</h2>
            <p className="text-sm leading-7 text-muted-foreground">كل درس: تهيئة، شرح بصري، سؤال، لعبة، تطبيق، تشجيع، ملاحظة للولي.</p>
          </CardContent>
        </Card>
      </div>

      <section>
        <h2 className="mb-3 flex items-center gap-2 text-lg font-bold"><BookOpen className="h-5 w-5" /> مواد الابتدائي</h2>
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {subjects.map(([icon, title, desc]) => (
            <Card key={title} className="transition hover:-translate-y-0.5 hover:shadow-md">
              <CardContent className="p-5">
                <div className="text-2xl font-black text-orange-600">{icon}</div>
                <h3 className="mt-2 font-bold">{title}</h3>
                <p className="mt-1 text-sm leading-7 text-muted-foreground">{desc}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      <div className="rounded-3xl border bg-white p-5 shadow-sm">
        <h2 className="font-bold">Primary Real Lesson Engine</h2>
        <p className="mt-2 leading-8 text-muted-foreground">
          الابتدائي ليس نسخة سهلة من الإعدادي. لذلك أضفنا محركًا خاصًا: micro-lessons، ألعاب صغيرة، إشارات للولي، دارجة افتراضية، وفصحى/فرنسية عند الطلب.
        </p>
        <Link href="/dashboard/leila" className="mt-4 inline-flex rounded-2xl bg-primary px-5 py-2.5 text-sm font-bold text-white">
          جرّب ليلى مع الابتدائي
        </Link>
      </div>
    </div>
  );
}

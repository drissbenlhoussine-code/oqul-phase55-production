import { BarChart3, BookOpen, Brain, Clock, Shield, Target } from "lucide-react";
import { Card, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { SectionHeading } from "@/components/landing/section-heading";

const features = [
  {
    icon: Brain,
    title: "تعرف أين يحتاج طفلك مساعدة",
    text: "أستاذة ليلى تكتشف نقاط الضعف تلقائياً وتركز عليها — بدل أن يظل الطفل عالقاً في نفس المشكلة.",
  },
  {
    icon: BookOpen,
    title: "دروس وتمارين حسب المنهج المغربي",
    text: "محتوى مبني على المنهج الرسمي للمملكة المغربية — من الابتدائي حتى الثانوي التأهيلي.",
  },
  {
    icon: BarChart3,
    title: "تتابع تقدم طفلك درساً بعد درس",
    text: "لوحة واضحة لولي الأمر تُظهر الدروس المكتملة ونقاط القوة وما يحتاج مراجعة.",
  },
  {
    icon: Target,
    title: "يقترح ما يجب مراجعته قبل الامتحان",
    text: "توصيات ذكية تبنى على سجل تعلّم طفلك — لا تخمين، بل تشخيص دقيق.",
  },
  {
    icon: Clock,
    title: "جلسات قصيرة وفعّالة",
    text: "10 إلى 15 دقيقة يومياً تكفي. ليلى تحافظ على تركيز الطفل وتجعل التعلم ممتعاً.",
  },
  {
    icon: Shield,
    title: "آمن للأطفال تماماً",
    text: "لا إعلانات، لا محتوى خارجي، لا بيانات شخصية. بيئة مغلقة ومراقبة مخصصة للتعلم فقط.",
  },
];

export function Features() {
  return (
    <section id="features" className="bg-muted/30 py-24">
      <div className="container">
        <SectionHeading
          eyebrow="لماذا عقول؟"
          title="ما يهم الأهل فعلاً"
          description="لا تسويق فارغ. عقول يحل مشاكل حقيقية يواجهها الأهل كل يوم مع أبنائهم."
        />
        <div className="mt-14 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {features.map((feature) => (
            <Card key={feature.title} className="glass-card p-2 transition hover:-translate-y-1 hover:shadow-glow">
              <CardHeader>
                <div className="mb-5 grid h-16 w-16 place-items-center rounded-3xl bg-primary/10 text-primary">
                  <feature.icon className="h-8 w-8" />
                </div>
                <CardTitle>{feature.title}</CardTitle>
                <CardDescription>{feature.text}</CardDescription>
              </CardHeader>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}

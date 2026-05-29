import { BarChart3, BookOpen, Brain, Globe2, Sparkles, Zap } from "lucide-react";
import { Card, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { SectionHeading } from "@/components/landing/section-heading";

const features = [
  { icon: Brain, title: "ليلى المعلمة الذكية", text: "تشرح للطفل بصبر ودفء، وتتكيف مع مستواه ونقاط ضعفه." },
  { icon: BookOpen, title: "مناهج مغربية", text: "محتوى مصمم للدعم المنزلي والمراجعة وفق بنية المناهج المغربية." },
  { icon: Globe2, title: "تعلم بثلاث لغات", text: "العربية، الفرنسية، والأمازيغية مع دارجة طبيعية عند الحاجة." },
  { icon: Zap, title: "تعلم تفاعلي", text: "تمارين واختبارات ذكية تجعل التعلم ممتعًا وليس مرهقًا." },
  { icon: BarChart3, title: "تتبع التقدم", text: "لوحة واضحة للأهل تعرض التقدم ونقاط القوة والتحسين." },
  { icon: Sparkles, title: "تجربة مخصصة", text: "توصيات تعليمية مبنية على أداء الطفل وسجل تعلمه." }
];

export function Features() {
  return (
    <section id="features" className="bg-muted/30 py-24">
      <div className="container">
        <SectionHeading
          eyebrow="لماذا عقول؟"
          title="تعليم مُصمم لطفلك"
          description="نجمع بين أحدث تقنيات الذكاء الاصطناعي وتجربة تعليمية عربية مغربية واضحة ودافئة."
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

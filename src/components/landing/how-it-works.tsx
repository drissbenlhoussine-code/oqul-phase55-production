import { Brain, Lightbulb, Trophy } from "lucide-react";
import { SectionHeading } from "@/components/landing/section-heading";

const steps = [
  { icon: Lightbulb, label: "الخطوة 1", title: "أنشئ حسابك", text: "سجّل مجانًا وأخبرنا عن مستوى طفلك وأهدافه التعليمية." },
  { icon: Brain, label: "الخطوة 2", title: "اختر المستوى", text: "نحدد المحتوى المناسب ونقترح خطة تعلم واضحة." },
  { icon: Trophy, label: "الخطوة 3", title: "تعلّم وتفوّق", text: "دروس مبسطة، تمارين، اختبارات، وتتبع مستمر للتقدم." }
];

export function HowItWorks() {
  return (
    <section id="how" className="py-24">
      <div className="container">
        <SectionHeading
          eyebrow="سهل وبسيط"
          title="كيف يعمل عقول؟"
          description="ثلاث خطوات بسيطة لبدء رحلة تعليمية ذكية ومنظمة من البيت."
        />
        <div className="mt-16 grid gap-8 md:grid-cols-3">
          {steps.map((step, index) => (
            <div key={step.title} className="relative text-center">
              {index < steps.length - 1 ? <div className="absolute left-0 top-14 hidden h-px w-full bg-border md:block" /> : null}
              <div className="relative mx-auto grid h-28 w-28 place-items-center rounded-full bg-primary text-primary-foreground shadow-glow">
                <step.icon className="h-10 w-10" />
              </div>
              <span className="mt-6 inline-flex rounded-full bg-secondary/20 px-4 py-1 text-sm font-black text-orange-700">
                {step.label}
              </span>
              <h3 className="mt-4 text-3xl font-black">{step.title}</h3>
              <p className="mx-auto mt-3 max-w-sm leading-8 text-muted-foreground">{step.text}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

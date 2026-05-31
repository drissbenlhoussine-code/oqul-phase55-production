import { Star } from "lucide-react";
import { Card } from "@/components/ui/card";
import { SectionHeading } from "@/components/landing/section-heading";

const testimonials = [
  { name: "فاطمة الزهراء", meta: "طالبة باكالوريا — الدار البيضاء", text: "عقول غيّر طريقة مذاكرتي. الذكاء الاصطناعي يعرف بالضبط أين أحتاج مساعدة ويركّز عليها." },
  { name: "يوسف أمين", meta: "طالب إعدادي — مراكش", text: "أحب أنه يدعم العربية والأمازيغية. الدروس ممتعة والاختبارات تساعدني أفهم أخطائي." },
  { name: "سارة", meta: "الأم — الرباط", text: "أخيراً أستطيع متابعة تقدم ابني بطريقة واضحة، ومعرفة المواد التي يحتاج فيها دعماً أكثر." }
];

export function Testimonials() {
  return (
    <section id="testimonials" className="bg-muted/30 py-24">
      <div className="container">
        <SectionHeading
          eyebrow="آراء الأهل"
          title="ماذا يقول الأهل؟"
          description="تجارب حقيقية من أولياء أمور يبحثون عن دعم تعليمي منظم وواضح لأبنائهم."
        />
        <div className="mt-14 grid gap-6 lg:grid-cols-3">
          {testimonials.map((item) => (
            <Card key={item.name} className="glass-card p-8">
              <div className="flex gap-1 text-secondary">
                {Array.from({ length: 5 }).map((_, index) => <Star key={index} className="h-5 w-5 fill-current" />)}
              </div>
              <p className="mt-6 text-lg leading-9 text-muted-foreground">“{item.text}”</p>
              <div className="mt-7 flex items-center gap-4">
                <div className="grid h-12 w-12 place-items-center rounded-full bg-primary/10 text-xl font-black text-primary">
                  {item.name[0]}
                </div>
                <div>
                  <p className="font-black">{item.name}</p>
                  <p className="text-sm text-muted-foreground">{item.meta}</p>
                </div>
              </div>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}

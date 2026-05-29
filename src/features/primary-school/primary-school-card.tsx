import { Baby, Gamepad2, Mic, Sparkles, Star, type LucideIcon } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";

const features: Array<[LucideIcon, string, string]> = [
  [Mic, "Voice-first", "ليلى تتكلم أكثر، تسأل بصوت، وتشجع الطفل بجمل قصيرة."],
  [Gamepad2, "Mini-games", "مطابقة، ترتيب، اختيار، وعدّ سريع بدل تمارين طويلة."],
  [Star, "Rewards", "نجوم، ملصقات، مهام يومية، ورسائل نجاح صغيرة."],
];

export function PrimarySchoolCard() {
  return (
    <div className="grid gap-4 md:grid-cols-3">
      {features.map(([Icon, title, body]) => (
        <Card key={title} className="border-amber-100 bg-amber-50/40">
          <CardContent className="space-y-2 p-5">
            <Icon className="h-5 w-5 text-amber-700" />
            <h3 className="font-bold">{title}</h3>
            <p className="text-sm leading-7 text-muted-foreground">{body}</p>
          </CardContent>
        </Card>
      ))}
      <Card className="md:col-span-3">
        <CardContent className="flex flex-col gap-3 p-5 md:flex-row md:items-center">
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-amber-100 text-amber-800">
            <Baby className="h-6 w-6" />
          </div>
          <div>
            <h3 className="font-black">Primary Layer جاهزة كطبقة طفل أولًا</h3>
            <p className="text-sm leading-7 text-muted-foreground">
              نفس قلب Oqul، لكن بتجربة مختلفة: دارجة دافئة، دروس قصيرة، ألعاب، صوت، وتشجيع نفسي مستمر.
            </p>
          </div>
          <Sparkles className="ms-auto hidden h-6 w-6 text-amber-600 md:block" />
        </CardContent>
      </Card>
    </div>
  );
}

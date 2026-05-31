import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Bell, UserCog, Shield, Palette } from "lucide-react";

const upcomingSettings = [
  { icon: UserCog,  title: "معلومات الحساب",    desc: "تعديل الاسم وكلمة المرور والبريد الإلكتروني." },
  { icon: Bell,     title: "الإشعارات",          desc: "تنبيهات يومية لتذكير طفلك بجلسة التعلم." },
  { icon: Palette,  title: "تخصيص التجربة",     desc: "اختيار اللغة المفضلة للشرح ومستوى الصعوبة." },
  { icon: Shield,   title: "إعدادات الخصوصية",  desc: "التحكم في البيانات والسماحيات." },
];

export default function SettingsPage() {
  return (
    <div className="max-w-2xl space-y-6">
      <div>
        <h1 className="text-2xl font-bold">الإعدادات</h1>
        <p className="mt-1 text-muted-foreground text-sm">سيتم إطلاق إعدادات الحساب قريبًا.</p>
      </div>

      <div className="grid gap-3 sm:grid-cols-2">
        {upcomingSettings.map(({ icon: Icon, title, desc }) => (
          <Card key={title} className="opacity-60">
            <CardHeader className="pb-2">
              <CardTitle className="text-sm flex items-center gap-2">
                <Icon className="w-4 h-4 text-muted-foreground" />
                {title}
              </CardTitle>
            </CardHeader>
            <CardContent className="text-xs text-muted-foreground leading-relaxed">
              {desc}
            </CardContent>
          </Card>
        ))}
      </div>

      <p className="text-xs text-muted-foreground text-center">
        لديك اقتراح؟ راسلنا على{" "}
        <a href="mailto:support@oqul.ma" className="text-primary hover:underline">
          support@oqul.ma
        </a>
      </p>
    </div>
  );
}

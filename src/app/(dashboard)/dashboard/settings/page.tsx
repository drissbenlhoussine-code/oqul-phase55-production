import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";

export default function SettingsPage() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-black">الإعدادات</h1>
        <p className="mt-2 text-muted-foreground">إعدادات الحساب والتجربة التعليمية.</p>
      </div>
      <Card>
        <CardHeader>
          <CardTitle>قريبًا</CardTitle>
          <CardDescription>سيتم تفعيل إعدادات الحساب والإشعارات في النسخة القادمة.</CardDescription>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">
          هذه الصفحة مضافة لمنع روابط مكسورة داخل القائمة الجانبية.
        </CardContent>
      </Card>
    </div>
  );
}

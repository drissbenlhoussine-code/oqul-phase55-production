# Oqul Phase38 — Core v1 Fusion Report

هذه النسخة تدمج النسخة المستقرة Phase37 مع أفضل فكرة قوية من v13: **عقول المتعدد / Multi-Agent Pipeline**.

## ما تم دمجه من v13

- مفهوم Pipeline متعدد الوكلاء.
- أنواع التشغيل: بحث شامل، بحث وملخص، تحليل عميق، إجابة فورية.
- تجربة عرض كل وكيل على حدة مع مخرجاته.
- تحويل الطلب إلى نتيجة Markdown قابلة للتنزيل.

## ما تم تطويره فوق v13

- أضيف وكيل تربوي جديد: **الخبير التربوي**.
- أضيف Flow جديد: **تحويل إلى درس**.
- تم ربط الميزة داخل Dashboard في `/dashboard/pipeline`.
- تم تحديث Sidebar لإظهار: **عقول المتعدد**.
- تم بناء API جديد متوافق مع نظام Auth الحالي في Phase37.
- تم استخدام SSE streaming لإظهار عمل الوكلاء لحظة بلحظة.
- تم الحفاظ على قاعدة البيانات والـ production build من Phase37 دون كسر.

## ملاحظات تشغيل

1. يجب وجود `GROQ_API_KEY` في `.env.local`.
2. يجب أن تكون مسجلاً للدخول لاستخدام `/dashboard/pipeline`.
3. الميزة لا تتصفح الويب حاليًا؛ هي بحث/تحليل/صياغة داخلية بالذكاء الاصطناعي. إذا احتاجت مصادر خارجية ستذكر ذلك بوضوح.

## الملفات المهمة المضافة

- `src/app/(dashboard)/dashboard/pipeline/page.tsx`
- `src/app/api/ai/pipeline/route.ts`
- `src/server/ai/pipeline/config.ts`
- `src/server/ai/pipeline/prompts.ts`
- `src/server/ai/pipeline/types.ts`
- `src/components/ui/textarea.tsx`

## الهدف من Phase38

العودة إلى روح v13: منتج واضح وسهل الاستخدام، لكن مع قوة Phase37 الإنتاجية.

# Oqul Phase42 — Middle School Intelligence Upgrade

## الهدف

تحويل Oqul من تجربة تعليمية عامة إلى **Moroccan AI Learning Companion for Middle School Students**، مع التركيز على الإعدادي أولًا:

- الأولى إعدادي
- الثانية إعدادي
- الثالثة إعدادي

تم تنفيذ هذه المرحلة كطبقة آمنة فوق Phase40، بدون إعادة كتابة المصادقة أو قاعدة البيانات أو البنية الحساسة.

---

## ما تمت إضافته

### 1) Curriculum Intelligence للإعدادي

ملفات جديدة:

- `src/server/middle-school/types.ts`
- `src/server/middle-school/curriculum.ts`

تحتوي على:

- المواد الأساسية كاملة
- كفاءات لكل مادة
- أهداف تعليمية
- prerequisites
- misconceptions
- lesson seeds
- exercise types

المواد:

- الرياضيات
- الفيزياء والكيمياء
- علوم الحياة والأرض
- العربية
- الفرنسية
- الاجتماعيات

---

### 2) Dynamic Language System

ملف جديد:

- `src/server/middle-school/language-policy.ts`

القرار الاستراتيجي:

- ليلى تبدأ بالفصحى السلسة للإعدادي
- تتحول تلقائيًا حسب طلب التلميذ:
  - الدارجة المغربية
  - الفرنسية
  - الإنجليزية
  - الفصحى

أمثلة مدعومة:

- `اشرح بالدارجة`
- `Explain in French`
- `Explain in English`
- `اشرح بالفصحى`

---

### 3) Real Lesson Engine

ملف جديد:

- `src/server/middle-school/lesson-engine.ts`

كل درس يُبنى كمسار:

1. هدف الدرس
2. شرح قصير
3. مثال قريب
4. سؤال تفاعلي
5. علاج خطأ
6. تقييم مصغر
7. ملخص

الهدف: عدم تحويل Oqul إلى dump للمحتوى، بل محرك تعلم قابل للتوسع.

---

### 4) Phase42 API

مسار جديد:

- `GET /api/learning/phase42?childId=...`

يعيد:

- مستوى الإعدادي
- اللغة المستهدفة
- الكفاءات ذات الأولوية
- lesson blocks
- tutor policy
- teaching loop

المسار محمي بـ `withAuth` ويستعمل `assertOwnsChild`، لذلك يحافظ على ownership checks.

---

### 5) Leila Tutor Evolution

تم تحديث:

- `src/server/ai/leila.ts`

ليلى أصبحت للإعدادي:

- تبدأ بالفصحى السلسة
- لا تستعمل أسلوب طفولي زائد
- تتبع Socratic tutoring
- تغير اللغة حسب الطلب
- تشرح، تسأل، تحلل الخطأ، ثم تصحح

---

### 6) UX مناسب للإعدادي

ملفات جديدة:

- `src/features/middle-school/middle-school-intelligence-card.tsx`
- `src/app/(dashboard)/dashboard/middle-school/page.tsx`

تمت إضافة بطاقة Phase42 إلى لوحة الطالب، مع صفحة مركز الإعدادي:

- modern
- smart
- motivating
- achievement-driven
- ليست childish cartoon

---

## ما لم يتم لمسه عمدًا

- auth
- JWT
- middleware
- Neon
- Redis
- BullMQ
- OpenTelemetry
- Sentry
- production deployment flow
- database migrations

هذه المرحلة تضيف depth ولا تضيف infrastructure complexity.

---

## أوامر التحقق

بعد فك الضغط محليًا:

```bash
npm install
npm run verify:phase42
```

ملاحظة: لم يتم تشغيل build داخل بيئة التعديل لأن `node_modules` غير موجودة داخل النسخة المضغوطة.

---

## الخلاصة

Phase42 يضع Oqul على مسار أوضح:

> Moroccan AI Learning Companion for Middle School Students

ليس موقع دروس، بل نظام تعلّم ذكي للإعدادي مبني حول:

- curriculum intelligence
- adaptive lesson engine
- dynamic language
- Socratic Leila
- واجهة أنضج للتلاميذ الأكبر سنًا

# عقول (OQUL) — منصة التعليم الذكي المغربي

## 🚀 البدء السريع

### المتطلبات
- Node.js 20+
- PostgreSQL (أو Neon.tech مجانًا)
- مفتاح Groq API من console.groq.com

### 1. تثبيت التبعيات
```bash
npm install
```

### 2. إعداد متغيرات البيئة
```bash
cp .env.example .env.local
```
ثم عدّل `.env.local`:
```env
DATABASE_URL=postgresql://...
AUTH_SECRET=minimum-32-characters-random-string
GROQ_API_KEY=gsk_your_key_here
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

### 3. إنشاء قاعدة البيانات
```bash
npm run db:push
npm run db:seed
```

### 4. تشغيل المشروع
```bash
npm run dev
```

الموقع متاح على http://localhost:3000

### بيانات التجربة
- البريد: demo@oqul.ma
- كلمة المرور: demo1234

---

## 🏗️ البنية التقنية

```
src/
├── app/                    # Next.js App Router
│   ├── (auth)/            # صفحات المصادقة
│   ├── (dashboard)/       # لوحة التحكم المحمية
│   ├── api/               # API routes
│   └── parent/            # لوحة الأهل
├── components/            # مكونات قابلة للاستخدام
│   ├── ui/                # مكونات أساسية
│   └── layout/            # هيكل الصفحة
├── db/                    # Drizzle ORM
│   ├── schema.ts          # جداول قاعدة البيانات
│   └── seed.ts            # البيانات الأولية
└── server/                # منطق الخادم فقط
    ├── auth/              # JWT + Cookies
    ├── repositories/      # طبقة البيانات
    ├── ai/                # ليلى AI (Groq)
    └── errors/            # معالجة الأخطاء
```

## 🌟 الميزات

- **ليلى AI**: مساعدة ذكية تتحدث الدارجة مع streaming حقيقي من Groq
- **المنهج الكامل**: ابتدائي → إعدادي → ثانوي
- **نظام التقدم**: تتبع الدروس والنتائج والنقاط
- **الاختبارات**: تصحيح تلقائي مع XP
- **لوحة الأهل**: متابعة تقدم الأطفال
- **RTL كامل**: واجهة عربية أصيلة

## 📦 النشر على Vercel + Neon

```bash
# 1. أنشئ قاعدة بيانات على neon.tech
# 2. انسخ DATABASE_URL
# 3. npm run db:push
# 4. npm run db:seed
# 5. vercel deploy
```

متغيرات البيئة المطلوبة في Vercel:
- DATABASE_URL
- AUTH_SECRET  
- GROQ_API_KEY
- NEXT_PUBLIC_APP_URL

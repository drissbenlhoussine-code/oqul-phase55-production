# دليل الإطلاق — OQUL v8

## المتطلبات
- Node.js 20+
- PostgreSQL (Neon.tech مجاني)
- Groq API Key (console.groq.com)

## الإطلاق في 5 دقائق

### 1. التثبيت
```bash
unzip oqul-v8-final.zip && cd oqul
npm install
```

### 2. متغيرات البيئة
```bash
cp .env.example .env.local
```
عدّل `.env.local`:
```env
DATABASE_URL=postgresql://...   # من Neon.tech
AUTH_SECRET=<openssl rand -base64 32>
GROQ_API_KEY=gsk_...            # مفتاح جديد من console.groq.com
NEXT_PUBLIC_APP_URL=https://oqul.ma
```

### 3. قاعدة البيانات
```bash
npm run db:push    # يُنشئ الجداول
npm run db:seed    # يملأ المنهج الدراسي
```

### 4. الإطلاق المحلي
```bash
npm run dev
# → http://localhost:3000
# حساب تجربة: demo@oqul.ma / demo1234
```

### 5. الإنتاج (Vercel + Neon)
```bash
# أنشئ مشروع على vercel.com
vercel deploy

# أضف متغيرات البيئة في Vercel Dashboard:
# DATABASE_URL, AUTH_SECRET, GROQ_API_KEY, NEXT_PUBLIC_APP_URL
```

## الاختبارات
```bash
npm test            # تشغيل 82 test case
npm run typecheck   # TypeScript check
npm run lint        # ESLint
npm run build       # بناء للإنتاج
```

## البنية السريعة
```
src/
├── app/                    # Next.js pages + API routes (22 endpoint)
├── features/               # Feature-based components
│   ├── ai-tutor/          # ليلى — streaming chat + memory
│   ├── learning/          # LessonViewer + QuizQuestion
│   ├── gamification/      # XP, badges, streak, mastery
│   ├── dashboard/         # StudentDashboard + DailyGreeting
│   ├── onboarding/        # 3-step wizard
│   └── parent/            # Parent dashboard
├── server/
│   ├── ai/               # Groq streaming + adaptive prompt
│   ├── auth/             # JWT + ownership + guards
│   ├── repositories/     # All DB queries
│   ├── services/         # Business logic (10 services)
│   └── security/         # Rate limiting + audit + CSRF
└── db/                    # Drizzle schema + seed
```

## مستويات الأمان
- ✅ CSP nonce + strict-dynamic (production)
- ✅ HSTS + X-Frame-Options + nosniff + Permissions-Policy
- ✅ JWT access token (httpOnly, 7d) + Refresh token rotation (30d)
- ✅ Token family theft detection (revoke entire family on reuse)
- ✅ Session management API (list/revoke devices)
- ✅ Rate limiting: login (5/15min), register (3/hr), AI (10/min)
- ✅ Ownership checks — zero-trust on all childId inputs
- ✅ 19/22 routes with withAuth() — 3 intentionally public
- ✅ Audit logging on all auth events
- ✅ Per-minute AI rate limiting to prevent abuse

## المنهج الدراسي الحالي
- السنة الأولى ابتدائي: عربية (8 دروس) + رياضيات (6 دروس)
- السنة الثانية ابتدائي: عربية (1 درس)
- السنة الرابعة ابتدائي: رياضيات/كسور (1 درس)
- + بنية كاملة لجميع المراحل جاهزة للإضافة

## إضافة محتوى جديد

### 1. عبر Admin UI (الأسهل)
```
/admin → مولّد المحتوى التعليمي
```
اختر المادة والمستوى والموضوع — الذكاء الاصطناعي يولد الدرس كاملاً في 10 ثوانٍ.

### 2. عبر Curriculum Files
```bash
# أضف بيانات لـ src/db/curriculum/
# ثم أضف الاستيراد في seed-curriculum.ts
npm run db:seed:curriculum
```

### 3. عبر Drizzle Studio
```bash
npm run db:studio
# → localhost:4983
```

### المحتوى الحالي (seed.ts)
- السنة الأولى: عربية (8 دروس) + رياضيات (6 دروس)
- السنة الثانية: عربية (2 درس)
- السنة الرابعة: رياضيات/كسور (1 درس)

### إضافة الحروف المتبقية (أ حتى ي)
```bash
npm run db:seed:curriculum
# يضيف 8 أحرف من الملف الجاهز
# للحروف المتبقية: استخدم Admin Generator
```

## Pre-Launch Checklist (Beta)

### Required before first users
- [ ] Database created (Neon.tech free tier)
- [ ] `npm run db:push && npm run db:seed` ran successfully
- [ ] GROQ_API_KEY set and working (`curl https://api.groq.com/openai/v1/models -H "Authorization: Bearer $GROQ_API_KEY"`)
- [ ] Test registration → onboarding → first lesson → quiz complete → XP awarded
- [ ] At least 3 subjects with lessons seeded for your target grade

### Content before launch
Run the admin content generator to add lessons for your target grade:
1. Login as admin user
2. Go to `/admin`
3. Generate 3-5 lessons per subject for your target grade
4. Each lesson takes ~10 seconds to generate

### Recommended for Beta (20-50 users)
- [ ] Set REDIS_URL (Upstash free tier: redis.upstash.com)
- [ ] Vercel deployment with env vars
- [ ] Monitor `/api/health` endpoint

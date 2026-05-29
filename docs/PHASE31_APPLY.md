# Phase 31 — دليل التطبيق الدقيق

## ما هذا؟
ملفات جديدة وتعديلات بسيطة تضيف 3 أشياء للمشروع:
1. نظام البريد الإلكتروني (verify + reset password)
2. صفحات Privacy & Terms
3. موافقة ولي الأمر في التسجيل

**لا يوجد تغيير على: middleware, auth JWT, Redis, BullMQ, DB migrations القديمة, أي infrastructure**

---

## الخطوة 1 — تشغيل migration قاعدة البيانات

```bash
psql $DATABASE_URL -f db/migrations/017_email_verification.sql
```

أو عبر Drizzle (إذا أضفت الحقول لـ schema.ts أولاً):
```bash
npm run db:push
```

---

## الخطوة 2 — تعديل schema.ts (6 أسطر)

في ملف `src/db/schema.ts`، داخل جدول `users`، بعد سطر `trialEndsAt`:

```ts
// Phase 31 — email & password reset
emailVerified:            boolean("email_verified").notNull().default(false),
emailVerificationToken:   text("email_verification_token"),
emailVerificationSentAt:  timestamp("email_verification_sent_at", { withTimezone: true }),
passwordResetToken:       text("password_reset_token"),
passwordResetExpiresAt:   timestamp("password_reset_expires_at", { withTimezone: true }),
termsAcceptedAt:          timestamp("terms_accepted_at", { withTimezone: true }),
```

---

## الخطوة 3 — نسخ الملفات الجديدة

انسخ هذه الملفات من هذا المجلد إلى المشروع (مسارات مطابقة):

### ملفات جديدة بالكامل (copy as-is):
```
src/server/email/email-service.ts
src/server/auth/tokens.ts
src/server/repositories/users-email-repo.ts
src/server/ai/leila-safety.ts

src/app/api/auth/verify-email/route.ts
src/app/api/auth/forgot-password/route.ts
src/app/api/auth/reset-password/route.ts

src/app/privacy/page.tsx
src/app/terms/page.tsx
```

### ملفات تحلّ محلّ الموجودة (replace):
```
src/app/api/auth/register/route.ts   ← يضيف termsAccepted + email verification
src/lib/env.ts                        ← يضيف RESEND_API_KEY + EMAIL_FROM
```

### ملفات auth pages (انسخ من auth-pages/ إلى المسار الصحيح):
```
src/app/auth-pages/login/page.tsx        → src/app/(auth)/login/page.tsx
src/app/auth-pages/forgot-password/      → src/app/(auth)/forgot-password/page.tsx
src/app/auth-pages/reset-password/       → src/app/(auth)/reset-password/page.tsx
src/app/(auth)/register/page.tsx         ← موجود في المجلد مباشرة
```

---

## الخطوة 4 — تعديل leila.ts (سطران)

في `src/server/ai/leila.ts`، أضف في الأعلى:
```ts
import { LEILA_SAFETY_RULES, sanitizeUserInput } from "./leila-safety";
```

في نهاية `buildLeilaSystemPrompt()` قبل الـ `return`:
```ts
return `...existing return content...\n\n${LEILA_SAFETY_RULES}`;
```

وفي مكان استقبال user message، مرّره عبر:
```ts
const safeMessage = sanitizeUserInput(userMessage);
```

---

## الخطوة 5 — إضافة متغيرات البيئة

```bash
cp .env.example .env.local
# ثم عدّل .env.local وأضف:
RESEND_API_KEY="re_..."
EMAIL_FROM="Oqul <no-reply@oqul.ma>"
```

---

## الخطوة 6 — تثبيت Resend

```bash
npm install resend
```

ملاحظة: `email-service.ts` يستخدم `fetch` مباشرة إلى Resend API — لا يحتاج الـ SDK إذا أردت تجنب التبعيات.
إذا أردت الـ SDK: `npm install resend` ثم عدّل `email-service.ts` لاستخدام `new Resend(apiKey).emails.send(...)`.

---

## الخطوة 7 — التحقق

```bash
npm run typecheck    # يجب أن يمر بدون أخطاء
npm run build        # يجب أن يبني بنجاح
npm run dev          # ثم اختبر:
```

اختبر هذه المسارات:
```
http://localhost:3000/privacy           ← يجب أن تفتح
http://localhost:3000/terms             ← يجب أن تفتح
http://localhost:3000/register          ← يجب أن يظهر checkbox الموافقة
http://localhost:3000/forgot-password   ← يجب أن تفتح
```

---

## ما لم يتغير ✅

- middleware.ts
- src/server/auth/jwt.ts
- src/server/auth/refresh-token.ts
- src/server/auth/cookies.ts
- src/server/repositories/users.ts (لم نعدّله، أضفنا users-email-repo.ts فقط)
- جميع ملفات infra/
- جميع migrations قبل 017
- BullMQ / Redis
- AI engine / Groq integration
- Dashboard / Learning features
- Gamification

# Oqul Fusion — Final Merged Local Build

هذه النسخة مدمجة من Phase32 + Phase34 fixes.

## التشغيل المحلي

```powershell
cd "$HOME\Downloads\oqul-fusion"
npm install
Copy-Item .env.example .env.local -Force
notepad .env.local
npm run dev
```

افتح:

- http://localhost:3000
- http://localhost:3000/test-routes
- http://localhost:3000/login
- http://localhost:3000/register
- http://localhost:3000/faq
- http://localhost:3000/privacy
- http://localhost:3000/terms
- http://localhost:3000/visual-demo
- http://localhost:3000/phase31-demo

## ملاحظات مهمة

- لا تشغّل `npm run db:push` على قاعدة Neon فيها schema قديم أو Neon Auth قبل التأكد من branch clean.
- لو ظهر خطأ cache/chunk: أوقف السيرفر ثم نفّذ `Remove-Item -Recurse -Force .next` وشغّل من جديد.

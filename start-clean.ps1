# Oqul clean local start
# يزيل متغيرات Turbopack والكاش ثم يشغل المشروع من Webpack العادي.
$ErrorActionPreference = "Stop"
Remove-Item Env:\TURBOPACK -ErrorAction SilentlyContinue
Remove-Item Env:\NEXT_TURBOPACK -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force .next -ErrorAction SilentlyContinue
npm run dev

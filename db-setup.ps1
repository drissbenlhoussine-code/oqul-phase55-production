Write-Host "Setting environment..." -ForegroundColor Cyan
Copy-Item .env.local .env -Force
$env:DATABASE_URL = (Select-String -Path .env.local -Pattern '^DATABASE_URL=').Line.Split('=',2)[1].Trim('"')
$groq = Select-String -Path .env.local -Pattern '^GROQ_API_KEY=' -ErrorAction SilentlyContinue
if ($groq) { $env:GROQ_API_KEY = $groq.Line.Split('=',2)[1].Trim('"') }
Write-Host "Pushing database schema..." -ForegroundColor Cyan
npm run db:push
Write-Host "Seeding curriculum..." -ForegroundColor Cyan
npm run db:seed
Write-Host "Database setup done." -ForegroundColor Green

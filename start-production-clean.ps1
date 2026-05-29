Write-Host "Preparing production build..." -ForegroundColor Cyan
Copy-Item .env.local .env -Force
Remove-Item -Recurse -Force .next -ErrorAction SilentlyContinue
npm run build
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "Starting production server..." -ForegroundColor Green
npm run start

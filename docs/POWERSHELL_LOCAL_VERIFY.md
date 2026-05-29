# PowerShell Local Verification

Run from inside the project folder:

```powershell
cd .\oqul-fusion

node -v
npm -v

npm ci
npm run typecheck
npm test
npm run build
```

If `npm ci` passes, the lockfile is aligned.

If `npm run build` fails, copy the first real error and fix only that error before adding any new features.

## Optional development server

```powershell
npm run dev
```

Then open:

```txt
http://localhost:3000
```

## Production preview API safety

Preview APIs are disabled in production unless:

```powershell
$env:ENABLE_PREVIEW_APIS="true"
```

Metrics endpoint should use:

```powershell
$env:METRICS_BEARER_TOKEN="your-secret-token"
```

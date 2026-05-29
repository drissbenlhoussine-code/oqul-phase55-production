# Phase 32 Product Polish Stabilization

This version fixes the last known TypeScript parsing risk in the product-polish snapshot.

## Fixed

- Removed raw Markdown triple-backticks from `src/server/ai/content-generator.ts` prompt text.
- Preserved the prompt intent: the model should still return JSON only, without Markdown/code fences.
- Normalized `next.config.ts` if it contained deprecated `experimental.serverComponentsExternalPackages`.

## Not touched

- auth logic
- database schema
- Redis/BullMQ
- governance/trust/replay/routing systems
- product architecture

## Verify locally

```powershell
npm run typecheck
npm run lint
npm run build
npm run dev
```

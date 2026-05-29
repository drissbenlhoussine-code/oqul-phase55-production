# Phase 32 Safe Product Polish Merge

This merge imports only product-facing UX improvements from the Phase 32 package.

## Added

- Landing pricing section
- FAQ page
- Dashboard skeleton loader
- Phase 32 CSS additions
- Product footer/hero improvements when compatible

## Avoided

No auth, database, middleware, Redis, BullMQ, routing, replay, governance, or PKI systems were touched.

## Why this matters

Oqul already has strong infrastructure. Phase 32 improves the public-facing product layer:
- parents understand pricing
- FAQ answers purchase objections
- footer links are real
- dashboard loading feels professional
- landing page looks closer to launch quality

## Verify

```powershell
npm run typecheck
npm run lint
npm run build
npm run dev
```

Open:

```txt
/
 /faq
 /visual-demo
 /phase31-demo
```

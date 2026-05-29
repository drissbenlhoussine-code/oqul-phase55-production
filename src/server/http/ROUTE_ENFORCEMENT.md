# Route Enforcement Map

Every API route in this project is protected by one of these mechanisms:

## 1. `withAuth()` wrapper — standard protected routes
Used by 18 routes. Auth delegated to `requireAuth()` → `getSession()`.
Any unauthenticated request gets 401 automatically.

## 2. Inline `getSession()` — streaming routes only
Used by `/api/ai/leila` (SSE streaming — cannot use withAuth wrapper).
First line: `const session = await getSession(); if (!session) return 401`.

## 3. `routeHandler()` + `getCurrentSession()` — legacy wrapper
Used by `/api/auth/refresh`. Auth-aware via `getCurrentSession()` alias.

## 4. Auth flow endpoints — intentionally public
- `/api/auth/login` — creates session
- `/api/auth/register` — creates session  
- `/api/auth/logout` — destroys session

## 5. Public data — intentionally open
- `/api/curriculum/grades` — needed for registration grade picker

## Ownership enforcement
All endpoints that accept `childId` call `assertOwnsChild(userId, childId)`,
which verifies the child belongs to the authenticated user's account.
Zero trust on client input.

## Adding a new protected route
```typescript
// ✅ CORRECT — always use withAuth
export const GET = withAuth(async ({ session, request }) => {
  // session.sub = userId (from JWT, server-side only)
  // ...
});
```

# FINAL ARCHITECTURE — OQUL Companion Platform

## Overview

OQUL is a two-layer platform:
- **Product Layer**: warm, Moroccan, child-first — feels like a companion
- **Infrastructure Layer**: resilient, observable, deterministic — operates like enterprise software

The child never touches the infrastructure layer.

---

## Runtime Structure

```
oqul/
├── src/
│   ├── app/                      # Next.js routes
│   │   ├── api/
│   │   │   ├── ai/leila/         # Streaming AI (SSE)
│   │   │   ├── auth/             # Login, register, refresh, logout, sessions
│   │   │   ├── health/           # Docker healthcheck
│   │   │   ├── metrics/          # Prometheus scraping
│   │   │   ├── progress/         # Lesson progress, quizzes
│   │   │   ├── adaptive/         # Adaptive engine recommendations
│   │   │   └── admin/            # Content generation (admin-only)
│   │   └── (dashboard)/          # Protected pages
│   │
│   ├── features/                 # Child-facing product components
│   │   ├── ai-tutor/            # TutorChat, streaming client
│   │   ├── learning/            # LessonViewer, QuizQuestion, DailyLoop
│   │   ├── gamification/        # XP, Streaks, Badges, Celebration
│   │   ├── engagement/          # LeilaWelcome, MilestoneAlert, SessionSummary
│   │   ├── dashboard/           # StudentDashboard, DailyGreeting
│   │   └── onboarding/          # OnboardingWizard
│   │
│   ├── server/                   # Server-only code
│   │   ├── ai/
│   │   │   ├── personas/         # Darija persona system (COMPANION)
│   │   │   ├── leila.ts          # Adaptive prompt builder
│   │   │   ├── streaming/        # SSE resilience (Phase 26)
│   │   │   ├── reliability/      # AI circuit-breaking (Phase 26)
│   │   │   └── content-generator.ts  # Curriculum production
│   │   │
│   │   ├── auth/                 # JWT, refresh tokens, session
│   │   ├── cache/                # Redis + memory fallback
│   │   ├── redis/                # Resilient Redis, reconnect
│   │   ├── jobs/                 # BullMQ queues
│   │   ├── telemetry/            # Prometheus metrics
│   │   ├── observability/        # OpenTelemetry, Sentry
│   │   ├── governance/           # Revocation epochs
│   │   ├── trust/                # Provider key management
│   │   ├── consistency/          # Aggregate locks, dedup
│   │   ├── reliability/          # Recovery budget
│   │   └── runtime/              # Circuit-breaker, retry, timeout
│   │
│   ├── db/
│   │   ├── schema.ts             # All 20 tables including auth_sessions
│   │   ├── seed.ts               # Real Moroccan curriculum
│   │   ├── seed-curriculum.ts    # Bulk curriculum import
│   │   └── curriculum/           # Structured lesson data
│   │
│   └── components/               # Shared UI
│
├── infra/                        # Grafana/Prometheus configs
├── load-tests/                   # k6 performance tests
├── scripts/                      # Governance, chaos, recovery
└── docker-compose.runtime.yml    # Full observability stack
```

---

## Authority Flow

```
Request
  ↓
Middleware (nonce + CSP + auth redirect)
  ↓
withAuth() wrapper
  ↓
requireAuth() ← single enforcement point
  ↓
getSession() ← reads JWT from httpOnly cookie
  ↓
assertOwnsChild() ← for all childId endpoints
  ↓
Handler (server-side only)
```

**Zero trust on client input**: userId and childId are always derived from the server-validated session, never trusted from the request body.

---

## AI Flow

```
Child types message
  ↓
TutorChat (client — useTutorStream hook)
  ↓
POST /api/ai/leila
  ↓
getSession() → ownership check → quota check → rate limit
  ↓
buildLeilaSystemPrompt(context) ← adaptive Darija persona
  ↓
getPersona(gradeLevel) ← primary/middle/high persona
  ↓
LEILA_DARIJA_FEW_SHOTS ← conversational steering
  ↓
Groq SDK (llama-3.3-70b, frequency_penalty: 0.3)
  ↓
SSE stream → client (stream-resilience.ts handles failures)
  ↓
chatRepo.saveMessage() ← persistent memory
  ↓
progressRepo.logAiUsage() ← quota tracking
```

**Leila personality is immutable**: The `personas/` folder is the product's most valuable asset. Infrastructure never touches it.

---

## Queue Systems

```
BullMQ (when Redis available)
  ├── ai-usage-events    ← async logging
  ├── progress-updates   ← non-blocking progress tracking
  └── curriculum-import  ← bulk content import

Memory Queue (when Redis unavailable / dev)
  └── Same interface, in-process
```

---

## Observability Stack

```
App → Prometheus metrics (/api/metrics)
App → OpenTelemetry traces → Jaeger (optional)
App → Sentry error tracking (optional)

Prometheus → Grafana dashboards
Redis → redis-exporter → Prometheus

docker-compose.runtime.yml starts:
  - Redis
  - redis-exporter
  - Prometheus
  - Grafana
```

---

## Recovery Semantics

1. **Redis unavailable**: All cache operations fall back to in-memory. No user impact.
2. **Groq timeout**: Circuit breaker opens after 5 failures. Leila shows friendly error message in Darija.
3. **DB unavailable**: Health endpoint returns 503. Load balancer stops routing.
4. **Queue overflow**: Dead-letter queue captures failed jobs for replay.
5. **Auth token expired**: Refresh token rotates automatically (30-day TTL).
6. **Token theft detected**: Entire family revoked instantly. User forced to re-login.

---

## Deployment Topology

```
Production:
  Vercel (Next.js) + Neon (PostgreSQL) + Upstash (Redis)

Development:
  npm run dev + docker-compose.runtime.yml (optional Redis/Grafana)

Monitoring:
  npm run infra:up → Grafana at :3001, Prometheus at :9090
```

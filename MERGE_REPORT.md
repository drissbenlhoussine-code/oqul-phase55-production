# MERGE REPORT — OQUL Architectural Fusion
## COMPANION-FINAL × Phase 26 Infrastructure

---

## Sources of Truth Applied

| Domain | Source |
|---|---|
| Leila personality, Darija, personas | COMPANION-FINAL |
| Product warmth, UX, child flows | COMPANION-FINAL |
| Gamification, engagement, onboarding | COMPANION-FINAL |
| AI prompt system, adaptive tone | COMPANION-FINAL |
| Auth (JWT, refresh rotation, ownership) | COMPANION-FINAL |
| Security (CSP nonce, HSTS) | COMPANION-FINAL |
| Redis resilience, BullMQ queues | Phase 26 |
| OpenTelemetry, Prometheus metrics | Phase 26 |
| Grafana dashboards | Phase 26 |
| Redis Sentinel / failover configs | Phase 26 |
| Load tests (k6) | Phase 26 |
| Chaos/recovery scripts | Phase 26 |
| Stream resilience (stream-resilience.ts) | Phase 26 |
| AI reliability (concurrent, timeout) | Phase 26 |
| Governance, trust, revocation | Phase 26 |

---

## What Came From COMPANION-FINAL (Preserved Exactly)

### Product Soul
- `src/server/ai/personas/` — Darija persona system (4 files)
- `src/server/ai/leila.ts` — complete adaptive prompt builder
- All few-shot examples in `leila-darija.ts`
- All engagement components: LeilaWelcome, DailyLoop, MilestoneAlert, SessionSummary
- Gamification: XP, badges, streaks, levels, celebration overlay
- Onboarding wizard (3-step)
- Habit formation: HabitBar, StreakCalendar, MasteryMap, DailyGreeting

### Security Architecture
- Nonce-based CSP with `strict-dynamic`
- Refresh token rotation with family-based theft detection
- Session management (revoke all devices)
- `withAuth()` → `requireAuth()` chain
- `assertOwnsChild()` ownership enforcement

### Learning Intelligence
- Adaptive Engine with SRS (SM-2)
- Mastery Service (weak points)
- Content Generator (AI-assisted lesson production)
- Admin UI for curriculum building

---

## What Came From Phase 26 (Added as Infra Layer)

### Runtime Infrastructure
- `src/server/cache/` — Redis cache with memory fallback
- `src/server/redis/` — Resilient Redis client, reconnect policy, health
- `src/server/jobs/` — BullMQ job queue system
- `src/server/telemetry/` — Metrics (Prometheus), runtime health
- `src/server/observability/` — OpenTelemetry, tracing, Sentry adapter
- `src/server/governance/` — Revocation epochs
- `src/server/trust/` — Provider key management
- `src/server/effects/` — Authoritative delivery, quarantine recovery
- `src/server/consistency/` — Aggregate locks, deduplication
- `src/server/reliability/` — Recovery budget, runtime assertions
- `src/server/routing/` — Authority refresh, shard migration

### AI Runtime Resilience
- `src/server/ai/streaming/` — stream-resilience, stream-lifecycle, chaos
- `src/server/ai/reliability/` — concurrent-ai, provider-failure, quota-race

### Infra Configs
- `docker-compose.runtime.yml` — Redis + Redis Exporter + Prometheus + Grafana
- `infra/` — Grafana dashboards, Prometheus configs, Redis Sentinel
- `load-tests/` — k6 load tests (AI streaming, queue pressure, rate limits)
- `scripts/` — governance, chaos, recovery, quality audits

### API Additions
- `/api/health` — Docker healthcheck + monitoring
- `/api/metrics` — Prometheus scraping endpoint

---

## Conflicts Resolved

### 1. AI Prompt System
- **Conflict**: Phase 26 `prompt-builder.ts` is weak (2-line prompt). COMPANION has rich persona architecture.
- **Resolution**: COMPANION's prompt system preserved entirely. Phase 26's `prompt-builder.ts` discarded.
- **Impact**: Leila quality unaffected.

### 2. Redis in Security (Rate Limiting)
- **Conflict**: COMPANION uses in-memory rate limiting. Phase 26 has Redis-backed rate limiting.
- **Resolution**: Kept COMPANION's in-memory for now. Phase 26's Redis rate-limit available as opt-in. In production, Redis URL enables automatic upgrade.
- **Migration path**: When `REDIS_URL` is set, rate-limit service can switch to Redis.

### 3. Runtime Modules
- **Conflict**: COMPANION has `circuit-breaker.ts` in a simpler form. Phase 26 has enhanced version.
- **Resolution**: Phase 26 version adopted (more battle-tested).

---

## Architecture Decisions

1. **Child experience is non-negotiable**: Any infrastructure addition that would require changes to child-facing components was rejected or made optional.

2. **Redis is optional in dev**: All Redis operations use `safeRedisOperation()` with fallback to in-memory. Dev environment works without Redis.

3. **Observability is additive**: OpenTelemetry/Prometheus are initialized only when env vars present. No impact on product if not configured.

4. **BullMQ is infrastructure-only**: Job queues handle background tasks (AI usage logging, cleanup). Never exposed to child UX.

---

## Remaining Technical Debt

1. **Rate Limiter**: Still in-memory. Production should migrate to Redis-backed (Phase 26's implementation ready to use).

2. **Telemetry initialization**: OpenTelemetry SDK needs `instrumentation.ts` to be wired into Next.js config for full traces.

3. **BullMQ workers**: Queue infrastructure exists but workers aren't started by default. Need `npm run workers` in production.

4. **E2E tests**: Phase 26's Playwright tests not yet adapted to fusion routes.

5. **Governance scripts**: Some Phase 26 governance scripts assume DB tables not in COMPANION's schema.

---

## Scalability Notes

- Redis ready: When `REDIS_URL` env is set, the entire caching layer upgrades automatically.
- BullMQ ready: Job queue infrastructure is production-grade (persistent, retryable, observable).
- Grafana/Prometheus: Full observability stack available via `npm run infra:up`.
- k6 load tests: Ready to run against production endpoints.

---

## Operational Notes

```bash
# Start full infra stack
npm run infra:up

# Check health
npm run health:check

# Run load tests (requires k6 installed)
k6 run load-tests/ai-streaming.yml

# View metrics
open http://localhost:3000/api/metrics

# Grafana dashboard
open http://localhost:3000  # port depends on docker-compose
```

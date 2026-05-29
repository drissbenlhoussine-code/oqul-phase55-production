# PRODUCT IDENTITY GUARDRAILS
## How to Preserve Leila's Soul Through Infrastructure Growth

---

## The Core Rule

> **The infrastructure must serve the child. The child must never serve the infrastructure.**

Any change that makes the child's experience colder, heavier, more formal, or more "enterprise-like" is **a regression**, regardless of how technically correct it is.

---

## Leila's Personality — Protected Files

These files are **sacred**. Never modify without explicit product review:

```
src/server/ai/personas/leila-darija.ts    ← Darija few-shots and vocabulary
src/server/ai/personas/leila-primary.ts   ← Primary school persona (6-12y)
src/server/ai/personas/leila-middle.ts    ← Middle school persona (12-15y)
src/server/ai/personas/leila-high.ts      ← High school persona (15-18y)
src/server/ai/leila.ts                    ← Adaptive prompt builder
```

### Why These Are Untouchable

These files encode years of product insight about how a Moroccan child expects to be spoken to. They are not just prompts — they are the emotional contract between OQUL and the child.

---

## Leila's Non-Negotiable Traits

| Trait | How It's Enforced |
|---|---|
| Speaks Darija | `LEILA_DARIJA_FEW_SHOTS` in `leila-darija.ts` |
| Age-appropriate tone | `getPersona(gradeLevel)` picks correct persona |
| Short responses | `max_tokens: 600` in `leila.ts` |
| Varied responses | `frequency_penalty: 0.3` in Groq call |
| Never starts formally | Rule #1 in `LEILA_CORE_RULES` |
| Ends with a question | Rule #3 in `LEILA_CORE_RULES` |
| Gentle on failure | "ماشي مشكل" — never "خطأ" |
| Remembers sessions | `chatRepo.getRecentMessages()` for context |
| Knows the child | `gradeLevel`, `weakPoints`, `avgScore`, `streak` in context |

---

## What Future Developers Must NEVER Do

### ❌ Don't add infrastructure logging to AI prompts
```typescript
// WRONG
const prompt = buildLeilaSystemPrompt(ctx) + "\n[REQUEST_ID: " + reqId + "]";
```

### ❌ Don't make error messages formal
```typescript
// WRONG
throw new Error("Quota exceeded. Please upgrade your plan.");

// RIGHT — in Darija, warmly
"وصلتي للحد اليومي 😊 — ارجعي غداً أو اطلبي من وليّك الترقية"
```

### ❌ Don't expose BullMQ/Redis errors to children
Queue failures must silently degrade, never surface to the UX.

### ❌ Don't increase max_tokens for "better" responses
Leila should be conversational, not lecture-like. Shorter = warmer.

### ❌ Don't add formal Arabic to the persona
"يجب" "ينبغي" "وبالتالي" "لذلك" — these are banned in `LEILA_CORE_RULES`.

### ❌ Don't make AI calls synchronous in UI
All AI interactions must stream. Children abandon non-streaming AI instantly.

---

## What Future Developers MUST Do

### ✅ Test Darija before deploying any persona change
```bash
npm test -- leila-darija
```

### ✅ Keep child-facing errors in Darija
All error messages in `src/features/` must be in Moroccan Arabic.

### ✅ Update all three personas when changing tone
If you adjust `leila-darija.ts`, also review `leila-primary.ts`, `leila-middle.ts`, `leila-high.ts`.

### ✅ Infrastructure changes must pass the "child warmth" test
Before merging any infrastructure PR, ask: "Does this make the child's experience warmer or colder?"

### ✅ Add to `LEILA_CORE_RULES` when adding behavior constraints
Never add constraints as ad-hoc instructions in API routes.

---

## How Infrastructure Is Prevented From Degrading UX

### Isolation Pattern
Infrastructure modules live exclusively in `src/server/`. They are **server-only** and have no import path from `src/features/` (child-facing components).

```
src/features/ai-tutor/tutor-chat.tsx
  → imports useTutorStream (client hook)
  → never imports from src/server/

src/server/ai/leila.ts
  → imports from personas/
  → never imports from cache/, redis/, jobs/
```

### Graceful Degradation Contract
Every infrastructure service must implement graceful degradation:
- Redis unavailable → in-memory fallback
- BullMQ down → synchronous fallback
- Groq timeout → circuit-breaker opens → friendly Darija error message
- Metrics endpoint down → app continues normally

**The child must never see a technical error.** They see Leila saying "واخا، كاين مشكل صغير — جرب مرة أخرى 😊"

---

## The Emotional Architecture

OQUL's competitive advantage is not technical — it's emotional:

```
Child opens app
  → Leila greets them by name in warm Darija
  → They feel remembered and welcomed
  → They do one lesson (DailyLoop makes it feel achievable)
  → They succeed → XP + Leila celebrates with them
  → They fail → Leila is gentle, not judgmental
  → They want to come back tomorrow (streak system creates habit)
```

**Preserving this loop is the most important engineering constraint.**

---

## Red Lines — Absolute Prohibitions

1. **Never make Leila's responses longer than 600 tokens** (coldness increases with length)
2. **Never use formal Arabic as the default register** (فصحى is for technical terms only)
3. **Never remove the question at the end of Leila's responses** (it's what creates dialogue)
4. **Never expose infrastructure state to the child** (queue size, Redis health, etc.)
5. **Never change the grade-based persona selection without pedagogical review**

---

## Versioning Leila's Personality

When making persona changes:
1. Create `leila-darija-v2.ts` as a draft
2. A/B test with a subset of users (future: analytics)
3. Measure engagement metrics (quiz completion rate, session length)
4. Only promote to `leila-darija.ts` when metrics improve

**Leila's personality is a product, not a config file.**

# Grade 2 Deployment Dashboard

**Sprint 0 — Production Validation**
Last updated: 2026-06-01
Branch: `claude/oqul-ux-stabilization-y9wBI`

---

## Status Overview

| Category                      | Count / Status |
|-------------------------------|---------------|
| Scripts ready                 | 30            |
| Scripts applied               | 0             |
| Scripts verified in UI        | 0             |
| Lessons completed end-to-end  | 0             |
| Parent verification passed    | No            |
| Leila verification passed     | No            |

**Gate:** Do not start Grade 3, Grade 2 French, or Grade 2 Science until all rows above are complete.

---

## Sprint 0 — Three-Day Rollout Plan

### Day 1 — Math (5 scripts)

Apply only after batch dry run shows 0 errors.

| # | Script                              | Dry Run | Applied | UI Verified |
|---|-------------------------------------|---------|---------|-------------|
| 1 | upgrade-g2-math-starter-lesson      | [ ]     | [ ]     | [ ]         |
| 2 | upgrade-g2-math-data-org-1-fahm     | [ ]     | [ ]     | [ ]         |
| 3 | upgrade-g2-math-data-org-2-atamaran | [ ]     | [ ]     | [ ]         |
| 4 | upgrade-g2-math-data-org-3-atatbaq  | [ ]     | [ ]     | [ ]         |
| 5 | upgrade-g2-math-data-org-4-arajai   | [ ]     | [ ]     | [ ]         |

Day 1 verification checklist:
- [ ] Lessons appear in child's curriculum view
- [ ] Exercises load and display correctly
- [ ] Progress saves after completing exercises
- [ ] Leila responds on at least 1 Math lesson
- [ ] No console errors in browser devtools

Day 1 gate: all boxes above checked before proceeding to Day 2.

---

### Day 2 — Arabic Unit 1: القراءة (5 scripts)

Apply only after Day 1 gate is passed. Test with real or demo student account. Verify mobile rendering.

| #  | Script                              | Dry Run | Applied | UI Verified |
|----|-------------------------------------|---------|---------|-------------|
| 6  | upgrade-g2-arabic-starter           | [ ]     | [ ]     | [ ]         |
| 7  | upgrade-g2-arabic-qiraa-1-fahm      | [ ]     | [ ]     | [ ]         |
| 8  | upgrade-g2-arabic-qiraa-2-atamaran  | [ ]     | [ ]     | [ ]         |
| 9  | upgrade-g2-arabic-qiraa-3-atatbaq   | [ ]     | [ ]     | [ ]         |
| 10 | upgrade-g2-arabic-qiraa-4-arajai    | [ ]     | [ ]     | [ ]         |

Day 2 verification checklist:
- [ ] Arabic RTL text renders correctly on desktop
- [ ] Arabic RTL text renders correctly on mobile (375px viewport)
- [ ] Diacritics (تشكيل) display correctly
- [ ] Fill_blank exercises score correctly (diacritics match)
- [ ] At least 1 lesson completed end-to-end by real/demo student
- [ ] Leila verified on 1 القراءة lesson

Day 2 gate: all boxes above checked before proceeding to Day 3.

---

### Day 3 — Arabic Units 2–6 (20 scripts) + Parent Verification

Apply units sequentially. Run Parent Verification after all Arabic lessons are live.

**التراكيب**

| #  | Script                                | Dry Run | Applied | UI Verified |
|----|---------------------------------------|---------|---------|-------------|
| 11 | upgrade-g2-arabic-tarakib-1-fahm      | [ ]     | [ ]     | [ ]         |
| 12 | upgrade-g2-arabic-tarakib-2-atamaran  | [ ]     | [ ]     | [ ]         |
| 13 | upgrade-g2-arabic-tarakib-3-atatbaq   | [ ]     | [ ]     | [ ]         |
| 14 | upgrade-g2-arabic-tarakib-4-arajai    | [ ]     | [ ]     | [ ]         |

**الصرف والتحويل**

| #  | Script                              | Dry Run | Applied | UI Verified |
|----|-------------------------------------|---------|---------|-------------|
| 15 | upgrade-g2-arabic-sarf-1-fahm       | [ ]     | [ ]     | [ ]         |
| 16 | upgrade-g2-arabic-sarf-2-atamaran   | [ ]     | [ ]     | [ ]         |
| 17 | upgrade-g2-arabic-sarf-3-atatbaq    | [ ]     | [ ]     | [ ]         |
| 18 | upgrade-g2-arabic-sarf-4-arajai     | [ ]     | [ ]     | [ ]         |

**الإملاء**

| #  | Script                              | Dry Run | Applied | UI Verified |
|----|-------------------------------------|---------|---------|-------------|
| 19 | upgrade-g2-arabic-imla-1-fahm       | [ ]     | [ ]     | [ ]         |
| 20 | upgrade-g2-arabic-imla-2-atamaran   | [ ]     | [ ]     | [ ]         |
| 21 | upgrade-g2-arabic-imla-3-atatbaq    | [ ]     | [ ]     | [ ]         |
| 22 | upgrade-g2-arabic-imla-4-arajai     | [ ]     | [ ]     | [ ]         |

**التعبير الكتابي**

| #  | Script                                | Dry Run | Applied | UI Verified |
|----|---------------------------------------|---------|---------|-------------|
| 23 | upgrade-g2-arabic-taabir-1-fahm       | [ ]     | [ ]     | [ ]         |
| 24 | upgrade-g2-arabic-taabir-2-atamaran   | [ ]     | [ ]     | [ ]         |
| 25 | upgrade-g2-arabic-taabir-3-atatbaq    | [ ]     | [ ]     | [ ]         |
| 26 | upgrade-g2-arabic-taabir-4-arajai     | [ ]     | [ ]     | [ ]         |

**الاستماع والتحدث**

| #  | Script                                | Dry Run | Applied | UI Verified |
|----|---------------------------------------|---------|---------|-------------|
| 27 | upgrade-g2-arabic-istima-1-fahm       | [ ]     | [ ]     | [ ]         |
| 28 | upgrade-g2-arabic-istima-2-atamaran   | [ ]     | [ ]     | [ ]         |
| 29 | upgrade-g2-arabic-istima-3-atatbaq    | [ ]     | [ ]     | [ ]         |
| 30 | upgrade-g2-arabic-istima-4-arajai     | [ ]     | [ ]     | [ ]         |

Day 3 verification checklist:
- [ ] All 6 Arabic unit cards visible in curriculum
- [ ] Leila verified on التعبير الكتابي lesson (vocabulary bank surfaced)
- [ ] Leila verified on الاستماع والتحدث lesson (no long writing prompt)

**Parent Verification (after all 30 applied)**
- [ ] Parent account logs in successfully
- [ ] Parent can see child's enrolled Grade 2 Arabic and Math
- [ ] Parent can see child's progress on newly-deployed lessons
- [ ] Parent progress view shows correct unit names in Arabic
- [ ] No 5xx errors in server logs during parent session

---

## Rollback Reference

| Scenario | Action |
|----------|--------|
| Script exits with ❌ Lesson not found | Stop. Query DB for actual title. Fix find condition. Re-run dry run. |
| Script crashes mid-run | Transaction rolled back automatically. Fix script. Re-run --apply. |
| Wrong content deployed | Re-apply corrected script (idempotent — safe to overwrite). |
| Fill_blank never scores | Check diacritics match between correctAnswer and expected input. |
| UI renders broken for whole unit | Not a content bug — investigate lesson renderer component. |

---

## Final Sign-off

Update the Status Overview table at the top of this file as each phase completes.
Sprint 0 is complete when:

- Scripts applied: **30**
- Scripts verified in UI: **30**
- Lessons completed end-to-end: **≥ 3**
- Parent verification passed: **Yes**
- Leila verification passed: **Yes**

Only after Sprint 0 sign-off: proceed to Grade 3 Arabic, Grade 2 French, or Grade 2 Science.

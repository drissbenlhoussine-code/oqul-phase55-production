# Pilot Batch Plan

The first Phase 58 pilot must be small, reviewable, and Mathematics-only.

Do not generate the full 2BAC curriculum immediately.

## First Pilot Subject

Subject: 2BAC Mathematics

## First Pilot Lessons

1. Derivative definition
2. Derivative rules
3. Variations and extrema
4. Exponential function
5. Logarithmic function

## Workflow

1. Audit existing 2BAC math lessons in the database.
2. Match lesson IDs to the roadmap.
3. Generate one lesson only.
4. Run quality gates.
5. Manually inspect the lesson.
6. Verify LessonViewer display.
7. Continue to the five-lesson pilot only after the first lesson passes.

## Expansion Rule

- 1 lesson passes deeply.
- Then 5 lessons.
- Then 20 lessons.
- Then full module.
- Then next subject.

## Stop Conditions

Stop generation if:

- Lesson quality score is below 80.
- Placeholder text appears.
- BAC section is missing.
- French terminology is missing.
- Examples are generic or non-Moroccan.
- Exercises lack answers or corrections.
- LessonViewer cannot display the content cleanly.

## First Lesson Acceptance Checklist

Before moving from one lesson to five lessons, confirm:

- The lesson follows the four-layer specification.
- The lesson passes automatic quality gates.
- The lesson passes educational review.
- The lesson includes BAC methodology and point allocation logic.
- The lesson includes French terminology equivalents.
- Leila prompts are specific and useful.
- Lesson Helper prompts are specific and useful.
- Research prompts are relevant to Moroccan BAC context.
- Exercises are progressive and corrected.
- The LessonViewer can render the lesson cleanly on desktop and mobile.

## Human Review Requirement

The first generated lesson must be reviewed manually before any batch generation.

If the first lesson fails, do not continue to the remaining four pilot lessons.

## Out of Scope for This Pilot

- No Physics-Chemistry generation.
- No Philosophy generation.
- No full 2BAC generation.
- No database writes until one lesson passes review.
- No deployment scripts until accepted content exists.

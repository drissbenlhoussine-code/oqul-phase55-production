# Quality Gates

No 2BAC lesson enters OQUL unless it passes all three gate types:

1. Automatic checks
2. Educational checks
3. OQUL compatibility checks

These gates apply before database insertion, deployment scripts, or production release.

## 1. Automatic Checks

### Required

- No placeholder text
- Minimum content length
- Minimum examples count
- Minimum solved exercises count
- Minimum progressive exercises count
- Summary exists
- Common mistakes exist
- BAC exercise exists
- Leila instructions exist
- French terminology exists

### Suggested Minimums for 2BAC

- Content length: 3500-6000 characters
- Guided examples: at least 3
- Solved exercises: at least 3
- Practice exercises: at least 8
- Challenge exercises: at least 2
- Common mistakes: at least 3
- BAC-style exercise: at least 1

## 2. Educational Checks

### Required

- Moroccan curriculum alignment
- BAC relevance
- Correct terminology
- No hallucinated concepts
- No level mismatch
- No invented exam rules
- Mathematical/scientific accuracy
- Philosophy concepts tied to recognized problematics

### Rejection Examples

- A Mathematics lesson uses concepts from a different level without explanation.
- A Physics-Chemistry lesson invents formulas or units.
- A Philosophy lesson lists names or ideas without a recognized problematic.
- A BAC methodology section gives generic advice without examiner expectations.
- Examples could belong to any country and do not reflect Moroccan BAC practice.

## 3. OQUL Compatibility Checks

### Required

- Compatible with Leila
- Compatible with Lesson Helper
- Compatible with Exam Prep
- Compatible with Learning Path
- Weak-point detection possible
- Exercises have answers and explanations
- Content can be chunked in LessonViewer

### Compatibility Meaning

- Leila can use the lesson to tutor step by step.
- Lesson Helper can answer targeted questions from the lesson.
- Exam Prep can extract BAC-style practice and methodology.
- Learning Path can connect the lesson to prerequisites and next steps.
- LessonViewer can display the content in readable sections.

## Scoring

| Score | Status | Decision |
| ---: | --- | --- |
| 90-100 | Production ready | Accept after final human review. |
| 80-89 | Acceptable after light review | Revise minor issues before insertion. |
| 70-79 | Needs revision | Do not insert. Regenerate or edit. |
| Below 70 | Reject | Do not use. Restart from prompt or source plan. |

## Mandatory Stop Rules

Stop content insertion if:

- Placeholder text appears.
- BAC section is missing.
- French terminology is missing.
- Exercises lack answers or corrections.
- Lesson cannot be displayed cleanly in LessonViewer.
- Content includes hallucinated concepts or non-curriculum material.
- The lesson is not usable by Leila or Lesson Helper.

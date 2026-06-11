# 2BAC Content Specification

This document defines the official production standard for every 2BAC lesson generated for OQUL.

Every lesson must contain four layers:

1. Core Learning Layer
2. Practice Layer
3. BAC Layer
4. AI Layer

The goal is to produce content that is understandable, practice-ready, BAC-relevant, and compatible with OQUL's AI systems.

## 1. Core Learning Layer

### Required Fields

- Lesson title
- Learning objectives
- Prerequisites
- Key concepts
- Key definitions
- Full explanation
- Moroccan classroom/context examples
- French terminology equivalents
- Short summary

### Purpose

Make the lesson understandable before practice begins.

The learner should know what the lesson is about, why it matters, which prior knowledge is needed, and how the main concepts are used in Moroccan BAC contexts.

## 2. Practice Layer

### Required Fields

- Guided examples
- Step-by-step solved exercises
- Progressive exercises
- Challenge exercises
- Hints
- Answers
- Detailed corrections

### Purpose

Move the learner from comprehension to independent solving.

The learner should first see the method, then apply it with support, then solve progressively harder exercises.

## 3. BAC Layer

### Required Fields

- BAC-style exercise
- Methodology
- Common mistakes
- Point allocation logic
- Examiner expectations
- Time-management advice
- How to recognize this question in the exam

### Purpose

Make every lesson exam-aware, not only explanatory.

Each lesson must help the learner understand how the concept appears in BAC exams and how examiners expect answers to be structured.

## 4. AI Layer

### Required Fields

- Suggested Leila tutor prompts
- Lesson Helper prompts
- Research prompts
- Learning Path links
- Remediation guidance
- Weak-point detection hints

### Purpose

Make content usable by OQUL's AI systems, not only by the visual lesson viewer.

Leila, Lesson Helper, Research, Learning Paths, and Exam Prep should all be able to use the lesson content consistently.

## Recommended Lesson Shape

This is a JSON-like structure for planning and QA only. It is not an implementation requirement.

```json
{
  "title": "Lesson title",
  "subject": "mathematics | physics-chemistry | philosophy",
  "level": "2BAC",
  "module": "Module name",
  "coreLearning": {
    "objectives": ["objective 1", "objective 2"],
    "prerequisites": ["prerequisite 1", "prerequisite 2"],
    "keyConcepts": ["concept 1", "concept 2"],
    "keyDefinitions": [
      { "term": "term", "definition": "definition" }
    ],
    "frenchTerminology": [
      { "arabic": "مصطلح", "french": "terme français" }
    ],
    "explanation": "Full explanation",
    "moroccanExamples": ["example 1", "example 2"],
    "summary": "Short summary"
  },
  "practice": {
    "guidedExamples": [
      {
        "problem": "problem statement",
        "steps": ["step 1", "step 2"],
        "answer": "answer"
      }
    ],
    "solvedExercises": [],
    "progressiveExercises": [],
    "challengeExercises": [],
    "hints": [],
    "answers": [],
    "detailedCorrections": []
  },
  "bac": {
    "bacStyleExercise": "exercise",
    "methodology": "method",
    "commonMistakes": [],
    "pointAllocation": [],
    "examinerExpectations": [],
    "timeManagementAdvice": "advice",
    "recognitionPattern": "How to recognize this question in the exam"
  },
  "ai": {
    "leilaPrompts": [],
    "lessonHelperPrompts": [],
    "researchPrompts": [],
    "learningPathLinks": [],
    "remediationGuidance": [],
    "weakPointDetectionHints": []
  }
}
```

## Production Notes

- Do not accept lessons that only explain concepts without practice.
- Do not accept lessons that contain practice without BAC methodology.
- Do not accept lessons that are not usable by Leila and Lesson Helper.
- Do not accept lessons with generic examples that could belong to any country or curriculum.

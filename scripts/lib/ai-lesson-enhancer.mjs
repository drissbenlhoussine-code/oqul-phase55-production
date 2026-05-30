import Groq from "groq-sdk";

export function requireGroqApiKey() {
  if (!process.env.GROQ_API_KEY) {
    throw new Error("GROQ_API_KEY is required for AI lesson enhancement. Dry-run audits do not need it.");
  }
  return process.env.GROQ_API_KEY;
}

function buildPrompt(lesson) {
  return `
You are Leila, OQUL's Moroccan curriculum tutor and lesson designer.

Create rich, original, curriculum-aligned lesson content for the Moroccan school system.
Return valid JSON only. Do not use Markdown fences.

Lesson metadata:
- Grade: ${lesson.grade_title ?? lesson.grade_slug ?? "unknown"}
- Subject: ${lesson.subject_title ?? lesson.subject_slug ?? "unknown"}
- Unit: ${lesson.unit_title ?? lesson.unit_slug ?? "unknown"}
- Lesson title: ${lesson.lesson_title}
- Existing objectives: ${JSON.stringify(lesson.objectives ?? [])}

Required quality:
- Arabic suitable for Morocco, with formal classroom tone.
- Clear concept explanation.
- Definitions.
- One worked step-by-step example.
- Guided practice.
- Three graded exercises with answers and explanations.
- Common mistakes.
- Hints.
- Correction/remediation method.
- Exam-style preparation.
- Short summary.
- Leila tutoring instructions.

Return exactly this JSON shape:
{
  "title": "Arabic lesson title",
  "objectives": ["objective 1", "objective 2", "objective 3"],
  "explanation": "Rich explanation with definitions, worked example, common mistakes, hints, remediation, exam preparation, and Leila instructions.",
  "vocabulary": [{"word": "...", "definition": "..."}],
  "examples": [{"text": "...", "note": "..."}],
  "summary": "Short summary",
  "exercises": [
    {"type": "short_answer", "question": "...", "correctAnswer": "...", "explanation": "...", "points": 10},
    {"type": "short_answer", "question": "...", "correctAnswer": "...", "explanation": "...", "points": 20},
    {"type": "short_answer", "question": "...", "correctAnswer": "...", "explanation": "...", "points": 30}
  ]
}
`;
}

function parseGeneratedJson(text) {
  const cleaned = String(text)
    .replace(/^```(?:json)?/i, "")
    .replace(/```$/i, "")
    .trim();
  return JSON.parse(cleaned);
}

export async function generateEnhancedLesson(lesson) {
  const groq = new Groq({ apiKey: requireGroqApiKey() });
  const completion = await groq.chat.completions.create({
    model: process.env.GROQ_MODEL ?? "llama-3.3-70b-versatile",
    messages: [{ role: "user", content: buildPrompt(lesson) }],
    temperature: 0.35,
    max_tokens: 2800,
    stream: false,
  });
  const text = completion.choices[0]?.message?.content ?? "{}";
  const parsed = parseGeneratedJson(text);

  return {
    title: parsed.title || lesson.lesson_title,
    objectives: Array.isArray(parsed.objectives) ? parsed.objectives : lesson.objectives ?? [],
    explanation: String(parsed.explanation ?? ""),
    vocabulary: Array.isArray(parsed.vocabulary) ? parsed.vocabulary : [],
    examples: Array.isArray(parsed.examples) ? parsed.examples : [],
    summary: String(parsed.summary ?? ""),
    exercises: Array.isArray(parsed.exercises)
      ? parsed.exercises.slice(0, 6).map((exercise, index) => ({
          type: ["mcq", "true_false", "fill_blank", "short_answer"].includes(exercise.type) ? exercise.type : "short_answer",
          question: String(exercise.question ?? ""),
          options: Array.isArray(exercise.options) ? exercise.options : undefined,
          correctAnswer: String(exercise.correctAnswer ?? exercise.answer ?? ""),
          explanation: String(exercise.explanation ?? ""),
          points: Number(exercise.points ?? (index + 1) * 10),
          orderIndex: index + 1,
        }))
      : [],
  };
}

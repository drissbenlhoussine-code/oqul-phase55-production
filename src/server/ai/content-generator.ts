/**
 * Content Generation Pipeline
 * Uses Groq/Llama to generate curriculum-aligned lesson content at scale.
 *
 * This is the solution to "Real Lesson Coverage 4.5/10":
 * Instead of writing all lessons manually, generate them from templates
 * aligned with the official Moroccan curriculum.
 */
import Groq from "groq-sdk";

function getGroqClient() {
  const apiKey = process.env.GROQ_API_KEY;
  if (!apiKey) {
    throw new Error("GROQ_API_KEY is required for lesson generation.");
  }
  return new Groq({ apiKey });
}

export interface LessonGenerationInput {
  subject:     string;   // "arabic" | "math" | "french" | "science"
  grade:       number;   // 1-12
  topic:       string;   // "الكسور العادية"
  objectives:  string[]; // ["فهم مفهوم الكسر", "قراءة الكسور"]
  difficulty:  "easy" | "medium" | "hard";
}

export interface GeneratedLesson {
  explanation: string;
  vocabulary:  { word: string; definition: string }[];
  examples:    { text: string; note: string }[];
  summary:     string;
  exercises:   {
    type:          "mcq" | "true_false" | "fill_blank";
    question:      string;
    options?:      string[];
    correctAnswer: string;
    explanation:   string;
    points:        number;
  }[];
}

const GENERATION_PROMPT = (input: LessonGenerationInput) => `
أنت خبير تربوي متخصص في المنهج المغربي للتعليم الابتدائي والإعدادي.

المهمة: أنشئ محتوى درس كامل للمعلومات التالية:
- المادة: ${input.subject}
- المستوى الدراسي: ${input.grade}
- الموضوع: ${input.topic}
- الأهداف: ${input.objectives.join("، ")}
- الصعوبة: ${input.difficulty}

أجب بـ JSON فقط بدون أي تنسيق Markdown أو code fences بهذا الهيكل:
{
  "explanation": "شرح مفصل (200-400 كلمة)، واضح، متدرج، مع أمثلة من الحياة المغربية",
  "vocabulary": [
    {"word": "...", "definition": "..."},
    (3-5 مفردات)
  ],
  "examples": [
    {"text": "...", "note": "..."},
    (2-4 أمثلة)
  ],
  "summary": "ملخص قصير جداً (جملة أو جملتان)",
  "exercises": [
    {
      "type": "mcq",
      "question": "...",
      "options": ["أ", "ب", "ج", "د"],
      "correctAnswer": "...",
      "explanation": "...",
      "points": 10
    },
    {
      "type": "true_false",
      "question": "...",
      "options": ["صحيح", "خطأ"],
      "correctAnswer": "صحيح",
      "explanation": "...",
      "points": 10
    },
    {
      "type": "fill_blank",
      "question": "أكمل: ...",
      "correctAnswer": "...",
      "explanation": "...",
      "points": 15
    }
  ]
}

مهم جداً:
- الشرح يجب أن يكون مناسبًا لعمر ${input.grade <= 6 ? "6-12 سنة (ابتدائي)" : input.grade <= 9 ? "12-15 سنة (إعدادي)" : "15-18 سنة (ثانوي)"}
- الأمثلة من الحياة المغربية (خبز، سوق، مدرسة، كرة قدم، أسرة)
- التمارين متنوعة ومتدرجة من السهل للصعب
`;

export async function generateLesson(input: LessonGenerationInput): Promise<GeneratedLesson> {
  const groq = getGroqClient();
  const completion = await groq.chat.completions.create({
    model:       "llama-3.3-70b-versatile",
    messages:    [{ role: "user", content: GENERATION_PROMPT(input) }],
    max_tokens:  2000,
    temperature: 0.4, // lower = more consistent educational content
    stream:      false,
  });

  const text = completion.choices[0]?.message?.content ?? "{}";

  try {
    const clean = text.replace(/JSON fenced code block\n?|code fence\n?/g, "").trim();
    return JSON.parse(clean) as GeneratedLesson;
  } catch {
    throw new Error(`Failed to parse generated lesson: ${text.slice(0, 200)}`);
  }
}

/**
 * Batch generate multiple lessons for a subject
 * Used by the admin curriculum builder
 */
export async function generateCurriculumBatch(
  subject: string,
  grade: number,
  topics: string[]
): Promise<Array<{ topic: string; lesson: GeneratedLesson | null; error?: string }>> {
  const results = [];
  for (const topic of topics) {
    try {
      const lesson = await generateLesson({
        subject, grade, topic,
        objectives: [`فهم ${topic}`, `تطبيق ${topic}`, `حل مسائل في ${topic}`],
        difficulty:  grade <= 3 ? "easy" : grade <= 6 ? "easy" : grade <= 9 ? "medium" : "hard",
      });
      results.push({ topic, lesson });
      // Rate limit: wait 1s between calls
      await new Promise((r) => setTimeout(r, 1000));
    } catch (e) {
      results.push({ topic, lesson: null, error: String(e) });
    }
  }
  return results;
}

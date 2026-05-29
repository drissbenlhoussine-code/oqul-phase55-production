export type DynamicLessonRequest = {
  title: string;
  grade?: string;
  subject?: string;
  learnerLevel?: "weak" | "average" | "strong";
  language?: "formal_arabic" | "darija" | "french" | "english";
};

export function generateDynamicLesson(req: DynamicLessonRequest) {
  const level = req.learnerLevel ?? "average";
  const language = req.language ?? "formal_arabic";
  const difficulty =
    level === "weak" ? "شرح بطيء ومبسط مع أمثلة كثيرة" :
    level === "strong" ? "شرح مختصر مع تحديات أعمق" :
    "شرح متوازن وتفاعلي";

  return {
    title: req.title,
    grade: req.grade,
    subject: req.subject,
    language,
    difficulty,
    lesson: {
      openingQuestion: `قبل أن نشرح ${req.title}، ماذا تعرف عنه؟`,
      explanation: `سنشرح ${req.title} بطريقة ${difficulty}. نبدأ بالفكرة الأساسية، ثم مثال، ثم سؤال قصير.`,
      examples: [
        `مثال بسيط حول ${req.title}`,
        `مثال متوسط حول ${req.title}`,
        `تحدي صغير حول ${req.title}`
      ],
      interactiveCheck: [
        "ما أول خطوة؟",
        "لماذا استعملنا هذه الطريقة؟",
        "هل تستطيع إعطاء مثال آخر؟"
      ],
      remediation: [
        "إذا كان الجواب خاطئًا، ارجع إلى المفهوم الأساسي.",
        "إذا كان التلميذ مترددًا، أعط مثالًا أبسط.",
        "إذا كان الجواب صحيحًا، ارفع الصعوبة."
      ],
      summary: [
        `تعلمنا ${req.title}.`,
        "طبقنا الفكرة في أمثلة.",
        "راجعنا الأخطاء المحتملة."
      ]
    }
  };
}
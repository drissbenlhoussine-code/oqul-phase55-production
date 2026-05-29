const mathPrompts = [
  "إذا كان عندك 12 درهم واشتريت حلوى بـ 5 دراهم، شحال بقا؟",
  "قسم خبزة على 4 صحاب بالتساوي. شحال ياخذ كل واحد؟",
  "عندك 3 فرق، كل فريق فيه 4 لاعبين. شحال المجموع؟",
];

const arabicPrompts = [
  "اقرأ هذه الجملة بصوت هادئ: ذهب يوسف إلى المدرسة.",
  "كوّن جملة فيها كلمة: كتاب.",
  "استخرج الفعل من الجملة: تلعب سلمى في الحديقة.",
];

export function generateDailyChallenge(input: {
  grade: number;
  subject?: "math" | "arabic" | "french" | "science";
  weakSkillId?: string;
}) {
  const subject = input.subject ?? (input.grade <= 2 ? "math" : "arabic");
  const bank = subject === "math" ? mathPrompts : arabicPrompts;
  const prompt = bank[input.grade % bank.length];

  return {
    subject,
    prompt,
    difficulty: input.grade <= 2 ? "easy" : "normal",
    estimatedMinutes: 5,
    rewardPoints: 10 + input.grade,
    reason: input.weakSkillId
      ? "تم اختيار التحدي لدعم مهارة تحتاج مراجعة."
      : "تحدي قصير للحفاظ على عادة التعلم اليومية.",
  };
}

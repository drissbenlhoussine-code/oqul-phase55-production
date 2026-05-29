export function buildLeilaNoticedNote(input: {
  childName?: string;
  strengths?: string[];
  weaknesses?: string[];
  emotion?: "confident" | "frustrated" | "tired" | "curious" | "neutral";
}) {
  const name = input.childName ? `${input.childName} ` : "الطفل";
  const strengths = input.strengths ?? [];
  const weaknesses = input.weaknesses ?? [];

  if (weaknesses.length > 0) {
    return `${name}كان مزيان اليوم، وبان لليلى خاصنا نرجعو شوية لـ ${weaknesses[0]} بطريقة سهلة.`;
  }

  if (strengths.length > 0) {
    return `${name}كان رائع اليوم خصوصًا في ${strengths[0]} 👏`;
  }

  if (input.emotion === "tired") {
    return `${name}تعلم اليوم بهدوء، والأفضل نخلي المراجعة القادمة قصيرة.`;
  }

  return `${name}دار خطوة جميلة اليوم مع ليلى.`;
}

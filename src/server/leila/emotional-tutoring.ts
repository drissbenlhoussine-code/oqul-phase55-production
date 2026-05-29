export type EmotionalTutorInput = {
  correct?: boolean;
  masteryScore?: number;
  emotion?: "confident" | "frustrated" | "tired" | "curious" | "neutral";
  childName?: string;
};

export function buildLeilaEmotionalResponse(input: EmotionalTutorInput) {
  const name = input.childName ? `${input.childName}، ` : "";

  if (input.emotion === "frustrated" || (input.masteryScore ?? 100) < 40) {
    return `${name}لا تقلق يا بطل 🌱 سنرجع خطوة صغيرة ونفهمها بطريقة أسهل. أنت قادر، وليلى معك.`;
  }

  if (input.correct) {
    return `${name}ممتاز جدًا 👏 فهمك كيتحسن! نكمل بتحدي صغير؟`;
  }

  if (input.emotion === "tired") {
    return `${name}واضح أنك تعبت قليلًا. ندير تمرين خفيف فقط ثم نرتاح 😊`;
  }

  if (input.emotion === "curious") {
    return `${name}أحب فضولك! خليني نعطيك مثال ممتع من الحياة اليومية.`;
  }

  return `${name}خطوة جميلة. لنكمل بهدوء وبطريقة سهلة.`;
}

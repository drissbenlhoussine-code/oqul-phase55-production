const examples: Record<string, string[]> = {
  fractions: [
    "تخيل خبزة مقسومة بين 4 صحاب.",
    "تخيل بيتزا صغيرة قسمناها على جوج.",
    "تخيل مسمن مقسوم إلى أجزاء متساوية.",
  ],
  money: [
    "تخيل عندك 20 درهم ومشيت للحانوت.",
    "تخيل اشتريت عصير وحلوى وبغيتي تعرف شحال بقا.",
  ],
  multiplication: [
    "تخيل 4 فرق ديال الكرة، كل فريق فيه 5 لاعبين.",
    "تخيل 3 صفوف فالقسم، كل صف فيه 6 تلاميذ.",
  ],
  reading: [
    "نقراو الجملة بحال قصة صغيرة.",
    "نبحثو على من؟ ماذا؟ أين؟ بحال بوليسي صغير.",
  ],
};

export function getMoroccanContextExample(topic: string) {
  const bank = examples[topic] ?? examples.reading;
  return bank[Math.abs(topic.length) % bank.length];
}

export function explainLikeHome(input: { topic: string; childName?: string }) {
  const name = input.childName ? `${input.childName}، ` : "";
  return `${name}${getMoroccanContextExample(input.topic)} نخدموها خطوة بخطوة وبالدارجة.`;
}

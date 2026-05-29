export function suggestPrimaryMiniGame(subject: string, competency: string) {
  const common = {
    goal: "تثبيت المفهوم بطريقة لعب قصيرة",
    durationMinutes: 3,
    feedback: "فوري ولطيف",
  };

  if (subject.includes("math")) {
    return {
      ...common,
      type: "number_match",
      title: "لعبة طابق الرقم",
      instruction: "اختار الجواب الصحيح قبل انتهاء النجوم.",
      competency,
    };
  }

  if (subject.includes("arabic")) {
    return {
      ...common,
      type: "word_builder",
      title: "ركّب الكلمة",
      instruction: "كوّن الكلمة الصحيحة من الحروف.",
      competency,
    };
  }

  return {
    ...common,
    type: "picture_choice",
    title: "اختار الصورة المناسبة",
    instruction: "اربط الفكرة بالصورة الصحيحة.",
    competency,
  };
}
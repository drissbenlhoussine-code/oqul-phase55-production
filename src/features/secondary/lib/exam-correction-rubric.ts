export function createExamCorrectionRubric(subject: string) {
  const base = [
    { criterion: "فهم المطلوب", points: 2 },
    { criterion: "اختيار الطريقة المناسبة", points: 2 },
    { criterion: "سلامة الخطوات", points: 3 },
    { criterion: "صحة النتيجة", points: 2 },
    { criterion: "التنظيم والتبرير", points: 1 },
  ];

  if (subject.includes("arabic") || subject.includes("french") || subject.includes("philosophy")) {
    return [
      { criterion: "فهم السؤال أو النص", points: 2 },
      { criterion: "بناء الفكرة", points: 2 },
      { criterion: "الاستدلال والأمثلة", points: 3 },
      { criterion: "سلامة اللغة", points: 2 },
      { criterion: "تنظيم الجواب", points: 1 },
    ];
  }

  return base;
}
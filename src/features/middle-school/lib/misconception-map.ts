export function detectMiddleSchoolMisconception(input: {
  subject: string;
  answer: string;
  expected?: string;
}) {
  const text = input.answer.toLowerCase();

  if (input.subject.includes("math") && text.includes("denominator")) {
    return {
      key: "fraction_denominator_confusion",
      explanation: "قد يكون هناك خلط في جمع أو مقارنة المقامات.",
      remediation: "ارجع إلى تمثيل بصري للكسر قبل الحساب.",
    };
  }

  if (input.subject.includes("physics") && text.includes("force")) {
    return {
      key: "force_motion_confusion",
      explanation: "قد يكون هناك خلط بين القوة والحركة.",
      remediation: "استعمل مثال سيارة تتحرك بسرعة ثابتة مقابل سيارة تتسارع.",
    };
  }

  return {
    key: "general_incomplete_reasoning",
    explanation: "الجواب يحتاج تبريرًا أو خطوة وسيطة.",
    remediation: "اطلب من التلميذ شرح كيف وصل إلى الجواب.",
  };
}
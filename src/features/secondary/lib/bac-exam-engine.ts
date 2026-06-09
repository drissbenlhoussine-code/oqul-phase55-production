export type BacExamPlanInput = {
  grade: "TC" | "1BAC" | "2BAC";
  subject: string;
  weakCompetencies: string[];
  daysAvailable?: number;
};

export type ExerciseTier = "easy" | "medium" | "exam";

export function createBacExamPlan(input: BacExamPlanInput) {
  const days = input.daysAvailable ?? 14;
  const alignment = getBacNationalExamAlignment(input.grade, input.subject);

  return {
    mode: input.grade === "2BAC" ? "national_exam_readiness" : "progressive_exam_training",
    subject: input.subject,
    days,
    nationalExamAlignment: alignment,
    plan: [
      { phase: "diagnostic",     goal: "تحديد نقاط الضعف الدقيقة",         durationDays: Math.max(1, Math.floor(days * 0.15)) },
      { phase: "remediation",    goal: "إصلاح التعثرات بتمارين موجهة",      focus: input.weakCompetencies, durationDays: Math.max(2, Math.floor(days * 0.35)) },
      { phase: "exam_practice",  goal: "حل تمارين بأسلوب الامتحان الحقيقي", durationDays: Math.max(2, Math.floor(days * 0.35)) },
      { phase: "final_review",   goal: "مراجعة مركزة على النقاط الحاسمة",  durationDays: Math.max(1, Math.floor(days * 0.15)) },
    ],
    methodology: getBacMethodologySteps(input.subject),
  };
}

export function generateBacExerciseTiers(subject: string, topic: string): Record<ExerciseTier, { description: string; timeMinutes: number; scoringNote: string }> {
  const isLanguage = subject.includes("arabic") || subject.includes("french") || subject.includes("philosophy");
  const isScience  = subject.includes("math") || subject.includes("physics") || subject.includes("svt");

  return {
    easy: {
      description: isLanguage
        ? `سؤال فهم مباشر حول ${topic} — تعريف مفهوم أو تحديد فكرة رئيسية`
        : `تطبيق مباشر للقانون أو الصيغة في ${topic} — معطيات واضحة ومطلوب واحد`,
      timeMinutes: 8,
      scoringNote: isScience
        ? "تُعطى نقطتان للمنهجية الصحيحة ونقطة للنتيجة الصحيحة"
        : "تُعطى نقطة للفهم ونقطة للصياغة السليمة",
    },
    medium: {
      description: isLanguage
        ? `تحليل فقرة أو نص قصير من ${topic} — استخراج الأفكار وتوظيف المفاهيم`
        : `مسألة مركبة في ${topic} تتطلب خطوتين أو أكثر مع تبرير مفصل`,
      timeMinutes: 15,
      scoringNote: "تُوزع النقاط على: فهم المطلوب (2) + المنهجية (3) + التنفيذ (3) + التحقق (2)",
    },
    exam: {
      description: isLanguage
        ? `وضعية مركبة بأسلوب الباكالوريا في ${topic} — تقتضي الحجة والنقد والتركيب`
        : `مسألة بمستوى الباكالوريا في ${topic} — وضعية مركبة تشمل عدة مفاهيم مترابطة مع تبرير كامل`,
      timeMinutes: 25,
      scoringNote: isScience
        ? "يُقيَّم حسب سلم تنقيط رسمي: المنهجية (4) + الحساب (4) + التحليل (4) + الصياغة (2) = 14 نقطة"
        : "يُقيَّم على: فهم الإشكالية (3) + بناء الحجة (5) + التركيب (4) + سلامة اللغة (2) = 14 نقطة",
    },
  };
}

export function getBacNationalExamAlignment(grade: "TC" | "1BAC" | "2BAC", subject: string) {
  const examName = grade === "2BAC" ? "الباكالوريا الوطنية" : grade === "1BAC" ? "الفرض الجهوي" : "الفرض الإقليمي";

  const timeMap: Record<string, number> = {
    math:            180,
    advanced_math:   180,
    physics_chemistry: 120,
    svt:             120,
    arabic:          120,
    french:          120,
    philosophy:      120,
    history_geography: 90,
    english:          90,
    islamic_education: 90,
  };
  const totalMinutes = timeMap[subject] ?? 120;

  return {
    examName,
    totalMinutes,
    timeAllocation: getTimeAllocationGuide(subject, totalMinutes),
    answerStructure: getBacAnswerStructure(subject),
    scoringCriteria: [
      "المنهجية والترتيب المنطقي",
      "دقة المعلومات وصحة التطبيق",
      "جودة التعليل والتبرير",
      "سلامة اللغة والكتابة",
    ],
  };
}

function getTimeAllocationGuide(subject: string, totalMinutes: number): string[] {
  if (subject.includes("philosophy") || subject.includes("arabic") || subject.includes("french")) {
    return [
      `${Math.round(totalMinutes * 0.07)} دقيقة: قراءة التعليمات وتخطيط الإجابة`,
      `${Math.round(totalMinutes * 0.10)} دقيقة: مقدمة + طرح الإشكالية`,
      `${Math.round(totalMinutes * 0.65)} دقيقة: بناء العرض (أطروحة + نقيضة + تركيب)`,
      `${Math.round(totalMinutes * 0.12)} دقيقة: خاتمة`,
      `${Math.round(totalMinutes * 0.06)} دقيقة: مراجعة اللغة والمراجعة النهائية`,
    ];
  }
  return [
    `${Math.round(totalMinutes * 0.08)} دقيقة: قراءة وتحديد المعطيات والمطلوب`,
    `${Math.round(totalMinutes * 0.70)} دقيقة: حل التمارين (من السهل إلى الصعب)`,
    `${Math.round(totalMinutes * 0.12)} دقيقة: مراجعة الحسابات والوحدات`,
    `${Math.round(totalMinutes * 0.10)} دقيقة: تدقيق الخطوات والمنهجية`,
  ];
}

function getBacAnswerStructure(subject: string): string[] {
  if (subject.includes("philosophy")) {
    return [
      "مقدمة: تعريف المفاهيم + طرح الإشكالية بجملة استفهامية واضحة",
      "الأطروحة: عرض الموقف الأول مع حججه ومبرراته",
      "النقيضة: عرض الموقف المضاد مع حججه ونقد الأطروحة",
      "التركيب: موقف شخصي مبرر لا مجرد وسط بين الموقفين",
      "خاتمة: إجابة مباشرة على الإشكالية + فتح أفق",
    ];
  }
  if (subject.includes("arabic") || subject.includes("french")) {
    return [
      "مقدمة: تقديم الموضوع + الإشكالية + خطة العرض",
      "العرض: فقرتان أو ثلاث فقرات متماسكة مع روابط منطقية",
      "الاستدلال: مثال أو شاهد لكل فكرة رئيسية",
      "خاتمة: خلاصة + رأي شخصي مبرر",
    ];
  }
  return [
    "قراءة المسألة: استخراج المعطيات والمطلوب بوضوح",
    "اختيار الطريقة: ذكر القانون أو النظرية المستعملة مع التبرير",
    "الحل: خطوات واضحة ومرقمة مع تبرير كل انتقال",
    "التحقق: صحة الوحدات، المجال المنطقي للنتيجة، التحقق العددي",
  ];
}

export function getBacMethodologySteps(subject: string): string[] {
  if (subject.includes("math") || subject.includes("physics")) {
    return [
      "اقرأ المسألة مرتين — لا تبدأ الحل قبل فهم المطلوب كاملاً",
      "اكتب المعطيات والمطلوب في جدول — يساعدك على اختيار القانون",
      "اختر القانون أو النظرية المناسبة وبررها قبل التطبيق",
      "حل خطوة بخطوة مع تبرير كل خطوة (لا تقفز إلى النتيجة)",
      "تحقق: الوحدات + الإشارة + المنطق العام للنتيجة",
    ];
  }
  if (subject.includes("philosophy")) {
    return [
      "اقرأ السؤال وحدد المفاهيم الأساسية — عرّف كل مفهوم بدقة",
      "صغ الإشكالية كجملة استفهامية مباشرة",
      "ابنِ الأطروحة مع ثلاث حجج على الأقل من مفكرين أو أمثلة",
      "قدم النقيضة بجدية — لا تختزلها",
      "التركيب يجب أن يكون موقفاً أصيلاً لا مجرد حل وسط",
    ];
  }
  return [
    "اقرأ التعليمات بعناية وحدد المطلوب من كل سؤال",
    "خصص زمناً لكل سؤال حسب عدد نقاطه",
    "ابدأ بالأسئلة المضمونة لضمان النقاط الأساسية",
    "لا تترك سؤالاً فارغاً — ابدأ بما تعرف واطلب نقاطاً جزئية",
    "راجع إجاباتك في الدقائق الأخيرة",
  ];
}

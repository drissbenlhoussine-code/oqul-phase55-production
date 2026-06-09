type RubricCriterion = { criterion: string; points: number; examinerNote?: string };

export function createExamCorrectionRubric(subject: string): RubricCriterion[] {
  if (subject.includes("philosophy")) {
    return [
      { criterion: "فهم الإشكالية وصياغتها", points: 2, examinerNote: "يُتوقع جملة استفهامية واضحة تُحدد موضوع التفكير" },
      { criterion: "بناء الأطروحة وحججها", points: 4, examinerNote: "الحجج يجب أن تكون مدعومة بمفكرين أو أمثلة دقيقة" },
      { criterion: "النقيضة وعمق النقد",    points: 3, examinerNote: "لا تقبل نقيضة ضعيفة أو مختزلة" },
      { criterion: "التركيب والموقف الشخصي", points: 3, examinerNote: "الموقف الشخصي يجب أن يكون مبرراً لا مجرد وسط" },
      { criterion: "سلامة اللغة والأسلوب",  points: 2, examinerNote: "لغة فلسفية أكاديمية — تجنب العبارات اليومية" },
      { criterion: "خاتمة وفتح الأفق",       points: 1, examinerNote: "خاتمة تجيب على الإشكالية وتفتح سؤالاً جديداً" },
    ];
  }

  if (subject.includes("arabic")) {
    return [
      { criterion: "فهم النص واستخراج الأفكار", points: 3, examinerNote: "يُتوقع تمييز الفكرة العامة عن الأفكار الجزئية" },
      { criterion: "تحليل الأساليب اللغوية",    points: 2, examinerNote: "الصور البيانية والأساليب البلاغية مع تأثيرها" },
      { criterion: "التعبير الكتابي",            points: 3, examinerNote: "تنظيم الفقرات، الروابط، الانسجام" },
      { criterion: "سلامة النحو والصرف",         points: 2, examinerNote: "أخطاء الإعراب تُخصم نقطة على الأقل" },
      { criterion: "الأصالة والإبداع في الرأي",  points: 0, examinerNote: "نقطة بونص للإجابات المتميزة" },
    ];
  }

  if (subject.includes("french")) {
    return [
      { criterion: "Compréhension du texte",    points: 3, examinerNote: "Identification des idées principales et secondaires" },
      { criterion: "Analyse linguistique",       points: 2, examinerNote: "Figures de style, registre, connecteurs" },
      { criterion: "Expression écrite",          points: 3, examinerNote: "Structure claire: introduction-développement-conclusion" },
      { criterion: "Correction grammaticale",    points: 2, examinerNote: "Conjugaison, accord, syntaxe — chaque faute grave = -0.5" },
    ];
  }

  if (subject.includes("physics") || subject.includes("svt")) {
    return [
      { criterion: "استخراج المعطيات والمطلوب",  points: 1, examinerNote: "معطيات واضحة ومرتبة — نقطة كاملة أو صفر" },
      { criterion: "اختيار القانون وتبريره",       points: 2, examinerNote: "ذكر القانون باسمه + سبب الاختيار" },
      { criterion: "سلامة الخطوات والحساب",       points: 4, examinerNote: "كل خطوة تُصحح مستقلة — خطأ الحساب لا يُلغي نقاط المنهجية" },
      { criterion: "التحقق: وحدات وإشارة",        points: 1, examinerNote: "وحدة خاطئة = خصم نقطة كاملة" },
      { criterion: "صحة النتيجة النهائية",        points: 2, examinerNote: "نتيجة صحيحة بمنهجية صحيحة فقط" },
    ];
  }

  // Default: math / generic STEM
  return [
    { criterion: "فهم المطلوب وتحديد المعطيات",  points: 1, examinerNote: "ملاحظة: الاستخراج الكامل للمعطيات ضروري قبل الحل" },
    { criterion: "اختيار الطريقة وتبريرها",       points: 2, examinerNote: "يُتوقع ذكر النظرية أو القانون المستعمل صراحةً" },
    { criterion: "سلامة الخطوات والمنهجية",       points: 3, examinerNote: "كل خطوة مستقلة — خطأ حسابي لا يُلغي نقاط المنهجية" },
    { criterion: "صحة النتيجة النهائية",           points: 2, examinerNote: "نقطة كاملة للنتيجة الصحيحة فقط إن كانت الطريقة صحيحة" },
    { criterion: "التنظيم والتبرير",               points: 1, examinerNote: "ترتيب الخطوات، الوحدات، الإشارات، والتبرير اللفظي" },
    { criterion: "التحقق من النتيجة",             points: 1, examinerNote: "بونص — التحقق يُثبت الفهم العميق" },
  ];
}

export function getCommonMistakesBySubject(subject: string): { mistake: string; correction: string; frequency: "very_common" | "common" | "occasional" }[] {
  if (subject.includes("math") || subject.includes("advanced_math")) {
    return [
      { mistake: "القفز إلى النتيجة دون كتابة الخطوات",             correction: "اكتب كل خطوة مع تبريرها حتى لو بدت واضحة",                   frequency: "very_common" },
      { mistake: "إهمال الوحدات في الفيزياء الرياضية",              correction: "أضف الوحدة دائماً في النهاية وتحقق من تجانسها",                frequency: "very_common" },
      { mistake: "الخلط بين الاشتقاق والتكامل في التطبيقات",        correction: "حدد الطلب أولاً: 'إيجاد المعدل' = اشتقاق | 'إيجاد المساحة' = تكامل", frequency: "common" },
      { mistake: "نسيان التحقق من شرط صحة الحل (النطاق، الإشارة)", correction: "أضف خطوة تحقق في نهاية كل حل",                                 frequency: "common" },
      { mistake: "أخطاء في التوزيع الجبري خاصة مع الإشارات السالبة", correction: "توسع ببطء وتحقق من إشارة كل حد",                               frequency: "very_common" },
    ];
  }
  if (subject.includes("philosophy")) {
    return [
      { mistake: "تقديم إشكالية كموضوع لا كسؤال",                  correction: "صغ الإشكالية دائماً كجملة استفهامية: 'هل...؟' أو 'ما...؟'",  frequency: "very_common" },
      { mistake: "نسب آراء خاطئة لفلاسفة بعينهم",                  correction: "إذا لم تكن متأكداً، قل 'يرى بعض الفلاسفة' بدلاً من الاسم",   frequency: "common" },
      { mistake: "النقيضة المختزلة ('البعض يقول العكس')",            correction: "عالج النقيضة بنفس عمق الأطروحة مع حجج حقيقية",               frequency: "very_common" },
      { mistake: "التركيب = 'إذاً الحقيقة في الوسط'",               correction: "التركيب موقف أصيل مبرر لا مجرد توفيق",                        frequency: "very_common" },
    ];
  }
  if (subject.includes("physics")) {
    return [
      { mistake: "تطبيق القانون دون ذكره",                           correction: "اكتب اسم القانون ثم طبقه",                                     frequency: "very_common" },
      { mistake: "إهمال وحدات القياس",                               correction: "تحويل الوحدات قبل التطبيق (km/h → m/s مثلاً)",                frequency: "very_common" },
      { mistake: "إشارة الشغل والطاقة (+ أو -)",                    correction: "الشغل موجب إذا كان في اتجاه الحركة — ارسم المتجهات أولاً",    frequency: "common" },
      { mistake: "الخلط بين الكتلة والوزن",                          correction: "الكتلة m بالـ kg | الوزن P = mg بالنيوتن",                    frequency: "common" },
    ];
  }
  return [
    { mistake: "عدم قراءة السؤال كاملاً قبل الإجابة",               correction: "اقرأ مرتين وضع خطاً تحت الكلمات المفتاحية",                   frequency: "very_common" },
    { mistake: "إجابات طويلة غير مركزة",                             correction: "ابدأ بجملة إجابة مباشرة ثم وضح",                             frequency: "common" },
    { mistake: "ترك الأسئلة الصعبة فارغة",                           correction: "اكتب ما تعرفه — النقاط الجزئية تُحسب",                       frequency: "common" },
  ];
}

export function getExaminerExpectations(grade: "TC" | "1BAC" | "2BAC", subject: string): string[] {
  const base = [
    "الوضوح والترتيب المنطقي للإجابة أهم من الطول",
    "التبرير لكل خطوة — 'لأن' أو 'بما أن' أو 'نستنتج أن'",
    "خط واضح ومقروء — المصحح لا يبحث عن الإجابة",
  ];

  if (grade === "2BAC") {
    return [
      ...base,
      "مستوى التعقيد يناسب الباكالوريا الوطنية — لا إجابات سطحية",
      "التعامل مع الوضعيات المركبة التي تجمع عدة مفاهيم",
      "المصحح يُقيّم المنهجية حتى لو كانت النتيجة الرقمية خاطئة",
    ];
  }
  if (grade === "1BAC") {
    return [
      ...base,
      "الفروض الجهوية تُركز على التطبيق المباشر والمسائل المتوسطة",
      "الخطأ في النتيجة لا يُلغي نقاط المنهجية الصحيحة",
    ];
  }
  return [
    ...base,
    "الفروض الإقليمية تختبر الفهم الأساسي والتطبيق المباشر",
    "التبرير مطلوب حتى في الأسئلة السهلة",
  ];
}

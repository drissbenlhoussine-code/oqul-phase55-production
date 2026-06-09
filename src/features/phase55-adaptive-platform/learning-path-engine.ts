export type LearnerSignal = {
  childId?: string;
  grade?: string | null;
  subject?: string | null;
  weakPoints?: string[];
  completedLessons?: number;
  averageScore?: number;
  confidence?: number;
};

type SubjectKey = "math" | "physics" | "arabic" | "french" | "philosophy" | "history" | "svt" | "default";
type WeaknessKey = "algebra" | "geometry" | "grammar" | "writing" | "reading" | "proof" | "generic";

function detectSubject(subject: string | null | undefined): SubjectKey {
  if (!subject) return "default";
  const s = subject.toLowerCase();
  if (s.includes("math") || s.includes("رياضيات")) return "math";
  if (s.includes("physics") || s.includes("فيزياء")) return "physics";
  if (s.includes("arabic") || s.includes("عرب")) return "arabic";
  if (s.includes("french") || s.includes("فرنسي") || s.includes("français")) return "french";
  if (s.includes("philosophy") || s.includes("فلسفة")) return "philosophy";
  if (s.includes("history") || s.includes("تاريخ") || s.includes("geography") || s.includes("جغرافيا")) return "history";
  if (s.includes("svt") || s.includes("علوم الحياة")) return "svt";
  return "default";
}

function detectWeakness(weakPoints: string[]): WeaknessKey {
  const joined = weakPoints.join(" ").toLowerCase();
  if (joined.includes("جبر") || joined.includes("معادلة") || joined.includes("algebra")) return "algebra";
  if (joined.includes("هندسة") || joined.includes("geometry") || joined.includes("برهان هندسي")) return "geometry";
  if (joined.includes("نحو") || joined.includes("صرف") || joined.includes("إعراب") || joined.includes("grammar")) return "grammar";
  if (joined.includes("إنشاء") || joined.includes("كتابة") || joined.includes("تعبير") || joined.includes("writing") || joined.includes("rédaction")) return "writing";
  if (joined.includes("قراءة") || joined.includes("فهم النص") || joined.includes("reading") || joined.includes("compréhension")) return "reading";
  if (joined.includes("برهان") || joined.includes("إثبات") || joined.includes("preuve") || joined.includes("démonstration")) return "proof";
  return "generic";
}

const SUBJECT_WEEKLY_PLANS: Record<SubjectKey, (weakness: WeaknessKey, risk: string) => { day: string; action: string; tool: string; durationMinutes: number }[]> = {
  math: (w, risk) => [
    { day: "اليوم 1", action: w === "algebra" ? "مراجعة المعادلات والجبر الأساسي — تشخيص سريع" : w === "geometry" ? "مراجعة النظريات الهندسية الأساسية" : "تشخيص شامل لنقاط الضعف", tool: "ليلى", durationMinutes: 20 },
    { day: "اليوم 2", action: w === "proof" ? "تدريب على كتابة البراهين خطوة بخطوة" : "شرح موجه للمفاهيم المتعثرة مع أمثلة مغربية", tool: "مولد الدروس", durationMinutes: 25 },
    { day: "اليوم 3", action: "تمارين سهلة ومتوسطة بتركيز على نقطة الضعف المحددة", tool: "استعداد للامتحان", durationMinutes: 30 },
    { day: "اليوم 4", action: "تمرين بمستوى الامتحان — حل كامل مع تبرير كل خطوة", tool: "استعداد للامتحان", durationMinutes: 30 },
    { day: "اليوم 5", action: "علاج الأخطاء التي ظهرت + إعادة الحل الصحيح", tool: "ليلى", durationMinutes: 20 },
    { day: "اليوم 6", action: risk === "high" ? "مراجعة prerequisite وأساسيات الرياضيات" : "تمارين متنوعة لتعزيز الثقة", tool: "مولد الدروس", durationMinutes: 25 },
    { day: "اليوم 7", action: "اختبار قصير شامل + مراجعة مستوى التقدم", tool: "استعداد للامتحان", durationMinutes: 20 },
  ],
  physics: (w, risk) => [
    { day: "اليوم 1", action: "مراجعة القوانين الأساسية في المادة المتعثرة", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "اليوم 2", action: "شرح المنهجية: المعطيات → القانون → التطبيق → التحقق", tool: "ليلى", durationMinutes: 25 },
    { day: "اليوم 3", action: "تمارين تطبيقية مباشرة مع التركيز على الوحدات", tool: "استعداد للامتحان", durationMinutes: 25 },
    { day: "اليوم 4", action: "تجارب فكرية: ماذا يحدث لو تغيرت المعطيات؟", tool: "ليلى", durationMinutes: 20 },
    { day: "اليوم 5", action: "تمرين بأسلوب الامتحان — وضعية مركبة كاملة", tool: "استعداد للامتحان", durationMinutes: 30 },
    { day: "اليوم 6", action: risk === "high" ? "مراجعة الأساسيات ومفاهيم الطاقة والحركة" : "تعميق الفهم: ربط المادة بالحياة اليومية المغربية", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "اليوم 7", action: "اختبار ذاتي + قائمة القوانين الأساسية للحفظ", tool: "استعداد للامتحان", durationMinutes: 20 },
  ],
  arabic: (w, risk) => [
    { day: "اليوم 1", action: w === "grammar" ? "مراجعة قواعد الإعراب والصرف الأساسية" : "تحليل نص عربي كامل خطوة بخطوة", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "اليوم 2", action: w === "writing" ? "بناء الفقرة: مقدمة + حجة + مثال + خاتمة" : "تدريب على استخراج الأفكار وتنظيمها", tool: "ليلى", durationMinutes: 25 },
    { day: "اليوم 3", action: "تمارين نحوية مع التعليل — لا إجابة بدون إعراب", tool: "مولد الدروس", durationMinutes: 25 },
    { day: "اليوم 4", action: "تمرين في التعبير الكتابي + تصحيح الأسلوب", tool: "ليلى", durationMinutes: 30 },
    { day: "اليوم 5", action: "مراجعة الأخطاء الشائعة في الفروض السابقة", tool: "استعداد للامتحان", durationMinutes: 20 },
    { day: "اليوم 6", action: "قراءة نص أدبي + استخراج الأساليب البيانية", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "اليوم 7", action: "تمرين بأسلوب الامتحان — تحليل نص + تعبير كتابي", tool: "استعداد للامتحان", durationMinutes: 30 },
  ],
  french: (w, risk) => [
    { day: "Jour 1", action: w === "writing" ? "Structure d'un paragraphe: idée + argument + exemple" : "Compréhension de texte: idées principales et secondaires", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "Jour 2", action: "Révision de grammaire ciblée: conjugaison et accord", tool: "ليلى", durationMinutes: 25 },
    { day: "Jour 3", action: "Exercices de vocabulaire en contexte marocain", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "Jour 4", action: w === "writing" ? "Rédaction guidée: introduction et développement" : "Analyse linguistique d'un texte court", tool: "ليلى", durationMinutes: 30 },
    { day: "Jour 5", action: "Correction des erreurs récurrentes — liste personnalisée", tool: "استعداد للامتحان", durationMinutes: 20 },
    { day: "Jour 6", action: risk === "high" ? "Révision des structures de base + vocabulaire fondamental" : "Texte authentique + questions de style BAC", tool: "مولد الدروس", durationMinutes: 25 },
    { day: "Jour 7", action: "Mini-devoir complet style examen + auto-correction", tool: "استعداد للامتحان", durationMinutes: 30 },
  ],
  philosophy: (w, risk) => [
    { day: "اليوم 1", action: "مراجعة منهجية المقالة الفلسفية: إشكالية + أطروحة + نقيضة + تركيب", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "اليوم 2", action: "تدريب على صياغة الإشكالية بدقة — الجملة الاستفهامية", tool: "ليلى", durationMinutes: 25 },
    { day: "اليوم 3", action: "تحليل نص فلسفي: استخراج الحجج والموقف", tool: "مولد الدروس", durationMinutes: 25 },
    { day: "اليوم 4", action: "تدريب على بناء النقيضة بعمق — لا نقيضة مختزلة", tool: "ليلى", durationMinutes: 25 },
    { day: "اليوم 5", action: "كتابة تركيب فلسفي أصيل — موقف شخصي مبرر", tool: "ليلى", durationMinutes: 30 },
    { day: "اليوم 6", action: "مراجعة أبرز الفلاسفة والمحاور المقررة", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "اليوم 7", action: "مقالة كاملة في ظرف الامتحان + تصحيح ذاتي", tool: "استعداد للامتحان", durationMinutes: 45 },
  ],
  history: (_w, risk) => [
    { day: "اليوم 1", action: "مراجعة الخريطة والخط الزمني لمحور الضعف", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "اليوم 2", action: "تحليل وثيقة تاريخية أو جغرافية كاملة", tool: "ليلى", durationMinutes: 25 },
    { day: "اليوم 3", action: "تمارين الربط السببي: علة ونتيجة في الأحداث", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "اليوم 4", action: "تدريب على إنتاج وثيقة: خريطة أو رسم بياني", tool: "استعداد للامتحان", durationMinutes: 25 },
    { day: "اليوم 5", action: risk === "high" ? "مراجعة أساسيات الجغرافيا المغربية" : "مراجعة الأحداث الكبرى والمعاهدات", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "اليوم 6", action: "فرض كامل بأسلوب الامتحان: تحليل + تركيب + رأي", tool: "استعداد للامتحان", durationMinutes: 30 },
    { day: "اليوم 7", action: "مراجعة الأخطاء وتلخيص المفاهيم الأساسية", tool: "ليلى", durationMinutes: 20 },
  ],
  svt: (_w, risk) => [
    { day: "اليوم 1", action: "مراجعة الرسوم البيانية والتخطيطات في المادة المتعثرة", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "اليوم 2", action: "قراءة وثيقة علمية: استخراج المعلومات والعلاقات", tool: "ليلى", durationMinutes: 25 },
    { day: "اليوم 3", action: "تمارين الربط: بنية ← وظيفة ← تأثير", tool: "مولد الدروس", durationMinutes: 25 },
    { day: "اليوم 4", action: "تمرين بأسلوب الامتحان مع سلم التنقيط", tool: "استعداد للامتحان", durationMinutes: 30 },
    { day: "اليوم 5", action: risk === "high" ? "مراجعة أساسيات الخلية والوظائف الحيوية" : "علاج الأخطاء الشائعة + مراجعة المصطلحات", tool: "ليلى", durationMinutes: 20 },
    { day: "اليوم 6", action: "قراءة نص علمي مغربي البيئة", tool: "مولد الدروس", durationMinutes: 20 },
    { day: "اليوم 7", action: "تمرين شامل + تلخيص النقاط الأساسية", tool: "استعداد للامتحان", durationMinutes: 25 },
  ],
  default: (_w, risk) => [
    { day: "اليوم 1", action: "تشخيص سريع + مراجعة الأساسيات", tool: "ليلى", durationMinutes: 20 },
    { day: "اليوم 2", action: "شرح موجه مع ليلى + مثالين من المنهج المغربي", tool: "ليلى", durationMinutes: 25 },
    { day: "اليوم 3", action: "تمارين سهلة ومتوسطة", tool: "مولد الدروس", durationMinutes: 25 },
    { day: "اليوم 4", action: "علاج الأخطاء الشائعة", tool: "استعداد للامتحان", durationMinutes: 20 },
    { day: "اليوم 5", action: risk === "high" ? "مراجعة الأساسيات من البداية" : "اختبار قصير + توصية تلقائية", tool: "استعداد للامتحان", durationMinutes: 20 },
  ],
};

export function buildPersonalizedLearningPath(signal: LearnerSignal) {
  const score      = signal.averageScore ?? 50;
  const confidence = signal.confidence ?? 3;
  const weakPoints = signal.weakPoints ?? [];
  const subjectKey = detectSubject(signal.subject);
  const weakKey    = detectWeakness(weakPoints);

  const risk =
    score < 45 || confidence <= 2 ? "high" :
    score < 65 || weakPoints.length >= 3 ? "medium" :
    "low";

  const pace =
    risk === "high" ? "slow_guided" :
    risk === "medium" ? "balanced" :
    "accelerated";

  const weeklyPlan = SUBJECT_WEEKLY_PLANS[subjectKey](weakKey, risk);

  const subjectRecommendations: Record<SubjectKey, string[]> = {
    math: [
      "اكتب كل خطوة حسابية مع تبريرها — المصحح يُقيّم المنهجية قبل النتيجة.",
      weakKey === "algebra" ? "للجبر: ابدأ دائماً بتبسيط التعبير قبل الحل." : "للهندسة: ارسم الشكل دائماً قبل البرهان.",
      "استعمل ليلى لشرح الخطأ — لا تنتقل لتمرين آخر قبل فهم الخطأ.",
    ],
    physics: [
      "قبل أي تطبيق: اكتب اسم القانون + بيان المعطيات + الوحدات.",
      "الخطأ في الوحدة = خصم نقطة كاملة في الامتحان.",
      "استعمل مولد الدروس لمراجعة أي قانون تشك فيه.",
    ],
    arabic: [
      weakKey === "grammar" ? "للنحو: لا تُجب على سؤال إعراب بدون ذكر العلامة والسبب." : "للإنشاء: اكتب مخططاً قبل الكتابة الكاملة.",
      "قراءة نص يومياً تُحسن الأسلوب أسرع من أي تمرين آخر.",
      "استعمل ليلى للمناقشة النحوية — تفاعل أفضل من الحفظ.",
    ],
    french: [
      weakKey === "writing" ? "Pour la rédaction: un plan avant d'écrire — 5 minutes de plan économisent 15 minutes d'écriture." : "Pour la grammaire: corrige tes erreurs sur une liste personnelle.",
      "Lis un texte court en français chaque jour — même 10 minutes.",
      "Utilise Leila en français — elle s'adapte à ta langue.",
    ],
    philosophy: [
      "المقالة الفلسفية: لا بداية بـ'منذ القدم' — ابدأ بطرح الإشكالية مباشرة.",
      "النقيضة يجب أن تكون بنفس قوة الأطروحة — لا تختزلها.",
      "ليلى تساعدك في بناء الحجة — اطلب منها مناقشة موقف فلسفي.",
    ],
    history: [
      "حفظ التواريخ أسهل بالتسلسل الزمني — ارسم خطاً زمنياً.",
      "لكل حدث تاريخي: سبب + نتيجة + أثر على المغرب.",
      "استعمل مولد الدروس لتحليل أي وثيقة تاريخية.",
    ],
    svt: [
      "لكل رسم: حدد البنية + الوظيفة + العلاقة مع الكل.",
      "المصطلحات العلمية الدقيقة = نقاط إضافية في الامتحان.",
      "استعمل ليلى لشرح الروابط البيولوجية الصعبة.",
    ],
    default: [
      risk === "high" ? "ابدأ من أساسيات أبسط ولا تنتقل بسرعة." : "استمر في التدرج مع تمارين متنوعة.",
      "اطلب من ليلى تفسير كل خطأ قبل إعطاء الجواب.",
      "استعمل اختباراً قصيراً بعد كل درس.",
    ],
  };

  return {
    risk,
    pace,
    subject: signal.subject ?? "غير محدد",
    detectedWeakness: weakKey !== "generic" ? weakKey : null,
    weeklyPlan,
    recommendations: subjectRecommendations[subjectKey],
    nextActions: weakPoints.length
      ? weakPoints.slice(0, 3).map((w) => `راجع: ${w}`)
      : [`ابدأ بدرس جديد في ${signal.subject ?? "المادة"} مع اختبار قبلي`],
    toolConnections: {
      leila:         "اسألي ليلى لشرح أي مفهوم صعب أو لمناقشة خطأ",
      lessonHelper:  "استعمل مولد الدروس للحصول على شرح كامل مع أمثلة وتمارين",
      examPrep:      "استعمل استعداد للامتحان لتمارين بمستوى الفرض والباكالوريا",
    },
  };
}

"use client";
import { useState, useEffect } from "react";
import { Send, RotateCcw, Copy, CheckCircle, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn }     from "@/lib/cn";

// ── Grade level (more granular than sidebar GradeLevel) ───────────────────────

type ExamGradeLevel = "primary" | "middle" | "tc" | "bac1" | "bac2" | "unknown";

function detectExamGradeLevel(slug: string | undefined): ExamGradeLevel {
  if (!slug) return "unknown";
  const s = slug.toLowerCase().trim();
  if (s === "ap" || s.startsWith("ap") || /^\dap/.test(s)) return "primary";

  // Secondary — most specific first
  if (s.includes("2bac") || s.startsWith("2bac") || /2.*bac/.test(s) || s === "tronc-commun-2" || s.includes("deuxième") || s.includes("ثانية باك"))
    return "bac2";
  if (s.includes("1bac") || s.startsWith("1bac") || /1.*bac/.test(s) || s.includes("première bac") || s.includes("أولى باك"))
    return "bac1";
  if (s === "tc" || s.startsWith("tc") || s.includes("tronc") || s.includes("common-core") || s.includes("trunk-common") || s.includes("جذع"))
    return "tc";
  if (s.includes("bac") || s.includes("lycee") || s.includes("lycée") || s.includes("secondary") || s.includes("ثانوي"))
    return "bac1"; // fallback secondary → bac1

  if (
    s === "ac" || /^\dac/.test(s) || s.startsWith("ac") ||
    s.includes("college") || s.includes("collège") || s.includes("middle") ||
    s.includes("اعدادي") || s.includes("الإعدادي")
  ) return "middle";

  return "unknown";
}

// ── Exam type labels per level ────────────────────────────────────────────────

const EXAM_TYPE: Record<ExamGradeLevel, string> = {
  middle:  "الفرض والامتحان الموحد الإقليمي",
  tc:      "الفرض والامتحان الموحد الإقليمي (جذع مشترك)",
  bac1:    "الفرض والامتحان الموحد الجهوي (السنة الأولى باك)",
  bac2:    "الفرض والامتحان الوطني الموحد (الباكالوريا)",
  primary: "",
  unknown: "",
};

const LEVEL_LABEL: Record<ExamGradeLevel, string> = {
  middle:  "الإعدادي",
  tc:      "الجذع المشترك",
  bac1:    "السنة الأولى باك",
  bac2:    "الباكالوريا (2BAC)",
  primary: "",
  unknown: "",
};

// ── Subjects per level ────────────────────────────────────────────────────────

const SUBJECTS: Record<ExamGradeLevel, string[]> = {
  middle: [
    "الرياضيات", "اللغة العربية", "الفيزياء والكيمياء",
    "علوم الحياة والأرض", "التاريخ والجغرافيا", "التربية الإسلامية", "اللغة الفرنسية",
  ],
  tc: [
    "الرياضيات", "الفيزياء والكيمياء", "علوم الحياة والأرض",
    "اللغة العربية", "التاريخ والجغرافيا", "اللغة الفرنسية",
  ],
  bac1: [
    "الرياضيات", "الفيزياء والكيمياء", "علوم الحياة والأرض",
    "اللغة العربية", "الفلسفة", "التاريخ والجغرافيا",
    "علوم اقتصادية واجتماعية", "اللغة الفرنسية",
  ],
  bac2: [
    "الرياضيات", "الفيزياء والكيمياء", "علوم الحياة والأرض",
    "اللغة العربية", "الفلسفة", "التاريخ والجغرافيا",
    "علوم اقتصادية واجتماعية", "اللغة الفرنسية",
  ],
  primary: [],
  unknown: [
    "الرياضيات", "اللغة العربية", "الفيزياء والكيمياء",
    "علوم الحياة والأرض", "التاريخ والجغرافيا",
  ],
};

// ── Topics per level × subject ────────────────────────────────────────────────

type TopicMap = Record<string, Record<string, string[]>>;

const TOPICS: Partial<TopicMap> = {
  middle: {
    "الرياضيات":        ["كسور وأعداد عشرية", "معادلات وتفاوتات", "هندسة مستوية", "نسب ومئويات", "إحصاء وتمثيلات", "أعداد صحيحة وعمليات"],
    "الفيزياء والكيمياء": ["المادة وتحولاتها", "الكهرباء الساكنة", "الضوء والأبصار", "المحاليل والتفاعلات", "الميكانيك"],
    "علوم الحياة والأرض": ["الخلية والكائنات الحية", "الهضم والتغذية", "الحركة والعضلات", "التوالد", "الجيولوجيا والصخور"],
    "اللغة العربية":    ["النصوص الأدبية", "قواعد اللغة", "التعبير والإنشاء", "البلاغة"],
    "التاريخ والجغرافيا": ["الحضارات القديمة", "الجغرافيا الاقتصادية", "تاريخ المغرب", "البيئة والتنمية"],
  },
  tc: {
    "الرياضيات":        ["الدوال العددية", "المشتقات", "المثلثية", "هندسة فضائية", "حساب المتجهات", "الإحصاء والاحتمالات"],
    "الفيزياء والكيمياء": ["الكيمياء العضوية المدخل", "الكهرباء والدوائر", "ميكانيك نيوتن", "الذرة والعنصر الكيميائي"],
    "علوم الحياة والأرض": ["الوراثة والخلية", "وحدة الكائنات الحية", "علم الأعصاب المدخل", "الجيولوجيا الخارجية"],
    "اللغة العربية":    ["الأجناس الأدبية", "النقد الأدبي", "قواعد متقدمة", "التعبير الكتابي"],
  },
  bac1: {
    "الرياضيات":        ["التفاضل والتكامل", "المتتاليات", "اللوغاريتم والأسي", "الاحتمالات", "المتجهات والفضاء"],
    "الفيزياء والكيمياء": ["الميكانيك الكلاسيكي", "الكهرومغناطيسية", "الكيمياء العضوية", "الضوئيات"],
    "علوم الحياة والأرض": ["الجهاز العصبي والهرموني", "المناعة", "الجيولوجيا الداخلية", "علم الوراثة"],
    "الفلسفة":          ["الإنسان والتفكير", "المعرفة والحقيقة", "الوجود والزمان", "السياسة والمجتمع"],
    "التاريخ والجغرافيا": ["الحرب العالمية والعلاقات الدولية", "التنمية والتفاوتات", "العولمة", "جغرافيا المغرب"],
  },
  bac2: {
    "الرياضيات":        ["الأعداد المركبة", "التكامل المتقدم", "المعادلات التفاضلية", "الاحتمالات المتقدمة", "الفضاء الإقليدي"],
    "الفيزياء والكيمياء": ["ميكانيك الموائع وتحليل الحركة", "الكيمياء العضوية المتقدمة", "الكهرومغناطيسية المتقدمة", "فيزياء النواة"],
    "علوم الحياة والأرض": ["أساليب الاستدلال العلمي", "الجينوم وتنظيم التعبير الجيني", "الجيولوجيا والبنية الداخلية"],
    "الفلسفة":          ["نظرية المعرفة", "فلسفة الفن", "الأخلاق والسياسة", "الوجودية والحرية"],
    "التاريخ والجغرافيا": ["العلاقات الدولية بعد الحرب الباردة", "الجغرافيا الاقتصادية العالمية", "قضايا المغرب المعاصر"],
  },
};

// ── Topic-specific required concepts ─────────────────────────────────────────
// Used to inject concrete concept lists so the AI produces topic-specific exercises
// instead of generic ones.

type TopicConceptsMap = Partial<Record<ExamGradeLevel, Record<string, Record<string, string[]>>>>;

const TOPIC_CONCEPTS: TopicConceptsMap = {
  middle: {
    "الرياضيات": {
      "كسور وأعداد عشرية": ["تبسيط الكسور", "ترتيب الكسور والأعداد العشرية", "الجمع والطرح والضرب والقسمة على الكسور", "التحويل بين الكسور والأعداد العشرية", "حل مسائل باستخدام الكسور"],
      "معادلات وتفاوتات": ["حل معادلة من الدرجة الأولى بمجهول", "التفاوتات وحلّها", "حل المعادلات بالعزل", "تطبيقات حياتية: مسائل عمرية وتجارية"],
      "هندسة مستوية": ["خصائص المثلثات والمضلعات", "محيط ومساحة المثلث والمستطيل والدائرة", "نظرية فيثاغورس وتطبيقاتها", "التشابه والتماثل"],
      "نسب ومئويات": ["مفهوم النسبة والتناسب", "النسبة المئوية", "تطبيقات: الأرباح والتخفيضات والفائدة"],
      "إحصاء وتمثيلات": ["مبيان الأعمدة والمبيان الدائري", "الوسط الحسابي والمنوال والوسيط", "قراءة جداول إحصائية وتفسيرها"],
      "أعداد صحيحة وعمليات": ["العمليات على الأعداد الصحيحة والنسبية", "القسمة الإقليدية", "مفهوم الأعداد الأولية"],
    },
    "اللغة العربية": {
      "قواعد اللغة": ["الإعراب والبناء", "الجملة الفعلية والاسمية", "الأساليب: النفي والاستفهام والتعجب", "الحال والتمييز والمفاعيل"],
      "النصوص الأدبية": ["تحديد الفكرة الرئيسية والأفكار الفرعية", "شرح المفردات والتراكيب", "تحليل الأسلوب: خصائص الخطاب والجماليات"],
      "التعبير والإنشاء": ["بناء فقرة وصفية أو سردية أو حجاجية", "تحرير إنشاء موجّه أو حر", "ربط الأفكار واستخدام الروابط المنطقية"],
      "البلاغة": ["الاستعارة والتشبيه والكناية", "التورية والجناس والطباق", "تحليل الصور البيانية"],
    },
    "الفيزياء والكيمياء": {
      "المادة وتحولاتها": ["الحالات الثلاث للمادة وتحولاتها", "الخصائص الفيزيائية والكيميائية للمادة", "الكتلة والحجم والكثافة وقياسها"],
      "الكهرباء الساكنة": ["الشحنات الكهربائية وقانون كولوم", "المجال الكهربائي والجهد الكهربائي"],
      "الضوء والأبصار": ["قوانين الانعكاس والانكسار", "المرايا والعدسات وتكوين الصور"],
    },
    "التاريخ والجغرافيا": {
      "تاريخ المغرب": ["الحضارة الإسلامية في المغرب", "الحماية والاستقلال", "مراحل التاريخ المغربي"],
      "الجغرافيا الاقتصادية": ["الموارد الطبيعية والاقتصاد", "الديموغرافيا والتوزيع السكاني", "التنمية والتهيئة الترابية"],
    },
  },
  tc: {
    "الرياضيات": {
      "الدوال العددية": [
        "تعريف مفهوم الدالة العددية (الاقتران)", "مجال تعريف الدالة Df",
        "حساب صورة عدد: f(a)", "إيجاد السوابق: حل f(x) = k",
        "جدول القيم وبناء التمثيل البياني", "قراءة التمثيل البياني وتفسير نقاطه",
        "جدول تغيرات الدالة (تصاعد / تناقص / نهاية عظمى/صغرى)",
        "الدالة الخطية f(x)=ax+b", "الدالة التآلفية والتربيعية: خصائصها ومنحناها",
      ],
      "المشتقات": [
        "تعريف المشتقة كحد نسبة تفاضلية", "قواعد الاشتقاق: الجمع والطرح والضرب والقسمة",
        "مشتقة الدوال الأساسية (التربيعية، الكسرية، الجذرية)",
        "تطبيق المشتقة: جدول إشارة وجدول تغيرات الدالة",
        "الدراسة الكاملة لدالة", "النهايات في ما لا نهاية والنهايات الجانبية",
      ],
      "المثلثية": [
        "قياس الزوايا بالراديان والتحويل", "الدائرة المثلثية",
        "جيب وجيب التمام والظل: التعريف والقيم الخاصة",
        "العلاقات الأساسية: sin²+cos²=1 وغيرها",
        "المعادلات المثلثية الأساسية", "خصائص الدوال المثلثية: دورية، رسم البيان",
      ],
      "هندسة فضائية": [
        "الاستقامية وعدم الاستقامية في الفضاء",
        "الأوضاع النسبية للمستقيمات والمستويات",
        "التعامد والتوازي في الفضاء", "مسقط نقطة على مستوى",
        "حساب مساحات وأحجام متعددات السطوح",
      ],
      "الإحصاء والاحتمالات": [
        "الوسط الحسابي والتباين والانحراف المعياري",
        "التمثيلات البيانية الإحصائية وقراءتها",
        "مفهوم الاحتمال وقواعده الأساسية", "الأحداث المتكاملة والمتنافية",
      ],
    },
    "الفيزياء والكيمياء": {
      "ميكانيك نيوتن": [
        "قوانين نيوتن الثلاثة", "قانون الجذب العام",
        "الحركة المنتظمة والمتسارعة: المعادلات", "الطاقة الحركية والكامنة والميكانيكية",
        "مبدأ حفظ الطاقة الميكانيكية",
      ],
      "الكهرباء والدوائر": [
        "قانون أوم: U=RI", "الدوائر المتسلسلة والمتوازية",
        "قوانين كيرشهوف", "الاستطاعة الكهربائية P=UI",
      ],
      "الكيمياء العضوية المدخل": [
        "العائلات الوظيفية: الكحولات، الألدهيدات، الكيتونات، الحموض",
        "التسمية الممنهجة IUPAC", "تفاعلات التأكسد والاختزال",
      ],
    },
    "اللغة العربية": {
      "الأجناس الأدبية": ["خصائص الشعر والنثر والمقامة والمسرحية", "تحليل النص الأدبي", "التحقيب والمدارس الأدبية"],
      "قواعد متقدمة": ["المفعولات الخمس وإعرابها", "أسماء الأفعال والأصوات", "الحروف وعملها في الجملة", "التوابع: النعت والعطف والبدل والتوكيد"],
      "التعبير الكتابي": ["بناء مقال أدبي أو نقدي", "خطاطة المقال: المقدمة والعرض والخاتمة", "أدوات الحجاج والتحليل"],
    },
    "علوم الحياة والأرض": {
      "الوراثة والخلية": ["الانقسام الخيطي والاختزالي", "تركيب الكروموزوم والحمض النووي DNA", "دورة الخلية"],
      "الجيولوجيا الخارجية": ["عوامل التعرية والتجوية", "دورة الصخور", "الأحواض الرسوبية وتشكّل الطبقات"],
    },
    "التاريخ والجغرافيا": {
      "الحرب العالمية والعلاقات الدولية": ["أسباب الحربين العالميتين ونتائجهما", "الحرب الباردة وتداعياتها", "المنظمات الدولية"],
      "البيئة والتنمية": ["التنمية المستدامة", "التغير المناخي والانعكاسات", "السياسات البيئية في المغرب"],
    },
  },
  bac1: {
    "الرياضيات": {
      "التفاضل والتكامل": [
        "الاشتقاق: قواعد متقدمة ومشتقة الدالة المركبة",
        "الدراسة الكاملة للدالة: النطاق والنهايات والتغيرات والبيان",
        "التكامل المحدد وتفسيره الهندسي (المساحة)", "التكامل غير المحدد وقواعده",
        "تطبيقات التكامل: المساحات والأحجام",
      ],
      "اللوغاريتم والأسي": [
        "الدالة الأسية e^x وخصائصها", "اللوغاريتم الطبيعي ln(x) وخصائصه",
        "العلاقات بين الأسي واللوغاريتم: ln(e^x)=x",
        "حل المعادلات الأسية واللوغاريتمية",
        "تطبيقات: النمو والتناقص الأسي في البيولوجيا والفيزياء",
      ],
      "المتتاليات": ["المتتالية الحسابية والهندسية", "الحد العام Un والمجموع Sn", "المتتاليات المعرفة بالتكرار: دراسة التقارب"],
      "الاحتمالات": ["الفضاء الاحتمالي والأحداث", "الاحتمال الشرطي", "المتغير العشوائي المنفصل والمنتظم"],
    },
    "الفلسفة": {
      "الإنسان والتفكير": ["العقل والحواس كمصادر للمعرفة", "قدرة العقل على بلوغ الحقيقة", "العقلانية والتجريبية"],
      "المعرفة والحقيقة": ["الشك المنهجي عند ديكارت", "المنهج العلمي والتجريب", "نظرية الحقيقة المطابقة والتماسك والنفعية"],
      "السياسة والمجتمع": ["الدولة والسلطة والشرعية", "العقد الاجتماعي عند روسو وهوبز", "الحرية والمسؤولية"],
    },
    "الفيزياء والكيمياء": {
      "الميكانيك الكلاسيكي": ["قوانين نيوتن التطبيقية", "ديناميكيا الدوران", "الطاقة الميكانيكية والعمل والاستطاعة"],
      "الكيمياء العضوية": ["تفاعلات الاستبدال والانضمام والتحليل", "الكيمياء العضوية الوظيفية", "تقنيات المعايرة"],
    },
    "التاريخ والجغرافيا": {
      "العولمة": ["مؤشرات العولمة الاقتصادية والثقافية", "التجارة الدولية والشركات المتعددة الجنسيات", "المغرب في الاقتصاد العالمي"],
      "جغرافيا المغرب": ["الموارد الطبيعية والطاقة", "الديموغرافيا والتهيئة الترابية", "التنمية الإقليمية والاختلالات"],
    },
  },
  bac2: {
    "الرياضيات": {
      "الأعداد المركبة": [
        "الشكل الجبري وعمليات الجمع والضرب",
        "المعامل والحجة: الشكل المثلثي والأسي",
        "صيغة موافر: e^(iθ)", "حل معادلات بالأعداد المركبة",
        "التحويلات الهندسية والأعداد المركبة",
      ],
      "التكامل المتقدم": ["طرق التكامل: التجزيء والتعويض والتجزئة", "التكامل المحدد وتطبيقاته في المساحات والأحجام", "التكامل بالأجزاء"],
      "الاحتمالات المتقدمة": ["التوزيع الثنائي b(n,p)", "التوزيع الطبيعي N(μ,σ)", "فاصل الثقة"],
    },
    "الفلسفة": {
      "نظرية المعرفة": ["الإبستيمولوجيا: موضوعها وإشكالاتها", "العلم وأسسه المعرفية", "الحقيقة العلمية والنسبية"],
      "فلسفة الفن": ["مفهوم الجمال والمحاكاة", "الفن والحقيقة والقيم", "الجماليات الحديثة"],
      "الأخلاق والسياسة": ["الواجب الأخلاقي عند كانط", "النفعية عند ميل", "الدولة والعدالة والحرية"],
    },
  },
};

// ── Grade context injected into prompt ────────────────────────────────────────

const GRADE_CONTEXT: Record<ExamGradeLevel, string> = {
  middle:  "المستوى: إعدادي (collège) — المغرب. نوع التقييم: الفرض المحروس والامتحان الموحد الإقليمي.\n",
  tc:      "المستوى: جذع مشترك (tronc commun) — ثانوي المغرب. نوع التقييم: الفرض المحروس والامتحان الموحد الإقليمي.\n",
  bac1:    "المستوى: السنة الأولى بكالوريا (1ère Bac) — المغرب. نوع التقييم: الفرض المحروس والامتحان الموحد الجهوي.\n",
  bac2:    "المستوى: الثانية بكالوريا (2ème Bac) — المغرب. نوع التقييم: الامتحان الوطني الموحد (الباكالوريا).\n",
  primary: "",
  unknown: "",
};

// ── Plan template ─────────────────────────────────────────────────────────────

function buildPlanTemplate(
  level:       ExamGradeLevel,
  subject:     string,
  topic:       string,
  examType:    string,
  weakAreas:   string[],
  avgScore:    number | null,
) {
  const weakSection = weakAreas.length > 0
    ? `نقاط الضعف المرصودة فعلياً من سجل الطالب: ${weakAreas.join("، ")}\n`
    : "";

  const scoreSection = avgScore !== null
    ? `معدل الطالب الحالي: ${avgScore}% — ${
        avgScore < 50 ? "مستوى ضعيف: يحتاج تركيزاً مكثفاً على الأساسيات قبل التمارين المتقدمة"
        : avgScore < 70 ? "مستوى متوسط: التركيز على التمارين المتوسطة وسد الثغرات"
        : "مستوى جيد: التركيز على التمارين المتقدمة والأخطاء الدقيقة"
      }.\n`
    : "";

  // Inject topic-specific concept list if available
  const concepts = topic ? (TOPIC_CONCEPTS[level]?.[subject]?.[topic] ?? []) : [];
  const conceptSection = concepts.length > 0
    ? `\nالمفاهيم المحورية التي يجب أن تُغطَّى حصرياً في هذا المحور:\n${concepts.map(c => `• ${c}`).join("\n")}\n\nتحذير للنموذج: كل تمرين ومثال يجب أن يرتبط بأحد هذه المفاهيم فقط.\n`
    : "";

  const topicInstruction = topic
    ? `المحور المختار: ${topic}${conceptSection}`
    : "لم يُختر محور محدد — أنتج خطة تشمل جميع محاور المادة بالتساوي.\n";

  const difficultyInstruction = avgScore !== null && avgScore < 50
    ? "ابدأ بتمرين أساسي جداً ثم توسط ثم متقدم."
    : avgScore !== null && avgScore >= 70
    ? "ركز على التمارين المتوسطة والمتقدمة مع تمرين تركيبي."
    : "تدرج من سهل إلى متوسط إلى متقدم.";

  return `${GRADE_CONTEXT[level]}المادة: ${subject}
${topicInstruction}
نوع الامتحان المستهدف: ${examType}
${weakSection}${scoreSection}
أنتج خطة استعداد كاملة ومخصصة للمحور المحدد بالترتيب التالي حصرياً:

## نقاط الضعف المحتملة
${weakAreas.length > 0
  ? `ابدأ بالنقاط المرصودة أعلاه (${weakAreas.join("، ")})، ثم أضف المفاهيم التي يخطئ فيها الطلاب عادةً في ${topic || subject}.`
  : `المفاهيم التي يخطئ فيها الطلاب عادةً في ${topic || subject} بمستوى ${LEVEL_LABEL[level] || "الطالب"}.`}
اذكر الخطأ الشائع وكيفية تجنبه.

## خطة مراجعة قصيرة
مقسمة على 3–5 أيام أو محاور فرعية — عملية وقابلة للتطبيق. خصصها للمحور${topic ? ` "${topic}"` : ""} ومستوى ${LEVEL_LABEL[level] || "الطالب"}.

## نموذج فرض مصغر
فرض محروس مصغر من 3 تمارين${topic ? ` من محور "${topic}"` : ""} بالتدرج:
- التمرين 1 (سهل): نص التمرين + الحل الكامل
- التمرين 2 (متوسط): نص التمرين + الحل الكامل
- التمرين 3 (متقدم): نص التمرين + الحل الكامل
${difficultyInstruction}

## تمارين مقترحة إضافية مع الحلول
تمرينان إضافيان يحاكيان أسلوب ${examType} مع الحلول الكاملة.

## نصائح للفرض والامتحان
إدارة الوقت حسب أسلوب ${examType}، ترتيب الإجابات، الأخطاء الشائعة، ما يجب تجنبه.

## مستوى التوقعات لـ${LEVEL_LABEL[level] || "هذا المستوى"}
ما الذي يُتوقع تحديداً من طالب ${LEVEL_LABEL[level] || ""} في ${subject}${topic ? ` — محور ${topic}` : ""}: المفاهيم الإلزامية، نوع الأسئلة، مستوى الصعوبة.`;
}

// ── Types ─────────────────────────────────────────────────────────────────────

interface ProgressItem { status: string; lesson?: { titleAr?: string } }

// ── Page ───────────────────────────────────────────────────────────────────────

export default function ExamPredictionPage() {
  const [subject,    setSubject]    = useState("");
  const [topic,      setTopic]      = useState("");
  const [concern,    setConcern]    = useState("");
  const [output,     setOutput]     = useState("");
  const [running,    setRunning]    = useState(false);
  const [copied,     setCopied]     = useState(false);
  const [error,      setError]      = useState("");

  const [level,      setLevel]      = useState<ExamGradeLevel>("unknown");
  const [avgScore,   setAvgScore]   = useState<number | null>(null);
  const [weakAreas,  setWeakAreas]  = useState<string[]>([]);

  useEffect(() => {
    async function load() {
      try {
        const cr = await fetch("/api/children").then(r => r.json()).catch(() => ({ success: false }));
        if (!cr.success || !cr.data?.[0]) return;
        const child = cr.data[0] as { id: string; grade?: { slug?: string } };
        const detectedLevel = detectExamGradeLevel(child.grade?.slug);
        setLevel(detectedLevel);

        const [sumRes, progRes] = await Promise.all([
          fetch(`/api/analytics/learning?childId=${child.id}`).then(r => r.json()).catch(() => ({})),
          fetch(`/api/progress?childId=${child.id}`).then(r => r.json()).catch(() => ({})),
        ]);

        if (sumRes.success && sumRes.data?.averageScore != null) {
          setAvgScore(sumRes.data.averageScore as number);
        }
        if (progRes.success && Array.isArray(progRes.data)) {
          const weak = (progRes.data as ProgressItem[])
            .filter(p => p.status === "needs_review" && p.lesson?.titleAr)
            .map(p => p.lesson!.titleAr as string)
            .slice(0, 5);
          setWeakAreas(weak);
        }
      } catch { /* silent */ }
    }
    void load();
  }, []);

  const subjects      = SUBJECTS[level] ?? SUBJECTS.unknown;
  const topicOptions: string[] = (subject ? TOPICS[level as keyof typeof TOPICS]?.[subject] : undefined) ?? [];
  const examType      = EXAM_TYPE[level];
  const levelLabel    = LEVEL_LABEL[level];

  function pickSubject(s: string) {
    setSubject(s);
    setTopic("");
    setOutput("");
    setError("");
  }

  async function generate() {
    if (!subject.trim() || running) return;
    setOutput("");
    setError("");
    setRunning(true);

    const prompt = buildPlanTemplate(level, subject, topic, examType, weakAreas, avgScore)
      + (concern.trim() ? `\n\nملاحظة إضافية من الطالب: ${concern.trim()}` : "");

    try {
      const res = await fetch("/api/ai/exam-prep", {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify({ prompt }),
      });

      if (!res.ok) {
        const err = await res.json().catch(() => ({})) as { message?: string };
        setError(err.message ?? "حدث خطأ غير متوقع. حاول مرة أخرى.");
        setRunning(false);
        return;
      }

      const reader  = res.body!.getReader();
      const decoder = new TextDecoder();
      let   buf     = "";
      let   live    = "";

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buf += decoder.decode(value, { stream: true });
        const lines = buf.split("\n");
        buf = lines.pop() ?? "";
        for (const line of lines) {
          if (!line.startsWith("data: ")) continue;
          try {
            const ev = JSON.parse(line.slice(6)) as Record<string, unknown>;
            if (ev.event === "delta") {
              live += (ev.delta ?? ev.text) as string;
              setOutput(live);
            } else if (ev.event === "end") {
              if (!live) setOutput((ev.finalOutput as string) ?? "");
            } else if (ev.event === "error") {
              setError((ev.message as string) ?? "حدث خطأ أثناء تشغيل الوكلاء.");
            }
          } catch { /* ignore */ }
        }
      }
    } catch {
      setError("تعذّر الاتصال بالخادم. تحقق من الاتصال بالإنترنت وأعد المحاولة.");
    } finally {
      setRunning(false);
    }
  }

  async function copy() {
    await navigator.clipboard.writeText(output);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  }

  function reset() {
    setOutput("");
    setConcern("");
    setSubject("");
    setTopic("");
    setError("");
  }

  const hasOutput = Boolean(output);

  return (
    <div className="mx-auto max-w-3xl space-y-6" dir="rtl">

      {/* ── Header ── */}
      <div>
        <h1 className="text-2xl font-black flex items-center gap-3">
          <span className="w-10 h-10 rounded-2xl bg-gradient-to-br from-orange-500 to-primary flex items-center justify-center text-white text-lg">
            🎯
          </span>
          استعداد للامتحان
          {levelLabel && (
            <span className="text-sm font-medium text-muted-foreground bg-secondary px-2 py-0.5 rounded-lg">
              {levelLabel}
            </span>
          )}
        </h1>
        <p className="mt-1 text-sm text-muted-foreground">
          {examType
            ? `خطة مراجعة مخصصة لـ${examType} — تمارين على أسلوب الامتحان الحقيقي`
            : "اختر المادة وسيُعدّ لك خطة مراجعة مخصصة مع تمارين ونصائح حسب مستواك"}
        </p>
      </div>

      {/* ── Progress context badges ── */}
      {(weakAreas.length > 0 || avgScore !== null) && (
        <div className="flex flex-wrap gap-2 text-xs">
          {avgScore !== null && (
            <span className={cn(
              "px-2.5 py-1 rounded-full border font-medium",
              avgScore >= 70 ? "bg-emerald-50 border-emerald-200 text-emerald-700"
                : avgScore >= 50 ? "bg-amber-50 border-amber-200 text-amber-700"
                : "bg-red-50 border-red-200 text-red-700"
            )}>
              معدلك {avgScore}%
            </span>
          )}
          {weakAreas.map((w) => (
            <span key={w} className="px-2.5 py-1 rounded-full bg-orange-50 border border-orange-200 text-orange-700">
              ⚠ {w}
            </span>
          ))}
        </div>
      )}

      {/* ── Subject picker ── */}
      <div className="space-y-2">
        <p className="text-[10px] font-semibold uppercase tracking-widest text-muted-foreground/60">اختر المادة</p>
        <div className="flex flex-wrap gap-2">
          {subjects.map((s) => (
            <button
              key={s}
              onClick={() => pickSubject(s)}
              type="button"
              className={cn(
                "px-3 py-1.5 rounded-xl text-sm border transition-colors",
                subject === s
                  ? "bg-primary text-white border-primary"
                  : "border-border hover:border-primary hover:text-primary"
              )}
            >
              {s}
            </button>
          ))}
        </div>
      </div>

      {/* ── Topic hint when subject selected but no topic yet ── */}
      {topicOptions.length > 0 && !topic && !running && (
        <div className="flex items-start gap-2 rounded-xl bg-amber-50 border border-amber-200 px-3 py-2 text-xs text-amber-700">
          <span className="shrink-0 mt-0.5">💡</span>
          <span>اختر محوراً للحصول على خطة دقيقة بتمارين خاصة بالموضوع — بدون اختيار المحور ستكون الخطة عامة.</span>
        </div>
      )}

      {/* ── Topic chips (appear after subject selected) ── */}
      {topicOptions.length > 0 && (
        <div className="space-y-2">
          <p className="text-[10px] font-semibold uppercase tracking-widest text-muted-foreground/60">
            المحور / الوحدة (اختياري)
          </p>
          <div className="flex flex-wrap gap-2">
            {topicOptions.map((t) => (
              <button
                key={t}
                onClick={() => setTopic(prev => prev === t ? "" : t)}
                type="button"
                className={cn(
                  "px-3 py-1.5 rounded-xl text-sm border transition-colors",
                  topic === t
                    ? "bg-orange-500 text-white border-orange-500"
                    : "border-border hover:border-orange-400 hover:text-orange-600"
                )}
              >
                {t}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* ── Optional concern ── */}
      <div className="space-y-2">
        <p className="text-[10px] font-semibold uppercase tracking-widest text-muted-foreground/60">ملاحظة إضافية (اختياري)</p>
        <textarea
          value={concern}
          onChange={(e) => setConcern(e.target.value)}
          onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); void generate(); } }}
          placeholder="مثال: الامتحان بعد أسبوع، أجد صعوبة في التمارين المركبة، أريد التركيز على الجزء الثاني..."
          rows={2}
          disabled={running}
          className="w-full resize-none rounded-2xl border border-border bg-background px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary disabled:opacity-60 transition-shadow"
        />
      </div>

      {/* ── Actions ── */}
      <div className="flex gap-3">
        <Button
          onClick={() => void generate()}
          disabled={!subject.trim() || running}
          variant={running ? "outline" : "default"}
          className="rounded-2xl px-6 py-3 h-auto"
        >
          {running ? (
            <span className="flex items-center gap-2">
              <span className="h-2 w-2 animate-ping rounded-full bg-primary" />
              يُعدّ الخطة...
            </span>
          ) : (
            <span className="flex items-center gap-2">
              <Send className="h-4 w-4" />
              أعدّ لي خطة المراجعة
            </span>
          )}
        </Button>
        {hasOutput && (
          <Button onClick={reset} variant="ghost" size="sm" className="rounded-xl">
            <RotateCcw className="h-4 w-4" />
          </Button>
        )}
      </div>

      {/* ── Error ── */}
      {error && (
        <div className="flex items-start gap-3 rounded-2xl border border-red-200 bg-red-50 px-4 py-3">
          <AlertCircle className="w-4 h-4 text-red-500 mt-0.5 shrink-0" />
          <p className="text-sm text-red-700 leading-6">{error}</p>
        </div>
      )}

      {/* ── Output ── */}
      {(hasOutput || running) && (
        <div className="overflow-hidden rounded-2xl border border-primary/20 bg-primary/5">
          <div className="flex items-center justify-between border-b border-primary/10 px-5 py-3">
            <div className="flex items-center gap-2">
              <CheckCircle className="h-4 w-4 text-primary" />
              <span className="text-sm font-semibold text-primary">خطة الاستعداد</span>
              {subject && (
                <span className="text-xs text-muted-foreground">— {subject}{topic ? ` / ${topic}` : ""}</span>
              )}
            </div>
            {hasOutput && (
              <button
                onClick={() => void copy()}
                type="button"
                className="flex items-center gap-1.5 text-xs text-muted-foreground hover:text-foreground transition-colors"
              >
                <Copy className="h-3.5 w-3.5" />
                {copied ? "تم النسخ ✓" : "نسخ"}
              </button>
            )}
          </div>
          <div className={cn(
            "min-h-32 max-h-[600px] overflow-y-auto px-5 py-4 text-sm leading-8 whitespace-pre-wrap",
            !output && "text-muted-foreground"
          )}>
            {output || "يُعدّ الخطة…"}
          </div>
        </div>
      )}

      {/* ── Empty state ── */}
      {!hasOutput && !running && !error && (
        <div className="py-12 text-center text-muted-foreground">
          <div className="mb-4 text-5xl">🎯</div>
          <p className="font-semibold">استعداد ذكي للامتحان</p>
          <p className="mx-auto mt-2 max-w-sm text-sm leading-7">
            اختر المادة أعلاه للحصول على خطة مراجعة مخصصة مع تمارين على أسلوب
            {examType ? ` ${examType}` : " الامتحان الحقيقي"}.
            لا يُحفظ شيء في قاعدة البيانات.
          </p>
        </div>
      )}

    </div>
  );
}

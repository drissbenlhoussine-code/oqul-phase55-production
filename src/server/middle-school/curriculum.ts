import type { MiddleSchoolCompetency, MiddleSchoolGrade, MiddleSchoolSubject } from "./types";

export const middleSchoolSubjects: Array<{ id: MiddleSchoolSubject; titleAr: string; titleFr: string; icon: string }> = [
  { id: "math", titleAr: "الرياضيات", titleFr: "Mathématiques", icon: "∑" },
  { id: "physics_chemistry", titleAr: "الفيزياء والكيمياء", titleFr: "Physique-Chimie", icon: "⚡" },
  { id: "life_earth_sciences", titleAr: "علوم الحياة والأرض", titleFr: "SVT", icon: "🧬" },
  { id: "arabic", titleAr: "اللغة العربية", titleFr: "Arabe", icon: "ض" },
  { id: "french", titleAr: "الفرنسية", titleFr: "Français", icon: "Fr" },
  { id: "social_studies", titleAr: "الاجتماعيات", titleFr: "Histoire-Géographie", icon: "🌍" },
];

const byGrade = (grade: MiddleSchoolGrade): MiddleSchoolCompetency[] => [
  {
    id: `${grade}-math-algebra-equations`,
    grade,
    subject: "math",
    titleAr: "التعابير الجبرية والمعادلات",
    titleFr: "Expressions algébriques et équations",
    skill: "استعمال الرموز، تبسيط التعابير، وحل معادلات من الدرجة الأولى بخطوات مبررة.",
    prerequisites: ["العمليات على الأعداد", "الأولوية في الحساب", "مفهوم المجهول"],
    misconceptions: ["تغيير طرف المعادلة دون تغيير الإشارة", "خلط المعامل مع الحد الثابت", "اعتبار x دائمًا يساوي 1"],
    objectives: ["يفهم معنى المتغير", "يبسط تعبيرًا جبريًا", "يحل معادلة بسيطة", "يشرح سبب كل خطوة"],
    lessonSeeds: ["قصة ميزان متوازن", "ثمن دفاتر وأقلام في مكتبة", "مباراة نقاط بين فريقين"],
    exerciseTypes: ["guided", "interactive", "socratic", "mini_assessment", "remediation"],
  },
  {
    id: `${grade}-math-geometry-core`,
    grade,
    subject: "math",
    titleAr: "الهندسة والبرهان",
    titleFr: "Géométrie et raisonnement",
    skill: "قراءة شكل هندسي، استعمال الخصائص، وبناء برهان قصير ومنظم.",
    prerequisites: ["الزوايا", "المستقيمات", "المثلثات", "القياس"],
    misconceptions: ["الاعتماد على مظهر الرسم فقط", "نسيان ذكر الخاصية المستعملة", "خلط المتوازي مع المتعامد"],
    objectives: ["يحدد المعطيات", "يختار الخاصية المناسبة", "يكتب برهانًا من ثلاث خطوات", "يراجع النتيجة"],
    lessonSeeds: ["خريطة حي مغربي", "ملعب كرة قدم", "تصميم نافذة أو باب"],
    exerciseTypes: ["guided", "interactive", "socratic", "mini_assessment"],
  },
  {
    id: `${grade}-pc-electricity-matter`,
    grade,
    subject: "physics_chemistry",
    titleAr: "الكهرباء والمادة",
    titleFr: "Électricité et matière",
    skill: "فهم الدارة الكهربائية والمادة والتحولات البسيطة باستعمال ملاحظات وتجارب آمنة.",
    prerequisites: ["الملاحظة", "القياس", "السلامة في التجارب"],
    misconceptions: ["الخلط بين التيار والتوتر", "اعتبار المصباح يستهلك التيار كله", "وصف التفاعل دون تمييز المتفاعلات والنواتج"],
    objectives: ["يميز مكونات الدارة", "يفسر نتيجة تجربة", "يستعمل مصطلحات علمية دقيقة", "يربط المفهوم بحياة يومية"],
    lessonSeeds: ["مصباح في غرفة", "بطارية وهاتف", "تغير لون أو غاز في تجربة"],
    exerciseTypes: ["guided", "interactive", "socratic", "remediation"],
  },
  {
    id: `${grade}-svt-living-earth`,
    grade,
    subject: "life_earth_sciences",
    titleAr: "الكائن الحي والبيئة والأرض",
    titleFr: "Vivant, environnement et Terre",
    skill: "تحليل وثائق ورسوم لفهم الخلايا والبيئة والجيولوجيا وجسم الإنسان.",
    prerequisites: ["الملاحظة العلمية", "قراءة رسم مبسط", "المقارنة"],
    misconceptions: ["حفظ أسماء دون وظيفة", "خلط العضو بالخلية", "اعتبار السلسلة الغذائية خطًا ثابتًا دائمًا"],
    objectives: ["يصف بنية ووظيفة", "يفسر علاقة سبب ونتيجة", "يقرأ وثيقة علمية", "يلخص فكرة علمية"],
    lessonSeeds: ["نبات في البيت", "غابة أو بحر مغربي", "رسم خلية مبسط"],
    exerciseTypes: ["guided", "interactive", "mini_assessment", "remediation"],
  },
  {
    id: `${grade}-arabic-text-grammar-writing`,
    grade,
    subject: "arabic",
    titleAr: "النصوص والقواعد والتعبير",
    skill: "فهم نص عربي، استخراج الأفكار، تطبيق قاعدة، وكتابة فقرة واضحة.",
    prerequisites: ["قراءة سليمة", "الجملة الاسمية والفعلية", "الفكرة العامة"],
    misconceptions: ["تلخيص النص بنسخه", "خلط الإعراب بالوظيفة المعنوية", "كتابة فقرة بلا روابط"],
    objectives: ["يحدد الفكرة العامة", "يستخرج حجة أو وصفًا", "يطبق قاعدة نحوية", "يكتب فقرة منظمة"],
    lessonSeeds: ["نص عن المدرسة", "قصة قصيرة", "موضوع عن المواطنة أو البيئة"],
    exerciseTypes: ["guided", "socratic", "interactive", "mini_assessment"],
  },
  {
    id: `${grade}-french-grammar-writing`,
    grade,
    subject: "french",
    titleAr: "الفهم واللغة والكتابة بالفرنسية",
    titleFr: "Compréhension, grammaire et rédaction",
    skill: "Comprendre un texte, conjuguer correctement, organiser une réponse et rédiger un court paragraphe.",
    prerequisites: ["vocabulaire de base", "phrase simple", "présent/passé composé"],
    misconceptions: ["traduction mot à mot", "accord sujet-verbe oublié", "réponse sans justification"],
    objectives: ["comprendre la consigne", "identifier l'idée principale", "corriger une phrase", "rédiger 5 à 8 lignes"],
    lessonSeeds: ["dialogue à l'école", "petite annonce", "texte narratif court"],
    exerciseTypes: ["guided", "interactive", "socratic", "mini_assessment", "remediation"],
  },
  {
    id: `${grade}-social-history-geography-citizenship`,
    grade,
    subject: "social_studies",
    titleAr: "التاريخ والجغرافيا والتربية على المواطنة",
    titleFr: "Histoire, géographie et citoyenneté",
    skill: "قراءة خريطة أو خط زمني أو وثيقة، وربط المفاهيم بالمجتمع المغربي والعالمي.",
    prerequisites: ["الاتجاهات على الخريطة", "الزمن التاريخي", "الفكرة الرئيسية في وثيقة"],
    misconceptions: ["حفظ التواريخ دون سبب", "خلط الظاهرة الطبيعية بالبشرية", "تعريف المواطنة كشعار فقط"],
    objectives: ["يقرأ خريطة", "يرتب أحداثًا", "يفسر ظاهرة", "يقترح سلوكًا مواطنًا"],
    lessonSeeds: ["خريطة المغرب", "مدينة وقرية", "حدث تاريخي مبسط"],
    exerciseTypes: ["guided", "interactive", "mini_assessment", "remediation"],
  },
];

export const middleSchoolCurriculum: Record<MiddleSchoolGrade, MiddleSchoolCompetency[]> = {
  "1AC": byGrade("1AC"),
  "2AC": byGrade("2AC"),
  "3AC": byGrade("3AC"),
};

export function getMiddleSchoolCompetencies(grade: MiddleSchoolGrade, subject?: MiddleSchoolSubject) {
  const list = middleSchoolCurriculum[grade] ?? middleSchoolCurriculum["1AC"];
  return subject ? list.filter((c) => c.subject === subject) : list;
}

export function normalizeMiddleSchoolGrade(level?: number | string | null): MiddleSchoolGrade {
  const raw = String(level ?? "").toLowerCase();
  if (raw.includes("3") || raw.includes("9") || raw.includes("third")) return "3AC";
  if (raw.includes("2") || raw.includes("8") || raw.includes("second")) return "2AC";
  return "1AC";
}

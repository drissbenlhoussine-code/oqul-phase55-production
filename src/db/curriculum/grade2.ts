import type { SubjectData } from "./types";

export const grade2: SubjectData[] = [
  {
    slug: "arabic", titleAr: "اللغة العربية", icon: "BookOpen", color: "#059669", orderIndex: 1,
    units: [
      {
        slug: "nahw-asasi", titleAr: "النحو الأساسي", orderIndex: 1,
        lessons: [
          {
            slug: "mubtada-khabar", titleAr: "المبتدأ والخبر", difficulty: "easy", durationMin: 25,
            objectives: ["تعريف المبتدأ والخبر", "تمييزهما في الجملة الاسمية", "بناء جمل صحيحة"],
            explanation: `الجملة الاسمية تتكون من:\n\n1️⃣ المبتدأ: اسم في بداية الجملة\n"من نتحدث عنه؟"\n\n2️⃣ الخبر: يُكمل المعنى\n"ماذا نقول عنه؟"\n\nأمثلة:\n• البيتُ كبيرٌ ← البيت (م) + كبير (خ)\n• الجوُّ صافٍ ← الجو (م) + صافٍ (خ)\n• المعلمُ طيبٌ ← المعلم (م) + طيب (خ)`,
            vocabulary: [
              { word: "مبتدأ", definition: "الاسم الأول في الجملة — ما نتحدث عنه" },
              { word: "خبر", definition: "ما نقوله عن المبتدأ — يكمل المعنى" },
              { word: "جملة اسمية", definition: "جملة تبدأ باسم وتتكون من مبتدأ وخبر" },
            ],
            examples: [{ text: "الطالبُ مجتهدٌ", note: "الطالب: مبتدأ | مجتهد: خبر" }, { text: "المغربُ جميلٌ", note: "المغرب: مبتدأ | جميل: خبر" }],
            summary: "مبتدأ = من نتحدث عنه. خبر = ما نقوله عنه. معاً يُكوّنان الجملة الاسمية.",
            exercises: [
              { type: "mcq", question: "في جملة 'الطالبُ مجتهدٌ' المبتدأ هو:", options: ["مجتهد", "الطالب", "في", "هو"], correctAnswer: "الطالب", explanation: "المبتدأ هو الاسم الأول الذي نتحدث عنه = الطالب", points: 10 },
              { type: "mcq", question: "الخبر في 'الكتابُ مفيدٌ' هو:", options: ["الكتاب", "مفيد", "في", "هو"], correctAnswer: "مفيد", explanation: "الخبر هو ما نقوله عن المبتدأ = مفيد", points: 10 },
              { type: "true_false", question: "الجملة الاسمية تبدأ باسم", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الجملة الاسمية تبدأ باسم (المبتدأ)", points: 10 },
              { type: "fill_blank", question: "أكمل: المدرسةُ ___ (اختر خبراً مناسباً)", correctAnswer: "جميلة", explanation: "المدرسة جميلة — جملة اسمية مفيدة", points: 15 },
              { type: "mcq", question: "في جملة 'السماءُ زرقاءُ' — ما الخبر؟", options: ["السماء", "زرقاء", "في", "هي"], correctAnswer: "زرقاء", explanation: "زرقاء هو الخبر — يخبرنا عن لون السماء", points: 10 },
            ],
          },
          {
            slug: "mufrad-jamaa", titleAr: "المفرد والجمع", difficulty: "easy", durationMin: 25,
            objectives: ["التمييز بين المفرد والجمع", "جمع المذكر والمؤنث السالم", "جمع التكسير الشائع"],
            explanation: `المفرد: يدل على واحد\nالجمع: يدل على أكثر من اثنين\n\nأنواع الجمع:\n\n1️⃣ جمع المذكر السالم: نضيف (ون/ين)\n   مُعلِّم → مُعلِّمون / مُعلِّمين\n\n2️⃣ جمع المؤنث السالم: نضيف (ات)\n   مُعلِّمة → مُعلِّمات\n   سيارة → سيارات\n\n3️⃣ جمع التكسير: يتغير شكل الكلمة\n   كتاب → كُتُب\n   قلم → أقلام\n   باب → أبواب\n   طالب → طلاب`,
            vocabulary: [
              { word: "مفرد", definition: "كلمة تدل على شيء واحد أو شخص واحد" },
              { word: "جمع", definition: "كلمة تدل على أكثر من اثنين" },
              { word: "جمع التكسير", definition: "جمع يتغير فيه شكل الكلمة كلياً" },
            ],
            examples: [{ text: "طالب → طلاب (جمع تكسير)", note: "تغير شكل الكلمة" }, { text: "لاعبة → لاعبات (جمع مؤنث سالم)", note: "إضافة (ات)" }],
            summary: "مفرد = واحد. جمع = أكثر من اثنين. ثلاثة أنواع: مذكر سالم (+ون/ين) | مؤنث سالم (+ات) | تكسير (تغيير الشكل).",
            exercises: [
              { type: "mcq", question: "جمع كلمة 'كتاب':", options: ["كتابون", "كتابات", "كتب", "كتابات"], correctAnswer: "كتب", explanation: "كتاب → كُتُب جمع تكسير", points: 10 },
              { type: "mcq", question: "جمع 'مُعلِّمة':", options: ["مُعلِّمون", "مُعلِّمات", "مُعلِّم", "تعليم"], correctAnswer: "مُعلِّمات", explanation: "مُعلِّمة → مُعلِّمات جمع مؤنث سالم (+ات)", points: 10 },
              { type: "true_false", question: "كلمة 'طلاب' مفرد", options: ["صحيح", "خطأ"], correctAnswer: "خطأ", explanation: "طلاب جمع تكسير — مفردها: طالب", points: 10 },
              { type: "fill_blank", question: "قلم → أ___", correctAnswer: "قلام", explanation: "قلم → أقلام جمع تكسير", points: 15 },
              { type: "mcq", question: "جمع 'مُعلِّم' (مذكر):", options: ["مُعلِّمات", "مُعلِّمون", "تعليم", "مُعلِّمة"], correctAnswer: "مُعلِّمون", explanation: "مُعلِّم → مُعلِّمون جمع مذكر سالم (+ون)", points: 10 },
            ],
          },
          {
            slug: "fail-fail", titleAr: "الفعل والفاعل والمفعول به", difficulty: "medium", durationMin: 25,
            objectives: ["تعريف الفعل والفاعل والمفعول به", "تمييزهما في الجمل", "بناء جمل فعلية"],
            explanation: `الجملة الفعلية تتكون من:\n\n1️⃣ الفعل: العمل الذي يحدث\n(كتب، أكل، لعب، قرأ)\n\n2️⃣ الفاعل: من قام بالفعل\n"من الذي فعل؟"\n\n3️⃣ المفعول به: ما وقع عليه الفعل\n"ماذا فعل به؟"\n\nمثال:\nكتبَ أحمدُ الدرسَ\n↑فعل  ↑فاعل  ↑مفعول به`,
            vocabulary: [
              { word: "فعل", definition: "كلمة تدل على حدث أو عمل: أكل، كتب، لعب" },
              { word: "فاعل", definition: "من قام بالفعل — يأتي بعد الفعل" },
              { word: "مفعول به", definition: "ما وقع عليه الفعل" },
            ],
            examples: [{ text: "قرأَ محمدٌ القصةَ", note: "قرأ(فعل) محمد(فاعل) القصة(مفعول به)" }, { text: "أكلَ الطفلُ التفاحةَ", note: "أكل(فعل) الطفل(فاعل) التفاحة(مفعول به)" }],
            summary: "الجملة الفعلية: فعل + فاعل + مفعول به. الفاعل من فعل. المفعول به ما تأثر بالفعل.",
            exercises: [
              { type: "mcq", question: "في 'أكلَ يوسفُ التفاحةَ' — الفاعل هو:", options: ["أكل", "يوسف", "التفاحة", "هو"], correctAnswer: "يوسف", explanation: "يوسف هو الذي أكل — الفاعل", points: 10 },
              { type: "mcq", question: "المفعول به في 'كتبَ الطالبُ الدرسَ':", options: ["كتب", "الطالب", "الدرس", "في"], correctAnswer: "الدرس", explanation: "الدرس هو الذي كُتب — المفعول به", points: 10 },
              { type: "true_false", question: "الفاعل هو من قام بالفعل", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الفاعل دائماً هو من قام بالعمل", points: 10 },
              { type: "fill_blank", question: "لعبَ ___ الكرةَ (الفاعل: أحمد)", correctAnswer: "أحمدُ", explanation: "لعب أحمدُ الكرةَ — أحمد هو الفاعل", points: 15 },
            ],
          },
        ],
      },
      {
        slug: "qiraa", titleAr: "القراءة والنصوص", orderIndex: 2,
        lessons: [
          {
            slug: "qissa-asad-faara", titleAr: "قصة الأسد والفأرة", difficulty: "easy", durationMin: 20,
            objectives: ["قراءة قصة بفهم", "استخراج الشخصيات والأحداث", "الدرس المستفاد"],
            explanation: `الأسد والفأرة 🦁🐭\n\nذاتَ يومٍ، نامَ الأسدُ الكبيرُ في الغابة.\nجاءت فأرةٌ صغيرةٌ تلعب فوقه فأيقظته!\nغضبَ الأسدُ وأمسكَ الفأرةَ.\nقالت الفأرة: "اعفُ عني! سأساعدك يوماً ما!"\nضحكَ الأسدُ وأطلقها.\n\nبعد أيام، وقعَ الأسدُ في شبكة صياد!\nسمعت الفأرةُ صرخاته فجاءت وقطعت الشبكة!\nنجا الأسدُ بفضل الفأرة الصغيرة.\n\n🌟 الدرس: لا تحتقر أحداً — المعروف لا يضيع.`,
            vocabulary: [
              { word: "احتقار", definition: "النظر إلى شخص ما بأنه أقل منك — وهو خطأ" },
              { word: "شبكة", definition: "أداة يصطاد بها الصياد" },
              { word: "معروف", definition: "عمل طيب تفعله لشخص آخر" },
            ],
            examples: [{ text: "الأسد ضحك من الفأرة", note: "خطأ الأسد — الاحتقار" }, { text: "الفأرة أنقذت الأسد", note: "النتيجة: المعروف لا يضيع" }],
            summary: "لا تستهن بأحد مهما كان صغيراً — الفأرة أنقذت الأسد! المعروف يُرد.",
            exercises: [
              { type: "mcq", question: "من أيقظ الأسد من نومه؟", options: ["صياد", "أسد آخر", "فأرة صغيرة", "طائر"], correctAnswer: "فأرة صغيرة", explanation: "الفأرة الصغيرة لعبت فوق الأسد فأيقظته", points: 10 },
              { type: "mcq", question: "كيف ساعدت الفأرة الأسد؟", options: ["أطعمته", "قطعت الشبكة", "هربت", "صرخت"], correctAnswer: "قطعت الشبكة", explanation: "الفأرة قطعت الشبكة التي أمسك بها الصياد الأسد", points: 10 },
              { type: "mcq", question: "الدرس المستفاد من القصة:", options: ["الأسد أقوى", "لا تحتقر أحداً", "الفأر خطر", "النوم مضر"], correctAnswer: "لا تحتقر أحداً", explanation: "المعروف لا يضيع — حتى الصغير يمكن أن يساعد الكبير", points: 15 },
              { type: "true_false", question: "الأسد أطلق الفأرة في البداية", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الأسد عفا عن الفأرة وهذا أدى إلى نجاته لاحقاً", points: 10 },
            ],
          },
        ],
      },
    ],
  },

  {
    slug: "math", titleAr: "الرياضيات", icon: "Calculator", color: "#2563eb", orderIndex: 2,
    units: [
      {
        slug: "aaadaad-20-100", titleAr: "الأعداد حتى 100", orderIndex: 1,
        lessons: [
          {
            slug: "aaadaad-20-50", titleAr: "الأعداد من 20 إلى 50", difficulty: "easy", durationMin: 20,
            objectives: ["قراءة الأعداد 20-50", "كتابتها أرقاماً وكلمات", "ترتيبها"],
            explanation: `الأعداد من 20 إلى 50:\n\n20 = عشرون\n21 = واحد وعشرون\n22 = اثنان وعشرون\n30 = ثلاثون\n40 = أربعون\n50 = خمسون\n\nالمئة = 100\nالعقود: 20، 30، 40، 50، 60، 70، 80، 90، 100\n\nللكتابة: الآحاد + "و" + العقد\n35 = خمسة وثلاثون`,
            vocabulary: [
              { word: "عقود", definition: "الأعداد 20، 30، 40، ... 90 تسمى العقود" },
              { word: "آحاد", definition: "الأرقام من 1 إلى 9 في خانة الآحاد" },
              { word: "عشرات", definition: "مرتبة يساوي الرقم فيها 10 مرات قيمته" },
            ],
            examples: [{ text: "35 = خمسة وثلاثون", note: "آحاد + و + عقد" }, { text: "42 = اثنان وأربعون", note: "نفس القاعدة" }],
            summary: "الأعداد 20-50: 20 عشرون، 30 ثلاثون، 40 أربعون، 50 خمسون. بينهما: الآحاد + و + العقد.",
            exercises: [
              { type: "mcq", question: "كيف نكتب 35 بالكلمات؟", options: ["ثلاثة وخمسون", "خمسة وثلاثون", "خمسة وعشرون", "ثلاثة وأربعون"], correctAnswer: "خمسة وثلاثون", explanation: "35 = خمسة (الآحاد) وثلاثون (العقد)", points: 10 },
              { type: "mcq", question: "العدد 'واحد وأربعون' بالأرقام:", options: ["14", "41", "40", "14"], correctAnswer: "41", explanation: "واحد وأربعون = 41 (1 في الآحاد و4 في العشرات)", points: 10 },
              { type: "true_false", question: "30 تُقرأ 'ثلاثون'", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — 30 = ثلاثون", points: 10 },
              { type: "fill_blank", question: "50 بالكلمات: ___", correctAnswer: "خمسون", explanation: "50 = خمسون (العقد الخامس)", points: 15 },
            ],
          },
          {
            slug: "darb-2-5", titleAr: "جدول الضرب 2 و5 و10", difficulty: "easy", durationMin: 25,
            objectives: ["حفظ جداول 2 و5 و10", "تطبيق الضرب في مسائل", "علاقة الضرب بالجمع المتكرر"],
            explanation: `الضرب = جمع متكرر!\n2×4 = 2+2+2+2 = 8\n\nجدول ×2: 2، 4، 6، 8، 10، 12، 14، 16، 18، 20\n(دائماً أعداد زوجية)\n\nجدول ×5: 5، 10، 15، 20، 25، 30، 35، 40، 45، 50\n(دائماً ينتهي بـ 0 أو 5)\n\nجدول ×10: 10، 20، 30، 40، 50، 60، 70، 80، 90، 100\n(نضيف صفراً للعدد!)`,
            vocabulary: [
              { word: "ضرب", definition: "جمع عدد مع نفسه عدة مرات" },
              { word: "جدول الضرب", definition: "قائمة نتائج ضرب عدد في 1 إلى 10" },
              { word: "مضروب", definition: "أحد العددين في عملية الضرب" },
            ],
            examples: [{ text: "5×6 = 30 (6 مجموعات من 5)", note: "جدول ×5" }, { text: "2×9 = 18 (2+2+2+2+2+2+2+2+2)", note: "الضرب كجمع متكرر" }],
            summary: "×2 أعداد زوجية | ×5 ينتهي بـ 0 أو 5 | ×10 نضيف صفراً للعدد.",
            exercises: [
              { type: "mcq", question: "5 × 7 = ؟", options: ["30", "35", "40", "45"], correctAnswer: "35", explanation: "5×7=35: 5+5+5+5+5+5+5=35", points: 10 },
              { type: "mcq", question: "2 × 9 = ؟", options: ["16", "18", "20", "14"], correctAnswer: "18", explanation: "2×9=18: 9+9=18", points: 10 },
              { type: "fill_blank", question: "10 × 7 = ___", correctAnswer: "70", explanation: "10×7=70: نضيف صفراً للعدد 7 يصبح 70", points: 15 },
              { type: "true_false", question: "ناتج ضرب 5×8 = 40", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "5×8=40 — صحيح", points: 10 },
              { type: "fill_blank", question: "2 × ___ = 14", correctAnswer: "7", explanation: "2×7=14", points: 15 },
            ],
          },
        ],
      },
      {
        slug: "masaail", titleAr: "المسائل الحسابية", orderIndex: 2,
        lessons: [
          {
            slug: "masaail-jam-tarh", titleAr: "مسائل الجمع والطرح", difficulty: "medium", durationMin: 25,
            objectives: ["حل مسائل من الحياة", "تحديد العملية المناسبة", "التحقق من الحل"],
            explanation: `كيف نحل المسألة الحسابية:\n\n1️⃣ اقرأ المسألة جيداً\n2️⃣ ابحث عن الأعداد والمطلوب\n3️⃣ حدد العملية: جمع أو طرح؟\n   جمع: إضافة، زيادة، اجتمع\n   طرح: نقص، أخذ، فقد، بقي\n4️⃣ احسب وتحقق\n\nمثال:\n"عند أحمد 15 كتاباً. أعطى 6 لصديقه. كم بقي معه؟"\n→ 15 − 6 = 9 كتب`,
            vocabulary: [
              { word: "مسألة", definition: "سؤال رياضي من الحياة اليومية نحله" },
              { word: "مطلوب", definition: "ما نريد إيجاده في المسألة" },
              { word: "تحقق", definition: "نتأكد من صحة الجواب بعملية معاكسة" },
            ],
            examples: [{ text: "اشترت سلمى 12 قلماً وفقدت 4 → 12−4=8 أقلام", note: "مسألة طرح" }, { text: "في الحديقة 8 ورود حمراء و7 صفراء → 8+7=15 وردة", note: "مسألة جمع" }],
            summary: "لحل المسألة: اقرأ ← ابحث عن الأعداد ← حدد العملية ← احسب ← تحقق.",
            exercises: [
              { type: "mcq", question: "كان معي 20 درهم. اشتريت بـ 8 دراهم. كم بقي؟", options: ["10", "11", "12", "13"], correctAnswer: "12", explanation: "20 − 8 = 12 درهم", points: 10 },
              { type: "mcq", question: "في الفصل 18 تلميذاً. جاء 5 آخرون. كم أصبح عددهم؟", options: ["21", "22", "23", "25"], correctAnswer: "23", explanation: "18 + 5 = 23 تلميذاً", points: 10 },
              { type: "fill_blank", question: "عند فاطمة 15 بيضة. كسرت 3. كم بقي؟ ___", correctAnswer: "12", explanation: "15 − 3 = 12 بيضة", points: 15 },
              { type: "true_false", question: "عملية 'أعطى' تعني جمع", options: ["صحيح", "خطأ"], correctAnswer: "خطأ", explanation: "أعطى يعني طرح — تقل الكمية عند من أعطى", points: 10 },
            ],
          },
        ],
      },
    ],
  },
  {
    slug: "french", titleAr: "اللغة الفرنسية", icon: "Globe", color: "#7c3aed", orderIndex: 3,
    units: [
      {
        slug: "la-famille", titleAr: "العائلة والمحيط", orderIndex: 1,
        lessons: [
          {
            slug: "famille", titleAr: "أفراد العائلة", difficulty: "easy", durationMin: 20,
            objectives: ["تعلم أفراد العائلة بالفرنسية", "بناء جمل وصفية", "الملكية"],
            explanation: `العائلة بالفرنسية:\n\nle père = الأب 👨\nla mère = الأم 👩\nle frère = الأخ 👦\nla sœur = الأخت 👧\nle grand-père = الجد 👴\nla grand-mère = الجدة 👵\n\nالملكية:\nmon père = أبي\nma mère = أمي\nmon frère = أخي\n\nجملة: Mon père s'appelle Hassan. = اسم أبي حسن.`,
            vocabulary: [
              { word: "père", definition: "الأب بالفرنسية" },
              { word: "mère", definition: "الأم بالفرنسية" },
              { word: "frère", definition: "الأخ بالفرنسية" },
            ],
            examples: [{ text: "J'ai un frère et une sœur.", note: "عندي أخ وأخت" }, { text: "Ma mère est gentille.", note: "أمي طيبة" }],
            summary: "père أب | mère أم | frère أخ | sœur أخت. نستخدم mon/ma للملكية (أبي، أمي).",
            exercises: [
              { type: "mcq", question: "ما معنى 'mère'؟", options: ["الأب", "الأم", "الأخ", "الأخت"], correctAnswer: "الأم", explanation: "mère = الأم بالفرنسية", points: 10 },
              { type: "mcq", question: "كيف تقول 'أخي' بالفرنسية؟", options: ["ma sœur", "mon père", "mon frère", "ma mère"], correctAnswer: "mon frère", explanation: "mon frère = أخي (mon للمذكر)", points: 10 },
              { type: "fill_blank", question: "الأخت بالفرنسية: ___", correctAnswer: "sœur", explanation: "sœur = الأخت | la sœur = الأخت (بأداة التعريف)", points: 15 },
              { type: "true_false", question: "père تعني الأم", options: ["صحيح", "خطأ"], correctAnswer: "خطأ", explanation: "père = الأب. الأم = mère", points: 10 },
            ],
          },
        ],
      },
    ],
  },
];

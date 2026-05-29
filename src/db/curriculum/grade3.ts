import type { SubjectData } from "./types";

export const grade3: SubjectData[] = [
  {
    slug: "arabic", titleAr: "اللغة العربية", icon: "BookOpen", color: "#059669", orderIndex: 1,
    units: [
      {
        slug: "nahw", titleAr: "النحو والصرف", orderIndex: 1,
        lessons: [
          {
            slug: "naat-mansoot", titleAr: "النعت والمنعوت", difficulty: "medium", durationMin: 25,
            objectives: ["تعريف النعت والمنعوت", "المطابقة في الجنس والعدد", "تكوين جمل بالنعت"],
            explanation: `النعت صفة تُبيّن صفة الاسم الذي قبله:\n\nالمنعوت = الاسم الموصوف\nالنعت = الصفة\n\nشروط المطابقة:\n- المذكر + نعت مذكر: الولدُ الذكيُّ\n- المؤنث + نعت مؤنث: البنتُ الذكيةُ\n- المفرد + نعت مفرد: الكتابُ المفيدُ\n- الجمع + نعت جمع: الكتبُ المفيدةُ\n\nأمثلة:\n• رأيتُ طالباً مجتهداً\n• عندي كتابٌ جديدٌ\n• المدرسةُ الكبيرةُ جميلةٌ`,
            vocabulary: [
              { word: "نعت", definition: "الصفة التي تصف الاسم قبلها — تتبعه في إعرابه" },
              { word: "منعوت", definition: "الاسم الموصوف بالنعت" },
              { word: "مطابقة", definition: "تشابه النعت والمنعوت في الجنس والعدد والتعريف" },
            ],
            examples: [{ text: "جاءَ الطالبُ المجتهدُ", note: "المجتهد نعت — يصف الطالب" }, { text: "اشتريتُ قلماً جديداً", note: "جديداً نعت لـ قلم" }],
            summary: "النعت = صفة الاسم. يجب أن يوافق المنعوت في التذكير والتأنيث والإفراد والجمع.",
            exercises: [
              { type: "mcq", question: "في جملة 'جاءَ الولدُ الطويلُ' — النعت هو:", options: ["جاء", "الولد", "الطويل", "في"], correctAnswer: "الطويل", explanation: "الطويل صفة تصف الولد — هي النعت", points: 10 },
              { type: "mcq", question: "نعت 'كتاب' (مذكر) في: 'كتابٌ ___':", options: ["مفيدة", "مفيد", "مفيدون", "مفيدات"], correctAnswer: "مفيد", explanation: "المذكر مع مذكر — كتاب مفيد", points: 10 },
              { type: "fill_blank", question: "المدرسةُ ___ (نعت لمدرسة المؤنثة: كبير)", correctAnswer: "الكبيرة", explanation: "المدرسة مؤنثة فنعتها مؤنث: الكبيرة", points: 15 },
              { type: "true_false", question: "النعت يجب أن يطابق المنعوت في الجنس", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — مذكر مع مذكر ومؤنث مع مؤنث", points: 10 },
            ],
          },
          {
            slug: "harf-jar", titleAr: "حروف الجر", difficulty: "medium", durationMin: 25,
            objectives: ["معرفة حروف الجر", "استخدام كل حرف", "بناء جمل بحروف الجر"],
            explanation: `حروف الجر تربط الكلمات وتُبيّن العلاقات:\n\nمِن: للانتهاء والتبعيض → جئتُ من المدرسة\nإلى: للانتهاء والغاية → ذهبتُ إلى البيت\nعلى: للاستعلاء → الكتابُ على الطاولة\nفي: للظرفية → الولدُ في الغرفة\nبِ: للإلصاق والمصاحبة → كتبتُ بالقلم\nلِ: للملكية والغاية → الكتابُ لأحمد\nعَن: للمجاوزة → ابتعدتُ عن الخطر`,
            vocabulary: [
              { word: "حرف جر", definition: "حرف يجر الاسم بعده — يغير حركته إلى الكسرة" },
              { word: "مجرور", definition: "الاسم الذي يأتي بعد حرف الجر" },
              { word: "جار ومجرور", definition: "حرف الجر مع الاسم المجرور معاً" },
            ],
            examples: [{ text: "ذهبَ أحمدُ إلى المدرسةِ", note: "إلى حرف جر + المدرسة مجرور" }, { text: "الكتابُ على الطاولةِ", note: "على حرف جر + الطاولة مجرور" }],
            summary: "حروف الجر: من إلى على في ب ل عن. تجر الاسم بعدها (يُضاف الكسر لآخره).",
            exercises: [
              { type: "mcq", question: "في 'الكتابُ على الطاولةِ' — حرف الجر هو:", options: ["الكتاب", "على", "الطاولة", "في"], correctAnswer: "على", explanation: "'على' حرف جر يدل على الاستعلاء", points: 10 },
              { type: "mcq", question: "حرف الجر الدال على الملكية:", options: ["من", "إلى", "لِ", "عَن"], correctAnswer: "لِ", explanation: "اللام للملكية: الكتاب لأحمد = كتاب أحمد", points: 10 },
              { type: "fill_blank", question: "جئتُ ___ المدرسةِ (حرف الجر: من)", correctAnswer: "من", explanation: "من: للانتهاء — جئتُ من المدرسة", points: 15 },
              { type: "true_false", question: "حرف الجر يجر الاسم بعده", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — حرف الجر يجعل الاسم مجروراً (آخره كسرة)", points: 10 },
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
        slug: "darb-qisma", titleAr: "الضرب والقسمة", orderIndex: 1,
        lessons: [
          {
            slug: "jadwal-darb-3-4", titleAr: "جداول الضرب 3 و4 و6", difficulty: "medium", durationMin: 25,
            objectives: ["حفظ جداول 3 و4 و6", "العلاقة بين الضرب والقسمة", "تطبيق في مسائل"],
            explanation: `جداول الضرب المهمة:\n\nجدول ×3: 3،6،9،12،15،18،21،24،27،30\nجدول ×4: 4،8،12،16،20،24،28،32،36،40\nجدول ×6: 6،12،18،24،30،36،42،48،54،60\n\n🌟 ملاحظة مهمة:\nإذا كان 3×4=12 إذن:\n12÷3=4 و 12÷4=3\n(الضرب والقسمة عملتان معكوستان!)`,
            vocabulary: [
              { word: "قسمة", definition: "توزيع عدد على أجزاء متساوية" },
              { word: "مقسوم", definition: "العدد الكبير الذي نقسمه" },
              { word: "مقسوم عليه", definition: "العدد الذي نقسم عليه" },
            ],
            examples: [{ text: "3×7=21 | التحقق: 21÷3=7 ✓", note: "العلاقة بين الضرب والقسمة" }, { text: "6×8=48 | التحقق: 48÷6=8 ✓", note: "جدول ×6" }],
            summary: "جداول 3، 4، 6 مهمة. الضرب والقسمة معكوستان: إذا أ×ب=ج إذن ج÷أ=ب.",
            exercises: [
              { type: "mcq", question: "3 × 8 = ؟", options: ["21", "24", "27", "30"], correctAnswer: "24", explanation: "3×8=24: 3+3+3+3+3+3+3+3=24", points: 10 },
              { type: "mcq", question: "4 × 7 = ؟", options: ["24", "28", "32", "36"], correctAnswer: "28", explanation: "4×7=28", points: 10 },
              { type: "fill_blank", question: "6 × 9 = ___", correctAnswer: "54", explanation: "6×9=54", points: 15 },
              { type: "mcq", question: "إذا 4×6=24 إذن 24÷4=؟", options: ["4", "6", "8", "24"], correctAnswer: "6", explanation: "الضرب والقسمة معكوستان: 24÷4=6", points: 10 },
              { type: "true_false", question: "3×6 = 6×3", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الضرب خاصية التبديل: الترتيب لا يؤثر على النتيجة", points: 10 },
            ],
          },
          {
            slug: "kusoor-basita", titleAr: "الكسور العادية البسيطة", difficulty: "medium", durationMin: 30,
            objectives: ["فهم مفهوم الكسر", "تمييز البسط والمقام", "قراءة وكتابة الكسور"],
            explanation: `الكسر يُعبّر عن جزء من كل:\n\nتخيل خبزة مقسمة إلى 4 أجزاء:\nأخذتَ جزء واحد = ¼ (ربع)\n\nأجزاء الكسر:\n• البسط (فوق): عدد الأجزاء التي أخذناها\n• المقام (تحت): مجموع الأجزاء\n• الخط يعني ÷\n\n½ = نصف | ¼ = ربع | ¾ = ثلاثة أرباع | ⅓ = ثلث\n\n⚠️ قاعدة مهمة:\nكلما كبر المقام → صغر الكسر\n½ > ¼ > ⅛`,
            vocabulary: [
              { word: "كسر", definition: "عدد يُعبّر عن جزء من كل" },
              { word: "بسط", definition: "العدد فوق خط الكسر — عدد الأجزاء التي أخذناها" },
              { word: "مقام", definition: "العدد تحت خط الكسر — مجموع الأجزاء الكلية" },
            ],
            examples: [{ text: "¾: أخذنا 3 من أصل 4 أجزاء", note: "البسط 3 والمقام 4" }, { text: "½ الخبزة = 1 من جزأين متساويين", note: "أشهر الكسور" }],
            summary: "كسر = بسط/مقام. بسط = ما أخذناه. مقام = الكل. ½>¼>⅛ (كبر المقام = صغر الكسر).",
            exercises: [
              { type: "mcq", question: "في ¾ — البسط هو:", options: ["4", "3", "7", "1"], correctAnswer: "3", explanation: "البسط = الرقم فوق خط الكسر = 3", points: 10 },
              { type: "mcq", question: "أيٌّ أكبر؟", options: ["½", "¼", "⅛", "⅓"], correctAnswer: "½", explanation: "½ أكبر لأن مقامه الأصغر", points: 10 },
              { type: "fill_blank", question: "نصف الشيء يُكتب: ___", correctAnswer: "½", explanation: "½ = النصف (بسط 1 ومقام 2)", points: 15 },
              { type: "true_false", question: "¾ تعني أخذنا 3 أجزاء من أصل 4", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — البسط 3 والمقام 4", points: 10 },
            ],
          },
        ],
      },
    ],
  },
  {
    slug: "science", titleAr: "التربية العلمية", icon: "Microscope", color: "#0891b2", orderIndex: 3,
    units: [
      {
        slug: "hayawanaat", titleAr: "عالم الحيوانات", orderIndex: 1,
        lessons: [
          {
            slug: "tassniif-hayawanaat", titleAr: "تصنيف الحيوانات", difficulty: "easy", durationMin: 20,
            objectives: ["تصنيف الحيوانات حسب غذائها", "حسب بيئتها", "خصائص كل مجموعة"],
            explanation: `تصنيف الحيوانات حسب الغذاء:\n\n🥩 آكلة اللحوم (مفترسة):\nالأسد، الذئب، التمساح، النسر\n\n🌿 آكلة النباتات (عاشبة):\nالبقرة، الخروف، الأرنب، الفيل\n\n🥩🌿 آكلة اللحوم والنباتات (قارتة):\nالإنسان، الدب، القرد\n\nتصنيف حسب البيئة:\n🌊 مائية: سمك، دلفين، حوت\n🏔️ برية: أسد، فيل، غزال\n✈️ طائرة: نسر، حمامة، ببغاء`,
            vocabulary: [
              { word: "مفترسة", definition: "حيوانات تأكل الحيوانات الأخرى — تصطادها" },
              { word: "عاشبة", definition: "حيوانات تأكل النباتات والأعشاب فقط" },
              { word: "قارتة", definition: "حيوانات تأكل النباتات واللحوم معاً" },
            ],
            examples: [{ text: "الأسد مفترس — يأكل الغزلان", note: "آكل لحوم" }, { text: "البقرة عاشبة — تأكل العشب", note: "آكلة نباتات" }],
            summary: "مفترسة تأكل لحوم | عاشبة تأكل نباتات | قارتة تأكل الاثنين. نصنف أيضاً حسب البيئة: مائية أو برية أو طائرة.",
            exercises: [
              { type: "mcq", question: "الأسد حيوان:", options: ["عاشب", "مفترس", "قارت", "مائي"], correctAnswer: "مفترس", explanation: "الأسد يأكل الحيوانات — مفترس (آكل لحوم)", points: 10 },
              { type: "mcq", question: "الأرنب يأكل:", options: ["اللحوم", "الأسماك", "النباتات", "الحشرات"], correctAnswer: "النباتات", explanation: "الأرنب عاشب يأكل الجزر والخضروات والأعشاب", points: 10 },
              { type: "mcq", question: "الإنسان حيوان:", options: ["مفترس", "عاشب", "قارت", "مائي"], correctAnswer: "قارت", explanation: "الإنسان يأكل اللحوم والنباتات معاً = قارت", points: 10 },
              { type: "true_false", question: "الدلفين حيوان مائي", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الدلفين يعيش في البحر = حيوان مائي", points: 10 },
            ],
          },
        ],
      },
    ],
  },
];

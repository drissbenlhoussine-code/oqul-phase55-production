import type { SubjectData } from "./types";
export const grade4: SubjectData[] = [
  {
    slug: "arabic", titleAr: "اللغة العربية", icon: "BookOpen", color: "#059669", orderIndex: 1,
    units: [{
      slug: "balaga", titleAr: "البلاغة والأسلوب", orderIndex: 1,
      lessons: [
        {
          slug: "tashbiih", titleAr: "التشبيه", difficulty: "medium", durationMin: 25,
          objectives: ["تعريف التشبيه", "أركانه الأربعة", "أنواعه وأمثلته"],
          explanation: `التشبيه: مقارنة شيء بشيء آخر في صفة مشتركة\n\nأركانه الأربعة:\n1️⃣ المشبه: الشيء الذي نشبّهه\n2️⃣ المشبه به: الشيء الذي نشبه به\n3️⃣ أداة التشبيه: كـ، مثل، كأن\n4️⃣ وجه الشبه: الصفة المشتركة\n\nأمثلة:\n• العلمُ كالنور يُضيء العقول\n  مشبه: العلم | أداة: كـ | مشبه به: النور\n  وجه الشبه: الإضاءة والهداية\n\n• الولدُ كالأسد في الشجاعة`,
          vocabulary: [
            { word: "تشبيه", definition: "إلحاق شيء بآخر في صفة لوجود مشابهة بينهما" },
            { word: "أداة التشبيه", definition: "الكلمة التي تربط المشبه بالمشبه به: كـ، مثل، كأن" },
            { word: "وجه الشبه", definition: "الصفة المشتركة بين المشبه والمشبه به" },
          ],
          examples: [{ text: "القلبُ كالمرآة — يعكس ما فيه", note: "أداة التشبيه: كـ" }, { text: "العلمُ نور — بدون أداة (تشبيه بليغ)", note: "تشبيه بليغ حذفت منه الأداة" }],
          summary: "التشبيه: مشبه + أداة (ك/مثل/كأن) + مشبه به + وجه شبه. مثال: العلم كالنور.",
          exercises: [
            { type: "mcq", question: "في 'الولدُ كالأسد' — المشبه هو:", options: ["كالأسد", "الولد", "الأسد", "شجاعة"], correctAnswer: "الولد", explanation: "المشبه هو الشيء الذي نصفه = الولد", points: 10 },
            { type: "mcq", question: "أداة التشبيه في 'القمرُ مثلُ الفضة':", options: ["القمر", "الفضة", "مثل", "في"], correctAnswer: "مثل", explanation: "مثل أداة تشبيه تربط القمر بالفضة", points: 10 },
            { type: "fill_blank", question: "أكمل: الصبرُ ___ المفتاح (أداة تشبيه)", correctAnswer: "كـ", explanation: "الصبر كالمفتاح يفتح أبواب النجاح", points: 15 },
            { type: "true_false", question: "التشبيه البليغ يحذف أداة التشبيه", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — 'العلم نور' بدون أداة يُسمى تشبيهاً بليغاً", points: 10 },
          ],
        },
      ],
    }],
  },
  {
    slug: "math", titleAr: "الرياضيات", icon: "Calculator", color: "#2563eb", orderIndex: 2,
    units: [
      {
        slug: "kusoor", titleAr: "الكسور", orderIndex: 1,
        lessons: [
          {
            slug: "kusoor-mutasawiya", titleAr: "الكسور المتساوية والمقارنة", difficulty: "medium", durationMin: 30,
            objectives: ["إيجاد كسور متساوية", "مقارنة الكسور", "ترتيب الكسور"],
            explanation: `الكسور المتساوية لها قيمة واحدة:\n½ = 2/4 = 3/6 = 4/8\n(نضرب البسط والمقام بنفس العدد)\n\nمقارنة الكسور:\nإذا المقام واحد → الأكبر بسطاً أكبر\n3/7 > 2/7 (لأن 3>2)\n\nإذا البسط واحد → الأكبر مقاماً أصغر\n1/3 > 1/5 (لأن 3<5)\n\nلمقارنة كسور مختلفة → نجعل المقام واحداً\n½ و ⅓ → 3/6 و 2/6 → ½ > ⅓`,
            vocabulary: [
              { word: "كسور متساوية", definition: "كسور لها نفس القيمة رغم اختلاف أرقامها: ½=2/4" },
              { word: "المضاعف المشترك الأصغر", definition: "أصغر عدد مشترك نضرب فيه المقامين" },
            ],
            examples: [{ text: "½ = 2/4 = 3/6 (نضرب بـ 2 ثم بـ 3)", note: "إيجاد كسور متساوية" }, { text: "2/3 vs 3/4: → 8/12 vs 9/12 → 3/4 أكبر", note: "المقارنة بالمقام المشترك" }],
            summary: "كسور متساوية: نضرب البسط والمقام بنفس العدد. للمقارنة: نوحّد المقام أولاً.",
            exercises: [
              { type: "mcq", question: "أيٌّ يساوي ½؟", options: ["1/3", "2/4", "3/5", "2/3"], correctAnswer: "2/4", explanation: "½ × 2/2 = 2/4 — كسران متساويان", points: 10 },
              { type: "mcq", question: "أيٌّ أكبر: 2/5 أم 3/5؟", options: ["2/5", "3/5", "متساويان"], correctAnswer: "3/5", explanation: "المقام واحد (5) — الأكبر بسطاً أكبر: 3>2", points: 10 },
              { type: "fill_blank", question: "½ = ___/6", correctAnswer: "3", explanation: "½ × 3/3 = 3/6", points: 15 },
              { type: "true_false", question: "1/4 أكبر من 1/3", options: ["صحيح", "خطأ"], correctAnswer: "خطأ", explanation: "1/3 أكبر لأن مقامه (3) أصغر من (4)", points: 10 },
            ],
          },
        ],
      },
      {
        slug: "qiyaas", titleAr: "القياس والهندسة", orderIndex: 2,
        lessons: [
          {
            slug: "muhiit-massaha", titleAr: "المحيط والمساحة", difficulty: "medium", durationMin: 30,
            objectives: ["حساب محيط المربع والمستطيل", "حساب مساحة المربع والمستطيل", "الفرق بين المحيط والمساحة"],
            explanation: `المحيط = مجموع أطوال الأضلاع (الخط الخارجي)\nالمساحة = الفضاء الداخلي للشكل\n\nالمربع (الأضلاع كلها = أ):\nمحيطه = 4 × أ\nمساحته = أ × أ\n\nالمستطيل (طول = ط، عرض = ع):\nمحيطه = 2 × (ط + ع)\nمساحته = ط × ع\n\nمثال: مستطيل طوله 6 وعرضه 4\nمحيط = 2×(6+4) = 2×10 = 20 سم\nمساحة = 6×4 = 24 سم²`,
            vocabulary: [
              { word: "محيط", definition: "طول الخط المحيط بالشكل من الخارج" },
              { word: "مساحة", definition: "الفضاء الداخلي للشكل — وحدتها مربعة" },
              { word: "سم²", definition: "سنتيمتر مربع — وحدة قياس المساحة" },
            ],
            examples: [{ text: "مربع ضلعه 5: محيط=4×5=20سم | مساحة=5×5=25سم²", note: "المربع" }, { text: "مستطيل 8×3: محيط=2×(8+3)=22 | مساحة=8×3=24", note: "المستطيل" }],
            summary: "محيط مربع=4×ضلع | محيط مستطيل=2×(ط+ع) | مساحة مربع=ضلع² | مساحة مستطيل=ط×ع",
            exercises: [
              { type: "mcq", question: "محيط مربع ضلعه 7 سم:", options: ["14", "21", "28", "49"], correctAnswer: "28", explanation: "محيط مربع = 4 × 7 = 28 سم", points: 10 },
              { type: "mcq", question: "مساحة مستطيل طوله 9 وعرضه 5:", options: ["28", "40", "45", "50"], correctAnswer: "45", explanation: "مساحة = 9 × 5 = 45 سم²", points: 10 },
              { type: "fill_blank", question: "مساحة مربع ضلعه 6 = ___ سم²", correctAnswer: "36", explanation: "6 × 6 = 36 سم²", points: 15 },
              { type: "true_false", question: "المحيط والمساحة لهما نفس الوحدة", options: ["صحيح", "خطأ"], correctAnswer: "خطأ", explanation: "المحيط وحدته خطية (سم) والمساحة وحدتها مربعة (سم²)", points: 10 },
            ],
          },
        ],
      },
    ],
  },
  {
    slug: "english", titleAr: "اللغة الإنجليزية", icon: "Languages", color: "#dc2626", orderIndex: 4,
    units: [{
      slug: "basics", titleAr: "أساسيات الإنجليزية", orderIndex: 1,
      lessons: [
        {
          slug: "greetings", titleAr: "التحية والتقديم بالإنجليزية", difficulty: "easy", durationMin: 20,
          objectives: ["تعلم التحية بالإنجليزية", "تقديم النفس", "أيام الأسبوع"],
          explanation: `Greetings (التحية):\nHello / Hi = مرحباً\nGood morning = صباح الخير\nGood afternoon = مساء الخير\nGood night = تصبح على خير\nGoodbye / Bye = مع السلامة\n\nIntroductions (التقديم):\nMy name is... = اسمي...\nI am... years old. = عمري... سنة\nI am from Morocco. = أنا من المغرب.\nI live in... = أسكن في...`,
          vocabulary: [
            { word: "Hello", definition: "مرحباً — أشهر تحية إنجليزية" },
            { word: "My name is", definition: "اسمي — للتعريف بالنفس" },
            { word: "Goodbye", definition: "مع السلامة — للوداع" },
          ],
          examples: [{ text: "Hello! My name is Youssef.", note: "مرحباً! اسمي يوسف" }, { text: "I am 10 years old.", note: "عمري 10 سنوات" }],
          summary: "Hello مرحباً | My name is اسمي | I am ... years old عمري | Goodbye مع السلامة",
          exercises: [
            { type: "mcq", question: "ما معنى 'Good morning'؟", options: ["مساء الخير", "صباح الخير", "تصبح على خير", "مع السلامة"], correctAnswer: "صباح الخير", explanation: "Good morning = صباح الخير — تُقال في الصباح", points: 10 },
            { type: "mcq", question: "كيف تقول 'اسمي' بالإنجليزية؟", options: ["I am", "My name is", "I live in", "Goodbye"], correctAnswer: "My name is", explanation: "My name is = اسمي", points: 10 },
            { type: "fill_blank", question: "مع السلامة بالإنجليزية: ___", correctAnswer: "Goodbye", explanation: "Goodbye = مع السلامة", points: 15 },
            { type: "true_false", question: "'Hello' و 'Hi' لهما نفس المعنى", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — Hello و Hi كلاهما يعنيان مرحباً", points: 10 },
          ],
        },
        {
          slug: "colors-numbers", titleAr: "الألوان والأرقام بالإنجليزية", difficulty: "easy", durationMin: 20,
          objectives: ["الألوان بالإنجليزية", "الأرقام 1-20", "الجمل الوصفية"],
          explanation: `Colours (الألوان):\nred أحمر | blue أزرق | green أخضر\nyellow أصفر | orange برتقالي | white أبيض\nblack أسود | brown بني | pink وردي\n\nNumbers (الأرقام 1-20):\none two three four five\nsix seven eight nine ten\neleven twelve thirteen fourteen fifteen\nsixteen seventeen eighteen nineteen twenty`,
          vocabulary: [
            { word: "red", definition: "اللون الأحمر بالإنجليزية" },
            { word: "blue", definition: "اللون الأزرق بالإنجليزية" },
            { word: "green", definition: "اللون الأخضر بالإنجليزية" },
          ],
          examples: [{ text: "The sky is blue.", note: "السماء زرقاء" }, { text: "I have twelve books.", note: "عندي 12 كتاباً" }],
          summary: "red أحمر | blue أزرق | green أخضر | yellow أصفر. الأرقام: one two three...twenty",
          exercises: [
            { type: "mcq", question: "ما معنى 'yellow'؟", options: ["أزرق", "أخضر", "أصفر", "أحمر"], correctAnswer: "أصفر", explanation: "yellow = أصفر — لون الشمس والليمون", points: 10 },
            { type: "mcq", question: "العدد 15 بالإنجليزية:", options: ["thirteen", "fourteen", "fifteen", "sixteen"], correctAnswer: "fifteen", explanation: "fifteen = 15 خمسة عشر", points: 10 },
            { type: "fill_blank", question: "اللون الأخضر بالإنجليزية: ___", correctAnswer: "green", explanation: "green = أخضر — لون الأشجار والأعشاب", points: 15 },
            { type: "true_false", question: "'red' تعني اللون الأحمر", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — red = أحمر، لون الورد والتفاح", points: 10 },
          ],
        },
      ],
    }],
  },
];

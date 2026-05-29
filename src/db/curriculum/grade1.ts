import type { SubjectData } from "./types";

export const grade1: SubjectData[] = [
  // ══════════════════════════════════════════
  // اللغة العربية — السنة الأولى
  // ══════════════════════════════════════════
  {
    slug: "arabic", titleAr: "اللغة العربية", icon: "BookOpen", color: "#059669", orderIndex: 1,
    units: [
      {
        slug: "huruf", titleAr: "الحروف الهجائية", orderIndex: 1,
        lessons: [
          {
            slug: "alef-baa", titleAr: "الألف والباء", difficulty: "easy", durationMin: 15,
            objectives: ["نطق الألف والباء", "كتابتهما في مواضعهما", "قراءة كلمات بهما"],
            explanation: `الألف والباء أول حرفين في الأبجدية.\n\nالألف (أ/إ/آ/ا): أَرنب | إِبرة | آمِن | بَاب\nالباء (ب): نقطة واحدة تحت — بَيت، بَاب، كِتَاب\n\nالباء في البداية: بـ | في الوسط: ـبـ | في النهاية: ـب`,
            vocabulary: [
              { word: "أرنب", definition: "حيوان صغير يقفز ويحب الجزر" },
              { word: "باب", definition: "مدخل البيت أو الغرفة" },
              { word: "بيت", definition: "المكان الذي تسكن فيه الأسرة" },
            ],
            examples: [{ text: "أَحمد يلعب", note: "الألف مفتوحة" }, { text: "البَيتُ كبير", note: "الباء في البداية" }],
            summary: "الألف أول الحروف وأشكاله: أَ إِ آ ا. الباء ثانيها وتحتها نقطة واحدة.",
            exercises: [
              { type: "mcq", question: "ما الحرف الأول في الأبجدية؟", options: ["الباء", "الألف", "التاء", "الجيم"], correctAnswer: "الألف", explanation: "الألف أول الحروف الهجائية الثمانية والعشرين", points: 10 },
              { type: "mcq", question: "كم نقطة تحت الباء؟", options: ["صفر", "واحدة", "اثنتان", "ثلاث"], correctAnswer: "واحدة", explanation: "الباء: نقطة واحدة تحت", points: 10 },
              { type: "true_false", question: "كلمة 'باب' تبدأ بالباء", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — بَاب تبدأ بالباء وتنتهي بالباء أيضاً", points: 10 },
              { type: "fill_blank", question: "أكمل: _رنب (حيوان صغير)", correctAnswer: "أ", explanation: "أَرنب بهمزة مفتوحة", points: 15 },
              { type: "fill_blank", question: "أكمل: _يت (مكان السكن)", correctAnswer: "ب", explanation: "بَيت يبدأ بالباء", points: 15 },
            ],
          },
          {
            slug: "taa-thaa", titleAr: "التاء والثاء", difficulty: "easy", durationMin: 15,
            objectives: ["التمييز بين التاء والثاء والباء", "كتابة التاء والثاء", "قراءة كلمات بهما"],
            explanation: `التاء والثاء تشبهان الباء لكن بنقاط مختلفة:\n\nب = نقطة تحت\nت = نقطتان فوق: تُفاح، تِلميذ، كِتاب\nث = ثلاث نقاط فوق: ثَعلب، ثَلاثة، ثَوب`,
            vocabulary: [
              { word: "تفاحة", definition: "فاكهة حمراء أو خضراء حلوة" },
              { word: "تلميذ", definition: "الطفل الذي يتعلم في المدرسة" },
              { word: "ثعلب", definition: "حيوان ذكي في الغابة" },
            ],
            examples: [{ text: "التفاحة حمراء", note: "التاء في البداية" }, { text: "الثعلب ذكي", note: "الثاء في البداية" }],
            summary: "ب نقطة تحت | ت نقطتان فوق | ث ثلاث نقاط فوق — الشكل واحد والنقاط تفرق.",
            exercises: [
              { type: "mcq", question: "كم نقطة فوق التاء؟", options: ["واحدة", "اثنتان", "ثلاث", "صفر"], correctAnswer: "اثنتان", explanation: "التاء: نقطتان فوق", points: 10 },
              { type: "mcq", question: "كم نقطة فوق الثاء؟", options: ["واحدة", "اثنتان", "ثلاث", "صفر"], correctAnswer: "ثلاث", explanation: "الثاء: ثلاث نقاط فوق — مثل عدد اسمها!", points: 10 },
              { type: "mcq", question: "كلمة 'تفاحة' تبدأ بـ:", options: ["باء", "تاء", "ثاء", "جيم"], correctAnswer: "تاء", explanation: "تُفاحة بالتاء", points: 10 },
              { type: "true_false", question: "التاء والثاء لهما نفس الشكل الأساسي", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الشكل واحد والفرق في عدد النقاط فوق", points: 10 },
              { type: "fill_blank", question: "أكمل: _علب (حيوان ذكي)", correctAnswer: "ث", explanation: "ثَعلب بالثاء", points: 15 },
            ],
          },
          {
            slug: "jeem-haa", titleAr: "الجيم والحاء والخاء", difficulty: "easy", durationMin: 15,
            objectives: ["التمييز بين ج ح خ", "كتابة الحروف الثلاثة", "قراءة كلمات بهم"],
            explanation: `الجيم والحاء والخاء أسرة واحدة — نفس الشكل:\n\nج = نقطة في الوسط: جَمل، جَبل، جَزرة\nح = بدون نقطة: حِصان، حَليب، حَديقة\nخ = نقطة فوق: خُبز، خَروف، خَيمة`,
            vocabulary: [
              { word: "جمل", definition: "حيوان الصحراء بالأسنمة" },
              { word: "حليب", definition: "شراب أبيض من البقرة مفيد للعظام" },
              { word: "خبز", definition: "الخبزة المغربية اللذيذة نأكلها يومياً" },
            ],
            examples: [{ text: "الجمل في الصحراء", note: "الجيم بنقطة وسط" }, { text: "الخبز طازج", note: "الخاء بنقطة فوق" }],
            summary: "ج بنقطة وسط | ح بلا نقطة | خ بنقطة فوق — الشكل واحد والنقطة تفرق.",
            exercises: [
              { type: "mcq", question: "أين نقطة الجيم؟", options: ["فوق", "تحت", "في الوسط", "لا نقطة"], correctAnswer: "في الوسط", explanation: "الجيم: نقطة داخل الحرف في الوسط", points: 10 },
              { type: "mcq", question: "الحاء عدد نقاطها:", options: ["صفر", "واحدة", "اثنتان", "ثلاث"], correctAnswer: "صفر", explanation: "الحاء بلا نقاط — هذا ما يميزها عن الجيم والخاء", points: 10 },
              { type: "mcq", question: "الخبز المغربي يبدأ بـ:", options: ["جيم", "حاء", "خاء", "كاف"], correctAnswer: "خاء", explanation: "خُبز بالخاء — نقطة فوق", points: 10 },
              { type: "true_false", question: "الجيم والحاء والخاء لهم نفس الشكل", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الشكل الأساسي واحد والنقاط تفرق", points: 10 },
              { type: "fill_blank", question: "أكمل: _مل (حيوان الصحراء)", correctAnswer: "ج", explanation: "جَمل بالجيم", points: 15 },
            ],
          },
          {
            slug: "dal-zay", titleAr: "الدال والذال والراء والزاي", difficulty: "easy", durationMin: 15,
            objectives: ["التمييز بين د ذ ر ز", "كتابتها في مواضعها", "قراءة كلمات بهم"],
            explanation: `د ذ: شبيهان — الذال بنقطة فوق\nد = بلا نقطة: دَجاجة، دَار، دَفتر\nذ = نقطة فوق: ذَهب، ذِئب، ذَرة\n\nر ز: شبيهان — الزاي بنقطة فوق\nر = بلا نقطة: رَأس، رَجل، كِراس\nز = نقطة فوق: زَيتون، زَهرة، كُوز`,
            vocabulary: [
              { word: "دجاجة", definition: "طير يعطينا البيض ولحمه لذيذ" },
              { word: "ذهب", definition: "معدن ثمين أصفر اللون" },
              { word: "زيتون", definition: "ثمرة صغيرة خضراء نستخرج منها الزيت" },
            ],
            examples: [{ text: "الدجاجة تبيض", note: "الدال بلا نقطة" }, { text: "الزيتون مغربي", note: "الزاي بنقطة فوق" }],
            summary: "د وذ أسرة — ذ بنقطة. ر وز أسرة — ز بنقطة. القاعدة: النقطة فوق تضيف صوتاً مختلفاً.",
            exercises: [
              { type: "mcq", question: "الذال يختلف عن الدال بـ:", options: ["الشكل", "نقطة فوق", "نقطة تحت", "الحجم"], correctAnswer: "نقطة فوق", explanation: "الذال = الدال + نقطة فوق", points: 10 },
              { type: "mcq", question: "الزاي يختلف عن الراء بـ:", options: ["الشكل", "نقطة فوق", "نقطة تحت", "نقطتان فوق"], correctAnswer: "نقطة فوق", explanation: "الزاي = الراء + نقطة فوق", points: 10 },
              { type: "true_false", question: "كلمة 'زهرة' تبدأ بالراء", options: ["صحيح", "خطأ"], correctAnswer: "خطأ", explanation: "زَهرة تبدأ بالزاي (بنقطة فوق) وليس الراء", points: 10 },
              { type: "fill_blank", question: "أكمل: _يتون (ثمرة خضراء)", correctAnswer: "ز", explanation: "زَيتون بالزاي", points: 15 },
            ],
          },
          {
            slug: "seen-sheen", titleAr: "السين والشين", difficulty: "easy", durationMin: 15,
            objectives: ["التمييز بين السين والشين", "كتابتهما", "قراءة كلمات بهما"],
            explanation: `السين والشين شبيهتان — الشين بثلاث نقاط فوق\n\nس = بلا نقاط: سَمك، سَماء، كُرسي، دِراسة\nش = ثلاث نقاط فوق: شَمس، شَجرة، شَباك`,
            vocabulary: [
              { word: "سمك", definition: "حيوان بحري لذيذ يسبح في الماء" },
              { word: "شمس", definition: "النجم الكبير الذي يضيء نهارنا ويدفئنا" },
              { word: "شجرة", definition: "نبات كبير له جذع وأغصان وأوراق" },
            ],
            examples: [{ text: "السمك في البحر", note: "السين بلا نقاط" }, { text: "الشمس مشرقة", note: "الشين بثلاث نقاط فوق" }],
            summary: "س بلا نقاط | ش بثلاث نقاط فوق. الشكل الأساسي واحد — الأسنان المتموجة.",
            exercises: [
              { type: "mcq", question: "الشين عدد نقاطها:", options: ["صفر", "واحدة", "اثنتان", "ثلاث"], correctAnswer: "ثلاث", explanation: "الشين: ثلاث نقاط فوق — مثل الثاء", points: 10 },
              { type: "mcq", question: "كلمة 'شمس' تبدأ بـ:", options: ["سين", "شين", "صاد", "ضاد"], correctAnswer: "شين", explanation: "شَمس بالشين — ثلاث نقاط فوق", points: 10 },
              { type: "true_false", question: "السين والشين لهما نفس الشكل الأساسي", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الفرق فقط في النقاط الثلاث فوق الشين", points: 10 },
              { type: "fill_blank", question: "أكمل: _مك (حيوان بحري)", correctAnswer: "س", explanation: "سَمك بالسين", points: 15 },
            ],
          },
          {
            slug: "sad-dad", titleAr: "الصاد والضاد والطاء والظاء", difficulty: "medium", durationMin: 20,
            objectives: ["التمييز بين ص ض ط ظ", "كتابة هذه الحروف", "الحروف المفخمة"],
            explanation: `هذه الحروف مفخمة — الصوت أعمق:\n\nص: صَفر، صَابون، قَفص\nض: ضَب، ضِفدع، أَرض\nط: طَاولة، طَائر، بَطاطا\nظ: ظِل، ظَرف، حَظ`,
            vocabulary: [
              { word: "صابون", definition: "نستخدمه لتنظيف أيدينا وجسمنا" },
              { word: "طاولة", definition: "أثاث نضع عليه الكتب والطعام" },
              { word: "ظل", definition: "المكان المظلل بعيداً عن الشمس" },
            ],
            examples: [{ text: "الصابون للنظافة", note: "الصاد مفخمة" }, { text: "أجلس في الظل", note: "الظاء مفخمة" }],
            summary: "ص ض ط ظ حروف مفخمة — الصوت أعمق. كل حرف منها له شكل مميز.",
            exercises: [
              { type: "mcq", question: "كلمة 'طاولة' تبدأ بـ:", options: ["تاء", "طاء", "ظاء", "ثاء"], correctAnswer: "طاء", explanation: "طَاولة بالطاء المفخمة", points: 10 },
              { type: "mcq", question: "أي هذه الكلمات يبدأ بالضاد؟", options: ["صفر", "ظرف", "ضفدع", "طير"], correctAnswer: "ضفدع", explanation: "ضِفدع بالضاد", points: 10 },
              { type: "true_false", question: "الصاد والضاد لهما نفس الصوت", options: ["صحيح", "خطأ"], correctAnswer: "خطأ", explanation: "لا — الصاد والضاد حرفان مختلفان تماماً بصوت وشكل مختلفين", points: 10 },
              { type: "fill_blank", question: "أكمل: _ابون (نستخدمه للنظافة)", correctAnswer: "ص", explanation: "صَابون بالصاد", points: 15 },
            ],
          },
          {
            slug: "ain-ghain", titleAr: "العين والغين والفاء والقاف", difficulty: "medium", durationMin: 20,
            objectives: ["تمييز ع غ ف ق", "كتابتها", "قراءة كلمات بهم"],
            explanation: `عين وغين أسرة:\nع = بلا نقطة: عَين، عَسل، مَعلم\nغ = نقطة فوق: غَنم، غَابة، فَراغ\n\nفاء وقاف:\nف = نقطة فوق في الوسط: فَراشة، فَم، كيف\nق = نقطتان فوق: قَمر، قَلم، سُوق`,
            vocabulary: [
              { word: "عسل", definition: "سائل حلو لذيذ تصنعه النحل" },
              { word: "غنم", definition: "حيوان يعطينا الصوف والحليب واللحم" },
              { word: "قمر", definition: "الجسم المضيء الذي نراه ليلاً" },
            ],
            examples: [{ text: "العسل حلو", note: "العين بلا نقطة" }, { text: "القمر يضيء الليل", note: "القاف بنقطتين" }],
            summary: "ع غ أسرة — غ بنقطة. ف نقطة فوق في الوسط. ق نقطتان فوق.",
            exercises: [
              { type: "mcq", question: "الغين تختلف عن العين بـ:", options: ["الشكل", "نقطة فوق", "نقطة تحت", "نقطتان"], correctAnswer: "نقطة فوق", explanation: "الغين = العين + نقطة فوق", points: 10 },
              { type: "mcq", question: "القاف عدد نقاطه:", options: ["واحدة", "اثنتان", "ثلاث", "صفر"], correctAnswer: "اثنتان", explanation: "القاف: نقطتان فوق", points: 10 },
              { type: "fill_blank", question: "أكمل: _مر (يضيء الليل)", correctAnswer: "ق", explanation: "قَمر بالقاف", points: 15 },
              { type: "true_false", question: "الفاء والقاف شبيهتان في الشكل", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الفاء نقطة والقاف نقطتان، الشكل الأساسي متشابه", points: 10 },
            ],
          },
          {
            slug: "kaf-lam-meem", titleAr: "الكاف واللام والميم والنون", difficulty: "easy", durationMin: 15,
            objectives: ["تمييز ك ل م ن", "كتابتها", "قراءة كلمات بهم"],
            explanation: `ك: كِتاب، كَلب، سَمَك\nل: لَيمون، لَبن، جَبَل\nم: مَاء، مَدرسة، قَلَم\nن: نَجمة، نَهر، حِصان — نقطة فوق`,
            vocabulary: [
              { word: "كتاب", definition: "أوراق مجلدة فيها معلومات ودروس" },
              { word: "ليمون", definition: "فاكهة صفراء حامضة" },
              { word: "نجمة", definition: "شكل هندسي بخمسة أطراف، أو الأجسام المضيئة في السماء ليلاً" },
            ],
            examples: [{ text: "الكتاب مفيد", note: "الكاف في البداية" }, { text: "النجوم جميلة", note: "النون بنقطة فوق" }],
            summary: "ك ل م ن حروف شائعة في العربية. النون وحده بنقطة فوق.",
            exercises: [
              { type: "mcq", question: "من هذه الحروف ما فيه نقطة:", options: ["كاف", "لام", "ميم", "نون"], correctAnswer: "نون", explanation: "النون: نقطة فوق، بقية الحروف بلا نقاط", points: 10 },
              { type: "fill_blank", question: "أكمل: _تاب (نقرأ فيه)", correctAnswer: "ك", explanation: "كِتاب بالكاف", points: 15 },
              { type: "mcq", question: "كلمة 'مدرسة' تبدأ بـ:", options: ["ميم", "دال", "راء", "سين"], correctAnswer: "ميم", explanation: "مَدرسة تبدأ بالميم", points: 10 },
              { type: "true_false", question: "اللام والميم يشبهان بعضهما", options: ["صحيح", "خطأ"], correctAnswer: "خطأ", explanation: "لا — اللام والميم حرفان مختلفان تماماً في الشكل", points: 10 },
            ],
          },
        ],
      },
      {
        slug: "kalimaat", titleAr: "الكلمات والجمل", orderIndex: 2,
        lessons: [
          {
            slug: "asmaa-hayawan", titleAr: "أسماء الحيوانات", difficulty: "easy", durationMin: 20,
            objectives: ["تعلم أسماء الحيوانات", "بناء جمل بسيطة", "وصف الحيوانات"],
            explanation: `الحيوانات من حولنا:\n\n🐄 البقرة: تعطينا الحليب\n🐔 الدجاجة: تعطينا البيض\n🐑 الخروف: يعطينا الصوف\n🐟 السمك: يسبح في البحر\n🦁 الأسد: ملك الغابة\n🐰 الأرنب: يحب الجزر\n🐴 الحصان: يركبه الفارس`,
            vocabulary: [
              { word: "بقرة", definition: "حيوان أليف يعطينا الحليب والزبدة" },
              { word: "أسد", definition: "أكبر القطط ويسمى ملك الغابة" },
              { word: "خروف", definition: "حيوان أليف نحتفل به في العيد" },
            ],
            examples: [{ text: "البقرةُ تعطينا الحليب", note: "جملة اسمية وصفية" }, { text: "الأسدُ في الغابة", note: "مبتدأ وخبر" }],
            summary: "تعلمنا أسماء الحيوانات وكيف نصنع جملاً بسيطة عنها.",
            exercises: [
              { type: "mcq", question: "من يعطينا الحليب؟", options: ["الأسد", "البقرة", "الأرنب", "السمك"], correctAnswer: "البقرة", explanation: "البقرة حيوان أليف يعطينا الحليب", points: 10 },
              { type: "mcq", question: "يُسمى ملك الغابة:", options: ["الحصان", "البقرة", "الأسد", "الخروف"], correctAnswer: "الأسد", explanation: "الأسد أقوى حيوانات الغابة فيُسمى ملكها", points: 10 },
              { type: "true_false", question: "السمك يعيش في البحر", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "السمك حيوان مائي يعيش في البحار والأنهار", points: 10 },
              { type: "fill_blank", question: "الأرنب يحب أكل الـ ___", correctAnswer: "جزر", explanation: "الأرنب يحب الجزر — وهذا مشهور جداً!", points: 15 },
            ],
          },
          {
            slug: "jumal-basita", titleAr: "الجمل البسيطة", difficulty: "easy", durationMin: 20,
            objectives: ["بناء جملة مفيدة", "المبتدأ والخبر", "الجملة الفعلية البسيطة"],
            explanation: `الجملة المفيدة تعطي معنى كاملاً:\n\nالجملة الاسمية = مبتدأ + خبر:\n• البيتُ كبيرٌ\n• الجوُّ جميلٌ\n• الطالبُ مجتهدٌ\n\nالجملة الفعلية = فعل + فاعل:\n• يلعبُ الولدُ\n• تقرأُ البنتُ\n• يأكلُ الطفلُ`,
            vocabulary: [
              { word: "مبتدأ", definition: "الاسم الذي نتحدث عنه في الجملة" },
              { word: "خبر", definition: "ما نقوله عن المبتدأ لإتمام المعنى" },
              { word: "جملة مفيدة", definition: "كلام يعطي معنى كاملاً" },
            ],
            examples: [{ text: "الطالبُ مجتهدٌ", note: "الطالب مبتدأ — مجتهد خبر" }, { text: "يلعبُ أحمدُ في الحديقة", note: "جملة فعلية" }],
            summary: "الجملة المفيدة: اسمية (مبتدأ+خبر) أو فعلية (فعل+فاعل).",
            exercises: [
              { type: "mcq", question: "في جملة 'البيتُ كبيرٌ' — المبتدأ هو:", options: ["كبير", "البيت", "في", "هو"], correctAnswer: "البيت", explanation: "المبتدأ هو الاسم الذي نتحدث عنه = البيت", points: 10 },
              { type: "mcq", question: "الخبر في 'الجوُّ جميلٌ' هو:", options: ["الجو", "جميل", "في", "هو"], correctAnswer: "جميل", explanation: "الخبر هو ما نقوله عن المبتدأ = جميل", points: 10 },
              { type: "true_false", question: "الجملة المفيدة تعطي معنى ناقصاً", options: ["صحيح", "خطأ"], correctAnswer: "خطأ", explanation: "الجملة المفيدة تعطي معنى كاملاً — هذا تعريفها", points: 10 },
              { type: "fill_blank", question: "أكمل الجملة: الطالبُ ___ (اختر خبراً مناسباً)", correctAnswer: "مجتهد", explanation: "الطالب مجتهد — جملة اسمية مفيدة", points: 15 },
            ],
          },
          {
            slug: "qissa-arnab", titleAr: "قصة الأرنب والسلحفاة", difficulty: "medium", durationMin: 25,
            objectives: ["قراءة نص قصير بفهم", "استخراج الشخصيات", "الدرس المستفاد"],
            explanation: `قصة الأرنب والسلحفاة 🐇🐢\n\nفي يوم مشمس، قال الأرنبُ للسلحفاة:\n"أنتِ بطيئةٌ جداً! لا أحد يتسابق معي!"\n\nقالت السلحفاة: "تعال نتسابق إذن!"\n\nبدأ السباق. أسرع الأرنب وتوقف لينام تحت شجرة...\n\nسارت السلحفاة ببطء... خطوة... خطوة...\n\nاستيقظ الأرنب فوجد السلحفاة وصلت!\n\n🌟 الدرس: المثابرة والتواضع أهم من الغرور.`,
            vocabulary: [
              { word: "مثابرة", definition: "الاستمرار في العمل بدون توقف" },
              { word: "غرور", definition: "الاعتقاد بأنك أفضل من الجميع بدون سبب" },
              { word: "سباق", definition: "منافسة بين شخصين أو أكثر للفوز" },
            ],
            examples: [{ text: "الأرنب سريع لكن متكبر", note: "صفة مركبة" }, { text: "السلحفاة بطيئة لكن مثابرة", note: "الصفة المقابلة" }],
            summary: "النجاح يأتي بالمثابرة لا بالتفاخر — درس الأرنب والسلحفاة الخالد.",
            exercises: [
              { type: "mcq", question: "من فاز في السباق؟", options: ["الأرنب", "السلحفاة", "كلاهما", "لم يفز أحد"], correctAnswer: "السلحفاة", explanation: "السلحفاة فازت لأنها واصلت السير ولم تتوقف", points: 10 },
              { type: "mcq", question: "لماذا خسر الأرنب؟", options: ["لأنه مريض", "لأنه نام وتكاسل", "لأنه أبطأ", "لأن السلحفاة غشت"], correctAnswer: "لأنه نام وتكاسل", explanation: "الأرنب اتكل على سرعته فنام، والسلحفاة واصلت", points: 10 },
              { type: "mcq", question: "الدرس المستفاد من القصة:", options: ["السرعة أهم شيء", "المثابرة أهم من الغرور", "النوم مفيد", "لا تتسابق أبداً"], correctAnswer: "المثابرة أهم من الغرور", explanation: "الاستمرار والتواضع يفوق الموهبة بدون جهد", points: 15 },
              { type: "true_false", question: "الغرور صفة إيجابية تساعد على النجاح", options: ["صحيح", "خطأ"], correctAnswer: "خطأ", explanation: "الغرور صفة سلبية تجعل الإنسان يتكاسل ويفشل", points: 10 },
            ],
          },
        ],
      },
    ],
  },

  // ══════════════════════════════════════════
  // الرياضيات — السنة الأولى
  // ══════════════════════════════════════════
  {
    slug: "math", titleAr: "الرياضيات", icon: "Calculator", color: "#2563eb", orderIndex: 2,
    units: [
      {
        slug: "aaadaad-1-10", titleAr: "الأعداد من 0 إلى 10", orderIndex: 1,
        lessons: [
          {
            slug: "count-1-5", titleAr: "العد من 0 إلى 5", difficulty: "easy", durationMin: 20,
            objectives: ["معرفة الأعداد 0-5", "العد بالأصابع", "ربط العدد بالكمية"],
            explanation: `نتعلم العد من 0 إلى 5 بالأصابع والأشياء!\n\n🫰 0 = الصفر — لا شيء\n☝️ 1 = واحد\n✌️ 2 = اثنان\n🤟 3 = ثلاثة\n🖖 4 = أربعة\n🖐️ 5 = خمسة — اليد كاملة!\n\n⬆️ تصاعدي: 0، 1، 2، 3، 4، 5\n⬇️ تنازلي: 5، 4، 3، 2، 1، 0`,
            vocabulary: [
              { word: "صفر", definition: "العدد 0 يعني لا شيء — لا يوجد" },
              { word: "تصاعدي", definition: "من الأصغر إلى الأكبر: 1، 2، 3..." },
              { word: "تنازلي", definition: "من الأكبر إلى الأصغر: 5، 4، 3..." },
            ],
            examples: [{ text: "عندي 3 تفاحات 🍎🍎🍎", note: "ربط العدد بالكمية" }, { text: "في الفصل 5 نوافذ", note: "العد من البيئة المحيطة" }],
            summary: "الأعداد 0-5: صفر واحد اثنان ثلاثة أربعة خمسة. نعدهم بالأصابع.",
            exercises: [
              { type: "mcq", question: "كم عدد النجوم؟ ⭐⭐⭐", options: ["2", "3", "4", "5"], correctAnswer: "3", explanation: "نعد: واحد، اثنان، ثلاثة = 3 نجوم", points: 10 },
              { type: "mcq", question: "ما الذي يأتي بعد العدد 3؟", options: ["2", "4", "5", "1"], correctAnswer: "4", explanation: "التسلسل: 1، 2، 3، 4، 5 — بعد 3 يأتي 4", points: 10 },
              { type: "true_false", question: "العدد 5 أكبر من العدد 3", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "5 > 3 — خمسة أكبر من ثلاثة", points: 10 },
              { type: "fill_blank", question: "أكمل: 1، 2، 3، ___", correctAnswer: "4", explanation: "التسلسل التصاعدي: 1، 2، 3، 4، 5", points: 15 },
              { type: "fill_blank", question: "أكمل: 5، 4، 3، ___", correctAnswer: "2", explanation: "التسلسل التنازلي: 5، 4، 3، 2، 1", points: 15 },
            ],
          },
          {
            slug: "count-6-10", titleAr: "العد من 6 إلى 10", difficulty: "easy", durationMin: 20,
            objectives: ["معرفة الأعداد 6-10", "المقارنة بين الأعداد", "ترتيب الأعداد"],
            explanation: `الأعداد من 6 إلى 10:\n\n6 = ستة 🎲🎲🎲🎲🎲🎲\n7 = سبعة\n8 = ثمانية\n9 = تسعة\n10 = عشرة 🖐️🖐️ — اليدان معاً!\n\nمقارنة: 6 < 7 < 8 < 9 < 10\n< تعني "أصغر من"\n> تعني "أكبر من"`,
            vocabulary: [
              { word: "ستة", definition: "العدد 6 — بعد خمسة" },
              { word: "عشرة", definition: "العدد 10 — أصابع اليدين مجتمعتان" },
              { word: "مقارنة", definition: "نقول أيّ عدد أكبر وأيّهم أصغر" },
            ],
            examples: [{ text: "8 > 6 (ثمانية أكبر من ستة)", note: "مقارنة باستخدام >" }, { text: "7 < 9 (سبعة أصغر من تسعة)", note: "مقارنة باستخدام <" }],
            summary: "الأعداد 6-10. نستخدم < و > للمقارنة. 10 = أصابع اليدين.",
            exercises: [
              { type: "mcq", question: "كم عدد 🍕🍕🍕🍕🍕🍕🍕؟", options: ["6", "7", "8", "9"], correctAnswer: "7", explanation: "نعد القطع: 1-2-3-4-5-6-7 = سبعة", points: 10 },
              { type: "mcq", question: "أيٌّ أكبر؟", options: ["6", "8", "7", "9"], correctAnswer: "9", explanation: "9 هو الأكبر من بين 6، 7، 8، 9", points: 10 },
              { type: "true_false", question: "10 = أصابع اليدين مجتمعتان", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "5 + 5 = 10 — اليد اليمنى + اليسرى", points: 10 },
              { type: "fill_blank", question: "أكمل: 7، 8، 9، ___", correctAnswer: "10", explanation: "التسلسل التصاعدي: 7، 8، 9، 10", points: 15 },
            ],
          },
          {
            slug: "ashkal-hindasiya", titleAr: "الأشكال الهندسية", difficulty: "easy", durationMin: 15,
            objectives: ["التعرف على المثلث والمربع والمستطيل والدائرة", "أضلاع كل شكل", "الأشكال في الحياة"],
            explanation: `الأشكال الهندسية حولنا:\n\n🔺 المثلث: 3 أضلاع، 3 رؤوس\n🟥 المربع: 4 أضلاع متساوية، 4 رؤوس\n🟦 المستطيل: 4 أضلاع (ضلعان طويلان وضلعان قصيران)\n⭕ الدائرة: لا أضلاع، لا رؤوس\n\nمن حياتنا:\n🍕 البيتزا = دائرة\n📱 الهاتف = مستطيل\n⛺ خيمة = مثلث`,
            vocabulary: [
              { word: "ضلع", definition: "الخط المستقيم الذي يشكل جانب الشكل" },
              { word: "رأس", definition: "نقطة التقاء الأضلاع في الشكل" },
              { word: "دائرة", definition: "شكل مستدير ليس له أضلاع" },
            ],
            examples: [{ text: "المثلث عنده 3 أضلاع و3 رؤوس", note: "خصائص المثلث" }, { text: "عجلة السيارة دائرة", note: "أشكال من الحياة" }],
            summary: "مثلث (3 أضلاع) | مربع (4 أضلاع متساوية) | مستطيل (4 أضلاع) | دائرة (لا أضلاع).",
            exercises: [
              { type: "mcq", question: "كم ضلع للمثلث؟", options: ["2", "3", "4", "5"], correctAnswer: "3", explanation: "المثلث له 3 أضلاع و3 رؤوس", points: 10 },
              { type: "mcq", question: "أيٌّ من الأشكال ليس له أضلاع؟", options: ["المثلث", "المربع", "الدائرة", "المستطيل"], correctAnswer: "الدائرة", explanation: "الدائرة شكل مستدير ليس له أضلاع أو رؤوس", points: 10 },
              { type: "true_false", question: "المربع والمستطيل لهما 4 أضلاع", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — كلاهما رباعي الأضلاع، لكن في المربع كلها متساوية", points: 10 },
              { type: "fill_blank", question: "المربع له ___ أضلاع متساوية", correctAnswer: "4", explanation: "المربع له 4 أضلاع كلها متساوية الطول", points: 15 },
            ],
          },
        ],
      },
      {
        slug: "jam-tarh", titleAr: "الجمع والطرح", orderIndex: 2,
        lessons: [
          {
            slug: "jam-hatta-10", titleAr: "الجمع حتى العدد 10", difficulty: "easy", durationMin: 25,
            objectives: ["جمع عددين ناتجهما ≤ 10", "استخدام الأصابع", "حل مسائل بسيطة"],
            explanation: `الجمع = نضم عددين معاً للحصول على عدد أكبر!\n\nرمز الجمع: +\nرمز المساواة: =\n\n1+1=2 | 2+2=4 | 3+3=6 | 4+4=8 | 5+5=10\n2+3=5 | 3+4=7 | 4+5=9 | 1+9=10\n\n🌟 حيلة: ابدأ بالعدد الأكبر وأضف الأصغر!\n5+3: ابدأ من 5، أضف 3 = 6، 7، 8`,
            vocabulary: [
              { word: "جمع", definition: "عملية ضم عددين للحصول على عدد أكبر" },
              { word: "ناتج", definition: "الجواب الذي نحصل عليه بعد عملية حسابية" },
              { word: "مجموع", definition: "الناتج النهائي للجمع" },
            ],
            examples: [{ text: "عندي 3 تفاحات وأضافت أمي 2 → 3+2=5", note: "مسألة من الحياة" }, { text: "4+3=7 (ابدأ من 4، عدّ 3 أصابع)", note: "طريقة الأصابع" }],
            summary: "الجمع: ضم عددين. نستخدم + للجمع و = للنتيجة. ابدأ بالأكبر وأضف الأصغر.",
            exercises: [
              { type: "mcq", question: "2 + 3 = ؟", options: ["4", "5", "6", "7"], correctAnswer: "5", explanation: "2 + 3 = 5 — اثنان وثلاثة يساويان خمسة", points: 10 },
              { type: "mcq", question: "عندك 4 حلوى وأعطاك أخوك 3. كم صار عندك؟", options: ["5", "6", "7", "8"], correctAnswer: "7", explanation: "4 + 3 = 7", points: 10 },
              { type: "fill_blank", question: "3 + ___ = 8", correctAnswer: "5", explanation: "8 - 3 = 5، إذن 3 + 5 = 8", points: 15 },
              { type: "true_false", question: "5 + 5 = 10", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "5 + 5 = 10 — أصابع اليدين مجتمعتان", points: 10 },
              { type: "fill_blank", question: "6 + 4 = ___", correctAnswer: "10", explanation: "6 + 4 = 10", points: 15 },
            ],
          },
          {
            slug: "tarh-hatta-10", titleAr: "الطرح حتى العدد 10", difficulty: "medium", durationMin: 25,
            objectives: ["طرح عدد من عدد أكبر", "مفهوم الباقي", "مسائل من الحياة"],
            explanation: `الطرح = نأخذ عدداً من عدد آخر أكبر!\n\nرمز الطرح: −\n\n5−2=3 | 7−3=4 | 10−4=6 | 9−6=3\n\n🌟 طريقة العد للخلف:\n8−3: ابدأ من 8، عدّ للخلف 3 مرات: 7، 6، 5\nالجواب: 5\n\n💡 التحقق: إذا 8−3=5، إذن 5+3=8 ✓`,
            vocabulary: [
              { word: "طرح", definition: "عملية أخذ عدد من عدد أكبر" },
              { word: "الباقي", definition: "العدد الذي يتبقى بعد الطرح" },
              { word: "تحقق", definition: "نتأكد من صحة الجواب بعملية معاكسة" },
            ],
            examples: [{ text: "كان معي 7 حلوى أكلت 2 → 7−2=5 حلوى", note: "مسألة من الحياة" }, { text: "10−6=4 (تحقق: 4+6=10 ✓)", note: "التحقق بالجمع" }],
            summary: "الطرح = نأخذ. الباقي = ما تبقى. التحقق: الباقي + المطروح = الأصلي.",
            exercises: [
              { type: "mcq", question: "8 − 3 = ؟", options: ["4", "5", "6", "7"], correctAnswer: "5", explanation: "8 − 3 = 5 (عدّ للخلف: 7، 6، 5)", points: 10 },
              { type: "mcq", question: "كان معي 6 كرات، فقدت 2. كم بقي؟", options: ["3", "4", "5", "8"], correctAnswer: "4", explanation: "6 − 2 = 4", points: 10 },
              { type: "fill_blank", question: "10 − ___ = 6", correctAnswer: "4", explanation: "10 − 4 = 6 (تحقق: 6+4=10 ✓)", points: 15 },
              { type: "true_false", question: "9 − 9 = 0", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "أي عدد ناقص نفسه = صفر", points: 10 },
              { type: "fill_blank", question: "7 − 4 = ___", correctAnswer: "3", explanation: "7 − 4 = 3", points: 15 },
            ],
          },
        ],
      },
    ],
  },

  // ══════════════════════════════════════════
  // اللغة الفرنسية — السنة الأولى
  // ══════════════════════════════════════════
  {
    slug: "french", titleAr: "اللغة الفرنسية", icon: "Globe", color: "#7c3aed", orderIndex: 3,
    units: [
      {
        slug: "salutations", titleAr: "التحية والتعارف", orderIndex: 1,
        lessons: [
          {
            slug: "bonjour", titleAr: "التحية بالفرنسية", difficulty: "easy", durationMin: 15,
            objectives: ["تعلم التحية بالفرنسية", "تقديم النفس", "أيام الأسبوع"],
            explanation: `التحية بالفرنسية:\n\nBonjour! = صباح الخير / مرحباً!\nBonsoir! = مساء الخير\nAu revoir! = مع السلامة\nSalut! = أهلاً (بين الأصدقاء)\n\nتقديم النفس:\nJe m'appelle... = اسمي...\nJ'ai ... ans = عمري ... سنة\nJ'habite à... = أسكن في...`,
            vocabulary: [
              { word: "Bonjour", definition: "مرحباً / صباح الخير بالفرنسية" },
              { word: "Je m'appelle", definition: "اسمي — للتعريف بالنفس" },
              { word: "Au revoir", definition: "مع السلامة / وداعاً" },
            ],
            examples: [{ text: "Bonjour! Je m'appelle Youssef.", note: "مرحباً! اسمي يوسف." }, { text: "J'ai 7 ans.", note: "عمري 7 سنوات." }],
            summary: "Bonjour = مرحباً | Je m'appelle = اسمي | J'ai ... ans = عمري",
            exercises: [
              { type: "mcq", question: "ما معنى 'Bonjour'؟", options: ["مع السلامة", "مرحباً", "شكراً", "من فضلك"], correctAnswer: "مرحباً", explanation: "Bonjour = مرحباً / صباح الخير — أشهر تحية فرنسية", points: 10 },
              { type: "mcq", question: "كيف تقول 'اسمي' بالفرنسية؟", options: ["J'ai", "Je m'appelle", "J'habite", "Au revoir"], correctAnswer: "Je m'appelle", explanation: "Je m'appelle = اسمي — نستخدمها للتعريف بأنفسنا", points: 10 },
              { type: "fill_blank", question: "أكمل: Au ___ ! (مع السلامة)", correctAnswer: "revoir", explanation: "Au revoir = مع السلامة", points: 15 },
              { type: "true_false", question: "Bonsoir تُقال في الصباح", options: ["صحيح", "خطأ"], correctAnswer: "خطأ", explanation: "Bonsoir = مساء الخير — تُقال مساءً، وليس صباحاً", points: 10 },
            ],
          },
          {
            slug: "les-couleurs", titleAr: "الألوان بالفرنسية", difficulty: "easy", durationMin: 15,
            objectives: ["تعلم الألوان الأساسية", "وصف الأشياء بالألوان", "الجملة الوصفية"],
            explanation: `الألوان بالفرنسية:\n\nrouge = أحمر 🔴\nbleu = أزرق 🔵\nvert = أخضر 🟢\njaune = أصفر 🟡\norange = برتقالي 🟠\nblanc = أبيض ⚪\nnoir = أسود ⚫\n\nاستخدام:\nLe ciel est bleu. = السماء زرقاء.\nLa pomme est rouge. = التفاحة حمراء.`,
            vocabulary: [
              { word: "rouge", definition: "اللون الأحمر بالفرنسية" },
              { word: "bleu", definition: "اللون الأزرق بالفرنسية — لون السماء" },
              { word: "vert", definition: "اللون الأخضر بالفرنسية — لون الأشجار" },
            ],
            examples: [{ text: "Le soleil est jaune.", note: "الشمس صفراء." }, { text: "L'herbe est verte.", note: "العشب أخضر." }],
            summary: "rouge أحمر | bleu أزرق | vert أخضر | jaune أصفر | blanc أبيض | noir أسود",
            exercises: [
              { type: "mcq", question: "ما معنى 'bleu'؟", options: ["أحمر", "أزرق", "أخضر", "أصفر"], correctAnswer: "أزرق", explanation: "bleu = أزرق — لون السماء والبحر", points: 10 },
              { type: "mcq", question: "كيف تقول 'أحمر' بالفرنسية؟", options: ["bleu", "vert", "rouge", "jaune"], correctAnswer: "rouge", explanation: "rouge = أحمر — لون الورد والتفاح", points: 10 },
              { type: "fill_blank", question: "La banane est ___ (الموزة صفراء)", correctAnswer: "jaune", explanation: "jaune = أصفر — والموزة فعلاً صفراء!", points: 15 },
              { type: "true_false", question: "vert تعني اللون الأخضر", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — vert = أخضر في الفرنسية", points: 10 },
            ],
          },
        ],
      },
      {
        slug: "les-chiffres", titleAr: "الأرقام بالفرنسية", orderIndex: 2,
        lessons: [
          {
            slug: "chiffres-1-10", titleAr: "الأرقام من 1 إلى 10", difficulty: "easy", durationMin: 20,
            objectives: ["نطق الأرقام 1-10 بالفرنسية", "كتابتها", "استخدامها في جمل"],
            explanation: `الأرقام من 1 إلى 10 بالفرنسية:\n\n1 = un (أُن)\n2 = deux (دُو)\n3 = trois (تْرُوا)\n4 = quatre (كاتر)\n5 = cinq (سَنك)\n6 = six (سِيس)\n7 = sept (سَت)\n8 = huit (وِيت)\n9 = neuf (نُف)\n10 = dix (دِيس)`,
            vocabulary: [
              { word: "un", definition: "العدد 1 بالفرنسية" },
              { word: "deux", definition: "العدد 2 بالفرنسية" },
              { word: "dix", definition: "العدد 10 بالفرنسية" },
            ],
            examples: [{ text: "J'ai deux chats. = عندي قطتان.", note: "استخدام deux" }, { text: "Il a sept ans. = عمره سبع سنوات.", note: "استخدام sept" }],
            summary: "un deux trois quatre cinq six sept huit neuf dix — 1 إلى 10 بالفرنسية",
            exercises: [
              { type: "mcq", question: "ما معنى 'cinq'؟", options: ["3", "4", "5", "6"], correctAnswer: "5", explanation: "cinq = 5 — خمسة بالفرنسية", points: 10 },
              { type: "mcq", question: "كيف تقول '3' بالفرنسية؟", options: ["un", "deux", "trois", "quatre"], correctAnswer: "trois", explanation: "trois = 3 — ثلاثة بالفرنسية", points: 10 },
              { type: "fill_blank", question: "العدد 10 بالفرنسية: ___", correctAnswer: "dix", explanation: "dix = 10 — عشرة بالفرنسية", points: 15 },
              { type: "true_false", question: "deux تعني العدد 2", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — deux = 2 بالفرنسية", points: 10 },
            ],
          },
        ],
      },
    ],
  },

  // ══════════════════════════════════════════
  // التربية الإسلامية — السنة الأولى
  // ══════════════════════════════════════════
  {
    slug: "islamic", titleAr: "التربية الإسلامية", icon: "Star", color: "#d97706", orderIndex: 4,
    units: [
      {
        slug: "aqida", titleAr: "العقيدة الإسلامية", orderIndex: 1,
        lessons: [
          {
            slug: "arkaan-islam", titleAr: "أركان الإسلام الخمسة", difficulty: "easy", durationMin: 20,
            objectives: ["حفظ أركان الإسلام الخمسة", "فهم معنى كل ركن", "تطبيقها في الحياة"],
            explanation: `أركان الإسلام الخمسة:\n\n1️⃣ الشهادتان: "أشهد أن لا إله إلا الله وأن محمداً رسول الله"\n\n2️⃣ الصلاة: نصلي 5 صلوات يومياً\n(الفجر، الظهر، العصر، المغرب، العشاء)\n\n3️⃣ الزكاة: إعطاء جزء من المال للفقراء\n\n4️⃣ الصوم: صيام رمضان شهراً كاملاً\n\n5️⃣ الحج: زيارة بيت الله الحرام مرة واحدة`,
            vocabulary: [
              { word: "شهادة", definition: "الإقرار بأن لا إله إلا الله وأن محمداً رسوله" },
              { word: "زكاة", definition: "إعطاء جزء من المال لمساعدة الفقراء — ركن من الإسلام" },
              { word: "حج", definition: "زيارة مكة المكرمة لأداء مناسك مخصوصة" },
            ],
            examples: [{ text: "نصلي 5 مرات في اليوم", note: "الصلاة ركن الإسلام الثاني" }, { text: "نصوم رمضان كل سنة", note: "الصوم ركن الإسلام الرابع" }],
            summary: "أركان الإسلام: شهادة + صلاة + زكاة + صوم + حج. خمسة أركان تقوم عليها حياة المسلم.",
            exercises: [
              { type: "mcq", question: "كم عدد أركان الإسلام؟", options: ["3", "4", "5", "6"], correctAnswer: "5", explanation: "أركان الإسلام خمسة: شهادة وصلاة وزكاة وصوم وحج", points: 10 },
              { type: "mcq", question: "كم صلاة نؤدي كل يوم؟", options: ["3", "4", "5", "6"], correctAnswer: "5", explanation: "الصلوات الخمس: فجر وظهر وعصر ومغرب وعشاء", points: 10 },
              { type: "mcq", question: "في أي شهر نصوم؟", options: ["شعبان", "رمضان", "شوال", "ذي الحجة"], correctAnswer: "رمضان", explanation: "شهر رمضان المبارك هو شهر الصيام", points: 10 },
              { type: "true_false", question: "الزكاة تعني مساعدة الفقراء", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الزكاة إعطاء جزء من المال للمحتاجين", points: 10 },
              { type: "fill_blank", question: "الركن الأول من الإسلام هو الـ___", correctAnswer: "شهادة", explanation: "الشهادتان أول أركان الإسلام الخمسة", points: 15 },
            ],
          },
          {
            slug: "asma-allah", titleAr: "أسماء الله الحسنى", difficulty: "easy", durationMin: 15,
            objectives: ["تعلم بعض أسماء الله الحسنى", "فهم معانيها", "ذكر الله"],
            explanation: `لله أسماء حسنى (99 اسماً):\n\nالله: اسم الجلالة — خالق كل شيء\nالرحمن: صاحب الرحمة الواسعة لجميع الخلق\nالرحيم: صاحب الرحمة الخاصة بالمؤمنين\nالكريم: كثير العطاء والجود\nالعليم: يعلم كل شيء\nالقدير: قادر على كل شيء\n\nنبدأ كل عمل بـ "بسم الله الرحمن الرحيم"`,
            vocabulary: [
              { word: "الرحمن", definition: "من أسماء الله — صاحب الرحمة الواسعة الشاملة" },
              { word: "الكريم", definition: "من أسماء الله — كثير العطاء والجود" },
              { word: "العليم", definition: "من أسماء الله — يعلم كل صغيرة وكبيرة" },
            ],
            examples: [{ text: "بسم الله الرحمن الرحيم", note: "نبدأ كل عمل بهذه الكلمات" }, { text: "الله رزقنا الطعام", note: "نشكر الله على نعمه" }],
            summary: "لله 99 اسماً حسناً. الرحمن والرحيم أكثرها تكراراً في القرآن والبسملة.",
            exercises: [
              { type: "mcq", question: "كم اسماً لله الحسنى؟", options: ["9", "19", "99", "999"], correctAnswer: "99", explanation: "لله 99 اسماً حسناً ثبتت في القرآن والسنة", points: 10 },
              { type: "mcq", question: "ماذا يعني اسم 'الرحمن'؟", options: ["القادر", "العالم", "صاحب الرحمة الواسعة", "الكريم"], correctAnswer: "صاحب الرحمة الواسعة", explanation: "الرحمن: صاحب الرحمة الواسعة لجميع خلقه", points: 10 },
              { type: "true_false", question: "نبدأ كل عمل بسم الله", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نبدأ بسم الله الرحمن الرحيم في كل أمر ذي بال", points: 10 },
              { type: "fill_blank", question: "بسم الله الرحمن الـ___", correctAnswer: "رحيم", explanation: "البسملة الكاملة: بسم الله الرحمن الرحيم", points: 15 },
            ],
          },
        ],
      },
    ],
  },
];

// ══════════════════════════════════════════
// التربية العلمية — السنة الأولى
// ══════════════════════════════════════════
export const grade1Science: import("./types").SubjectData = {
  slug: "science", titleAr: "التربية العلمية", icon: "Microscope", color: "#0891b2", orderIndex: 5,
  units: [
    {
      slug: "hayawaanaat-sg1", titleAr: "الحيوانات", orderIndex: 1,
      lessons: [
        {
          slug: "hayawanaat-alfiyya", titleAr: "الحيوانات الأليفة والبرية", difficulty: "easy", durationMin: 20,
          objectives: ["التمييز بين الحيوانات الأليفة والبرية", "فوائد الحيوانات الأليفة", "أمثلة من البيئة المغربية"],
          explanation: `الحيوانات نوعان:\n\n🐄 الحيوانات الأليفة: تعيش مع الإنسان وتفيده\n• البقرة 🐄 — تعطينا الحليب واللحم\n• الخروف 🐑 — يعطينا الصوف واللحم\n• الدجاجة 🐔 — تعطينا البيض واللحم\n• الحصان 🐴 — يساعدنا في العمل والتنقل\n• القط 🐈 — يصطاد الفئران\n• الكلب 🐕 — يحرس البيت\n\n🦁 الحيوانات البرية: تعيش في الطبيعة\n• الأسد — ملك الغابة\n• الذئب — يعيش في الجبال\n• القرد — يعيش في الغابات\n• الغزال — يعيش في السهول`,
          vocabulary: [
            { word: "أليف", definition: "حيوان يعيش مع الإنسان ويستأنس به" },
            { word: "بري", definition: "حيوان يعيش في الطبيعة بعيداً عن الإنسان" },
            { word: "فوائد", definition: "الخيرات التي يقدمها الحيوان للإنسان" },
          ],
          examples: [{ text: "الكلب حيوان أليف يحرس البيت", note: "مثال على الحيوان الأليف وفائدته" }, { text: "الأسد حيوان بري يعيش في الغابة", note: "مثال على الحيوان البري" }],
          summary: "الحيوانات الأليفة تعيش مع الإنسان وتفيده. الحيوانات البرية تعيش في الطبيعة.",
          exercises: [
            { type: "mcq", question: "أيٌّ من هذه الحيوانات أليف؟", options: ["الأسد", "الذئب", "البقرة", "الغزال"], correctAnswer: "البقرة", explanation: "البقرة حيوان أليف تعيش مع الإنسان وتعطيه الحليب", points: 10 },
            { type: "mcq", question: "الدجاجة تعطينا:", options: ["الحليب", "الصوف", "البيض", "العسل"], correctAnswer: "البيض", explanation: "الدجاجة تعطينا البيض — وهي من الطيور الأليفة", points: 10 },
            { type: "true_false", question: "الأسد حيوان أليف", options: ["صحيح", "خطأ"], correctAnswer: "خطأ", explanation: "الأسد حيوان بري خطير يعيش في الغابة", points: 10 },
            { type: "fill_blank", question: "الخروف يعطينا الـ ___ (لحم وهذا)", correctAnswer: "صوف", explanation: "الخروف يعطينا الصوف والحليب واللحم", points: 15 },
          ],
        },
        {
          slug: "hawas-khamsa", titleAr: "الحواس الخمس", difficulty: "easy", durationMin: 20,
          objectives: ["تعرف الحواس الخمس", "أعضاء الحس", "وظيفة كل حاسة"],
          explanation: `الحواس الخمس تساعدنا على اكتشاف العالم:\n\n👁️ البصر — العين\nنرى الألوان والأشكال والأضواء\n\n👂 السمع — الأذن\nنسمع الأصوات والموسيقى\n\n👃 الشم — الأنف\nنشم الروائح الطيبة والكريهة\n\n👅 الذوق — اللسان\nنتذوق الحلو والمالح والحامض والمر\n\n✋ اللمس — الجلد\nنحس بالحرارة والبرودة والملمس`,
          vocabulary: [
            { word: "حاسة", definition: "قدرة الجسم على استقبال المعلومات من البيئة المحيطة" },
            { word: "بصر", definition: "حاسة الرؤية — بالعيون" },
            { word: "سمع", definition: "حاسة الاستماع — بالآذان" },
          ],
          examples: [{ text: "نرى بالعيون — حاسة البصر", note: "العين = عضو البصر" }, { text: "نشم بالأنف — حاسة الشم", note: "الأنف = عضو الشم" }],
          summary: "خمس حواس: بصر (عين) + سمع (أذن) + شم (أنف) + ذوق (لسان) + لمس (جلد).",
          exercises: [
            { type: "mcq", question: "أيٌّ عضو يستخدم لحاسة السمع؟", options: ["العين", "الأنف", "الأذن", "اللسان"], correctAnswer: "الأذن", explanation: "الأذن هي عضو حاسة السمع", points: 10 },
            { type: "mcq", question: "نتذوق الطعام بـ:", options: ["العين", "اللسان", "الأذن", "الجلد"], correctAnswer: "اللسان", explanation: "اللسان عضو الذوق — يميز الحلو والمالح والحامض والمر", points: 10 },
            { type: "true_false", question: "الجلد يساعدنا على الإحساس باللمس", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الجلد عضو حاسة اللمس يحس بالحرارة والبرودة والملمس", points: 10 },
            { type: "fill_blank", question: "نرى الألوان بحاسة الـ ___", correctAnswer: "بصر", explanation: "البصر حاسة الرؤية — عضوها العين", points: 15 },
          ],
        },
        {
          slug: "nabataat-sg1", titleAr: "النباتات من حولنا", difficulty: "easy", durationMin: 20,
          objectives: ["التعرف على أجزاء النبات", "فوائد النباتات", "ظروف نمو النبات"],
          explanation: `النبات له أجزاء:\n\n🌿 الجذر: تحت الأرض — يثبت النبات ويمتص الماء\n🌱 الساق: ينقل الماء والغذاء\n🍃 الأوراق: تصنع الغذاء من الشمس والهواء\n🌸 الزهرة: تجذب الحشرات للتلقيح\n🍎 الثمرة: تحتوي البذور لإنبات نباتات جديدة\n\nيحتاج النبات للنمو:\n☀️ ضوء الشمس\n💧 الماء\n🌱 التربة الجيدة\n\nفوائد النباتات:\n• نأكل الخضروات والفواكه\n• نتنفس الأكسجين الذي تنتجه\n• تُجمّل البيئة`,
          vocabulary: [
            { word: "جذر", definition: "الجزء تحت الأرض — يثبت النبات ويمتص الماء والأملاح" },
            { word: "ساق", definition: "جزء النبات الرابط بين الجذر والأوراق — ينقل الماء والغذاء" },
            { word: "تمثيل ضوئي", definition: "عملية صنع الغذاء في الأوراق باستخدام الضوء والماء وثاني أكسيد الكربون" },
          ],
          examples: [{ text: "الشجرة لها جذور عميقة تثبتها في التربة", note: "وظيفة الجذر" }, { text: "الأوراق الخضراء تصنع الغذاء بضوء الشمس", note: "التمثيل الضوئي" }],
          summary: "النبات: جذر + ساق + أوراق + زهرة + ثمرة. يحتاج: شمس + ماء + تربة. فائدته: غذاء وأكسجين.",
          exercises: [
            { type: "mcq", question: "أيٌّ جزء النبات يمتص الماء؟", options: ["الساق", "الجذر", "الأوراق", "الزهرة"], correctAnswer: "الجذر", explanation: "الجذر يمتص الماء والأملاح من التربة", points: 10 },
            { type: "mcq", question: "يحتاج النبات للنمو إلى:", options: ["الظلام والبرودة", "الضوء والماء", "الملح فقط", "الهواء فقط"], correctAnswer: "الضوء والماء", explanation: "النبات يحتاج ضوء الشمس والماء والتربة الجيدة للنمو", points: 10 },
            { type: "true_false", question: "الأوراق تصنع غذاء النبات", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الأوراق تصنع الغذاء بالتمثيل الضوئي", points: 10 },
            { type: "fill_blank", question: "الجزء الذي يثبت النبات في التربة هو الـ ___", correctAnswer: "جذر", explanation: "الجذر يثبت النبات ويمتص الماء", points: 15 },
          ],
        },
      ],
    },
  ],
};

// Extend French lessons
export const grade1FrenchExtra: import("./types").LessonData[] = [
  {
    slug: "le-corps", titleAr: "أعضاء الجسم بالفرنسية", difficulty: "easy", durationMin: 20,
    objectives: ["تعلم أعضاء الجسم بالفرنسية", "الأرقام 11-20", "جمل وصفية بسيطة"],
    explanation: `أعضاء الجسم بالفرنسية:\n\nla tête = الرأس\nles yeux = العيون (مفرد: l'œil)\nle nez = الأنف\nla bouche = الفم\nles oreilles = الآذان\nles mains = اليدان\nles pieds = القدمان\nle ventre = البطن\n\nجملة: J'ai deux yeux. = عندي عينان.\nMon nez est petit. = أنفي صغير.`,
    vocabulary: [
      { word: "la tête", definition: "الرأس بالفرنسية" },
      { word: "les yeux", definition: "العيون بالفرنسية (مفردها l'œil)" },
      { word: "les mains", definition: "اليدان بالفرنسية" },
    ],
    examples: [{ text: "J'ai deux mains et deux pieds.", note: "عندي يدان وقدمان" }, { text: "Ma bouche est grande.", note: "فمي كبير" }],
    summary: "tête رأس | yeux عيون | nez أنف | bouche فم | mains يدان | pieds قدمان",
    exercises: [
      { type: "mcq", question: "ما معنى 'la tête'؟", options: ["الفم", "الرأس", "الأنف", "اليد"], correctAnswer: "الرأس", explanation: "la tête = الرأس بالفرنسية", points: 10 },
      { type: "mcq", question: "كيف تقول 'الأنف' بالفرنسية؟", options: ["la bouche", "les yeux", "le nez", "la tête"], correctAnswer: "le nez", explanation: "le nez = الأنف بالفرنسية", points: 10 },
      { type: "fill_blank", question: "العيون بالفرنسية: les ___", correctAnswer: "yeux", explanation: "les yeux = العيون (مفردها l'œil)", points: 15 },
      { type: "true_false", question: "'les mains' تعني اليدان", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — les mains = اليدان بالفرنسية", points: 10 },
    ],
  },
  {
    slug: "animaux-sg1", titleAr: "الحيوانات بالفرنسية", difficulty: "easy", durationMin: 20,
    objectives: ["أسماء الحيوانات بالفرنسية", "أصوات الحيوانات", "الجمع في الفرنسية"],
    explanation: `الحيوانات بالفرنسية:\n\nun chat = قطة 🐈\nun chien = كلب 🐕\nun cheval = حصان 🐴\nune vache = بقرة 🐄\nun lion = أسد 🦁\nun lapin = أرنب 🐰\nun oiseau = طائر 🐦\n\nللجمع نضيف s:\nchats = قطط | chiens = كلاب\n\nجملة: J'ai un chat. = عندي قطة.`,
    vocabulary: [
      { word: "chat", definition: "القطة بالفرنسية" },
      { word: "chien", definition: "الكلب بالفرنسية" },
      { word: "lion", definition: "الأسد بالفرنسية" },
    ],
    examples: [{ text: "Le lion est grand. = الأسد كبير.", note: "وصف بالفرنسية" }, { text: "J'aime les lapins. = أحب الأرانب.", note: "الإعجاب بالفرنسية" }],
    summary: "chat قطة | chien كلب | cheval حصان | vache بقرة | lion أسد | lapin أرنب",
    exercises: [
      { type: "mcq", question: "ما معنى 'un lion'؟", options: ["أرنب", "أسد", "كلب", "قطة"], correctAnswer: "أسد", explanation: "un lion = أسد بالفرنسية", points: 10 },
      { type: "mcq", question: "القطة بالفرنسية:", options: ["chien", "cheval", "chat", "lapin"], correctAnswer: "chat", explanation: "chat = قطة بالفرنسية", points: 10 },
      { type: "fill_blank", question: "الكلب بالفرنسية: un ___", correctAnswer: "chien", explanation: "un chien = كلب بالفرنسية", points: 15 },
      { type: "true_false", question: "'un lapin' تعني أرنب", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — un lapin = أرنب بالفرنسية", points: 10 },
    ],
  },
];

// Extend Islamic lessons
export const grade1IslamicExtra: import("./types").LessonData[] = [
  {
    slug: "tahaara", titleAr: "الطهارة والنظافة في الإسلام", difficulty: "easy", durationMin: 20,
    objectives: ["أهمية الطهارة في الإسلام", "الوضوء وخطواته", "النظافة الشخصية"],
    explanation: `الطهارة في الإسلام عبادة:\n\nالوضوء — شرط الصلاة:\n1️⃣ النية في القلب\n2️⃣ غسل اليدين 3 مرات\n3️⃣ المضمضة — غسل الفم\n4️⃣ استنشاق الماء بالأنف\n5️⃣ غسل الوجه\n6️⃣ غسل اليدين إلى المرفقين\n7️⃣ مسح الرأس\n8️⃣ غسل القدمين\n\nالنبي ﷺ قال: "النظافة من الإيمان"\n\nمن آداب النظافة الإسلامية:\n• قص الأظافر\n• السواك وتنظيف الأسنان\n• الاستحمام بانتظام`,
    vocabulary: [
      { word: "الوضوء", definition: "الطهارة بالماء قبل الصلاة وفق خطوات مخصوصة" },
      { word: "المرفق", definition: "المفصل بين الذراع والساعد" },
      { word: "استنشاق", definition: "سحب الماء إلى الأنف" },
    ],
    examples: [{ text: "نتوضأ قبل الصلاة", note: "الوضوء شرط لصحة الصلاة" }, { text: "النظافة من الإيمان — حديث النبي ﷺ", note: "أهمية النظافة في الإسلام" }],
    summary: "الوضوء: يدان + فم + أنف + وجه + يدان للمرفق + رأس + قدمان. النظافة من الإيمان.",
    exercises: [
      { type: "mcq", question: "نتوضأ قبل:", options: ["الأكل", "الصلاة", "النوم", "اللعب"], correctAnswer: "الصلاة", explanation: "الوضوء شرط لصحة الصلاة", points: 10 },
      { type: "mcq", question: "ماذا نغسل أولاً في الوضوء؟", options: ["الوجه", "القدمين", "اليدين", "الرأس"], correctAnswer: "اليدين", explanation: "أول خطوة في الوضوء بعد النية: غسل اليدين", points: 10 },
      { type: "true_false", question: "النظافة من الإيمان", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — هذا حديث النبي ﷺ الشريف", points: 10 },
      { type: "fill_blank", question: "نغسل اليدين إلى الـ ___ في الوضوء", correctAnswer: "مرفقين", explanation: "نغسل اليدين إلى المرفقين في الوضوء", points: 15 },
    ],
  },
  {
    slug: "quran-fatiha", titleAr: "سورة الفاتحة", difficulty: "easy", durationMin: 25,
    objectives: ["حفظ سورة الفاتحة", "فهم معانيها", "فضلها"],
    explanation: `سورة الفاتحة — أم القرآن\nتُقرأ في كل ركعة من الصلاة\n\nبِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n(بدأنا باسم الله الرحيم بعباده)\n\nالْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ\n(كل الحمد لله خالق الكون)\n\nالرَّحْمَٰنِ الرَّحِيمِ\n(الرحيم بعباده)\n\nمَالِكِ يَوْمِ الدِّينِ\n(يملك يوم الحساب)\n\nإِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ\n(نعبدك وحدك ونستعين بك)\n\nاهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ\n(وجّهنا للطريق الصحيح)\n\nصِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ\n(طريق الأنبياء والصالحين)\n\nغَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ\n(لا طريق الضالين)`,
    vocabulary: [
      { word: "العالمين", definition: "جميع المخلوقات في الكون" },
      { word: "الصراط المستقيم", definition: "الطريق الصحيح الذي يرضى الله عنه" },
      { word: "يوم الدين", definition: "يوم القيامة والحساب" },
    ],
    examples: [{ text: "نقرأ الفاتحة في كل ركعة من الصلاة", note: "أهمية الفاتحة" }, { text: "الفاتحة تسمى أم القرآن لأنها تجمع معاني القرآن", note: "لماذا تسمى أم القرآن" }],
    summary: "الفاتحة 7 آيات، تُقرأ في كل ركعة. تبدأ بالحمد وتطلب الهداية. تسمى أم القرآن.",
    exercises: [
      { type: "mcq", question: "كم عدد آيات سورة الفاتحة؟", options: ["5", "6", "7", "8"], correctAnswer: "7", explanation: "سورة الفاتحة 7 آيات", points: 10 },
      { type: "mcq", question: "متى نقرأ الفاتحة؟", options: ["قبل النوم فقط", "في كل ركعة من الصلاة", "يوم الجمعة فقط", "في رمضان فقط"], correctAnswer: "في كل ركعة من الصلاة", explanation: "الفاتحة ركن في كل ركعة — لا تصح الصلاة بدونها", points: 10 },
      { type: "true_false", question: "الفاتحة تسمى أم القرآن", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — تسمى الفاتحة 'أم القرآن' لجمعها معانيه", points: 10 },
      { type: "fill_blank", question: "الفاتحة هي أول سورة في الـ ___", correctAnswer: "قرآن", explanation: "الفاتحة أولى سور القرآن الكريم", points: 15 },
    ],
  },
];

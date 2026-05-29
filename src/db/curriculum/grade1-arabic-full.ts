/**
 * Grade 1 Arabic — Huruf lessons data
 * 8 seeded letters + pattern for remaining 20 via Admin Generator
 */

export interface LetterLesson {
  slug: string; titleAr: string; letter: string;
  words: { word: string; meaning: string }[];
  explanation: string;
  exercises: {
    type: "mcq" | "true_false" | "fill_blank";
    question: string; options?: string[];
    correctAnswer: string; explanation: string; points: number;
  }[];
}

export const ARABIC_LETTERS: LetterLesson[] = [
  {
    slug: "alef", titleAr: "حرف الألف", letter: "أ/إ/آ/ا",
    words: [{ word: "أرنب", meaning: "حيوان صغير يقفز" }, { word: "إبرة", meaning: "أداة خياطة دقيقة" }, { word: "آمل", meaning: "متفائل" }],
    explanation: "الألف أول الحروف. أشكاله: أَ (فتحة) كـ أَرنب | إِ (كسرة) كـ إِبرة | آ (مد) كـ آمِن | ا (ساكنة) كـ باب",
    exercises: [
      { type: "mcq", question: "ما الحرف الأول في الأبجدية؟", options: ["الباء","الألف","التاء","الجيم"], correctAnswer: "الألف", explanation: "الألف أول 28 حرفاً", points: 10 },
      { type: "mcq", question: "'إبرة' تبدأ بـ:", options: ["ألف مفتوحة","ألف مكسورة","ألف ممدودة","باء"], correctAnswer: "ألف مكسورة", explanation: "إِبرة: الهمزة مكسورة", points: 10 },
      { type: "true_false", question: "كلمة 'باب' تحتوي الألف الساكنة", options: ["صحيح","خطأ"], correctAnswer: "صحيح", explanation: "با-ب: الألف ساكنة في المنتصف", points: 10 },
      { type: "fill_blank", question: "أكمل: _رنب (حيوان صغير)", correctAnswer: "أ", explanation: "أَرنب بهمزة مفتوحة", points: 15 },
    ],
  },
  {
    slug: "baa", titleAr: "حرف الباء", letter: "ب",
    words: [{ word: "بيت", meaning: "مكان السكن" }, { word: "باب", meaning: "مدخل البيت" }, { word: "بقرة", meaning: "حيوان الحليب" }],
    explanation: "الباء صوتها 'بْ' — نقطة واحدة تحت. بـ في البداية | ـبـ في الوسط | ـب في النهاية",
    exercises: [
      { type: "mcq", question: "كم نقطة تحت الباء؟", options: ["صفر","نقطة واحدة","نقطتان","ثلاث"], correctAnswer: "نقطة واحدة", explanation: "الباء: نقطة واحدة تحت", points: 10 },
      { type: "mcq", question: "الباء في 'كتاب' تقع:", options: ["أول","وسط","آخر","لا توجد"], correctAnswer: "آخر", explanation: "ك-ت-ا-ب: الباء في النهاية", points: 10 },
      { type: "true_false", question: "كلمة 'بقرة' تبدأ بالباء", options: ["صحيح","خطأ"], correctAnswer: "صحيح", explanation: "بَقرة: الباء في البداية", points: 10 },
      { type: "fill_blank", question: "أكمل: _يت (مكان السكن)", correctAnswer: "ب", explanation: "بَيت يبدأ بالباء", points: 15 },
    ],
  },
  {
    slug: "taa", titleAr: "حرف التاء", letter: "ت",
    words: [{ word: "تفاحة", meaning: "فاكهة حمراء" }, { word: "تلميذ", meaning: "الطفل في المدرسة" }, { word: "تمر", meaning: "ثمرة النخلة" }],
    explanation: "التاء مثل الباء لكن بنقطتين فوق (وليس تحت). ب=نقطة تحت | ت=نقطتان فوق",
    exercises: [
      { type: "mcq", question: "الفرق بين ب وت:", options: ["الشكل","النقاط","الحجم","الصوت"], correctAnswer: "النقاط", explanation: "ب: نقطة تحت | ت: نقطتان فوق", points: 10 },
      { type: "mcq", question: "كم نقطة فوق التاء؟", options: ["صفر","واحدة","نقطتان","ثلاث"], correctAnswer: "نقطتان", explanation: "التاء: نقطتان فوق", points: 10 },
      { type: "fill_blank", question: "أكمل: _فاحة (فاكهة)", correctAnswer: "ت", explanation: "تُفاحة تبدأ بالتاء", points: 15 },
    ],
  },
  {
    slug: "thaa", titleAr: "حرف الثاء", letter: "ث",
    words: [{ word: "ثعلب", meaning: "حيوان ذكي في الغابة" }, { word: "ثلاثة", meaning: "العدد 3" }, { word: "ثوب", meaning: "قطعة ملابس" }],
    explanation: "الثاء مثل التاء لكن بثلاث نقاط فوق. ب=نقطة تحت | ت=نقطتان فوق | ث=ثلاث نقاط فوق",
    exercises: [
      { type: "mcq", question: "كم نقطة فوق الثاء؟", options: ["واحدة","اثنتان","ثلاث","أربع"], correctAnswer: "ثلاث", explanation: "الثاء لها ثلاث نقاط — مثل عدد اسمها!", points: 10 },
      { type: "true_false", question: "الثاء والتاء لهما نفس الشكل بدون نقاط", options: ["صحيح","خطأ"], correctAnswer: "صحيح", explanation: "نعم — فقط عدد النقاط يختلف", points: 10 },
    ],
  },
  {
    slug: "jeem", titleAr: "حرف الجيم", letter: "ج",
    words: [{ word: "جمل", meaning: "حيوان الصحراء" }, { word: "جبل", meaning: "تلة عالية" }, { word: "جزرة", meaning: "خضرة برتقالية" }],
    explanation: "الجيم صوتها 'جْ' بنقطة واحدة في المنتصف. جـ في البداية | ـجـ في الوسط | ـج في النهاية",
    exercises: [
      { type: "mcq", question: "أين نقطة الجيم؟", options: ["تحت","فوق","وسط الحرف","لا نقطة"], correctAnswer: "وسط الحرف", explanation: "الجيم: نقطة في داخل الحرف", points: 10 },
      { type: "fill_blank", question: "أكمل: _مل (حيوان الصحراء)", correctAnswer: "ج", explanation: "جَمل يبدأ بالجيم", points: 15 },
    ],
  },
  {
    slug: "haa-h", titleAr: "حرف الحاء", letter: "ح",
    words: [{ word: "حصان", meaning: "حيوان الفارس" }, { word: "حليب", meaning: "شراب أبيض من البقرة" }, { word: "حديقة", meaning: "مكان الأشجار والزهور" }],
    explanation: "الحاء تشبه الجيم لكن بدون نقطة. ج بنقطة وسط | ح بدون نقطة | خ بنقطة فوق",
    exercises: [
      { type: "mcq", question: "الفرق بين ح وج:", options: ["الشكل","النقطة","الحجم","الصوت"], correctAnswer: "النقطة", explanation: "ج بنقطة في الوسط | ح بدون نقطة", points: 10 },
      { type: "true_false", question: "الحاء لها نقطة فوقها", options: ["صحيح","خطأ"], correctAnswer: "خطأ", explanation: "الحاء بدون نقاط — الخاء فوقها نقطة", points: 10 },
    ],
  },
  {
    slug: "khaa", titleAr: "حرف الخاء", letter: "خ",
    words: [{ word: "خبز", meaning: "الخبزة المغربية" }, { word: "خروف", meaning: "حيوان الصوف" }, { word: "خيمة", meaning: "بيت الصحراء" }],
    explanation: "الخاء مثل الحاء بنقطة فوق. الأسرة: ج (نقطة وسط) | ح (بدون) | خ (نقطة فوق)",
    exercises: [
      { type: "mcq", question: "الخبز المغربي يبدأ بـ:", options: ["حاء","جيم","خاء","كاف"], correctAnswer: "خاء", explanation: "خُبز بالخاء", points: 10 },
      { type: "true_false", question: "الخاء تشبه الحاء بنقطة فوق", options: ["صحيح","خطأ"], correctAnswer: "صحيح", explanation: "نعم — الشكل واحد والفرق هو النقطة", points: 10 },
    ],
  },
  {
    slug: "dal", titleAr: "حرف الدال", letter: "د",
    words: [{ word: "دجاجة", meaning: "طير البيض" }, { word: "دار", meaning: "البيت الكبير" }, { word: "دفتر", meaning: "كراسة الدروس" }],
    explanation: "الدال شكله كالهلال الصغير، بدون نقطة. الدال والذال متشابهان — الذال بنقطة فوق",
    exercises: [
      { type: "mcq", question: "الدجاجة تبدأ بـ:", options: ["ذال","دال","راء","زاي"], correctAnswer: "دال", explanation: "دَجاجة بالدال", points: 10 },
      { type: "true_false", question: "الدال والذال لهما نفس الشكل", options: ["صحيح","خطأ"], correctAnswer: "صحيح", explanation: "نعم — فقط الذال فوقها نقطة", points: 10 },
    ],
  },
];

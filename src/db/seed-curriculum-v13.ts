/**
 * seed-curriculum-v13.ts — Phase 36 Merge
 * Path: src/db/seed-curriculum-v13.ts
 *
 * Seeds the database with 24 complete lessons from v13 (real content,
 * Moroccan examples, quizQuestions for each lesson).
 *
 * Run: npm run db:seed:v13
 *
 * Requires: db:seed (base data — grades/subjects/units) to run first.
 * This script ADDS lessons ON TOP of the existing seed.
 *
 * Uses onConflictDoNothing so it's safe to run multiple times.
 */

import "dotenv/config";
import { db }    from "@/db";
import * as schema from "@/db/schema";
import { eq, and } from "drizzle-orm";

// ── Lesson content data (from v13 curriculum-seed-data.ts) ────────────────────
// Full content: introduction, mainText, explanation, Moroccan examples,
// exercises, and 5 quiz questions per lesson.

const LESSONS_DATA = [
  // ═══ السنة الأولى — الرياضيات ════════════════════════════════════════════
  {
    grade: "1", subject: "الرياضيات", title: "الأعداد من 0 إلى 5",
    unit: 1, order: 1,
    objectives: ["التعرف على الأعداد 0-5", "كتابتها بالأرقام", "ربطها بالكميات"],
    keyWords: ["صفر", "واحد", "اثنان", "ثلاثة", "أربعة", "خمسة", "عدد", "كمية"],
    content: {
      introduction: "نبدأ رحلتنا مع الأعداد من الصفر إلى خمسة.",
      mainText: `الأعداد من 0 إلى 5:\n0 = صفر (لا شيء)\n1 = واحد 🍎\n2 = اثنان 🍎🍎\n3 = ثلاثة 🍎🍎🍎\n4 = أربعة 🍎🍎🍎🍎\n5 = خمسة 🍎🍎🍎🍎🍎\n\nالترتيب: 0 < 1 < 2 < 3 < 4 < 5`,
      explanation: "تخيل أن عندك تفاحات. 0 تفاحة = الطبق فارغ. كلما أضفت تفاحة، الرقم يكبر بواحد!",
      examples: "🇲🇦 من حياتنا:\n• 0: الطبق فارغ — لا خبز\n• 1: خبزة واحدة في يدك\n• 2: كوزتين من الزيتون\n• 3: 3 شمعات في عيد الميلاد\n• 4: 4 أرجل للكرسي\n• 5: أصابع يد واحدة",
      summary: "الأعداد 0-5 تمثل كميات من لا شيء إلى خمسة.",
    },
    exercises: [
      { q: "كم عدد الأصابع في يد واحدة؟", type: "text", answer: "5" },
      { q: "ما العدد الذي يأتي بعد 2؟", type: "text", answer: "3" },
    ],
    quizQuestions: [
      { q: "ما العدد الذي يأتي بعد 4؟", options: ["3", "5", "6", "2"], correct: 1, explanation: "بعد 4 يأتي 5 في ترتيب الأعداد." },
      { q: "أي عدد يعني 'لا شيء'؟", options: ["1", "2", "0", "3"], correct: 2, explanation: "الصفر (0) يعني لا شيء أو فارغ." },
      { q: "ما العدد الذي بين 2 و4؟", options: ["1", "3", "5", "0"], correct: 1, explanation: "بين 2 و4 يأتي العدد 3." },
      { q: "كم تفاحة في 3 أطباق كل طبق فيه تفاحة؟", options: ["1", "2", "3", "4"], correct: 2, explanation: "3 أطباق × 1 تفاحة = 3 تفاحات." },
      { q: "أي العددين أكبر: 2 أم 5؟", options: ["2", "5", "متساويان", "لا أعرف"], correct: 1, explanation: "5 أكبر من 2 لأنه يأتي بعده في الترتيب." },
    ],
  },
  {
    grade: "1", subject: "الرياضيات", title: "الأعداد من 6 إلى 10",
    unit: 1, order: 2,
    objectives: ["التعرف على الأعداد 6-10", "قراءتها وكتابتها", "مقارنتها"],
    keyWords: ["ستة", "سبعة", "ثمانية", "تسعة", "عشرة", "مقارنة"],
    content: {
      introduction: "بعد أن تعلمنا 0-5، نكمل مع الأعداد 6-10 — أصابع اليدين كلتيهما!",
      mainText: "6 = ستة ✋👆\n7 = سبعة ✋👆👆\n8 = ثمانية ✋👆👆👆\n9 = تسعة ✋👆👆👆👆\n10 = عشرة ✋✋\n\nالترتيب: 6 < 7 < 8 < 9 < 10",
      explanation: "أصابع يدك اليمنى = 5. أضف أصابع اليسرى: 6، 7، 8، 9، 10!",
      examples: "• 6: ضلوع النجمة ⭐\n• 7: أيام الأسبوع\n• 8: أرجل العنكبوت\n• 9: لاعبو فريق البيسبول\n• 10: أصابع اليدين كلتيهما",
      summary: "الأعداد 6-10 تكمل العقد الأول. 10 = عشرة = ✋✋",
    },
    exercises: [
      { q: "كم يوماً في الأسبوع؟", type: "text", answer: "7" },
      { q: "ما العدد بعد 9؟", type: "text", answer: "10" },
    ],
    quizQuestions: [
      { q: "كم أصبعاً في اليدين معاً؟", options: ["8", "9", "10", "7"], correct: 2, explanation: "5 + 5 = 10 أصابع في اليدين." },
      { q: "ما العدد بين 7 و9؟", options: ["6", "8", "10", "5"], correct: 1, explanation: "بين 7 و9 يأتي العدد 8." },
      { q: "أي عدد أكبر: 6 أم 9؟", options: ["6", "9", "متساويان", "لا أعرف"], correct: 1, explanation: "9 أكبر من 6." },
      { q: "كم يوماً في الأسبوع؟", options: ["5", "6", "7", "8"], correct: 2, explanation: "الأسبوع = 7 أيام: الاثنين إلى الأحد." },
      { q: "ما العدد الذي يأتي قبل 10؟", options: ["11", "8", "9", "7"], correct: 2, explanation: "قبل 10 يأتي 9." },
    ],
  },
  {
    grade: "1", subject: "الرياضيات", title: "الجمع حتى 10",
    unit: 2, order: 1,
    objectives: ["فهم مفهوم الجمع", "حساب مجاميع حتى 10"],
    keyWords: ["جمع", "مجموع", "يساوي", "+", "="],
    content: {
      introduction: "الجمع يعني إضافة شيء إلى آخر — مثل إضافة تمرات إلى طبق!",
      mainText: "الجمع = إضافة عدد إلى عدد آخر\n\nأمثلة:\n2 + 3 = 5\n4 + 1 = 5\n3 + 3 = 6\n5 + 5 = 10",
      explanation: "فكّر في أصابعك! عندك 3 تمرات في اليمين و4 في اليسار. كم عندك؟ 3 + 4 = 7 تمرات!",
      examples: "🇲🇦 من حياتنا:\n• عندك 2 خبزة في الصباح + 3 في المساء = 5 خبزات\n• 4 أولاد في القسم + 3 بنات = 7 تلاميذ\n• 1 درهم + 2 درهم = 3 دراهم",
      summary: "الجمع يعطينا المجموع. 3 + 4 = 7 ← المجموع",
    },
    exercises: [
      { q: "احسب: 5 + 3 = ?", type: "text", answer: "8" },
      { q: "احسب: 2 + 7 = ?", type: "text", answer: "9" },
    ],
    quizQuestions: [
      { q: "ما هو مجموع 4 + 5؟", options: ["8", "9", "10", "7"], correct: 1, explanation: "4 + 5 = 9." },
      { q: "ما هو مجموع 6 + 4؟", options: ["9", "11", "10", "8"], correct: 2, explanation: "6 + 4 = 10." },
      { q: "ما هو مجموع 3 + 3؟", options: ["5", "7", "6", "4"], correct: 2, explanation: "3 + 3 = 6." },
      { q: "ما مجموع 1 + 9؟", options: ["8", "10", "11", "9"], correct: 1, explanation: "1 + 9 = 10." },
      { q: "عندك 5 تفاحات وأضفت 2. كم عندك؟", options: ["6", "7", "8", "5"], correct: 1, explanation: "5 + 2 = 7 تفاحات." },
    ],
  },
  // ═══ السنة الأولى — اللغة العربية ════════════════════════════════════════
  {
    grade: "1", subject: "اللغة العربية", title: "حروف أ، ب، ت، ث",
    unit: 1, order: 1,
    objectives: ["التعرف على الحروف الهجائية الأولى", "نطقها وكتابتها"],
    keyWords: ["ألف", "باء", "تاء", "ثاء", "حرف", "هجاء"],
    content: {
      introduction: "نبدأ رحلتنا مع الحروف الهجائية — لبنات اللغة العربية.",
      mainText: "أ — ألف: أسد، أرنب، أم\nب — باء: باب، بيت، بنت\nت — تاء: تفاحة، تمر، تلميذ\nث — ثاء: ثعلب، ثلاثة، ثوب",
      explanation: "كل حرف له صوت خاص. مثل موسيقى! أ = 'آ'، ب = 'بَ'، ت = 'تَ'، ث = 'ثَ'",
      examples: "🇲🇦 كلمات مغربية:\n• أرض: هي الأرض التي نسير عليها\n• باب: كل بيت له باب\n• تمر: الفاكهة التي تؤكل في رمضان\n• ثلاجة: توضع فيها الأطعمة",
      summary: "أ ب ت ث — أربعة حروف من أوائل الأبجدية العربية.",
    },
    exercises: [
      { q: "ما الحرف الأول في كلمة 'أرنب'؟", type: "text", answer: "أ" },
      { q: "ما الحرف الأول في كلمة 'باب'؟", type: "text", answer: "ب" },
    ],
    quizQuestions: [
      { q: "ما الحرف الأول في الأبجدية؟", options: ["ب", "أ", "ت", "ث"], correct: 1, explanation: "الألف 'أ' هو أول حرف في الأبجدية العربية." },
      { q: "أي كلمة تبدأ بحرف 'ب'؟", options: ["تفاحة", "أسد", "باب", "ثعلب"], correct: 2, explanation: "باب تبدأ بحرف الباء." },
      { q: "ما الحرف الثالث في الأبجدية؟", options: ["أ", "ب", "ت", "ث"], correct: 2, explanation: "الترتيب: أ، ب، ت. التاء هي الثالثة." },
      { q: "أي كلمة تبدأ بحرف 'ث'؟", options: ["تمر", "ثعلب", "باب", "أرنب"], correct: 1, explanation: "ثعلب تبدأ بحرف الثاء." },
      { q: "كم حرفاً تعلمنا في هذا الدرس؟", options: ["2", "3", "4", "5"], correct: 2, explanation: "تعلمنا 4 حروف: أ، ب، ت، ث." },
    ],
  },
  // ═══ السنة الثانية ════════════════════════════════════════════════════════
  {
    grade: "2", subject: "الرياضيات", title: "الأعداد حتى 100",
    unit: 1, order: 1,
    objectives: ["قراءة الأعداد حتى 100", "الآحاد والعشرات", "المقارنة"],
    keyWords: ["عشرة", "عشرات", "آحاد", "مئة", "مقارنة", "أكبر", "أصغر"],
    content: {
      introduction: "بعد العشرة نعدّ بالعشرات حتى نصل لـ100!",
      mainText: "العشرات: 10، 20، 30، 40، 50، 60، 70، 80، 90، 100\n\nكل عدد فيه آحاد وعشرات:\n45 = 4 عشرات + 5 آحاد\n73 = 7 عشرات + 3 آحاد\n100 = 10 عشرات",
      explanation: "تخيل الدراهم! 10 دراهم = ورقة واحدة. 3 ورقات = 30 درهم. 3 ورقات + 5 قطع = 35 درهم!",
      examples: "🇲🇦 من حياتنا:\n• خبزة: 3 دراهم → 3 آحاد\n• حافلة: 10 دراهم → 1 عشرة\n• كتاب: 45 درهم → 4 عشرات + 5 آحاد\n• لعبة: 100 درهم → مئة",
      summary: "الأعداد حتى 100 = آحاد (1-9) + عشرات (10-90) + مئة (100).",
    },
    exercises: [
      { q: "اكتب بالأرقام: ستة وسبعون", type: "text", answer: "76" },
      { q: "كم عشرة في العدد 80؟", type: "text", answer: "8" },
    ],
    quizQuestions: [
      { q: "كم آحاداً في العدد 57؟", options: ["5", "7", "2", "12"], correct: 1, explanation: "57 = 5 عشرات + 7 آحاد. الآحاد هي 7." },
      { q: "ما الأكبر: 63 أم 36؟", options: ["36", "63", "متساويان", "لا أعرف"], correct: 1, explanation: "63 أكبر لأن عشراته (6) أكبر من عشرات 36 (3)." },
      { q: "كم عشرة في 70؟", options: ["7", "0", "70", "17"], correct: 0, explanation: "70 = 7 عشرات + 0 آحاد." },
      { q: "ما الذي يساوي 3 عشرات + 8 آحاد؟", options: ["83", "38", "30", "80"], correct: 1, explanation: "3 عشرات + 8 آحاد = 38." },
      { q: "ما العدد بين 49 و51؟", options: ["48", "52", "50", "45"], correct: 2, explanation: "50 يقع بين 49 و51." },
    ],
  },
  {
    grade: "2", subject: "اللغة العربية", title: "المفرد والجمع",
    unit: 2, order: 1,
    objectives: ["التمييز بين المفرد والجمع", "تحويل الكلمات من مفرد لجمع"],
    keyWords: ["مفرد", "جمع", "جمع مذكر سالم", "جمع مؤنث سالم", "جمع التكسير"],
    content: {
      introduction: "المفرد = شيء واحد. الجمع = أكثر من واحد!",
      mainText: "المفرد: كتاب، قلم، ولد، بنت\nالجمع:\n• كتاب → كُتُب\n• قلم → أقلام\n• ولد → أولاد\n• بنت → بنات",
      explanation: "عندك 'تفاحة' واحدة — هذا مفرد. عندك أكثر من تفاحة — 'تفاحات' — هذا جمع!",
      examples: "🇲🇦 من البيت المغربي:\n• خبزة → خبز\n• طاجين → طواجن\n• دريسة → دراريس\n• طريق → طرقات",
      summary: "المفرد = واحد. الجمع = أكثر من واحد.",
    },
    exercises: [
      { q: "حوّل للجمع: قلم", type: "text", answer: "أقلام" },
      { q: "حوّل للمفرد: بنات", type: "text", answer: "بنت" },
    ],
    quizQuestions: [
      { q: "ما جمع 'كتاب'؟", options: ["كتابات", "كُتُب", "كتابون", "أكتاب"], correct: 1, explanation: "جمع كتاب هو كُتُب (جمع تكسير)." },
      { q: "ما مفرد 'أولاد'؟", options: ["أولادة", "والد", "ولد", "ولدان"], correct: 2, explanation: "مفرد أولاد هو ولد." },
      { q: "أيٌّ من التالي جمع؟", options: ["قلم", "باب", "أقلام", "بيت"], correct: 2, explanation: "أقلام جمع لكلمة قلم." },
      { q: "ما جمع 'بنت'؟", options: ["بنتان", "بنات", "بنتون", "أبنت"], correct: 1, explanation: "جمع بنت هو بنات." },
      { q: "الكلمة 'تلاميذ' هي:", options: ["مفرد", "جمع", "مثنى", "لا شيء"], correct: 1, explanation: "تلاميذ جمع لكلمة تلميذ." },
    ],
  },
  // ═══ السنة الثالثة ════════════════════════════════════════════════════════
  {
    grade: "3", subject: "الرياضيات", title: "الضرب — الجدول الكامل",
    unit: 1, order: 1,
    objectives: ["حفظ جداول الضرب 1-10", "تطبيق الضرب في المسائل"],
    keyWords: ["ضرب", "جداول", "حاصل الضرب", "مضروب", "مضروب فيه"],
    content: {
      introduction: "الضرب هو جمع متكرر! 3 × 4 = 4 + 4 + 4 = 12",
      mainText: "جدول الضرب في 2: 1×2=2، 2×2=4، 3×2=6...\nجدول الضرب في 5: 1×5=5، 2×5=10، 3×5=15...\nجدول الضرب في 10: 1×10=10، 2×10=20...",
      explanation: "تخيل لديك 4 أكياس، في كل كيس 3 تفاحات. الإجمالي: 4 × 3 = 12 تفاحة!",
      examples: "🇲🇦 الضرب في الحياة:\n• 5 أسرة × 4 أشخاص = 20 شخصاً\n• 3 أيام × 10 دراهم = 30 درهماً\n• 7 أسابيع × 7 أيام = 49 يوماً",
      summary: "الضرب = جمع متكرر. a × b = b + b + ... (a مرة)",
    },
    exercises: [
      { q: "احسب: 7 × 8 = ?", type: "text", answer: "56" },
      { q: "احسب: 9 × 6 = ?", type: "text", answer: "54" },
    ],
    quizQuestions: [
      { q: "ما حاصل 6 × 7؟", options: ["42", "48", "36", "56"], correct: 0, explanation: "6 × 7 = 42." },
      { q: "ما حاصل 8 × 9؟", options: ["63", "72", "81", "64"], correct: 1, explanation: "8 × 9 = 72." },
      { q: "ما حاصل 5 × 5؟", options: ["20", "30", "25", "15"], correct: 2, explanation: "5 × 5 = 25." },
      { q: "إذا كان 4 × _ = 32، فما الناتج؟", options: ["6", "8", "9", "7"], correct: 1, explanation: "4 × 8 = 32." },
      { q: "ما حاصل 3 × 9؟", options: ["24", "27", "21", "30"], correct: 1, explanation: "3 × 9 = 27." },
    ],
  },
  {
    grade: "3", subject: "النشاط العلمي", title: "النباتات وحياتها",
    unit: 1, order: 1,
    objectives: ["التعرف على أجزاء النبات", "فهم عملية البناء الضوئي"],
    keyWords: ["جذر", "ساق", "ورقة", "زهرة", "ثمرة", "بناء ضوئي", "ضوء", "ماء"],
    content: {
      introduction: "النباتات كائنات حية رائعة تصنع غذاءها من الشمس!",
      mainText: "أجزاء النبات:\n• الجذر: يمتص الماء والمعادن من التربة\n• الساق: تنقل الماء والغذاء\n• الورقة: مصنع الغذاء (البناء الضوئي)\n• الزهرة: للتكاثر\n• الثمرة: تحمي البذور",
      explanation: "الورقة مثل مصنع صغير! تأخذ ضوء الشمس + ماء + ثاني أكسيد الكربون → وتصنع السكر + الأكسجين!",
      examples: "🇲🇦 نباتات مغربية:\n• الأركان: شجرة مغربية تنتج زيت الأركان\n• النعناع: يُستخدم في الشاي المغربي\n• الحنة: تلوّن الأيدي في الأعراس\n• اللوز: يُزرع في جبال الأطلس",
      summary: "النبات: جذر + ساق + ورقة (مصنع الغذاء) + زهرة + ثمرة.",
    },
    exercises: [
      { q: "ما وظيفة الجذر؟", type: "text", answer: "امتصاص الماء والمعادن من التربة" },
      { q: "أين يحدث البناء الضوئي؟", type: "text", answer: "في الورقة" },
    ],
    quizQuestions: [
      { q: "أي جزء من النبات يمتص الماء؟", options: ["الساق", "الورقة", "الجذر", "الزهرة"], correct: 2, explanation: "الجذر يمتص الماء والمعادن من التربة." },
      { q: "ماذا تصنع الورقة في البناء الضوئي؟", options: ["الماء", "السكر والأكسجين", "ثاني أكسيد الكربون", "البروتين"], correct: 1, explanation: "الورقة تصنع السكر (الغذاء) والأكسجين." },
      { q: "ما وظيفة الزهرة؟", options: ["امتصاص الماء", "التكاثر", "صنع الغذاء", "حمل الغذاء"], correct: 1, explanation: "الزهرة للتكاثر وإنتاج البذور." },
      { q: "ماذا تحتاج الورقة للبناء الضوئي؟", options: ["الظلام فقط", "الضوء والماء وثاني أكسيد الكربون", "التربة فقط", "الهواء فقط"], correct: 1, explanation: "البناء الضوئي يحتاج: ضوء + ماء + ثاني أكسيد الكربون." },
      { q: "ما الشجرة المغربية المشهورة التي تنتج زيتاً خاصاً؟", options: ["الزيتون", "الأركان", "التين", "العناب"], correct: 1, explanation: "شجرة الأركان مغربية 100% وزيتها مشهور عالمياً." },
    ],
  },
  // ═══ السنة الرابعة ════════════════════════════════════════════════════════
  {
    grade: "4", subject: "الرياضيات", title: "الكسور — القراءة والكتابة والمقارنة",
    unit: 1, order: 1,
    objectives: ["تعريف الكسر", "قراءة وكتابة الكسور", "مقارنة كسرين"],
    keyWords: ["كسر", "بسط", "مقام", "نصف", "ثلث", "ربع", "مقارنة", "تكافؤ"],
    content: {
      introduction: "الكسر يمثل جزءاً من كل. مثل قطعة من البيتزا!",
      mainText: "الكسر = البسط / المقام\n• البسط: الأجزاء التي أخذناها\n• المقام: مجموع الأجزاء\n\nأمثلة:\n1/2 = نصف\n1/3 = ثلث\n1/4 = ربع\n3/4 = ثلاثة أرباع",
      explanation: "قُطّعت خبزة لـ4 أجزاء متساوية. أخذت جزأين → أخذت 2/4 = نصف الخبزة!",
      examples: "🇲🇦 من حياتنا:\n• ربع البطيخ = 1/4\n• نصف الخبزة = 1/2\n• ثلثا الكيلو من الزيتون = 2/3\n• ثلاثة أرباع الساعة = 45 دقيقة",
      summary: "الكسر = بسط/مقام. المقام = الكل. البسط = الجزء الذي أخذناه.",
    },
    exercises: [
      { q: "اكتب بالأرقام: ثلاثة أخماس", type: "text", answer: "3/5" },
      { q: "ما أكبر: 3/4 أم 1/4؟", type: "text", answer: "3/4" },
    ],
    quizQuestions: [
      { q: "في الكسر 3/5 ما هو المقام؟", options: ["3", "5", "8", "2"], correct: 1, explanation: "المقام هو العدد الأسفل — 5." },
      { q: "ما الأكبر: 1/2 أم 1/4؟", options: ["1/4", "1/2", "متساويان", "لا يمكن المقارنة"], correct: 1, explanation: "1/2 أكبر. كلما كبر المقام، صغُر الكسر." },
      { q: "ما يساوي نصف؟", options: ["1/3", "2/4", "1/4", "3/4"], correct: 1, explanation: "2/4 = 1/2 (نضرب وتقسم: كلاهما نصف)." },
      { q: "أخذت 2 شرائح من بيتزا مقسمة لـ8. ما الكسر؟", options: ["2/6", "8/2", "2/8", "6/8"], correct: 2, explanation: "أخذت 2 من أصل 8 → الكسر = 2/8." },
      { q: "ما مجموع 1/4 + 1/4؟", options: ["1/8", "2/4", "2/8", "1/2"], correct: 1, explanation: "1/4 + 1/4 = 2/4 (نجمع البسطَين والمقام ثابت)." },
    ],
  },
  {
    grade: "4", subject: "اللغة العربية", title: "الفعل المضارع وعلاماته",
    unit: 2, order: 1,
    objectives: ["التعرف على الفعل المضارع", "علاماته ودلالاته الزمنية"],
    keyWords: ["فعل", "مضارع", "يتصدر", "حروف المضارعة", "أنيت", "حاضر", "مستقبل"],
    content: {
      introduction: "الفعل المضارع يدل على الحاضر أو المستقبل — ما يحدث الآن أو سيحدث.",
      mainText: "علامات الفعل المضارع:\n1. يتصدره أحد حروف المضارعة: أ، ن، ي، ت (أَنَيْت)\n2. يقبل السين وسوف: سيدرس، سوف يجيء\n3. يقبل لم ولن: لم يقرأ، لن يتأخر\n\nأمثلة: يدرس، تكتب، نلعب، أقرأ",
      explanation: "كلمة 'يلعب' = مضارع. لماذا؟ لأنها تبدأ بـ'ي' ويمكن أن نقول 'لم يلعب' أو 'سيلعب'!",
      examples: "🇲🇦 جمل بالفعل المضارع:\n• يذهب التلاميذ إلى المدرسة كل يوم.\n• تطبخ أمي الكسكس في الجمعة.\n• نلعب في الملعب بعد الدراسة.\n• يبيع التاجر التوابل في السوق.",
      summary: "الفعل المضارع: يبدأ بأنيت + يقبل السين وسوف ولم ولن.",
    },
    exercises: [
      { q: "استخرج الفعل المضارع: 'تحب فاطمة القراءة'", type: "text", answer: "تحب" },
      { q: "حوّل للمضارع: 'ذهب'", type: "text", answer: "يذهب" },
    ],
    quizQuestions: [
      { q: "أيٌّ من التالي فعل مضارع؟", options: ["ذهب", "كتب", "يقرأ", "لعب"], correct: 2, explanation: "'يقرأ' مضارع لأنه يبدأ بحرف المضارعة 'ي'." },
      { q: "ما حروف المضارعة؟", options: ["ب ت ث ج", "أ ن ي ت", "م ن ل ه", "ق ر س ص"], correct: 1, explanation: "حروف المضارعة: أ، ن، ي، ت — كلمة (أَنَيْت)." },
      { q: "أيٌّ من الجمل يحتوي على فعل مضارع؟", options: ["ذهب علي.", "سيذهب علي غداً.", "ذهب علي أمس.", "ذهاب علي مفيد."], correct: 1, explanation: "'سيذهب' مضارع (يقبل السين)." },
      { q: "الفعل المضارع يدل على:", options: ["الماضي فقط", "الحاضر أو المستقبل", "الأمر فقط", "الماضي والمستقبل"], correct: 1, explanation: "المضارع يدل على الحاضر أو المستقبل." },
      { q: "حوّل 'يكتب' إلى ماضٍ:", options: ["كتابة", "كاتب", "كَتَبَ", "مكتوب"], correct: 2, explanation: "ماضي 'يكتب' هو 'كَتَبَ'." },
    ],
  },
  // ═══ السنة الخامسة ════════════════════════════════════════════════════════
  {
    grade: "5", subject: "الرياضيات", title: "الأعداد العشرية — العمليات",
    unit: 1, order: 1,
    objectives: ["إجراء العمليات على الأعداد العشرية", "ضبط الفاصلة العشرية"],
    keyWords: ["عشري", "فاصلة", "جمع", "طرح", "ضرب", "قسمة", "دقة"],
    content: {
      introduction: "الأعداد العشرية تعطينا دقة أكبر من الأعداد الصحيحة!",
      mainText: "الجمع والطرح: نرتب الفاصلات فوق بعض!\n  12.50\n+  3.75\n------\n  16.25\n\nالضرب: نضرب ثم نضع الفاصلة\n2.5 × 3 = 7.5\n\nالقسمة: نحوّل إلى أعداد صحيحة أولاً",
      explanation: "عند دفع الثمن في الدكان: لديك 20.50 درهماً، اشتريت شيئاً بـ 8.75 — كم تبقى؟\n20.50 - 8.75 = 11.75 درهماً",
      examples: "🇲🇦 في السوق المغربي:\n• 1.5 كغ لحم × 65 درهم = 97.5 درهم\n• 2.75 كغ برتقال × 8 دراهم = 22 درهماً\n• 50 - 13.60 = 36.40 درهماً بقية",
      summary: "الفاصلة العشرية تفصل الجزء الصحيح عن الكسري. نرتّبها في الجمع والطرح.",
    },
    exercises: [
      { q: "احسب: 15.75 + 8.50 = ?", type: "text", answer: "24.25" },
      { q: "احسب: 30 - 12.75 = ?", type: "text", answer: "17.25" },
    ],
    quizQuestions: [
      { q: "ما ناتج 3.5 + 2.7؟", options: ["5.2", "6.2", "5.12", "6.12"], correct: 1, explanation: "3.5 + 2.7 = 6.2" },
      { q: "ما ناتج 10.0 - 4.5؟", options: ["5.5", "6.5", "5.0", "4.5"], correct: 0, explanation: "10.0 - 4.5 = 5.5" },
      { q: "ما ناتج 2.5 × 4؟", options: ["8.0", "10.0", "6.0", "9.0"], correct: 1, explanation: "2.5 × 4 = 10.0" },
      { q: "أيٌّ أكبر: 3.9 أم 4.1؟", options: ["3.9", "4.1", "متساويان", "لا يمكن المقارنة"], correct: 1, explanation: "4.1 أكبر لأن جزءها الصحيح أكبر." },
      { q: "عندك 50 درهم وأنفقت 23.50. كم تبقى؟", options: ["26.50", "27.50", "26.00", "27.00"], correct: 0, explanation: "50 - 23.50 = 26.50 درهماً." },
    ],
  },
  {
    grade: "5", subject: "النشاط العلمي", title: "الجهاز التنفسي",
    unit: 2, order: 1,
    objectives: ["التعرف على أعضاء الجهاز التنفسي", "فهم آلية التنفس"],
    keyWords: ["رئة", "قصبة هوائية", "حجاب حاجز", "شهيق", "زفير", "أكسجين", "ثاني أكسيد الكربون"],
    content: {
      introduction: "الجهاز التنفسي يجلب الأكسجين لجسمك ويطرد ثاني أكسيد الكربون.",
      mainText: "أعضاء الجهاز التنفسي:\n• الأنف: يدفئ ويرطب ويصفي الهواء\n• القصبة الهوائية: تنقل الهواء للرئتين\n• الرئتان: يحدث فيهما تبادل الغازات\n• الحجاب الحاجز: عضلة تتحكم في التنفس\n\nالشهيق: هواء يدخل → أكسجين للدم\nالزفير: هواء يخرج → ثاني أكسيد الكربون يطرد",
      explanation: "عندما تشهق، رئتيك تتمدد كالبالون وتملئ بالأكسجين. عندما تزفر، تنكمش وتطرد ثاني أكسيد الكربون.",
      examples: "🇲🇦 للحفاظ على الرئتين:\n• تجنب التدخين (يضر الرئتين جداً)\n• التهوية الجيدة في المنازل المغربية\n• ممارسة الرياضة في الهواء النقي\n• الابتعاد عن التلوث في المدن",
      summary: "الجهاز التنفسي: أنف → قصبة هوائية → رئتان. الشهيق = O₂ يدخل. الزفير = CO₂ يخرج.",
    },
    exercises: [
      { q: "ما وظيفة الحجاب الحاجز؟", type: "text", answer: "التحكم في حركة التنفس" },
      { q: "ما الغاز الذي ندخله عند الشهيق؟", type: "text", answer: "الأكسجين" },
    ],
    quizQuestions: [
      { q: "ما العضو الذي تحدث فيه عملية تبادل الغازات؟", options: ["الأنف", "القصبة الهوائية", "الرئتان", "الحجاب الحاجز"], correct: 2, explanation: "تبادل الغازات يحدث في الرئتين." },
      { q: "ما الغاز الذي يُطرد عند الزفير؟", options: ["الأكسجين", "النيتروجين", "ثاني أكسيد الكربون", "الهيدروجين"], correct: 2, explanation: "نطرد ثاني أكسيد الكربون (CO₂) عند الزفير." },
      { q: "كم رئة في الجسم البشري؟", options: ["واحدة", "اثنتان", "ثلاث", "أربع"], correct: 1, explanation: "لدينا رئتان: يمنى ويسرى." },
      { q: "ما وظيفة الأنف في التنفس؟", options: ["تبادل الغازات", "تدفئة وترطيب وتصفية الهواء", "ضخ الدم", "إنتاج الأكسجين"], correct: 1, explanation: "الأنف يدفئ ويرطب ويصفي الهواء قبل وصوله للرئتين." },
      { q: "الحجاب الحاجز هو:", options: ["عظم", "عضلة", "عرق", "غدة"], correct: 1, explanation: "الحجاب الحاجز عضلة تفصل الصدر عن البطن وتتحكم في التنفس." },
    ],
  },
  // ═══ السنة السادسة ════════════════════════════════════════════════════════
  {
    grade: "6", subject: "الرياضيات", title: "النسبة المئوية",
    unit: 1, order: 1,
    objectives: ["حساب النسبة المئوية", "تطبيقاتها في الحياة"],
    keyWords: ["نسبة مئوية", "%", "من مئة", "تخفيض", "ربح", "خسارة"],
    content: {
      introduction: "النسبة المئوية تعني 'من كل مئة'. 50% = نصف!",
      mainText: "النسبة المئوية = (الجزء ÷ الكل) × 100\n\nأمثلة:\n• 25 من 100 = 25%\n• 1 من 2 = 50%\n• 3 من 4 = 75%\n\nالتطبيق:\nتخفيض 20% على 300 درهم:\n300 × (20/100) = 60 درهم خصم\nالسعر الجديد: 300 - 60 = 240 درهم",
      explanation: "في رمضان، المحلات تعلن '30% خصم'. معناها: من كل 100 درهم، توفر 30 درهماً!",
      examples: "🇲🇦 في الحياة المغربية:\n• تخفيضات العيد: خصم 40% = 4 دراهم من كل 10\n• ضريبة TVA: 20% على أسعار السلع\n• نتيجة 85% في الامتحان\n• فائدة بنكية: 5% على الادخار",
      summary: "النسبة المئوية = الجزء/الكل × 100. 100% = الكل. 50% = النصف.",
    },
    exercises: [
      { q: "ما 25% من 80؟", type: "text", answer: "20" },
      { q: "حصل طالب على 36 من 40. ما نسبته المئوية؟", type: "text", answer: "90%" },
    ],
    quizQuestions: [
      { q: "ما 50% من 200 درهم؟", options: ["50", "100", "150", "25"], correct: 1, explanation: "50% = نصف. 200 ÷ 2 = 100 درهم." },
      { q: "إذا كان الخصم 20% على سعر 500 درهم، فما السعر الجديد؟", options: ["480", "400", "420", "450"], correct: 1, explanation: "الخصم: 500 × 20% = 100. السعر الجديد: 500 - 100 = 400 درهم." },
      { q: "ما النسبة المئوية لـ 3 من 4؟", options: ["60%", "70%", "75%", "80%"], correct: 2, explanation: "(3 ÷ 4) × 100 = 75%." },
      { q: "ما 10% من 350؟", options: ["30", "35", "40", "25"], correct: 1, explanation: "350 × (10/100) = 35." },
      { q: "100% تعني:", options: ["النصف", "الكل", "الربع", "الثلث"], correct: 1, explanation: "100% = الكل كاملاً." },
    ],
  },
  {
    grade: "6", subject: "اللغة العربية", title: "الإعراب — المبتدأ والخبر والفاعل",
    unit: 2, order: 1,
    objectives: ["تعريف المبتدأ والخبر والفاعل", "ضبطها بالشكل الصحيح"],
    keyWords: ["مبتدأ", "خبر", "فاعل", "مرفوع", "منصوب", "مجرور", "إعراب", "جملة اسمية", "جملة فعلية"],
    content: {
      introduction: "الإعراب يعني تحديد وظيفة كل كلمة في الجملة.",
      mainText: "الجملة الاسمية: مبتدأ + خبر\n• المبتدأ: مرفوع بالضمة → مبتدأٌ\n• الخبر: مرفوع بالضمة → خبرٌ\nمثال: المدرسةُ جميلةٌ\n\nالجملة الفعلية: فعل + فاعل\n• الفاعل: مرفوع بالضمة\nمثال: جاءَ الطالبُ",
      explanation: "فكّر في الجملة كلعبة أدوار! المبتدأ هو 'من نتحدث عنه'. الخبر هو 'ما نقوله عنه'. الفاعل هو 'من فعل الفعل'.",
      examples: "🇲🇦 جمل من حياتنا:\n• المغربُ بلدٌ جميلٌ. (مبتدأ + خبر)\n• يلعبُ الأولادُ في الزنقة. (فعل + فاعل)\n• الكسكسُ طعامٌ لذيذٌ. (مبتدأ + خبر)\n• جاءَ العيدُ بالفرحة. (فعل + فاعل)",
      summary: "مبتدأ وخبر وفاعل: كلها مرفوعة بالضمة.",
    },
    exercises: [
      { q: "أعرب: 'محمدٌ مجتهدٌ'", type: "text", answer: "محمد: مبتدأ مرفوع بالضمة. مجتهد: خبر مرفوع بالضمة." },
      { q: "استخرج الفاعل: 'يدرسُ الطالبُ'", type: "text", answer: "الطالب" },
    ],
    quizQuestions: [
      { q: "في جملة 'المدرسةُ كبيرةٌ'، ما المبتدأ؟", options: ["كبيرة", "المدرسة", "الجملة كلها", "لا يوجد مبتدأ"], correct: 1, explanation: "المبتدأ هو 'المدرسة' — هي ما نتحدث عنها." },
      { q: "ما حركة إعراب المبتدأ؟", options: ["الفتحة", "الكسرة", "الضمة", "السكون"], correct: 2, explanation: "المبتدأ مرفوع بالضمة." },
      { q: "في 'جاءَ الطالبُ'، ما الفاعل؟", options: ["جاء", "الطالب", "الجملة", "لا فاعل"], correct: 1, explanation: "الفاعل هو 'الطالب' — هو من فعل فعل المجيء." },
      { q: "الجملة التي تبدأ بفعل تسمى:", options: ["جملة اسمية", "جملة فعلية", "جملة خبرية", "جملة إنشائية"], correct: 1, explanation: "الجملة التي تبدأ بفعل تسمى جملة فعلية." },
      { q: "أيٌّ من التالي مبتدأ؟", options: ["مجتهدٌ", "يدرسُ", "القلمُ", "في المدرسة"], correct: 2, explanation: "'القلمُ' يمكن أن يكون مبتدأ في جملة مثل 'القلمُ مكسورٌ'." },
    ],
  },
  {
    grade: "6", subject: "اللغة الفرنسية", title: "Le passé composé — الماضي المركب",
    unit: 3, order: 1,
    objectives: ["تكوين الماضي المركب", "استخدام avoir وêtre مساعدَين"],
    keyWords: ["passé composé", "avoir", "être", "participe passé", "auxiliaire"],
    content: {
      introduction: "Le passé composé يستخدم للحديث عن أحداث مضت وانتهت!",
      mainText: "التركيب: auxiliaire (avoir / être) + participe passé\n\nمع avoir:\nJ'ai mangé (أكلت)\nTu as joué (لعبت)\nIl a fini (أنهى)\n\nمع être (أفعال الحركة والتحول):\nJe suis allé(e) (ذهبت)\nTu es venu(e) (جئت)\nNous sommes partis (غادرنا)",
      explanation: "تخيل أنك تحكي ما فعلته أمس: 'أكلت الكسكس' = J'ai mangé le couscous. 'ذهبت للمدرسة' = Je suis allé(e) à l'école.",
      examples: "🇲🇦 حوار بسيط:\n— Tu as fait quoi hier? (ماذا فعلت أمس؟)\n— J'ai mangé la harira avec ma famille. (أكلت الحريرة مع عائلتي)\n— Et après? (وبعد؟)\n— Je suis allé au souk. (ذهبت للسوق)",
      summary: "Passé composé = avoir/être + participe passé. Être مع أفعال الحركة: aller, venir, partir...",
    },
    exercises: [
      { q: "Conjuguez au passé composé: manger (je)", type: "text", answer: "j'ai mangé" },
      { q: "Conjuguez au passé composé: aller (tu)", type: "text", answer: "tu es allé(e)" },
    ],
    quizQuestions: [
      { q: "Quel auxiliaire utilise-t-on avec 'manger'?", options: ["être", "avoir", "aller", "venir"], correct: 1, explanation: "Manger utilise avoir: j'ai mangé." },
      { q: "Quel est le participe passé de 'finir'?", options: ["finit", "fini", "finis", "finie"], correct: 1, explanation: "Le participe passé de finir est fini." },
      { q: "Comment dit-on 'elle est venue' en passé composé?", options: ["elle a venue", "elle est venu", "elle est venue", "elle a venu"], correct: 2, explanation: "Venir utilise être, et le participe s'accorde avec le sujet féminin: venue." },
      { q: "Quel verbe utilise être au passé composé?", options: ["manger", "jouer", "partir", "finir"], correct: 2, explanation: "Partir utilise être: je suis parti(e)." },
      { q: "J'__ travaillé toute la journée.", options: ["suis", "ai", "es", "est"], correct: 1, explanation: "Travailler utilise avoir: j'ai travaillé." },
    ],
  },
  // ═══ مواد متنوعة ═════════════════════════════════════════════════════════
  {
    grade: "2", subject: "التربية الإسلامية", title: "الطهارة والوضوء",
    unit: 1, order: 1,
    objectives: ["معرفة أهمية الطهارة", "تعلم خطوات الوضوء"],
    keyWords: ["طهارة", "وضوء", "نية", "نظافة", "صلاة", "طهور"],
    content: {
      introduction: "الطهارة من الإيمان — النظافة أساس العبادة في الإسلام.",
      mainText: "خطوات الوضوء:\n1. النية (في القلب)\n2. غسل اليدين 3 مرات\n3. المضمضة (شطف الفم) 3 مرات\n4. الاستنشاق (استنشاق الماء) 3 مرات\n5. غسل الوجه 3 مرات\n6. غسل اليدين للمرفقين 3 مرات\n7. مسح الرأس مرة واحدة\n8. غسل القدمين للكعبين 3 مرات",
      explanation: "الوضوء يطهّرك للوقوف أمام الله في الصلاة. مثل ما تغسل يديك قبل الأكل، تتوضأ قبل الصلاة!",
      examples: "🇲🇦 من حياتنا:\n• نتوضأ قبل كل صلاة\n• يُفضَّل الوضوء بالماء البارد في الصيف\n• يعلم الآباء أبناءهم الوضوء منذ الصغر\n• المسجد له ميضأة (مكان الوضوء)",
      summary: "الوضوء 8 خطوات تطهّر أعضاء خاصة للصلاة. ينقض بعدة أشياء.",
    },
    exercises: [
      { q: "كم مرة نغسل الوجه في الوضوء؟", type: "text", answer: "3 مرات" },
      { q: "ما أول خطوة في الوضوء؟", type: "text", answer: "النية" },
    ],
    quizQuestions: [
      { q: "ما أول خطوة في الوضوء؟", options: ["غسل اليدين", "النية", "المضمضة", "غسل الوجه"], correct: 1, explanation: "تبدأ بالنية في القلب ثم التسمية." },
      { q: "كم مرة نغسل الوجه؟", options: ["مرة", "مرتين", "3 مرات", "4 مرات"], correct: 2, explanation: "نغسل الوجه 3 مرات." },
      { q: "ما الذي يُمسح (وليس يُغسل) في الوضوء؟", options: ["اليدان", "الوجه", "الرأس", "القدمان"], correct: 2, explanation: "الرأس يُمسح (لا يُغسل) مرة واحدة." },
      { q: "الطهارة من:", options: ["العادات", "الإيمان", "التقاليد", "الفلسفة"], correct: 1, explanation: "قال النبي ﷺ: 'الطهور شطر الإيمان'." },
      { q: "قبل ماذا يجب الوضوء؟", options: ["النوم فقط", "الأكل فقط", "الصلاة", "الدراسة"], correct: 2, explanation: "الوضوء شرط لصحة الصلاة." },
    ],
  },
  {
    grade: "3", subject: "التربية الوطنية", title: "المغرب — أرضنا وشعبنا",
    unit: 1, order: 1,
    objectives: ["التعرف على خصائص المغرب الجغرافية والبشرية", "تنمية الانتماء الوطني"],
    keyWords: ["المغرب", "مملكة", "الملك", "مناطق", "تضاريس", "شعب", "هوية"],
    content: {
      introduction: "المغرب بلد رائع في شمال أفريقيا، غني بالتنوع الجغرافي والثقافي!",
      mainText: "المغرب:\n• رسمياً: المملكة المغربية\n• العاصمة: الرباط\n• أكبر مدينة: الدار البيضاء\n• المساحة: 710,000 كم²\n• السكان: ~37 مليون نسمة\n\nالتضاريس:\n• جبال الأطلس الكبير (أعلى قمة: توبقال 4,167م)\n• الصحراء الكبرى (جنوباً)\n• السواحل: المتوسط والأطلسي",
      explanation: "المغرب مثل قطعة شطرنج جميلة — فيها جبال وصحراء وبحار وسهول وغابات. كل منطقة لها طعامها وملابسها وموسيقاها!",
      examples: "🇲🇦 من هويتنا المغربية:\n• اللغات: العربية، الأمازيغية، الدارجة، الفرنسية\n• الأطباق: الكسكس (الوطني)، الطاجين، البسطيلة\n• الموسيقى: الكناوة، العيطة، الحسانية\n• الصناعات التقليدية: الزليج، الجلد، النسيج",
      summary: "المغرب مملكة متنوعة: جبال + صحراء + سواحل + شعب متعدد الثقافات.",
    },
    exercises: [
      { q: "ما عاصمة المغرب؟", type: "text", answer: "الرباط" },
      { q: "ما أعلى قمة جبلية في المغرب؟", type: "text", answer: "جبل توبقال" },
    ],
    quizQuestions: [
      { q: "ما عاصمة المغرب؟", options: ["الدار البيضاء", "مراكش", "الرباط", "فاس"], correct: 2, explanation: "الرباط هي العاصمة السياسية للمغرب." },
      { q: "ما الطبق الوطني للمغرب؟", options: ["الطاجين", "الحريرة", "الكسكس", "البسطيلة"], correct: 2, explanation: "الكسكس معترف به أممياً تراثاً مغربياً مشتركاً." },
      { q: "ما أعلى جبل في المغرب؟", options: ["الكاردوس", "توبقال", "الأطلس", "سيدي شامهروش"], correct: 1, explanation: "جبل توبقال بارتفاع 4,167 متر هو الأعلى في شمال أفريقيا." },
      { q: "بكم بحر يحدّ المغرب؟", options: ["بحر واحد", "بحرين", "ثلاثة", "لا يوجد"], correct: 1, explanation: "يحده البحر المتوسط شمالاً والمحيط الأطلسي غرباً." },
      { q: "اللغة الرسمية للمغرب هي:", options: ["الفرنسية فقط", "العربية والأمازيغية", "الدارجة فقط", "الإسبانية"], correct: 1, explanation: "اللغتان الرسميتان دستورياً هما العربية والأمازيغية." },
    ],
  },
] as const;

// ── DB Seeder ──────────────────────────────────────────────────────────────────

async function findSubjectId(gradeNum: number, subjectAr: string): Promise<string | null> {
  const gradeSlug = gradeNum <= 6
    ? `${gradeNum}ap`
    : gradeNum <= 9
    ? `${gradeNum - 6}ac`
    : gradeNum === 10 ? "tc" : gradeNum === 11 ? "bac1" : "bac2";

  const [grade] = await db
    .select({ id: schema.grades.id })
    .from(schema.grades)
    .where(eq(schema.grades.slug, gradeSlug))
    .limit(1);

  if (!grade) return null;

  const [subject] = await db
    .select({ id: schema.subjects.id })
    .from(schema.subjects)
    .where(and(
      eq(schema.subjects.gradeId, grade.id),
      eq(schema.subjects.titleAr, subjectAr),
    ))
    .limit(1);

  return subject?.id ?? null;
}

async function findOrCreateUnit(
  subjectId: string,
  unitNumber: number,
  titleAr: string,
): Promise<string> {
  const slug = `unit-${unitNumber}`;
  const [existing] = await db
    .select({ id: schema.units.id })
    .from(schema.units)
    .where(and(
      eq(schema.units.subjectId, subjectId),
      eq(schema.units.slug, slug),
    ))
    .limit(1);

  if (existing) return existing.id;

  const [created] = await db
    .insert(schema.units)
    .values({ subjectId, slug, titleAr, orderIndex: unitNumber })
    .returning({ id: schema.units.id });

  return created.id;
}

async function main() {
  console.log("🌍 Seeding v13 curriculum data...\n");

  let ok = 0;
  let skipped = 0;

  for (const lesson of LESSONS_DATA) {
    const gradeNum = parseInt(lesson.grade);
    const subjectId = await findSubjectId(gradeNum, lesson.subject);

    if (!subjectId) {
      console.warn(`  ⚠ Subject not found: Grade ${lesson.grade} — ${lesson.subject}`);
      skipped++;
      continue;
    }

    const unitId = await findOrCreateUnit(
      subjectId,
      lesson.unit,
      lesson.subject === "الرياضيات" ? "الأعداد والعمليات" : "الوحدة الأولى",
    );

    const slug = `v13-${lesson.grade}-${lesson.subject.replace(/\s+/g, "-")}-${lesson.order}`;

    // Upsert lesson
    const [lessonRow] = await db
      .insert(schema.lessons)
      .values({
        unitId,
        slug,
        titleAr:                     lesson.title,
        difficulty:                  "medium",
        estimatedDurationMinutes:    15,
        objectives:                  lesson.objectives as unknown as string[],
        orderIndex:                  lesson.order,
        isPublished:                 true,
      })
      .onConflictDoNothing()
      .returning({ id: schema.lessons.id });

    if (!lessonRow) { skipped++; continue; }

    // Insert lesson content
    await db
      .insert(schema.lessonContents)
      .values({
        lessonId:      lessonRow.id,
        explanation:   `${lesson.content.introduction}\n\n${lesson.content.mainText}\n\n${lesson.content.explanation}`,
        examples:      [{ text: lesson.content.examples }],
        summary:       lesson.content.summary,
        vocabulary:    lesson.keyWords.map((w: string) => ({ word: w, definition: "" })),
      })
      .onConflictDoNothing();

    const exerciseRows = [
      ...lesson.exercises.map((ex: { q: string; answer: string }, index: number) => ({
        lessonId: lessonRow.id,
        type: "short_answer" as const,
        question: ex.q,
        options: null,
        correctAnswer: ex.answer,
        explanation: "إجابة قصيرة للتأكد من الفهم.",
        orderIndex: index + 1,
        points: 10,
      })),
      ...lesson.quizQuestions.map((q, index: number) => ({
        lessonId: lessonRow.id,
        type: "mcq" as const,
        question: q.q,
        options: [...q.options],
        correctAnswer: q.options[q.correct] ?? "",
        explanation: q.explanation,
        orderIndex: lesson.exercises.length + index + 1,
        points: 10,
      })),
    ];
    if (exerciseRows.length) {
      await db.insert(schema.exercises).values(exerciseRows).onConflictDoNothing();
    }

    console.log(`  ✅ Grade ${lesson.grade} | ${lesson.subject} | ${lesson.title}`);
    ok++;
  }

  console.log(`\n✨ Done! ${ok} lessons seeded, ${skipped} skipped.`);
  console.log("Run npm run db:seed:v13 to re-run if needed.");
}

main().catch((e) => { console.error(e); process.exit(1); });

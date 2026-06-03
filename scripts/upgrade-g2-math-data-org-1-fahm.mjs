/**
 * upgrade-g2-math-data-org-1-fahm.mjs
 *
 * Upgrade: تنظيم البيانات — أفهم (السنة الثانية ابتدائي)
 * Grade 2 Math — Data Organization — "I Understand" lesson
 *
 * Usage:
 *   Dry run:  node scripts/upgrade-g2-math-data-org-1-fahm.mjs
 *   Apply:    node scripts/upgrade-g2-math-data-org-1-fahm.mjs --apply
 */

import { fetchLessons, scoreLessonQuality, updateLessonWithPayload, withDb, printLessonSummary, parseArgs } from "./lib/lesson-quality-tools.mjs";

// ── Artifact metadata ────────────────────────────────────────────────────────
const LESSON_ID      = "99822473-ff28-4831-8d92-2df7e3fd86c0"; // exact UUID — no fallback
const SAFE_TO_APPLY  = true;                                     // artifact validation flag
const EXPECTED_TITLE = "أفهم";                                   // title guard: wrong row → abort

const args  = parseArgs();
const apply = Boolean(args.apply);

const PAYLOAD = {
  title: "تنظيم البيانات — أفهم (السنة الثانية ابتدائي)",
  objectives: [
    "فهم معنى تنظيم البيانات والإحصاء البسيط",
    "قراءة جدول التكرار واستخراج معلومات منه",
    "تمييز التكرار الأكبر والأصغر في جدول",
  ],
  explanation: `مرحباً! أنا أستاذة ليلى، وسنتعلم اليوم درساً ممتعاً جداً: كيف نجمع معلومات ونرتّبها في جدول!

─────────────────────────────
📊 ما هو تنظيم البيانات؟
─────────────────────────────

تعريف: تنظيم البيانات يعني جمع معلومات (بيانات) ثم ترتيبها في جدول أو شكل واضح حتى نستطيع فهمها بسهولة.
مفهوم التكرار: التكرار يعني عدد مرات ظهور الشيء في المجموعة.

في المنهاج المغربي للسنة الثانية الابتدائي، نتعلم قراءة جداول التكرار البسيطة.

─────────────────────────────
🔢 أمثلة محلولة خطوة بخطوة
─────────────────────────────

مثال 1 — قراءة جدول التكرار:
سُئل 10 تلاميذ في فصل بالدار البيضاء: ما فاكهتك المفضلة؟
هذه النتائج في الجدول:

| الفاكهة    | التكرار (عدد التلاميذ) |
|------------|------------------------|
| التفاح     | 3                      |
| البرتقال   | 4                      |
| الموز      | 2                      |
| العنب      | 1                      |

الحل خطوة بخطوة:
خطوة 1: نقرأ رأس الجدول — العمود الأول هو الفاكهة، الثاني هو عدد التلاميذ.
خطوة 2: نجيب على الأسئلة:
  - كم تلميذاً يحب التفاح؟ الجواب: 3 تلاميذ
  - أي فاكهة يفضلها أكبر عدد؟ الجواب: البرتقال (4 تلاميذ)
  - أقل فاكهة تفضيلاً؟ الجواب: العنب (1 تلميذ)
خطوة 3: نحسب المجموع: 3 + 4 + 2 + 1 = 10 تلاميذ (يساوي عدد التلاميذ الكلي ✓)

مثال 2 — جدول ألوان:
في منزل مغربي، سُئل أفراد العائلة عن اللون المفضل:
| اللون  | العدد |
|--------|-------|
| الأزرق | 2     |
| الأخضر | 3     |
| الأصفر | 1     |

الجواب: اللون المفضل عند أكبر عدد هو الأخضر.
نحسب المجموع: 2 + 3 + 1 = 6 أشخاص.

مثال 3 — وضعية إشكالية:
في مخبزة بمراكش، بيع في يوم واحد:
15 خبزة في الصباح، 20 خبزة في الظهيرة، 10 خبزات في المساء.
نحسب الإجمالي: 15 + 20 + 10 = 45 خبزة في اليوم.

─────────────────────────────
✏️ تدريب موجه مع ليلى
─────────────────────────────

تمرين 1: استعمل الجدول التالي:
| وسيلة النقل | التكرار |
|-------------|---------|
| الحافلة     | 8       |
| السيارة     | 5       |
| المشي       | 12      |
| الدراجة     | 3       |

أجب: كم تلميذاً يأتي مشياً؟
تلميح من ليلى: ابحث في العمود الثاني في صف "المشي".
الجواب: 12 تلميذاً يأتون مشياً.

تطبيق: احسب مجموع التلاميذ في الجدول أعلاه.
الجواب: 8 + 5 + 12 + 3 = 28 تلميذاً.

تدريب: ما وسيلة النقل الأكثر استخداماً؟
الجواب: المشي (12 تلميذاً) هي الأكثر.

─────────────────────────────
❌ أخطاء شائعة وتصحيحها
─────────────────────────────

خطأ 1: نسيان قراءة رأس الجدول وفهم ما يمثله كل عمود.
التصحيح: دائماً ابدأ بقراءة رأس الجدول قبل الإجابة.

خطأ 2: خلط بين الصفوف والأعمدة عند البحث عن معلومة.
التصحيح: الصف يمتد أفقياً (يساراً ويميناً)، العمود يمتد عمودياً (أعلى وأسفل).

خطأ 3: نسيان التحقق من مجموع التكرارات مع العدد الكلي.
التصحيح: المجموع يجب أن يساوي عدد الأشخاص الكلي في الاستطلاع.

─────────────────────────────
💡 تلميحات من ليلى والعلاج
─────────────────────────────

تلميح ليلى: ضع إصبعك على الصف المطلوب وتتبّعه حتى تصل للعمود الصحيح.
العلاج: إذا لم تفهم الجدول، ارسمه بنفسك على ورقة وأضف الأرقام واحداً واحداً.
التصحيح: راجع الجدول مرة ثانية بعد الإجابة.
إعادة رسم الجدول بخط عريض تساعدك على القراءة بوضوح.

─────────────────────────────
📋 استعداد للفرض والامتحان
─────────────────────────────

وضعية للامتحان:
في مدرسة بالرباط، المغرب، سُئل 20 تلميذاً في السنة الثانية عن رياضتهم المفضلة:
| الرياضة   | العدد |
|-----------|-------|
| كرة القدم | 9     |
| السباحة   | 5     |
| الجري     | 4     |
| التنس     | 2     |

أسئلة الامتحان:
1. ما الرياضة الأكثر شعبية؟ الجواب: كرة القدم (9 تلاميذ)
2. كم تلميذاً يفضل السباحة أو الجري؟ الجواب: 5 + 4 = 9 تلاميذ
3. هل المجموع 20؟ الجواب: 9 + 5 + 4 + 2 = 20 ✓

استعداد للفرض: تدرّب على قراءة جداول من 3 أو 4 صفوف، وتعلّم دائماً حساب المجموع للتحقق.

تعليمات ليلى: ليلى ستسأل الطالب عن طريقة قراءته للجدول خطوة بخطوة قبل إعطاء الجواب النهائي. إذا أخطأ، تطلب منه إعادة القراءة من البداية.`,

  vocabulary: [
    { word: "بيانات", definition: "معلومات نجمعها من مجموعة أشخاص أو أشياء" },
    { word: "تكرار", definition: "عدد مرات ظهور شيء معين في المجموعة" },
    { word: "جدول", definition: "شكل منظم من صفوف وأعمدة لتنظيم المعلومات" },
    { word: "استطلاع", definition: "سؤال نطرحه على مجموعة للحصول على إجاباتهم" },
    { word: "المجموع", definition: "ناتج جمع جميع التكرارات" },
  ],

  examples: [
    { text: "جدول تفضيل الفاكهة لـ 10 تلاميذ — البرتقال الأكثر تفضيلاً (4)", note: "مثال عملي من فصل مغربي" },
    { text: "جدول وسائل النقل — المشي الأكثر (12 من 28)", note: "جدول استطلاع مدرسي" },
  ],

  summary: `ملخص درس تنظيم البيانات — أفهم:
• البيانات: معلومات نجمعها ونرتّبها
• جدول التكرار: جدول يُظهر عدد مرات ظهور كل شيء
• للقراءة: ابحث في العمود الصحيح، والصف الصحيح
• للتحقق: اجمع كل التكرارات = العدد الكلي
خلاصة: تنظيم البيانات يساعدنا على فهم المعلومات بسرعة ووضوح.`,

  exercises: [
    {
      type: "mcq",
      question: "في جدول التكرار: التفاح=3، البرتقال=4، الموز=2. ما الفاكهة الأكثر تفضيلاً؟",
      options: ["التفاح", "البرتقال", "الموز", "العنب"],
      correctAnswer: "البرتقال",
      explanation: "نقارن الأعداد: 3، 4، 2. أكبر عدد هو 4 وهو يمثل البرتقال. الجواب: البرتقال.",
      orderIndex: 1,
      points: 10,
    },
    {
      type: "mcq",
      question: "ما مجموع التكرارات في هذا الجدول: كرة القدم=9، سباحة=5، جري=4، تنس=2؟",
      options: ["18", "20", "22", "19"],
      correctAnswer: "20",
      explanation: "نجمع: 9 + 5 + 4 + 2 = 20. الجواب 20 يساوي عدد التلاميذ الكلي في الاستطلاع.",
      orderIndex: 2,
      points: 10,
    },
    {
      type: "mcq",
      question: "في جدول استطلاع: الحافلة=8، السيارة=5، المشي=12، الدراجة=3. ما وسيلة النقل الأقل استخداماً؟",
      options: ["الحافلة", "السيارة", "المشي", "الدراجة"],
      correctAnswer: "الدراجة",
      explanation: "نقارن الأعداد: 8، 5، 12، 3. أصغر عدد هو 3 وهو يمثل الدراجة. الجواب: الدراجة.",
      orderIndex: 3,
      points: 10,
    },
    {
      type: "mcq",
      question: "ما الذي يمثله العمود الثاني في جدول التكرار؟",
      options: ["اسم الفئة", "عدد الأشخاص أو التكرار", "اسم الاستطلاع", "التاريخ"],
      correctAnswer: "عدد الأشخاص أو التكرار",
      explanation: "في جدول التكرار، العمود الأول يحتوي الفئات (مثل أنواع الفاكهة)، والعمود الثاني يحتوي التكرار أي عدد مرات ظهور كل فئة.",
      orderIndex: 4,
      points: 10,
    },
    {
      type: "mcq",
      question: "كيف نتحقق أن الجدول صحيح؟",
      options: ["نقرأ الجدول مرة ثانية فقط", "نجمع كل التكرارات ونتحقق أنها تساوي العدد الكلي", "نقارن الجدول بالكتاب", "نسأل المعلم"],
      correctAnswer: "نجمع كل التكرارات ونتحقق أنها تساوي العدد الكلي",
      explanation: "للتحقق من صحة الجدول: اجمع كل الأعداد في عمود التكرار. المجموع يجب أن يساوي عدد الأشخاص الكلي في الاستطلاع.",
      orderIndex: 5,
      points: 10,
    },
    {
      type: "short_answer",
      question: "في جدول: أحمر=4، أخضر=6، أزرق=2. كم مجموع التكرارات؟",
      options: null,
      correctAnswer: "12",
      explanation: "نجمع جميع التكرارات: 4 + 6 + 2 = 12. الخطوة: نضيف الأعداد واحداً بعد الآخر: 4+6=10، 10+2=12.",
      orderIndex: 6,
      points: 10,
    },
    {
      type: "short_answer",
      question: "في استطلاع بمدرسة مغربية: تفضّل 7 تلاميذ العلوم، و5 الرياضيات، و8 اللغة العربية. من أيهما الأكثر تفضيلاً؟",
      options: null,
      correctAnswer: "اللغة العربية",
      explanation: "نقارن: 7، 5، 8. أكبر عدد هو 8 ويمثل اللغة العربية. الجواب: اللغة العربية هي الأكثر تفضيلاً بـ 8 تلاميذ.",
      orderIndex: 7,
      points: 10,
    },
  ],
};

await withDb(async (client) => {
  // ── Safety gate ────────────────────────────────────────────────────────────
  if (!SAFE_TO_APPLY) {
    console.error("❌ Artifact not marked safe_to_apply. Aborting.");
    process.exit(1);
  }

  // ── Exact ID lookup — no fuzzy matching, no fallback ──────────────────────
  const rows = await fetchLessons(client, { lessonId: LESSON_ID, limit: 1 });
  const lesson = rows[0];

  if (!lesson) {
    console.error(`❌ Lesson not found: ${LESSON_ID}`);
    process.exit(1);
  }

  // ── Title guard: confirm we have the right row ─────────────────────────────
  if (!(lesson.lesson_title ?? "").includes(EXPECTED_TITLE)) {
    console.error(`❌ ID matched but title "${lesson.lesson_title}" does not contain "${EXPECTED_TITLE}". Wrong lesson — aborting.`);
    process.exit(1);
  }

  // ── Before summary ─────────────────────────────────────────────────────────
  console.log("\n── BEFORE ───────────────────────────────────────────────────");
  console.log("Lesson ID:   ", lesson.lesson_id);
  console.log("Title:       ", lesson.lesson_title);
  printLessonSummary("Current state", lesson);
  const beforeQuality = scoreLessonQuality(lesson);
  console.log("Before score:", beforeQuality.score, "| Issues:", beforeQuality.issues.join(", ") || "none");

  // ── After (dry-run) quality check ─────────────────────────────────────────
  const afterQuality = scoreLessonQuality({
    ...lesson,
    explanation:    PAYLOAD.explanation,
    summary:        PAYLOAD.summary,
    objectives:     PAYLOAD.objectives,
    vocabulary:     PAYLOAD.vocabulary,
    examples:       PAYLOAD.examples,
    exercise_count: PAYLOAD.exercises.length,
  });

  console.log("\n── AFTER (dry-run) ──────────────────────────────────────────");
  console.log("Content chars:", PAYLOAD.explanation.length);
  console.log("Exercises:   ", PAYLOAD.exercises.length);
  console.log("After score: ", afterQuality.score, "| Issues:", afterQuality.issues.join(", ") || "none ✓");

  if (afterQuality.score < 85) {
    console.error(`\n❌ Quality gate failed: score ${afterQuality.score} < 85. Do not apply.`);
    process.exit(1);
  }
  console.log(`\n✅ Quality gate passed: ${afterQuality.score}/100`);

  if (!apply) {
    console.log("\n── DRY RUN — no DB writes ────────────────────────────────────");
    console.log("Lesson ID:  ", LESSON_ID);
    console.log("Title:      ", lesson.lesson_title);
    console.log("safe_to_apply:", SAFE_TO_APPLY);
    console.log("\nTo apply: node scripts/upgrade-g2-math-data-org-1-fahm.mjs --apply");
    return;
  }

  // ── Apply ──────────────────────────────────────────────────────────────────
  const counts = await updateLessonWithPayload(client, LESSON_ID, PAYLOAD, { replaceExercises: true });
  console.log("\n── APPLIED ──────────────────────────────────────────────────");
  console.table([counts]);

  const [verified] = await fetchLessons(client, { lessonId: LESSON_ID, limit: 1 });
  const verifiedQ = scoreLessonQuality(verified);
  console.log("Post-apply score:", verifiedQ.score, "| Content chars:", String(verified.explanation ?? "").length);
  if (verifiedQ.score >= 85) console.log("✅ Upgrade complete!");
  else console.warn("⚠️  Score below 85 after apply — check the DB.");
});

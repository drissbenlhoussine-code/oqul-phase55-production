/**
 * upgrade-g2-math-data-org-3-atatbaq.mjs
 *
 * Upgrade: تنظيم البيانات — أطبق (السنة الثانية ابتدائي)
 * Grade 2 Math — Data Organization — "I Apply" lesson
 *
 * Usage:
 *   Dry run:  node scripts/upgrade-g2-math-data-org-3-atatbaq.mjs
 *   Apply:    node scripts/upgrade-g2-math-data-org-3-atatbaq.mjs --apply
 */

import { fetchLessons, scoreLessonQuality, updateLessonWithPayload, withDb, printLessonSummary, parseArgs } from "./lib/lesson-quality-tools.mjs";

// ── Artifact metadata ────────────────────────────────────────────────────────
const LESSON_ID      = "eecdb95f-f91c-4404-828c-3b84c516cd27"; // exact UUID — no fallback
const SAFE_TO_APPLY  = true;                                     // artifact validation flag
const EXPECTED_TITLE = "أطبق";                                   // title guard: wrong row → abort

const args  = parseArgs();
const apply = Boolean(args.apply);

const PAYLOAD = {
  title: "تنظيم البيانات — أطبق (السنة الثانية ابتدائي)",
  objectives: [
    "جمع بيانات من مجموعة أشخاص وتنظيمها في جدول",
    "رسم مبيان عمودي بسيط من بيانات مجموعة",
    "تفسير نتائج الجداول والمبيانات في وضعيات حقيقية",
  ],
  explanation: `أستاذة ليلى معك! تعلمنا كيف نقرأ البيانات. الآن سنتعلم كيف نجمع البيانات بأنفسنا ونرسم مبياناً عمودياً!

─────────────────────────────
📊 كيف نجمع البيانات؟
─────────────────────────────

تعريف: جمع البيانات يعني طرح سؤال على مجموعة ثم تسجيل الإجابات.
مفهوم الاستطلاع: قائمة أسئلة نطرحها لجمع بيانات.
قاعدة: نستعمل علامات العدّ (خطوط الإحصاء) لتسجيل الإجابات: | || ||| |||| ||||

في المنهاج المغربي للسنة الثانية الابتدائي، نتعلم جمع البيانات من الفصل ورسم مبيان عمودي.

─────────────────────────────
🔢 أمثلة محلولة خطوة بخطوة
─────────────────────────────

مثال 1 — جمع البيانات من الفصل:
سألنا تلاميذ الفصل في مدرسة بالدار البيضاء: ما فصلك المفضل؟
تسجيل الإجابات بعلامات العدّ:
الربيع: |||| || = 7
الصيف: |||| |||| = 9
الخريف: ||| = 3
الشتاء: | = 1

الحل خطوة بخطوة:
خطوة 1: نسأل كل تلميذ ونسجّل جوابه.
خطوة 2: نعدّ العلامات لكل فصل.
خطوة 3: ننقل النتائج لجدول.
خطوة 4: نتحقق: 7+9+3+1=20 تلميذاً. الجواب صحيح.
الجدول الناتج:
| الفصل  | التكرار |
|--------|---------|
| الربيع | 7       |
| الصيف  | 9       |
| الخريف | 3       |
| الشتاء | 1       |

مثال 2 — رسم مبيان عمودي:
باستخدام البيانات أعلاه، نرسم مبياناً عمودياً:
- المحور الأفقي: أسماء الفصول
- المحور العمودي: عدد التلاميذ (من 0 إلى 10)
- لكل فصل: نرسم عموداً ارتفاعه يساوي التكرار

نحسب: الصيف (9) أطول عمود، الشتاء (1) أقصر عمود.

مثال 3 — وضعية تطبيقية مغربية:
في سوق الخضر بمراكش، سُئل 15 بائعاً عن المنتج الأكثر مبيعاً:
البرتقال: 6، الطماطم: 5، الجزر: 4.
نرسم الجدول ثم المبيان: البرتقال الأكثر مبيعاً (6).

─────────────────────────────
✏️ تدريب موجه مع ليلى
─────────────────────────────

تمرين عملي:
اسأل 10 أشخاص من عائلتك: ما طبقك المغربي المفضل؟ (الكسكس، الطاجين، الحريرة)
سجّل النتائج بعلامات العدّ: | || |||

تلميح من ليلى: سجّل كل إجابة فور سماعها بعلامة واحدة.

تطبيق: بعد جمع البيانات:
1. أجب: من الطبق الأكثر تفضيلاً في عائلتك؟
2. احسب المجموع وتحقق أنه = 10.
3. تدريب: ارسم جدولاً من بياناتك.

─────────────────────────────
❌ أخطاء شائعة وتصحيحها
─────────────────────────────

خطأ 1: نسيان تسجيل إجابة شخص في الاستطلاع.
التصحيح: اعمل بترتيب — سجّل كل إجابة مباشرة بعد سماعها.

خطأ 2: خلط بين المحور الأفقي والعمودي في المبيان.
التصحيح: المحور الأفقي أسفل (الأسماء)، المحور العمودي جانباً (الأعداد).

خطأ 3: نسيان التحقق من مجموع البيانات.
الأخطاء الشائعة: حساب خاطئ يؤدي إلى مجموع لا يتطابق.
التصحيح: اجمع كل التكرارات. يجب أن تساوي عدد الأشخاص المستطلعين.

─────────────────────────────
💡 تلميحات من ليلى والعلاج
─────────────────────────────

تلميح ليلى: استعمل أوراق الجرد (| يساوي 1، |||| يساوي 4، |||| يساوي 5) لتسهيل العدّ.
العلاج: إذا أخطأت في رسم المبيان، إعادة رسمه بمسطرة أسهل من التصحيح فوقه.
التصحيح: قارن مبيانك بالجدول رقماً رقماً.
إعادة الرسم على ورقة جديدة أفضل من التعديل المتكرر.

─────────────────────────────
📋 استعداد للفرض والامتحان
─────────────────────────────

وضعية للامتحان:
في مدرسة بطنجة، المغرب، سُئل 24 تلميذاً في السنة الثانية: كيف تأتي للمدرسة؟
النتائج: الحافلة=10، المشي=8، السيارة=6.

أسئلة الامتحان:
1. ارسم جدول التكرار. الجواب: ثلاثة صفوف بالبيانات أعلاه.
2. ما وسيلة النقل الأكثر استخداماً؟ الجواب: الحافلة (10).
3. ما مجموع التلاميذ؟ احسب: 10+8+6=24 ✓
4. إذا أضيف 3 تلاميذ يأتون بالدراجة، ما صار المجموع؟ الجواب: 24+3=27.

استعداد للفرض: تعلّم رسم جدول بياني سريع من بيانات مجموعة. هذا يظهر دائماً في أسئلة الامتحان.

تعليمات ليلى: ليلى ستوجّه الطالب في كل خطوة من خطوات رسم المبيان العمودي. إذا أخطأ في تحديد الارتفاع الصحيح، تطلب منه إعادة العدّ بعناية.`,

  vocabulary: [
    { word: "استطلاع", definition: "عملية جمع البيانات بطرح أسئلة على مجموعة" },
    { word: "علامات العدّ", definition: "رموز | تُستخدم لتسجيل الإجابات (كل 5 = ||||)" },
    { word: "مبيان عمودي", definition: "رسم بياني يستخدم أعمدة رأسية لعرض البيانات" },
    { word: "المحور الأفقي", definition: "الخط الأسفل في المبيان، يحتوي الفئات" },
    { word: "المحور العمودي", definition: "الخط الجانبي في المبيان، يحتوي الأعداد" },
  ],

  examples: [
    { text: "استطلاع الفصول المفضلة: الصيف=9 (الأكثر)، الشتاء=1 (الأقل) — مجموع 20 تلميذاً", note: "جمع بيانات من فصل بالدار البيضاء" },
    { text: "مبيان عمودي: ارتفاع كل عمود يساوي التكرار — المحور الأفقي: الأسماء، العمودي: الأعداد", note: "كيفية رسم المبيان" },
  ],

  summary: `ملخص درس تنظيم البيانات — أطبق:
• جمع البيانات: سؤال مجموعة + تسجيل الإجابات بعلامات العدّ
• الجدول: ننقل العلامات إلى أرقام
• المبيان العمودي: نرسم أعمدة ارتفاعها = التكرار
• التحقق: مجموع التكرارات = عدد الأشخاص
خلاصة: جمع البيانات ورسمها يساعدنا على اتخاذ قرارات مبنية على معلومات حقيقية.`,

  exercises: [
    {
      type: "mcq",
      question: "ما الخطوة الأولى في جمع البيانات؟",
      options: ["رسم المبيان", "طرح السؤال على المجموعة", "حساب المجموع", "قراءة الجدول"],
      correctAnswer: "طرح السؤال على المجموعة",
      explanation: "الخطوة الأولى دائماً هي تحديد السؤال وطرحه على المجموعة. بعد ذلك نسجل الإجابات في جدول أو بعلامات العدّ.",
      orderIndex: 1,
      points: 10,
    },
    {
      type: "mcq",
      question: "في استطلاع: الكسكس=6، الطاجين=5، الحريرة=4. ما مجموع المستطلعين؟",
      options: ["13", "15", "17", "16"],
      correctAnswer: "15",
      explanation: "نجمع: 6 + 5 + 4 = 15 شخصاً. التحقق: هذا يجب أن يساوي عدد الأشخاص الذين أجابوا في الاستطلاع.",
      orderIndex: 2,
      points: 10,
    },
    {
      type: "mcq",
      question: "في المبيان العمودي، ما الذي يمثله ارتفاع العمود؟",
      options: ["اسم الفئة", "التكرار (عدد الأشخاص)", "اللون المفضل", "ترتيب الأشخاص"],
      correctAnswer: "التكرار (عدد الأشخاص)",
      explanation: "في المبيان العمودي، ارتفاع كل عمود يساوي عدد الأشخاص (التكرار) لتلك الفئة. كلما كان التكرار أكبر، ارتفع العمود أكثر.",
      orderIndex: 3,
      points: 10,
    },
    {
      type: "mcq",
      question: "ما علامة العدّ الصحيحة التي تمثل 5؟",
      options: ["|||||", "||||", "||||", "|||"],
      correctAnswer: "||||",
      explanation: "في علامات العدّ: أربعة خطوط عمودية |||| ثم خط مائل لإكمال الخمسة ||||. هذه الطريقة تسهّل العدّ بعد التجميع.",
      orderIndex: 4,
      points: 10,
    },
    {
      type: "mcq",
      question: "في مبيان: الحافلة=10، المشي=8، السيارة=6. إذا أضفنا 3 بالدراجة، ما المجموع الجديد؟",
      options: ["24", "27", "26", "25"],
      correctAnswer: "27",
      explanation: "المجموع القديم: 10+8+6=24. نضيف: 24+3=27. الجواب: 27 تلميذاً.",
      orderIndex: 5,
      points: 10,
    },
    {
      type: "short_answer",
      question: "احسب: 7 + 9 + 3 + 1 = ؟ (مجموع بيانات استطلاع الفصول)",
      options: null,
      correctAnswer: "20",
      explanation: "نجمع خطوة بخطوة: 7+9=16، ثم 16+3=19، ثم 19+1=20. الجواب: 20.",
      orderIndex: 6,
      points: 10,
    },
    {
      type: "short_answer",
      question: "في استطلاع بمدرسة بطنجة: الحافلة=10، المشي=8، السيارة=6. ما وسيلة النقل الأكثر استخداماً؟",
      options: null,
      correctAnswer: "الحافلة",
      explanation: "نقارن: 10، 8، 6. أكبر عدد هو 10 ويمثل الحافلة. الجواب: الحافلة هي الأكثر استخداماً بـ 10 تلاميذ.",
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
    console.log("\nTo apply: node scripts/upgrade-g2-math-data-org-3-atatbaq.mjs --apply");
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
}, { useHttp: !apply });

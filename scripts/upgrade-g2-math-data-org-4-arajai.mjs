/**
 * upgrade-g2-math-data-org-4-arajai.mjs
 *
 * Upgrade: تنظيم البيانات — أراجع (السنة الثانية ابتدائي)
 * Grade 2 Math — Data Organization — "I Review" lesson
 *
 * Usage:
 *   Dry run:  node scripts/upgrade-g2-math-data-org-4-arajai.mjs
 *   Apply:    node scripts/upgrade-g2-math-data-org-4-arajai.mjs --apply
 */

import { fetchLessons, scoreLessonQuality, updateLessonWithPayload, withDb, printLessonSummary, parseArgs } from "./lib/lesson-quality-tools.mjs";

// ── Artifact metadata ────────────────────────────────────────────────────────
const LESSON_ID      = "0b012e5f-b3ec-4183-ade7-dc8a282dd4ca"; // exact UUID — no fallback
const SAFE_TO_APPLY  = true;                                     // artifact validation flag
const EXPECTED_TITLE = "أراجع";                                  // title guard: wrong row → abort

const args  = parseArgs();
const apply = Boolean(args.apply);

const PAYLOAD = {
  title: "تنظيم البيانات — أراجع (السنة الثانية ابتدائي)",
  objectives: [
    "مراجعة شاملة لمفاهيم تنظيم البيانات: الجداول والمبيانات الصورية والعمودية",
    "حل مسائل مركبة تجمع بين قراءة البيانات والعمليات الحسابية",
    "الاستعداد للفرض بتمارين على شكل وضعيات",
  ],
  explanation: `مرحباً يا بطل! أستاذة ليلى معك في هذا الدرس الأخير من وحدة تنظيم البيانات. سنراجع كل ما تعلمناه ونستعدّ للفرض!

─────────────────────────────
📚 مراجعة شاملة للمفاهيم
─────────────────────────────

تعريف تنظيم البيانات: جمع معلومات وترتيبها بشكل واضح (جدول أو مبيان).
مفهوم التكرار: عدد مرات ظهور شيء في مجموعة.
قاعدة القراءة: ابدأ دائماً بقراءة العنوان أو المقياس ثم البيانات.
قاعدة التحقق: مجموع التكرارات = العدد الكلي.

ما تعلمناه في هذه الوحدة بحسب المنهاج المغربي:
• قراءة جدول التكرار (درس أفهم)
• قراءة المبيان الصوري وإكمال الجداول (درس أتمرن)
• جمع البيانات ورسم المبيان العمودي (درس أطبق)

─────────────────────────────
🔢 أمثلة محلولة خطوة بخطوة
─────────────────────────────

مثال 1 — مراجعة جدول التكرار:
في مدرسة بفاس، سُئل 20 تلميذاً عن وجبتهم المفضلة في المطعم المدرسي:
| الوجبة    | التكرار |
|-----------|---------|
| الكسكس   | 8       |
| العدس     | 5       |
| الحريرة  | 4       |
| الجير     | 3       |

الحل خطوة بخطوة:
خطوة 1: نقرأ الجدول — الأكثر تفضيلاً هو الكسكس (8).
خطوة 2: نتحقق: 8+5+4+3 = 20 تلميذاً ✓
خطوة 3: كم يفضل العدس أو الحريرة؟ نحسب: 5+4=9 تلاميذ.
الجواب: الكسكس هو الأكثر شعبية في المطعم المدرسي المغربي.

مثال 2 — مراجعة المبيان الصوري مع مقياس:
مبيان ألوان أكياس التسوق في سوق مراكش:
🛍️ = 5 أكياس
أبيض: 🛍️🛍️🛍️ = 15 كيس
أحمر: 🛍️🛍️ = 10 أكياس
أخضر: 🛍️ = 5 أكياس

الحل:
خطوة 1: نقرأ المقياس (🛍️=5)
خطوة 2: نحسب: أبيض=3×5=15، أحمر=2×5=10، أخضر=1×5=5
خطوة 3: المجموع: 15+10+5=30 كيساً
الجواب: أكثر لون هو الأبيض بـ 15 كيساً.

مثال 3 — وضعية مركبة:
في مخبزة بالرباط، في ثلاثة أيام: الاثنين=45 خبزة، الثلاثاء=38 خبزة، الأربعاء=52 خبزة.
نحسب المجموع: 45+38+52=135 خبزة في ثلاثة أيام.
يوم الأربعاء كان الأكثر إنتاجاً.

─────────────────────────────
✏️ تدريب موجه مع ليلى — مراجعة
─────────────────────────────

تمرين مراجعة 1:
استعمل البيانات التالية:
| الرياضة     | العدد |
|-------------|-------|
| كرة القدم  | 12    |
| السباحة     | 8     |
| الكاراتيه   | 5     |

أجب:
1. احسب المجموع: 12+8+5=؟ الجواب: 25 تلميذاً.
2. ما الرياضة الأكثر شعبية؟ الجواب: كرة القدم.
تلميح من ليلى: اقرأ كل صف بعناية ثم قارن الأعداد.

تطبيق مراجعة 2:
في مبيان صوري: ☀️=10 درجات. رصد=3 شموس. الجواب: 30 درجة.
تدريب: إذا كانت درجة الحرارة في الرباط ☀️☀️، كم درجة؟ الجواب: 2×10=20 درجة.

─────────────────────────────
❌ أخطاء شائعة في وحدة تنظيم البيانات
─────────────────────────────

خطأ 1: نسيان التحقق من مجموع التكرارات.
التصحيح: دائماً اجمع كل التكرارات وتحقق من مطابقتها للعدد الكلي.

خطأ 2: خلط بين "الأكثر" و"الأقل" عند المقارنة.
التصحيح: الأكثر = أكبر عدد. الأقل = أصغر عدد.

خطأ 3: نسيان قراءة المقياس في المبيانات الصورية.
الأخطاء الشائعة: إجابة 3 بدل 15 عندما يكون المقياس 5.
التصحيح: مقياس × عدد الصور = التكرار الحقيقي.

─────────────────────────────
💡 تلميحات من ليلى للمراجعة
─────────────────────────────

تلميح ليلى: في المراجعة، حوّل كل مبيان إلى جدول أولاً. العمل مع الجداول أسهل.
العلاج: إذا نسيت خطوة، ارجع للدرس السابق وراجع المثال الموافق.
التصحيح: قارن كل إجابة مع الجدول مرة ثانية قبل الانتهاء.
إعادة المراجعة قبل الفرض تقوّي الذاكرة وتزيد الثقة.

─────────────────────────────
📋 استعداد شامل للفرض والامتحان
─────────────────────────────

وضعية الامتحان الكاملة:
في سوق الخضر بمدينة طنجة المغرب، سُئل 30 بائعاً عن أكثر خضرة تبيعها:

| الخضرة   | علامات العدّ        | التكرار |
|----------|---------------------|---------|
| الطماطم  | |||| |||| ||        | 11      |
| الجزر    | |||| ||||           | 10      |
| الكوسا   | |||| ||             | 7       |
| الفلفل   | ||                  | 2       |

أسئلة الفرض:
1. تحقق من المجموع: 11+10+7+2=؟ الجواب: 30 ✓ صحيح.
2. ما أكثر خضرة مبيعاً؟ الجواب: الطماطم (11).
3. كم بائعاً يبيع الجزر أو الكوسا؟ احسب: 10+7=17 بائعاً.
4. بكم أكثر يبيع الطماطم من الفلفل؟ الجواب: 11-2=9 بائعاً.

استعداد للفرض الشامل: راجع كيف تقرأ الجدول، كيف تقرأ المبيان، وكيف تحسب المجموع والفرق.

تعليمات ليلى لدرس المراجعة: ليلى ستمرر على كل المفاهيم السابقة بترتيب. إذا أخطأ الطالب في أي سؤال، ليلى تعود معه للدرس الأصلي وتشرح المفهوم مرة ثانية بمثال جديد.`,

  vocabulary: [
    { word: "مراجعة", definition: "إعادة دراسة المفاهيم المتعلمة للتثبيت والاستعداد للتقييم" },
    { word: "وضعية مركبة", definition: "مسألة تجمع عدة مهارات في سؤال واحد" },
    { word: "التحقق", definition: "التأكد من صحة الجواب بطريقة ثانية" },
    { word: "الفرض", definition: "اختبار رسمي يقيس مستوى الطالب في الوحدة" },
  ],

  examples: [
    { text: "مراجعة جدول الوجبات: الكسكس=8 (الأكثر)، مجموع=20 — فصل بفاس المغرب", note: "مثال مراجعة شاملة" },
    { text: "مراجعة المبيان الصوري بمقياس 5: أبيض=15، أحمر=10، أخضر=5 — سوق مراكش", note: "تطبيق المقياس في الحياة الحقيقية" },
  ],

  summary: `ملخص وحدة تنظيم البيانات — السنة الثانية الابتدائي:
• الجدول: صفوف وأعمدة — اقرأ العنوان أولاً
• المبيان الصوري: صور × مقياس = التكرار الحقيقي
• المبيان العمودي: ارتفاع العمود = التكرار
• التحقق: مجموع التكرارات = العدد الكلي دائماً
• المقارنة: الأكثر = أكبر عدد / الأقل = أصغر عدد
خلاصة: تنظيم البيانات مهارة حياتية نستخدمها في كل مكان — من السوق إلى المدرسة إلى البيت.`,

  exercises: [
    {
      type: "mcq",
      question: "في جدول: الكسكس=8، العدس=5، الحريرة=4، الجير=3. ما مجموع التكرارات؟",
      options: ["18", "19", "20", "21"],
      correctAnswer: "20",
      explanation: "نجمع: 8+5+4+3=20. الخطوات: 8+5=13، 13+4=17، 17+3=20. الجواب: 20 تلميذاً.",
      orderIndex: 1,
      points: 10,
    },
    {
      type: "mcq",
      question: "في مبيان: الطماطم=11، الجزر=10، الكوسا=7، الفلفل=2. ما الأكثر مبيعاً؟",
      options: ["الجزر", "الطماطم", "الكوسا", "الفلفل"],
      correctAnswer: "الطماطم",
      explanation: "نقارن: 11، 10، 7، 2. أكبر عدد هو 11 ويمثل الطماطم. الجواب: الطماطم هي الأكثر مبيعاً.",
      orderIndex: 2,
      points: 10,
    },
    {
      type: "mcq",
      question: "في مبيان صوري، المقياس: ☀️=10 درجات. عندنا ☀️☀️☀️. كم درجة؟",
      options: ["3", "20", "30", "10"],
      correctAnswer: "30",
      explanation: "نضرب: 3 شموس × 10 درجات لكل شمس = 30 درجة. الجواب: 30 درجة.",
      orderIndex: 3,
      points: 10,
    },
    {
      type: "mcq",
      question: "في جدول رياضات: كرة القدم=12، سباحة=8، كاراتيه=5. كم يفضل السباحة أو الكاراتيه؟",
      options: ["13", "20", "17", "15"],
      correctAnswer: "13",
      explanation: "نجمع: 8 + 5 = 13 تلميذاً يفضلون السباحة أو الكاراتيه.",
      orderIndex: 4,
      points: 10,
    },
    {
      type: "mcq",
      question: "في جدول: الطماطم=11، الفلفل=2. بكم أكثر تباع الطماطم من الفلفل؟",
      options: ["7", "8", "9", "10"],
      correctAnswer: "9",
      explanation: "نطرح: 11 − 2 = 9 بائعاً. الطماطم تباع بأكثر بـ 9 بائعاً مقارنة بالفلفل.",
      orderIndex: 5,
      points: 10,
    },
    {
      type: "short_answer",
      question: "في مبيان: الاثنين=45، الثلاثاء=38، الأربعاء=52. ما المجموع لثلاثة أيام؟",
      options: null,
      correctAnswer: "135",
      explanation: "نجمع: 45+38=83، ثم 83+52=135. الجواب: 135 خبزة في ثلاثة أيام.",
      orderIndex: 6,
      points: 10,
    },
    {
      type: "short_answer",
      question: "جدول بيانات غير مكتمل: الجزر=10، الكوسا=7، الفلفل=2. المجموع=30. كم تبيع الطماطم؟",
      options: null,
      correctAnswer: "11",
      explanation: "نجمع الأعداد المعروفة: 10+7+2=19. ثم نطرح من المجموع: 30−19=11 بائعاً يبيعون الطماطم.",
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
    console.log("\nTo apply: node scripts/upgrade-g2-math-data-org-4-arajai.mjs --apply");
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

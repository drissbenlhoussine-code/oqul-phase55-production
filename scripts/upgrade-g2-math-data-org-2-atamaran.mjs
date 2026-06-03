/**
 * upgrade-g2-math-data-org-2-atamaran.mjs
 *
 * Upgrade: تنظيم البيانات — أتمرن (السنة الثانية ابتدائي)
 * Grade 2 Math — Data Organization — "I Practice" lesson
 *
 * Usage:
 *   Dry run:  node scripts/upgrade-g2-math-data-org-2-atamaran.mjs
 *   Apply:    node scripts/upgrade-g2-math-data-org-2-atamaran.mjs --apply
 */

import { fetchLessons, scoreLessonQuality, updateLessonWithPayload, withDb, printLessonSummary, parseArgs } from "./lib/lesson-quality-tools.mjs";

// ── Artifact metadata ────────────────────────────────────────────────────────
const LESSON_ID      = "24540419-242e-4da5-9dbe-d994b6cecb16"; // exact UUID — no fallback
const SAFE_TO_APPLY  = true;                                     // artifact validation flag
const EXPECTED_TITLE = "أتمرن";                                  // title guard: wrong row → abort

const args  = parseArgs();
const apply = Boolean(args.apply);

const PAYLOAD = {
  title: "تنظيم البيانات — أتمرن (السنة الثانية ابتدائي)",
  objectives: [
    "قراءة الرسم البياني بالصور (مبيان صوري) واستخراج معلومات منه",
    "إكمال جدول تكرار بمعلومات ناقصة",
    "المقارنة بين بيانتين مختلفتين",
  ],
  explanation: `مرحباً مجدداً! أستاذة ليلى معك. في درس أفهم تعلمنا قراءة الجداول. الآن في أتمرن سنتدرب أكثر على الرسوم البيانية الصورية!

─────────────────────────────
📊 الرسم البياني بالصور (المبيان الصوري)
─────────────────────────────

تعريف: المبيان الصوري هو طريقة لعرض البيانات باستخدام صور أو رموز بدل الأرقام.
مفهوم المقياس: كل صورة تمثل عدداً محدداً من الوحدات.
قاعدة: لقراءة المبيان، اقرأ المقياس أولاً ثم عدّ الصور.

في المنهاج المغربي للسنة الثانية الابتدائي، نقرأ مبيانات صورية بمقياس 1 صورة = 1 وحدة أو 1 صورة = 2 وحدات.

─────────────────────────────
🔢 أمثلة محلولة خطوة بخطوة
─────────────────────────────

مثال 1 — قراءة مبيان صوري:
في مدرسة بفاس، سُئل التلاميذ عن حيوانهم المفضل. النتائج بالمبيان:
🐱 القطة: 🌟🌟🌟 (3 نجوم)
🐶 الكلب: 🌟🌟🌟🌟🌟 (5 نجوم)
🐠 السمكة: 🌟🌟 (نجمتان)
المقياس: 🌟 = تلميذ واحد

الحل خطوة بخطوة:
خطوة 1: نقرأ المقياس — كل نجمة = 1 تلميذ.
خطوة 2: نعدّ النجوم لكل حيوان.
خطوة 3: القطة=3، الكلب=5، السمكة=2.
خطوة 4: الحيوان المفضل: الكلب (5 تلاميذ).
الجواب: الكلب هو الحيوان المفضل لأكبر عدد.

مثال 2 — إكمال جدول:
الجدول الناقص:
| المادة      | العدد |
|-------------|-------|
| الرياضيات  | 7     |
| العربية     | ؟     |
| الفرنسية   | 4     |
المجموع = 18 تلميذاً.

الحل: 7 + ؟ + 4 = 18
نحسب: 11 + ؟ = 18
الجواب: ؟ = 18 − 11 = 7 تلاميذ يحبون العربية.

مثال 3 — وضعية مقارنة:
في حي مغربي، سُئل 30 شخصاً: هل تفضلون الشاي أم القهوة؟
يفضل الشاي: 22 شخصاً.
يفضل القهوة: 8 أشخاص.
نحسب: 22 + 8 = 30 ✓
الجواب: الشاي هو المفضل بـ 22 شخصاً مقابل 8.

─────────────────────────────
✏️ تدريب موجه مع ليلى
─────────────────────────────

تمرين 1: مبيان صوري لألوان الأقلام في مقلمة يوسف:
🔴 أحمر: ✏️✏️ (قلمان)
🔵 أزرق: ✏️✏️✏️✏️ (4 أقلام)
🟢 أخضر: ✏️✏️✏️ (3 أقلام)
المقياس: ✏️ = قلم واحد

تلميح من ليلى: عدّ الأقلام في كل صف بعناية.
أجب: كم قلماً أحمر عند يوسف؟ الجواب: 2 أقلام.
أجب: كم مجموع الأقلام؟ احسب: 2 + 4 + 3 = 9 أقلام.

تطبيق: من له أكثر أقلام؟ الجواب: اللون الأزرق (4 أقلام).
تدريب: إذا فقد يوسف 2 من الأقلام الزرقاء، كم يتبقى؟ الجواب: 4 − 2 = 2 أقلام زرقاء.

─────────────────────────────
❌ أخطاء شائعة وتصحيحها
─────────────────────────────

خطأ 1: نسيان قراءة المقياس قبل عدّ الصور.
التصحيح: دائماً ابدأ بقراءة المقياس. إذا كانت صورة = 2، فـ 3 صور = 6 وليس 3.

خطأ 2: خلط بين عمود البيانات وعمود الأسئلة.
التصحيح: حدّد الصف المطلوب أولاً ثم انتقل للعمود الصحيح.

خطأ 3: نسيان جمع الباقي عند إيجاد العدد الناقص.
الأخطاء الشائعة: 7+4=11، ثم نسيان طرح 11 من 18.
التصحيح: المجموع − الأعداد المعروفة = العدد الناقص.

─────────────────────────────
💡 تلميحات من ليلى والعلاج
─────────────────────────────

تلميح ليلى: حوّل المبيان الصوري إلى جدول أرقام لتسهّل الحساب.
العلاج: إذا نسيت المقياس، ارجع لأعلى الرسم أو أسفله دائماً.
التصحيح: بعد الإجابة، اجمع كل الأعداد وتحقق من المجموع.
إعادة رسم المبيان كجدول أرقام يساعد كثيراً.

─────────────────────────────
📋 استعداد للفرض والامتحان
─────────────────────────────

وضعية للامتحان:
في مطعم مغربي يقدم طاجين، كسكس، بسطيلة. سُئل 25 زبون عن طبقهم المفضل:
| الطبق    | المبيان (كل رمز = 5 أشخاص) |
|----------|------------------------------|
| الطاجين  | 🍲🍲🍲 (3 رموز)              |
| الكسكس  | 🍲🍲 (رمزان)                 |
| البسطيلة | ؟                            |

أسئلة الامتحان:
1. كم شخصاً يفضل الطاجين؟ الجواب: 3 × 5 = 15 شخصاً.
2. كم شخصاً يفضل الكسكس؟ الجواب: 2 × 5 = 10 أشخاص.
3. كم شخصاً يفضل البسطيلة؟ الجواب: 25 − 15 − 10 = 0 (لا أحد في هذا المثال التعليمي).

استعداد للفرض: تدرّب على قراءة مبيانات بمقياس 1، 2، و5.

تعليمات ليلى: ليلى تطلب من الطالب شرح كيف وصل إلى الجواب قبل التأكيد عليه. إذا نسي المقياس، تذكّره برفق وتطلب منه إعادة القراءة.`,

  vocabulary: [
    { word: "مبيان صوري", definition: "رسم يستخدم صوراً أو رموزاً لعرض البيانات" },
    { word: "مقياس", definition: "القيمة التي تمثلها كل صورة في المبيان" },
    { word: "بيان ناقص", definition: "جدول أو مبيان يحتوي على عدد مجهول" },
    { word: "مقارنة", definition: "تحديد الأكثر والأقل بين قيمتين أو أكثر" },
  ],

  examples: [
    { text: "مبيان الحيوانات المفضلة: الكلب=5، القطة=3، السمكة=2 (مقياس: 1 نجمة = 1 تلميذ)", note: "مبيان صوري من فصل مغربي" },
    { text: "إيجاد عدد ناقص في جدول المواد: الجواب = المجموع − الأعداد المعروفة", note: "طريقة الطرح لإيجاد المجهول" },
  ],

  summary: `ملخص درس تنظيم البيانات — أتمرن:
• المبيان الصوري: كل صورة تمثل عدداً = المقياس
• قراءة المقياس أولاً ضرورية قبل العدّ
• إيجاد العدد الناقص: المجموع − الأعداد المعروفة
خلاصة: التدرب على المبيانات الصورية يساعدنا على قراءة البيانات في الكتب والجرائد.`,

  exercises: [
    {
      type: "mcq",
      question: "في مبيان صوري: 🌟 = 2 تلميذاً. إذا رأيت 4 نجوم، كم عدد التلاميذ؟",
      options: ["4", "6", "8", "2"],
      correctAnswer: "8",
      explanation: "نضرب عدد الصور في المقياس: 4 × 2 = 8 تلاميذ. المقياس أساسي في قراءة المبيان الصوري.",
      orderIndex: 1,
      points: 10,
    },
    {
      type: "mcq",
      question: "في جدول: الرياضيات=7، العربية=؟، الفرنسية=4. المجموع=18. ما العدد الناقص؟",
      options: ["5", "6", "7", "8"],
      correctAnswer: "7",
      explanation: "نحسب: 7 + 4 = 11. ثم: 18 − 11 = 7. العدد الناقص للعربية هو 7.",
      orderIndex: 2,
      points: 10,
    },
    {
      type: "mcq",
      question: "في مبيان: الشاي=22، القهوة=8. كم مجموع المستطلعين؟",
      options: ["28", "30", "32", "26"],
      correctAnswer: "30",
      explanation: "نجمع: 22 + 8 = 30 شخصاً في مجموع الاستطلاع.",
      orderIndex: 3,
      points: 10,
    },
    {
      type: "mcq",
      question: "في مبيان صوري، ما أول شيء نقرأه قبل عدّ الصور؟",
      options: ["عنوان المبيان", "عدد الأشخاص", "المقياس", "نتيجة الاستطلاع"],
      correctAnswer: "المقياس",
      explanation: "المقياس هو ما تمثله كل صورة. بدون قراءة المقياس، لا يمكننا فهم قيمة الصور في المبيان.",
      orderIndex: 4,
      points: 10,
    },
    {
      type: "mcq",
      question: "في مطعم: طاجين=15، كسكس=10. المجموع=30. كم يفضل البسطيلة؟",
      options: ["3", "5", "10", "15"],
      correctAnswer: "5",
      explanation: "نطرح: 30 − 15 − 10 = 5 أشخاص يفضلون البسطيلة. التحقق: 15 + 10 + 5 = 30 ✓",
      orderIndex: 5,
      points: 10,
    },
    {
      type: "short_answer",
      question: "مبيان: أحمر=2 أقلام، أزرق=4 أقلام، أخضر=3 أقلام. ما مجموع الأقلام؟",
      options: null,
      correctAnswer: "9",
      explanation: "نجمع: 2 + 4 + 3 = 9 أقلام. الخطوة: 2+4=6، ثم 6+3=9.",
      orderIndex: 6,
      points: 10,
    },
    {
      type: "short_answer",
      question: "في مبيان: 🌟 = 5 أشخاص. رأيت 3 نجوم. كم عدد الأشخاص؟",
      options: null,
      correctAnswer: "15",
      explanation: "نضرب: 3 نجوم × 5 أشخاص لكل نجمة = 15 شخصاً. هذا هو مفهوم المقياس في المبيانات الصورية.",
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
    console.log("\nTo apply: node scripts/upgrade-g2-math-data-org-2-atamaran.mjs --apply");
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

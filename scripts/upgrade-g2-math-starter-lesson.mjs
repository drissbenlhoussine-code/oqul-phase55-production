/**
 * upgrade-g2-math-starter-lesson.mjs
 *
 * One-shot upgrade for: الرياضيات — درس البداية (السنة الثانية ابتدائي)
 *
 * Workflow:
 *   Dry run:  node scripts/upgrade-g2-math-starter-lesson.mjs
 *   Apply:    node scripts/upgrade-g2-math-starter-lesson.mjs --apply
 *
 * Quality gate: score >= 85 required before applying.
 */

import { fetchLessons, scoreLessonQuality, updateLessonWithPayload, withDb, printLessonSummary } from "./lib/lesson-quality-tools.mjs";
import { parseArgs } from "./lib/lesson-quality-tools.mjs";

const args = parseArgs();
const apply = Boolean(args.apply);

// ── High-quality lesson payload ─────────────────────────────────────────────

const PAYLOAD = {
  title: "الرياضيات — درس البداية (السنة الثانية ابتدائي)",
  objectives: [
    "مراجعة الأعداد والجمع والطرح من السنة الأولى",
    "التعرف على محاور رياضيات السنة الثانية الابتدائي",
    "حل مسائل جمع وطرح بسيطة من الحياة اليومية",
  ],
  explanation: `مرحباً بك في السنة الثانية الابتدائية! أنا أستاذة ليلى، وسأكون معك طوال هذا العام لنتعلم رياضيات السنة الثانية معاً بطريقة سهلة وممتعة.

بحسب المنهاج المغربي للسنة الثانية الابتدائي، محاور الرياضيات هذا العام هي:
• الأعداد حتى 999
• الجمع والطرح حتى 999
• مدخل إلى الضرب: جداول 2 و3 و4 و5
• الكسور البسيطة: النصف (½)، الثلث (⅓)، الربع (¼)
• القياس: الطول (سم، م)، الكتلة (كغ)، السعة (ليتر)
• الأشكال الهندسية: المربع، المستطيل، المثلث، الدائرة
• تنظيم البيانات في جداول وأعمدة بيانية

─────────────────────────────
📚 مراجعة من السنة الأولى
─────────────────────────────

مفهوم الجمع:
تعريف: الجمع يعني إضافة عدد إلى عدد آخر للحصول على المجموع.
قاعدة: العدد الأول + العدد الثاني = المجموع

مفهوم الطرح:
تعريف: الطرح يعني إيجاد الفرق بين عددين.
قاعدة: العدد الكبير − العدد الصغير = الباقي

─────────────────────────────
🔢 أمثلة محلولة خطوة بخطوة
─────────────────────────────

مثال 1 — الجمع البسيط:
في سوق فاس بالمغرب، اشترت الأم 5 برتقالات صباحاً و4 برتقالات مساءً. كم صار عندها؟
الحل خطوة بخطوة:
خطوة 1: نكتب العملية: 5 + 4 = ؟
خطوة 2: نعدّ من 5 أربع خطوات للأمام: 6، 7، 8، 9
خطوة 3: المجموع هو 9
الجواب الصحيح: 9 برتقالات.

مثال 2 — الطرح البسيط:
عند يوسف 10 دراهم، دفع منها 3 دراهم ثمن خبزة. كم تبقى معه؟
الحل خطوة بخطوة:
خطوة 1: نكتب: 10 − 3 = ؟
خطوة 2: نبدأ من 10 وننقص 3: 9، 8، 7
خطوة 3: الباقي هو 7
الجواب الصحيح: 7 دراهم تبقت مع يوسف.

مثال 3 — وضعية إشكالية:
في مدرسة بالرباط، في الفصل الأول 14 بنتاً و11 ولداً.
نحسب المجموع: 14 + 11 = 25 تلميذاً في الفصل.

─────────────────────────────
✏️ تدريب موجه مع ليلى
─────────────────────────────

تمرين 1: احسب 7 + 8 = ؟
تلميح من ليلى: ابدأ من 7 وعدّ 8 خطوات للأمام على أصابعك.
الجواب: 7 + 8 = 15

تمرين 2: احسب 16 − 9 = ؟
تلميح من ليلى: استعمل طريقة التكملة: 9 + ؟ = 16
الجواب: 16 − 9 = 7

تطبيق عملي: عندك 20 درهماً واشتريت شيئاً بـ 12 درهماً. كم يتبقى؟
أجب: 20 − 12 = 8 دراهم

─────────────────────────────
❌ أخطاء شائعة وكيفية التصحيح
─────────────────────────────

خطأ 1: نسيان حمل الرقم في الجمع
مثال الخطأ: 8 + 5 = 3 (بدل 13)
التصحيح: نحسب الآحاد أولاً (8+5=13)، نكتب 3 ونحمل 1 إلى العشرات.

خطأ 2: خلط إشارة الجمع (+) بالطرح (−)
التصحيح: اقرأ المسألة جيداً — "أضاف / اشترى" = جمع؛ "أعطى / دفع / فقد" = طرح.

خطأ 3: نسيان الترتيب الصحيح في الطرح
التصحيح: دائماً نطرح العدد الصغير من الكبير في الأعداد الطبيعية.

─────────────────────────────
💡 تلميحات من ليلى والعلاج
─────────────────────────────

تلميح ليلى: استعمل أصابعك أو ارسم نقاطاً صغيرة عند الصعوبة — هذه طريقة ذكية!
العلاج التربوي: إذا أخطأت، لا تحزن. ارجع للمثال وأعد الحل خطوة بخطوة.
التصحيح الذاتي: بعد كل تمرين، راجع إجابتك قبل التسليم.
إعادة المحاولة تقوّيك أكثر من أي شيء آخر!

─────────────────────────────
📋 استعداد للفرض والامتحان
─────────────────────────────

وضعية للامتحان:
في سوق بمراكش، عند بائع 25 كيلو برتقال. باع 17 كيلو. كم تبقى؟
الحل:
1. نحدد نوع العملية: "باع" تعني نقص → طرح
2. نكتب: 25 − 17 = ؟
3. نحسب: 25 − 17 = 8
4. الجواب: تبقى 8 كيلو من البرتقال.

استعداد للفرض: تدرّب على الجمع والطرح حتى 20، وتذكّر: الجمع يزيد، الطرح ينقص.

تعليمات ليلى للمساعدة: ليلى تسأل الطالب عن منهج تفكيره قبل الجواب. إذا أخطأ، تعطيه تلميحاً صغيراً وتطلب منه إعادة المحاولة بدل إعطاء الجواب مباشرة.`,

  vocabulary: [
    { word: "الجمع", definition: "عملية إضافة عددين للحصول على المجموع" },
    { word: "الطرح", definition: "عملية إيجاد الفرق بين عددين" },
    { word: "المجموع", definition: "ناتج عملية الجمع" },
    { word: "الباقي", definition: "ناتج عملية الطرح" },
    { word: "المنهاج", definition: "البرنامج الدراسي الرسمي للسنة الثانية الابتدائي بالمغرب" },
  ],

  examples: [
    { text: "5 برتقالات + 4 برتقالات = 9 برتقالات (من سوق فاس)", note: "مثال جمع من الحياة اليومية المغربية" },
    { text: "10 دراهم − 3 دراهم = 7 دراهم (ثمن الخبزة)", note: "مثال طرح بالدرهم المغربي" },
  ],

  summary: `ملخص درس البداية — الرياضيات السنة الثانية الابتدائي:
• الجمع: نضيف عدداً إلى آخر → المجموع
• الطرح: نجد الفرق بين عددين → الباقي
• محاور السنة الثانية: الأعداد حتى 999، الضرب، الكسور، القياس، الهندسة، تنظيم البيانات
خلاصة: نبني على رياضيات السنة الأولى وننطلق نحو مفاهيم جديدة مثيرة!`,

  exercises: [
    {
      type: "mcq",
      question: "ما مجموع 7 + 8؟",
      options: ["13", "15", "14", "16"],
      correctAnswer: "15",
      explanation: "الحساب: 7 + 8 = 15. طريقة التحقق: 8 + 7 = 15 أيضاً (الجمع تبادلي). الجواب هو 15.",
      orderIndex: 1,
      points: 10,
    },
    {
      type: "mcq",
      question: "ما الفرق بين 16 و9؟",
      options: ["6", "8", "7", "5"],
      correctAnswer: "7",
      explanation: "الطرح: 16 − 9 = 7. للتحقق: 9 + 7 = 16 صحيح. الجواب هو 7.",
      orderIndex: 2,
      points: 10,
    },
    {
      type: "mcq",
      question: "عندك 20 درهماً واشتريت شيئاً بـ 12 درهماً. كم يتبقى؟",
      options: ["32", "8", "9", "7"],
      correctAnswer: "8",
      explanation: "نطرح: 20 − 12 = 8 دراهم. الجواب 8 دراهم لأننا دفعنا 12 من أصل 20.",
      orderIndex: 3,
      points: 10,
    },
    {
      type: "mcq",
      question: "في الفصل 14 بنتاً و11 ولداً. كم عدد التلاميذ؟",
      options: ["24", "26", "25", "23"],
      correctAnswer: "25",
      explanation: "الجمع: 14 + 11 = 25. الحساب: 14 + 10 = 24، ثم 24 + 1 = 25. الجواب 25 تلميذاً.",
      orderIndex: 4,
      points: 10,
    },
    {
      type: "mcq",
      question: "ما المحور الجديد الذي سنتعلمه في السنة الثانية ولم ندرسه في الأولى؟",
      options: ["الجمع فقط", "الضرب البسيط", "الطرح فقط", "الأعداد 1-10"],
      correctAnswer: "الضرب البسيط",
      explanation: "في السنة الثانية نبدأ تعلم الضرب (جداول 2 و3 و4 و5) وهو مفهوم جديد لم يظهر في السنة الأولى.",
      orderIndex: 5,
      points: 10,
    },
    {
      type: "short_answer",
      question: "احسب: 13 + 9 = ؟",
      options: null,
      correctAnswer: "22",
      explanation: "13 + 9: نضيف 7 أولاً لنصل إلى 20، ثم نضيف 2 المتبقية: 20 + 2 = 22. الجواب: 22.",
      orderIndex: 6,
      points: 10,
    },
    {
      type: "short_answer",
      question: "احسب: 25 − 17 = ؟",
      options: null,
      correctAnswer: "8",
      explanation: "25 − 17: نطرح 5 أولاً لنصل إلى 20، ثم نطرح 12 الباقية: 20 − 12 = 8. أو مباشرة: 25 − 17 = 8.",
      orderIndex: 7,
      points: 10,
    },
  ],
};

// ── Self-score against quality gate ─────────────────────────────────────────

function selfScore() {
  const fakeRow = {
    lesson_title: PAYLOAD.title,
    unit_title: "مدخل إلى الرياضيات",
    subject_title: "الرياضيات",
    grade_title: "السنة الثانية ابتدائي",
    explanation: PAYLOAD.explanation,
    summary: PAYLOAD.summary,
    objectives: PAYLOAD.objectives,
    vocabulary: PAYLOAD.vocabulary,
    examples: PAYLOAD.examples,
    exercise_count: PAYLOAD.exercises.length,
  };
  return scoreLessonQuality(fakeRow);
}

// ── Main ─────────────────────────────────────────────────────────────────────

await withDb(async (client) => {
  const matches = await fetchLessons(client, {
    grade: "2ap",
    subject: "الرياضيات",
    title: "درس البداية",
    limit: 5,
  });

  if (matches.length === 0) {
    console.error("❌ Lesson not found. Make sure db:seed has been run first.");
    process.exit(1);
  }
  if (matches.length > 1) {
    console.log("Multiple matches:");
    console.table(matches.map((r) => ({ id: r.lesson_id, title: r.lesson_title, grade: r.grade_slug })));
    const exact = matches.find((r) => r.lesson_title?.includes("درس البداية") && r.grade_slug === "2ap");
    if (!exact) {
      console.error("❌ Safety abort: could not narrow to one lesson. Use --lesson-id flag.");
      process.exit(1);
    }
    matches.splice(0, matches.length, exact);
  }

  const lesson = matches[0];

  console.log("\n── Current state ────────────────────────────────────────");
  printLessonSummary("Before upgrade", lesson);
  const currentQuality = scoreLessonQuality(lesson);
  console.log("Current score:", currentQuality.score, "| Issues:", currentQuality.issues.join(", ") || "none");

  console.log("\n── Dry-run quality check on new payload ─────────────────");
  const dryQuality = selfScore();
  console.log("New content score:", dryQuality.score);
  console.log("Issues after upgrade:", dryQuality.issues.join(", ") || "none ✓");
  console.log("Content length:", PAYLOAD.explanation.length, "chars");
  console.log("Exercises:", PAYLOAD.exercises.length);

  if (dryQuality.score < 85) {
    console.error(`\n❌ Quality gate failed: score ${dryQuality.score} < 85. Do not apply.`);
    process.exit(1);
  }

  console.log(`\n✅ Quality gate passed: score ${dryQuality.score}/100`);

  if (!apply) {
    console.log("\nDry run complete. No changes written.");
    console.log("To apply: node scripts/upgrade-g2-math-starter-lesson.mjs --apply");
    console.log("Lesson ID:", lesson.lesson_id);
    return;
  }

  console.log("\n── Applying upgrade ─────────────────────────────────────");
  const counts = await updateLessonWithPayload(client, lesson.lesson_id, PAYLOAD, { replaceExercises: true });
  console.log("Rows changed:");
  console.table([counts]);

  // Verify
  const [verified] = await fetchLessons(client, { lessonId: lesson.lesson_id, limit: 1 });
  const verifiedQuality = scoreLessonQuality(verified);
  console.log("\n── Post-apply verification ──────────────────────────────");
  console.log({
    lessonId: verified.lesson_id,
    title: verified.lesson_title,
    qualityScore: verifiedQuality.score,
    contentChars: String(verified.explanation ?? "").length,
    exercises: verified.exercise_count,
    issues: verifiedQuality.issues,
  });

  if (verifiedQuality.score < 85) {
    console.error(`\n⚠️  Post-apply score ${verifiedQuality.score} < 85 — check the DB.`);
  } else {
    console.log(`\n✅ Upgrade complete! Lesson ${lesson.lesson_id} now scores ${verifiedQuality.score}/100.`);
  }
});

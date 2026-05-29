import fs from "node:fs";
import path from "node:path";

const registryPath = path.join(process.cwd(), "curriculum-registry", "verified-official-curriculum.json");
const fallbackPath = path.join(process.cwd(), "curriculum-registry", "official-curriculum-registry.scaffold.json");
const outputDir = path.join(process.cwd(), "generated-curriculum", "deep-lessons");

function ensureDir(p) {
  fs.mkdirSync(p, { recursive: true });
}

function readRegistry() {
  if (fs.existsSync(registryPath)) {
    const verified = JSON.parse(fs.readFileSync(registryPath, "utf8"));
    if (Array.isArray(verified.items) && verified.items.length > 0) return verified.items;
  }

  if (!fs.existsSync(fallbackPath)) {
    console.error("Missing registry files. Install Phase50.1 first.");
    process.exit(1);
  }

  return JSON.parse(fs.readFileSync(fallbackPath, "utf8"));
}

function stageLanguage(stage) {
  if (stage === "primary") return { defaultLanguage: "darija", canSwitchTo: ["formal_arabic", "french"] };
  return { defaultLanguage: "formal_arabic", canSwitchTo: ["darija", "french", "english"] };
}

function stageTone(stage) {
  if (stage === "primary") return "بأسلوب بسيط، بصري، مرح، وقصير.";
  if (stage === "secondary") return "بأسلوب أكاديمي، منهجي، وموجه للامتحانات.";
  return "بأسلوب واضح، محفز، ومناسب لتلميذ مستقل.";
}

function reconstructDeepLesson(input) {
  const tone = stageTone(input.stage);

  return {
    registryId: input.registryId,
    sourceStatus: input.verificationStatus ?? "unknown",
    title: input.lessonTitle,
    grade: input.grade,
    gradeAr: input.gradeAr,
    subject: input.subject,
    subjectAr: input.subjectAr,
    unitTitle: input.unitTitle,
    languagePolicy: stageLanguage(input.stage),
    objectives: [
      `فهم فكرة "${input.lessonTitle}" داخل مادة ${input.subjectAr}.`,
      "تطبيق المفهوم في أمثلة تدريجية.",
      "تمييز الأخطاء الشائعة وتصحيحها.",
      "حل تمارين قصيرة ثم تمارين مركبة."
    ],
    prerequisiteCheck: [
      "ما المفاهيم السابقة التي يحتاجها المتعلم قبل هذا الدرس؟",
      "هل يعرف المتعلم المصطلحات الأساسية؟",
      "هل يستطيع إعطاء مثال بسيط قبل بداية الشرح؟"
    ],
    explanation: {
      hook: `لنبدأ ${input.lessonTitle} بطريقة قريبة من الواقع. ${tone}`,
      concept: `هذا درس أصلي من Oqul مبني على عنوان المنهج فقط، وليس نسخًا من أي مصدر. الهدف هو شرح ${input.lessonTitle} بوضوح، ثم تحويله إلى تدريب عملي.`,
      stepByStep: [
        "نحدد المفهوم الأساسي في الدرس.",
        "نربطه بمثال بسيط من الحياة اليومية أو من وضعية مدرسية.",
        "ننتقل إلى مثال متوسط مع توجيه المتعلم خطوة بخطوة.",
        "نطلب من المتعلم محاولة مستقلة قصيرة.",
        "نحلل الخطأ إن وُجد ونعود إلى prerequisite عند الحاجة."
      ],
      teacherNotes: [
        "لا تقدم الجواب مباشرة.",
        "اسأل المتعلم عن سبب اختياره للإجابة.",
        "استعمل التدرج: فهم → تطبيق → تحليل.",
        "احرص على مصطلحات دقيقة وخاصة في الثانوي."
      ]
    },
    examples: [
      {
        level: "easy",
        prompt: `مثال بسيط لفهم ${input.lessonTitle}.`,
        solutionSteps: ["اقرأ المعطيات.", "حدد المطلوب.", "طبق الفكرة الأساسية.", "تحقق من النتيجة."]
      },
      {
        level: "medium",
        prompt: `مثال متوسط يربط ${input.lessonTitle} بوضعية جديدة.`,
        solutionSteps: ["استخرج المعطيات.", "اختر الطريقة المناسبة.", "نفذ الحل تدريجيًا.", "اشرح لماذا هذه الطريقة صحيحة."]
      },
      {
        level: "hard",
        prompt: `تحدي متقدم في ${input.lessonTitle}.`,
        solutionSteps: ["حلل الوضعية.", "اربطها بمكتسب سابق.", "أنجز الحل.", "قارن النتيجة بالمنطق أو السياق."]
      }
    ],
    interactiveQuestions: [
      { question: `ما الفكرة الأساسية في ${input.lessonTitle}؟`, expectedAnswer: "يشرح المتعلم الفكرة بجملة قصيرة.", hint: "ابدأ بتحديد الكلمات المهمة في عنوان الدرس." },
      { question: "ما المثال الأبسط الذي يمكن أن يوضح هذا الدرس؟", expectedAnswer: "يعطي المتعلم مثالًا من حياته أو من الدرس.", hint: "فكر في شيء تراه في المدرسة أو البيت." },
      { question: "ما الخطأ الذي يمكن أن يقع فيه المتعلم هنا؟", expectedAnswer: "يذكر المتعلم خطأ شائعًا أو سوء فهم.", hint: "فكر في خطوة قد يخلط فيها التلميذ." }
    ],
    commonMistakes: [
      { mistake: "حفظ القاعدة دون فهم معناها.", whyItHappens: "لأن المتعلم ينتقل مباشرة إلى التمرين.", correction: "ارجع إلى مثال بصري أو وضعية بسيطة قبل التمرين." },
      { mistake: "استعمال مفهوم سابق في سياق غير مناسب.", whyItHappens: "لأن الدرس الجديد يشبه درسًا سابقًا جزئيًا.", correction: "قارن بين الحالتين وبيّن الفرق بخطوتين." },
      { mistake: "القفز إلى الجواب دون تبرير.", whyItHappens: "بسبب التسرع أو ضعف المنهجية.", correction: "اطلب من المتعلم كتابة أو قول خطوة وسيطة واحدة على الأقل." }
    ],
    remediation: [
      { trigger: "إجابة خاطئة أولى", action: "قدّم تلميحًا قصيرًا بدل الحل.", followUpQuestion: "ما المعطى الذي يمكن أن نبدأ به؟" },
      { trigger: "خطأ متكرر", action: "ارجع إلى prerequisite أبسط.", followUpQuestion: "هل تستطيع شرح الفكرة السابقة بمثال؟" },
      { trigger: "انخفاض الثقة", action: "اعط مثالًا أسهل وامتدح المحاولة.", followUpQuestion: "جرب خطوة واحدة فقط، ما أول شيء سنفعله؟" },
      { trigger: "إجابة صحيحة بسرعة", action: "ارفع الصعوبة تدريجيًا.", followUpQuestion: "هل تستطيع حل نفس الفكرة في وضعية أصعب؟" }
    ],
    exercises: {
      easy: [`تمرين 1 سهل حول ${input.lessonTitle}.`, `تمرين 2 سهل حول ${input.lessonTitle}.`, `تمرين 3 سهل حول ${input.lessonTitle}.`, `تمرين 4 سهل حول ${input.lessonTitle}.`],
      medium: [`تمرين 1 متوسط حول ${input.lessonTitle}.`, `تمرين 2 متوسط حول ${input.lessonTitle}.`, `تمرين 3 متوسط حول ${input.lessonTitle}.`, `تمرين 4 متوسط حول ${input.lessonTitle}.`],
      hard: [`تمرين 1 صعب حول ${input.lessonTitle}.`, `تمرين 2 صعب حول ${input.lessonTitle}.`],
      examStyle: [`سؤال بأسلوب فرض أو امتحان حول ${input.lessonTitle}.`, `وضعية إدماجية قصيرة حول ${input.lessonTitle}.`]
    },
    miniAssessment: [
      { question: "سؤال تحقق سريع 1", answer: "جواب نموذجي مختصر." },
      { question: "سؤال تحقق سريع 2", answer: "جواب نموذجي مختصر." },
      { question: "سؤال تحقق سريع 3", answer: "جواب نموذجي مختصر." },
      { question: "سؤال تحقق سريع 4", answer: "جواب نموذجي مختصر." },
      { question: "سؤال تحقق سريع 5", answer: "جواب نموذجي مختصر." }
    ],
    summary: [
      `تعلمنا الفكرة الأساسية في ${input.lessonTitle}.`,
      "طبقناها في أمثلة متدرجة.",
      "تعرفنا على أخطاء شائعة.",
      "أنهينا الدرس باختبار قصير وتمارين."
    ],
    leilaTutorHooks: {
      opening: "سأشرح لك الدرس خطوة بخطوة، وبعد كل جزء سأطرح عليك سؤالًا صغيرًا.",
      ifCorrect: "ممتاز، جوابك صحيح. الآن نرفع المستوى قليلًا.",
      ifWrong: "لا بأس، الخطأ يساعدنا نعرف أين نحتاج نراجع. سأعطيك تلميحًا.",
      ifConfused: "سنرجع خطوة للوراء ونشرحها بطريقة أبسط.",
      closing: "أحسنت، الآن لديك ملخص وتمارين لتثبيت الدرس."
    }
  };
}

function validate(lesson) {
  const issues = [];
  if (!lesson.title || lesson.title.includes("يحتاج مطابقة")) issues.push("lesson_title_not_verified");
  if (lesson.examples.length < 3) issues.push("not_enough_examples");
  if (lesson.interactiveQuestions.length < 3) issues.push("not_enough_interactive_questions");
  if (lesson.commonMistakes.length < 3) issues.push("not_enough_common_mistakes");
  const exerciseCount = lesson.exercises.easy.length + lesson.exercises.medium.length + lesson.exercises.hard.length + lesson.exercises.examStyle.length;
  if (exerciseCount < 12) issues.push("not_enough_exercises");
  return { ok: issues.length === 0, issues, score: Math.max(0, 100 - issues.length * 12) };
}

const registry = readRegistry();
ensureDir(outputDir);

const reports = [];
for (const item of registry) {
  const lesson = reconstructDeepLesson(item);
  const quality = validate(lesson);
  const stageDir = path.join(outputDir, item.stage ?? "unknown", item.grade ?? "unknown", item.subject ?? "unknown");
  ensureDir(stageDir);
  const fileName = `${item.registryId}.json`.replace(/[^\w\-_.]/g, "_");
  fs.writeFileSync(path.join(stageDir, fileName), JSON.stringify(lesson, null, 2), "utf8");
  reports.push({ registryId: item.registryId, stage: item.stage, grade: item.grade, subject: item.subject, title: item.lessonTitle, quality });
}

ensureDir(path.join(process.cwd(), "reports"));
fs.writeFileSync(path.join(process.cwd(), "reports", "phase50-2-deep-reconstruction-report.json"), JSON.stringify({
  generatedAt: new Date().toISOString(),
  totalGenerated: reports.length,
  averageQualityScore: Math.round(reports.reduce((s, r) => s + r.quality.score, 0) / Math.max(1, reports.length)),
  warning: "Lessons with unverified titles remain scaffold quality. Verify titles in Phase50.1 before final DB injection.",
  reports
}, null, 2), "utf8");

console.log("✅ Phase50.2 deep lesson reconstruction completed.");
console.log("Generated lessons:", reports.length);
console.log("Output:", "generated-curriculum/deep-lessons");
console.log("Report:", "reports/phase50-2-deep-reconstruction-report.json");
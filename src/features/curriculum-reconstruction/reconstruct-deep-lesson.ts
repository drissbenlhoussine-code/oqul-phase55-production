import type { DeepLesson, DeepLessonInput } from "./lesson-shape";

function stageLanguage(stage: DeepLessonInput["stage"]) {
  if (stage === "primary") {
    return {
      defaultLanguage: "darija" as const,
      canSwitchTo: ["formal_arabic", "french"],
    };
  }

  return {
    defaultLanguage: "formal_arabic" as const,
    canSwitchTo: ["darija", "french", "english"],
  };
}

function stageTone(stage: DeepLessonInput["stage"]) {
  if (stage === "primary") return "بأسلوب بسيط، بصري، مرح، وقصير.";
  if (stage === "secondary") return "بأسلوب أكاديمي، منهجي، وموجه للامتحانات.";
  return "بأسلوب واضح، محفز، ومناسب لتلميذ مستقل.";
}

export function reconstructDeepLesson(input: DeepLessonInput): DeepLesson {
  const tone = stageTone(input.stage);

  return {
    registryId: input.registryId,
    title: input.lessonTitle,
    grade: input.grade,
    subject: input.subject,
    unitTitle: input.unitTitle,
    languagePolicy: stageLanguage(input.stage),
    objectives: [
      `فهم فكرة "${input.lessonTitle}" داخل مادة ${input.subjectAr}.`,
      "تطبيق المفهوم في أمثلة تدريجية.",
      "تمييز الأخطاء الشائعة وتصحيحها.",
      "حل تمارين قصيرة ثم تمارين مركبة.",
    ],
    prerequisiteCheck: [
      "ما المفاهيم السابقة التي تحتاجها قبل هذا الدرس؟",
      "هل يعرف المتعلم المصطلحات الأساسية؟",
      "هل يستطيع إعطاء مثال بسيط قبل بداية الشرح؟",
    ],
    explanation: {
      hook: `لنبدأ ${input.lessonTitle} بطريقة قريبة من الواقع. ${tone}`,
      concept: `هذا درس أصلي من Oqul مبني على عنوان المنهج فقط، وليس نسخًا من أي مصدر. الهدف هو شرح ${input.lessonTitle} بوضوح، ثم تحويله إلى تدريب عملي.`,
      stepByStep: [
        "نحدد المفهوم الأساسي في الدرس.",
        "نربطه بمثال بسيط من الحياة اليومية أو من وضعية مدرسية.",
        "ننتقل إلى مثال متوسط مع توجيه المتعلم خطوة بخطوة.",
        "نطلب من المتعلم محاولة مستقلة قصيرة.",
        "نحلل الخطأ إن وُجد ونعود إلى prerequisite عند الحاجة.",
      ],
      teacherNotes: [
        "لا تقدم الجواب مباشرة.",
        "اسأل المتعلم عن سبب اختياره للإجابة.",
        "استعمل التدرج: فهم → تطبيق → تحليل.",
        "احرص على مصطلحات دقيقة وخاصة في الثانوي.",
      ],
    },
    examples: [
      {
        level: "easy",
        prompt: `مثال بسيط لفهم ${input.lessonTitle}.`,
        solutionSteps: ["اقرأ المعطيات.", "حدد المطلوب.", "طبق الفكرة الأساسية.", "تحقق من النتيجة."],
      },
      {
        level: "medium",
        prompt: `مثال متوسط يربط ${input.lessonTitle} بوضعية جديدة.`,
        solutionSteps: ["استخرج المعطيات.", "اختر الطريقة المناسبة.", "نفذ الحل تدريجيًا.", "اشرح لماذا هذه الطريقة صحيحة."],
      },
      {
        level: "hard",
        prompt: `تحدي متقدم في ${input.lessonTitle}.`,
        solutionSteps: ["حلل الوضعية.", "اربطها بمكتسب سابق.", "أنجز الحل.", "قارن النتيجة بالمنطق أو السياق."],
      },
    ],
    interactiveQuestions: [
      {
        question: `ما الفكرة الأساسية في ${input.lessonTitle}؟`,
        expectedAnswer: "يشرح المتعلم الفكرة بجملة قصيرة.",
        hint: "ابدأ بتحديد الكلمات المهمة في عنوان الدرس.",
      },
      {
        question: "ما المثال الأبسط الذي يمكن أن يوضح هذا الدرس؟",
        expectedAnswer: "يعطي المتعلم مثالًا من حياته أو من الدرس.",
        hint: "فكر في شيء تراه في المدرسة أو البيت.",
      },
      {
        question: "ما الخطأ الذي يمكن أن يقع فيه المتعلم هنا؟",
        expectedAnswer: "يذكر المتعلم خطأ شائعًا أو سوء فهم.",
        hint: "فكر في خطوة قد يخلط فيها التلميذ.",
      },
    ],
    commonMistakes: [
      {
        mistake: "حفظ القاعدة دون فهم معناها.",
        whyItHappens: "لأن المتعلم ينتقل مباشرة إلى التمرين.",
        correction: "ارجع إلى مثال بصري أو وضعية بسيطة قبل التمرين.",
      },
      {
        mistake: "استعمال مفهوم سابق في سياق غير مناسب.",
        whyItHappens: "لأن الدرس الجديد يشبه درسًا سابقًا جزئيًا.",
        correction: "قارن بين الحالتين وبيّن الفرق بخطوتين.",
      },
      {
        mistake: "القفز إلى الجواب دون تبرير.",
        whyItHappens: "بسبب التسرع أو ضعف المنهجية.",
        correction: "اطلب من المتعلم كتابة أو قول خطوة وسيطة واحدة على الأقل.",
      },
    ],
    remediation: [
      {
        trigger: "إجابة خاطئة أولى",
        action: "قدّم تلميحًا قصيرًا بدل الحل.",
        followUpQuestion: "ما المعطى الذي يمكن أن نبدأ به؟",
      },
      {
        trigger: "خطأ متكرر",
        action: "ارجع إلى prerequisite أبسط.",
        followUpQuestion: "هل تستطيع شرح الفكرة السابقة بمثال؟",
      },
      {
        trigger: "انخفاض الثقة",
        action: "اعط مثالًا أسهل وامتدح المحاولة.",
        followUpQuestion: "جرب خطوة واحدة فقط، ما أول شيء سنفعله؟",
      },
      {
        trigger: "إجابة صحيحة بسرعة",
        action: "ارفع الصعوبة تدريجيًا.",
        followUpQuestion: "هل تستطيع حل نفس الفكرة في وضعية أصعب؟",
      },
    ],
    exercises: {
      easy: [
        `تمرين 1 سهل حول ${input.lessonTitle}.`,
        `تمرين 2 سهل حول ${input.lessonTitle}.`,
        `تمرين 3 سهل حول ${input.lessonTitle}.`,
        `تمرين 4 سهل حول ${input.lessonTitle}.`,
      ],
      medium: [
        `تمرين 1 متوسط حول ${input.lessonTitle}.`,
        `تمرين 2 متوسط حول ${input.lessonTitle}.`,
        `تمرين 3 متوسط حول ${input.lessonTitle}.`,
        `تمرين 4 متوسط حول ${input.lessonTitle}.`,
      ],
      hard: [
        `تمرين 1 صعب حول ${input.lessonTitle}.`,
        `تمرين 2 صعب حول ${input.lessonTitle}.`,
      ],
      examStyle: [
        `سؤال بأسلوب فرض أو امتحان حول ${input.lessonTitle}.`,
        `وضعية إدماجية قصيرة حول ${input.lessonTitle}.`,
      ],
    },
    miniAssessment: [
      { question: "سؤال تحقق سريع 1", answer: "جواب نموذجي مختصر." },
      { question: "سؤال تحقق سريع 2", answer: "جواب نموذجي مختصر." },
      { question: "سؤال تحقق سريع 3", answer: "جواب نموذجي مختصر." },
      { question: "سؤال تحقق سريع 4", answer: "جواب نموذجي مختصر." },
      { question: "سؤال تحقق سريع 5", answer: "جواب نموذجي مختصر." },
    ],
    summary: [
      `تعلمنا الفكرة الأساسية في ${input.lessonTitle}.`,
      "طبقناها في أمثلة متدرجة.",
      "تعرفنا على أخطاء شائعة.",
      "أنهينا الدرس باختبار قصير وتمارين.",
    ],
    leilaTutorHooks: {
      opening: "سأشرح لك الدرس خطوة بخطوة، وبعد كل جزء سأطرح عليك سؤالًا صغيرًا.",
      ifCorrect: "ممتاز، جوابك صحيح. الآن نرفع المستوى قليلًا.",
      ifWrong: "لا بأس، الخطأ يساعدنا نعرف أين نحتاج نراجع. سأعطيك تلميحًا.",
      ifConfused: "سنرجع خطوة للوراء ونشرحها بطريقة أبسط.",
      closing: "أحسنت، الآن لديك ملخص وتمارين لتثبيت الدرس.",
    },
  };
}
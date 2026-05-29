import type { PrimaryGrade, PrimaryLesson, PrimarySubject } from "./types";

export const primarySubjects: Array<{ id: PrimarySubject; titleAr: string; titleFr: string; icon: string }> = [
  { id: "math", titleAr: "الرياضيات", titleFr: "Mathématiques", icon: "🔢" },
  { id: "arabic", titleAr: "اللغة العربية", titleFr: "Arabe", icon: "ض" },
  { id: "french", titleAr: "اللغة الفرنسية", titleFr: "Français", icon: "Fr" },
  { id: "science", titleAr: "النشاط العلمي", titleFr: "Activité scientifique", icon: "🔬" },
  { id: "islamic_education", titleAr: "التربية الإسلامية", titleFr: "Éducation islamique", icon: "☪" },
  { id: "social_studies", titleAr: "الاجتماعيات والتربية المدنية", titleFr: "Éveil social", icon: "🌍" },
];

export const primaryCurriculum: Record<PrimaryGrade, Record<PrimarySubject, PrimaryLesson[]>> = 
{
  "1AP": {
    "math": [
      {
        "id": "1AP-math-01",
        "grade": "1AP",
        "subject": "math",
        "unit": "الأعداد من 0 إلى 99",
        "titleAr": "الأعداد من 0 إلى 99",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الأعداد من 0 إلى 99",
          "يطبق الأعداد من 0 إلى 99 في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأعداد من 0 إلى 99 بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-math-02",
        "grade": "1AP",
        "subject": "math",
        "unit": "المقارنة والترتيب",
        "titleAr": "المقارنة والترتيب",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم المقارنة والترتيب",
          "يطبق المقارنة والترتيب في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المقارنة والترتيب بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-math-03",
        "grade": "1AP",
        "subject": "math",
        "unit": "الجمع والطرح البسيط",
        "titleAr": "الجمع والطرح البسيط",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الجمع والطرح البسيط",
          "يطبق الجمع والطرح البسيط في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الجمع والطرح البسيط بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-math-04",
        "grade": "1AP",
        "subject": "math",
        "unit": "الأشكال الهندسية",
        "titleAr": "الأشكال الهندسية",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الأشكال الهندسية",
          "يطبق الأشكال الهندسية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأشكال الهندسية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-math-05",
        "grade": "1AP",
        "subject": "math",
        "unit": "القياس: الطول والكتلة",
        "titleAr": "القياس: الطول والكتلة",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم القياس: الطول والكتلة",
          "يطبق القياس: الطول والكتلة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القياس: الطول والكتلة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-math-06",
        "grade": "1AP",
        "subject": "math",
        "unit": "الزمان والأيام",
        "titleAr": "الزمان والأيام",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الزمان والأيام",
          "يطبق الزمان والأيام في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الزمان والأيام بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-math-07",
        "grade": "1AP",
        "subject": "math",
        "unit": "المسائل المصورة",
        "titleAr": "المسائل المصورة",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم المسائل المصورة",
          "يطبق المسائل المصورة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المسائل المصورة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-math-08",
        "grade": "1AP",
        "subject": "math",
        "unit": "تنظيم المعطيات البسيطة",
        "titleAr": "تنظيم المعطيات البسيطة",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم تنظيم المعطيات البسيطة",
          "يطبق تنظيم المعطيات البسيطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح تنظيم المعطيات البسيطة بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "arabic": [
      {
        "id": "1AP-arabic-01",
        "grade": "1AP",
        "subject": "arabic",
        "unit": "الحروف والأصوات",
        "titleAr": "الحروف والأصوات",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الحروف والأصوات",
          "يطبق الحروف والأصوات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الحروف والأصوات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-arabic-02",
        "grade": "1AP",
        "subject": "arabic",
        "unit": "المقاطع والكلمات",
        "titleAr": "المقاطع والكلمات",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم المقاطع والكلمات",
          "يطبق المقاطع والكلمات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المقاطع والكلمات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-arabic-03",
        "grade": "1AP",
        "subject": "arabic",
        "unit": "قراءة جمل قصيرة",
        "titleAr": "قراءة جمل قصيرة",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم قراءة جمل قصيرة",
          "يطبق قراءة جمل قصيرة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح قراءة جمل قصيرة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-arabic-04",
        "grade": "1AP",
        "subject": "arabic",
        "unit": "فهم نص قصير",
        "titleAr": "فهم نص قصير",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم فهم نص قصير",
          "يطبق فهم نص قصير في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح فهم نص قصير بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-arabic-05",
        "grade": "1AP",
        "subject": "arabic",
        "unit": "الجملة المفيدة",
        "titleAr": "الجملة المفيدة",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الجملة المفيدة",
          "يطبق الجملة المفيدة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الجملة المفيدة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-arabic-06",
        "grade": "1AP",
        "subject": "arabic",
        "unit": "التعبير الشفهي",
        "titleAr": "التعبير الشفهي",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم التعبير الشفهي",
          "يطبق التعبير الشفهي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التعبير الشفهي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-arabic-07",
        "grade": "1AP",
        "subject": "arabic",
        "unit": "الخط والإملاء",
        "titleAr": "الخط والإملاء",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الخط والإملاء",
          "يطبق الخط والإملاء في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الخط والإملاء بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-arabic-08",
        "grade": "1AP",
        "subject": "arabic",
        "unit": "قصة قصيرة ومغزى",
        "titleAr": "قصة قصيرة ومغزى",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم قصة قصيرة ومغزى",
          "يطبق قصة قصيرة ومغزى في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح قصة قصيرة ومغزى بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "french": [
      {
        "id": "1AP-french-01",
        "grade": "1AP",
        "subject": "french",
        "unit": "Alphabet et sons",
        "titleAr": "Alphabet et sons",
        "titleFr": "Alphabet et sons",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Alphabet et sons",
          "Appliquer Alphabet et sons dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Alphabet et sons بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-french-02",
        "grade": "1AP",
        "subject": "french",
        "unit": "Mots de la classe",
        "titleAr": "Mots de la classe",
        "titleFr": "Mots de la classe",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Mots de la classe",
          "Appliquer Mots de la classe dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Mots de la classe بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-french-03",
        "grade": "1AP",
        "subject": "french",
        "unit": "Se présenter",
        "titleAr": "Se présenter",
        "titleFr": "Se présenter",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Se présenter",
          "Appliquer Se présenter dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Se présenter بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-french-04",
        "grade": "1AP",
        "subject": "french",
        "unit": "Consignes simples",
        "titleAr": "Consignes simples",
        "titleFr": "Consignes simples",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Consignes simples",
          "Appliquer Consignes simples dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Consignes simples بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-french-05",
        "grade": "1AP",
        "subject": "french",
        "unit": "Articles simples",
        "titleAr": "Articles simples",
        "titleFr": "Articles simples",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Articles simples",
          "Appliquer Articles simples dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Articles simples بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-french-06",
        "grade": "1AP",
        "subject": "french",
        "unit": "Nombres et couleurs",
        "titleAr": "Nombres et couleurs",
        "titleFr": "Nombres et couleurs",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Nombres et couleurs",
          "Appliquer Nombres et couleurs dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Nombres et couleurs بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-french-07",
        "grade": "1AP",
        "subject": "french",
        "unit": "Petites phrases",
        "titleAr": "Petites phrases",
        "titleFr": "Petites phrases",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Petites phrases",
          "Appliquer Petites phrases dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Petites phrases بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-french-08",
        "grade": "1AP",
        "subject": "french",
        "unit": "Compréhension orale",
        "titleAr": "Compréhension orale",
        "titleFr": "Compréhension orale",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Compréhension orale",
          "Appliquer Compréhension orale dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Compréhension orale بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "science": [
      {
        "id": "1AP-science-01",
        "grade": "1AP",
        "subject": "science",
        "unit": "الحواس الخمس",
        "titleAr": "الحواس الخمس",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الحواس الخمس",
          "يطبق الحواس الخمس في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الحواس الخمس بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-science-02",
        "grade": "1AP",
        "subject": "science",
        "unit": "النظافة والصحة",
        "titleAr": "النظافة والصحة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم النظافة والصحة",
          "يطبق النظافة والصحة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح النظافة والصحة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-science-03",
        "grade": "1AP",
        "subject": "science",
        "unit": "النباتات القريبة",
        "titleAr": "النباتات القريبة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم النباتات القريبة",
          "يطبق النباتات القريبة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح النباتات القريبة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-science-04",
        "grade": "1AP",
        "subject": "science",
        "unit": "الحيوانات الأليفة",
        "titleAr": "الحيوانات الأليفة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الحيوانات الأليفة",
          "يطبق الحيوانات الأليفة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الحيوانات الأليفة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-science-05",
        "grade": "1AP",
        "subject": "science",
        "unit": "الماء في حياتنا",
        "titleAr": "الماء في حياتنا",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الماء في حياتنا",
          "يطبق الماء في حياتنا في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الماء في حياتنا بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-science-06",
        "grade": "1AP",
        "subject": "science",
        "unit": "الطقس والفصول",
        "titleAr": "الطقس والفصول",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الطقس والفصول",
          "يطبق الطقس والفصول في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الطقس والفصول بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-science-07",
        "grade": "1AP",
        "subject": "science",
        "unit": "سلامة الطفل",
        "titleAr": "سلامة الطفل",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم سلامة الطفل",
          "يطبق سلامة الطفل في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح سلامة الطفل بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-science-08",
        "grade": "1AP",
        "subject": "science",
        "unit": "ملاحظة وتصنيف",
        "titleAr": "ملاحظة وتصنيف",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم ملاحظة وتصنيف",
          "يطبق ملاحظة وتصنيف في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح ملاحظة وتصنيف بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "islamic_education": [
      {
        "id": "1AP-islamic_education-01",
        "grade": "1AP",
        "subject": "islamic_education",
        "unit": "الطهارة والنظافة",
        "titleAr": "الطهارة والنظافة",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الطهارة والنظافة",
          "يطبق الطهارة والنظافة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الطهارة والنظافة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-islamic_education-02",
        "grade": "1AP",
        "subject": "islamic_education",
        "unit": "آداب التحية",
        "titleAr": "آداب التحية",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم آداب التحية",
          "يطبق آداب التحية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح آداب التحية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-islamic_education-03",
        "grade": "1AP",
        "subject": "islamic_education",
        "unit": "الصدق والأمانة",
        "titleAr": "الصدق والأمانة",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الصدق والأمانة",
          "يطبق الصدق والأمانة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الصدق والأمانة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-islamic_education-04",
        "grade": "1AP",
        "subject": "islamic_education",
        "unit": "بر الوالدين",
        "titleAr": "بر الوالدين",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم بر الوالدين",
          "يطبق بر الوالدين في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح بر الوالدين بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-islamic_education-05",
        "grade": "1AP",
        "subject": "islamic_education",
        "unit": "سور قصيرة وفهم عام",
        "titleAr": "سور قصيرة وفهم عام",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم سور قصيرة وفهم عام",
          "يطبق سور قصيرة وفهم عام في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح سور قصيرة وفهم عام بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-islamic_education-06",
        "grade": "1AP",
        "subject": "islamic_education",
        "unit": "الرحمة والتعاون",
        "titleAr": "الرحمة والتعاون",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الرحمة والتعاون",
          "يطبق الرحمة والتعاون في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الرحمة والتعاون بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-islamic_education-07",
        "grade": "1AP",
        "subject": "islamic_education",
        "unit": "آداب المسجد",
        "titleAr": "آداب المسجد",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم آداب المسجد",
          "يطبق آداب المسجد في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح آداب المسجد بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-islamic_education-08",
        "grade": "1AP",
        "subject": "islamic_education",
        "unit": "سلوك يومي حسن",
        "titleAr": "سلوك يومي حسن",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم سلوك يومي حسن",
          "يطبق سلوك يومي حسن في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح سلوك يومي حسن بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "social_studies": [
      {
        "id": "1AP-social_studies-01",
        "grade": "1AP",
        "subject": "social_studies",
        "unit": "أسرتي ومدرستي",
        "titleAr": "أسرتي ومدرستي",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم أسرتي ومدرستي",
          "يطبق أسرتي ومدرستي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح أسرتي ومدرستي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-social_studies-02",
        "grade": "1AP",
        "subject": "social_studies",
        "unit": "قواعد القسم",
        "titleAr": "قواعد القسم",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم قواعد القسم",
          "يطبق قواعد القسم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح قواعد القسم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-social_studies-03",
        "grade": "1AP",
        "subject": "social_studies",
        "unit": "الطريق والسلامة",
        "titleAr": "الطريق والسلامة",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الطريق والسلامة",
          "يطبق الطريق والسلامة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الطريق والسلامة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-social_studies-04",
        "grade": "1AP",
        "subject": "social_studies",
        "unit": "حيي ومدينتي",
        "titleAr": "حيي ومدينتي",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم حيي ومدينتي",
          "يطبق حيي ومدينتي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح حيي ومدينتي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-social_studies-05",
        "grade": "1AP",
        "subject": "social_studies",
        "unit": "الأعياد والمناسبات",
        "titleAr": "الأعياد والمناسبات",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الأعياد والمناسبات",
          "يطبق الأعياد والمناسبات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأعياد والمناسبات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-social_studies-06",
        "grade": "1AP",
        "subject": "social_studies",
        "unit": "احترام الآخر",
        "titleAr": "احترام الآخر",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم احترام الآخر",
          "يطبق احترام الآخر في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح احترام الآخر بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-social_studies-07",
        "grade": "1AP",
        "subject": "social_studies",
        "unit": "المواطنة الصغيرة",
        "titleAr": "المواطنة الصغيرة",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم المواطنة الصغيرة",
          "يطبق المواطنة الصغيرة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المواطنة الصغيرة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "1AP-social_studies-08",
        "grade": "1AP",
        "subject": "social_studies",
        "unit": "الزمان والمكان",
        "titleAr": "الزمان والمكان",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الزمان والمكان",
          "يطبق الزمان والمكان في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الزمان والمكان بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ]
  },
  "2AP": {
    "math": [
      {
        "id": "2AP-math-01",
        "grade": "2AP",
        "subject": "math",
        "unit": "الأعداد إلى 999",
        "titleAr": "الأعداد إلى 999",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الأعداد إلى 999",
          "يطبق الأعداد إلى 999 في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأعداد إلى 999 بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-math-02",
        "grade": "2AP",
        "subject": "math",
        "unit": "الجمع بالاحتفاظ",
        "titleAr": "الجمع بالاحتفاظ",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الجمع بالاحتفاظ",
          "يطبق الجمع بالاحتفاظ في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الجمع بالاحتفاظ بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-math-03",
        "grade": "2AP",
        "subject": "math",
        "unit": "الطرح بالاستلاف",
        "titleAr": "الطرح بالاستلاف",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الطرح بالاستلاف",
          "يطبق الطرح بالاستلاف في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الطرح بالاستلاف بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-math-04",
        "grade": "2AP",
        "subject": "math",
        "unit": "بداية الضرب",
        "titleAr": "بداية الضرب",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم بداية الضرب",
          "يطبق بداية الضرب في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح بداية الضرب بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-math-05",
        "grade": "2AP",
        "subject": "math",
        "unit": "الأطوال والنقود",
        "titleAr": "الأطوال والنقود",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الأطوال والنقود",
          "يطبق الأطوال والنقود في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأطوال والنقود بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-math-06",
        "grade": "2AP",
        "subject": "math",
        "unit": "المجسمات والأشكال",
        "titleAr": "المجسمات والأشكال",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم المجسمات والأشكال",
          "يطبق المجسمات والأشكال في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المجسمات والأشكال بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-math-07",
        "grade": "2AP",
        "subject": "math",
        "unit": "قراءة جداول بسيطة",
        "titleAr": "قراءة جداول بسيطة",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم قراءة جداول بسيطة",
          "يطبق قراءة جداول بسيطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح قراءة جداول بسيطة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-math-08",
        "grade": "2AP",
        "subject": "math",
        "unit": "حل مسائل من خطوتين",
        "titleAr": "حل مسائل من خطوتين",
        "titleFr": "Mathématiques",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم حل مسائل من خطوتين",
          "يطبق حل مسائل من خطوتين في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح حل مسائل من خطوتين بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "arabic": [
      {
        "id": "2AP-arabic-01",
        "grade": "2AP",
        "subject": "arabic",
        "unit": "قراءة نصوص قصيرة",
        "titleAr": "قراءة نصوص قصيرة",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم قراءة نصوص قصيرة",
          "يطبق قراءة نصوص قصيرة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح قراءة نصوص قصيرة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-arabic-02",
        "grade": "2AP",
        "subject": "arabic",
        "unit": "المفرد والجمع",
        "titleAr": "المفرد والجمع",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم المفرد والجمع",
          "يطبق المفرد والجمع في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المفرد والجمع بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-arabic-03",
        "grade": "2AP",
        "subject": "arabic",
        "unit": "الجملة الاسمية والفعلية",
        "titleAr": "الجملة الاسمية والفعلية",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الجملة الاسمية والفعلية",
          "يطبق الجملة الاسمية والفعلية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الجملة الاسمية والفعلية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-arabic-04",
        "grade": "2AP",
        "subject": "arabic",
        "unit": "التنوين والشدة",
        "titleAr": "التنوين والشدة",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم التنوين والشدة",
          "يطبق التنوين والشدة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التنوين والشدة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-arabic-05",
        "grade": "2AP",
        "subject": "arabic",
        "unit": "فهم المعنى والسؤال",
        "titleAr": "فهم المعنى والسؤال",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم فهم المعنى والسؤال",
          "يطبق فهم المعنى والسؤال في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح فهم المعنى والسؤال بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-arabic-06",
        "grade": "2AP",
        "subject": "arabic",
        "unit": "كتابة فقرة قصيرة",
        "titleAr": "كتابة فقرة قصيرة",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم كتابة فقرة قصيرة",
          "يطبق كتابة فقرة قصيرة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح كتابة فقرة قصيرة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-arabic-07",
        "grade": "2AP",
        "subject": "arabic",
        "unit": "التعبير عن الصور",
        "titleAr": "التعبير عن الصور",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم التعبير عن الصور",
          "يطبق التعبير عن الصور في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التعبير عن الصور بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-arabic-08",
        "grade": "2AP",
        "subject": "arabic",
        "unit": "الإملاء الموجه",
        "titleAr": "الإملاء الموجه",
        "titleFr": "Arabe",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الإملاء الموجه",
          "يطبق الإملاء الموجه في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الإملاء الموجه بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "french": [
      {
        "id": "2AP-french-01",
        "grade": "2AP",
        "subject": "french",
        "unit": "Lecture de syllabes",
        "titleAr": "Lecture de syllabes",
        "titleFr": "Lecture de syllabes",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Lecture de syllabes",
          "Appliquer Lecture de syllabes dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Lecture de syllabes بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-french-02",
        "grade": "2AP",
        "subject": "french",
        "unit": "Verbes être et avoir",
        "titleAr": "Verbes être et avoir",
        "titleFr": "Verbes être et avoir",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Verbes être et avoir",
          "Appliquer Verbes être et avoir dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Verbes être et avoir بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-french-03",
        "grade": "2AP",
        "subject": "french",
        "unit": "Phrase simple",
        "titleAr": "Phrase simple",
        "titleFr": "Phrase simple",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Phrase simple",
          "Appliquer Phrase simple dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Phrase simple بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-french-04",
        "grade": "2AP",
        "subject": "french",
        "unit": "Famille et école",
        "titleAr": "Famille et école",
        "titleFr": "Famille et école",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Famille et école",
          "Appliquer Famille et école dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Famille et école بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-french-05",
        "grade": "2AP",
        "subject": "french",
        "unit": "Présent des verbes usuels",
        "titleAr": "Présent des verbes usuels",
        "titleFr": "Présent des verbes usuels",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Présent des verbes usuels",
          "Appliquer Présent des verbes usuels dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Présent des verbes usuels بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-french-06",
        "grade": "2AP",
        "subject": "french",
        "unit": "Questions simples",
        "titleAr": "Questions simples",
        "titleFr": "Questions simples",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Questions simples",
          "Appliquer Questions simples dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Questions simples بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-french-07",
        "grade": "2AP",
        "subject": "french",
        "unit": "Petit dialogue",
        "titleAr": "Petit dialogue",
        "titleFr": "Petit dialogue",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Petit dialogue",
          "Appliquer Petit dialogue dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Petit dialogue بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-french-08",
        "grade": "2AP",
        "subject": "french",
        "unit": "Production de phrases",
        "titleAr": "Production de phrases",
        "titleFr": "Production de phrases",
        "durationMinutes": 8,
        "objectives": [
          "Comprendre: Production de phrases",
          "Appliquer Production de phrases dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Production de phrases بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "science": [
      {
        "id": "2AP-science-01",
        "grade": "2AP",
        "subject": "science",
        "unit": "حاجات النباتات",
        "titleAr": "حاجات النباتات",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم حاجات النباتات",
          "يطبق حاجات النباتات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح حاجات النباتات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-science-02",
        "grade": "2AP",
        "subject": "science",
        "unit": "حاجات الحيوانات",
        "titleAr": "حاجات الحيوانات",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم حاجات الحيوانات",
          "يطبق حاجات الحيوانات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح حاجات الحيوانات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-science-03",
        "grade": "2AP",
        "subject": "science",
        "unit": "التغذية السليمة",
        "titleAr": "التغذية السليمة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم التغذية السليمة",
          "يطبق التغذية السليمة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التغذية السليمة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-science-04",
        "grade": "2AP",
        "subject": "science",
        "unit": "الهواء والحركة",
        "titleAr": "الهواء والحركة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الهواء والحركة",
          "يطبق الهواء والحركة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الهواء والحركة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-science-05",
        "grade": "2AP",
        "subject": "science",
        "unit": "الضوء والظل",
        "titleAr": "الضوء والظل",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الضوء والظل",
          "يطبق الضوء والظل في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الضوء والظل بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-science-06",
        "grade": "2AP",
        "subject": "science",
        "unit": "الماء والحالات",
        "titleAr": "الماء والحالات",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الماء والحالات",
          "يطبق الماء والحالات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الماء والحالات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-science-07",
        "grade": "2AP",
        "subject": "science",
        "unit": "السلامة المنزلية",
        "titleAr": "السلامة المنزلية",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم السلامة المنزلية",
          "يطبق السلامة المنزلية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح السلامة المنزلية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-science-08",
        "grade": "2AP",
        "subject": "science",
        "unit": "تجربة بسيطة",
        "titleAr": "تجربة بسيطة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم تجربة بسيطة",
          "يطبق تجربة بسيطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح تجربة بسيطة بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "islamic_education": [
      {
        "id": "2AP-islamic_education-01",
        "grade": "2AP",
        "subject": "islamic_education",
        "unit": "الوضوء والصلاة",
        "titleAr": "الوضوء والصلاة",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الوضوء والصلاة",
          "يطبق الوضوء والصلاة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الوضوء والصلاة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-islamic_education-02",
        "grade": "2AP",
        "subject": "islamic_education",
        "unit": "احترام الوالدين",
        "titleAr": "احترام الوالدين",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم احترام الوالدين",
          "يطبق احترام الوالدين في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح احترام الوالدين بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-islamic_education-03",
        "grade": "2AP",
        "subject": "islamic_education",
        "unit": "الأمانة في القسم",
        "titleAr": "الأمانة في القسم",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الأمانة في القسم",
          "يطبق الأمانة في القسم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأمانة في القسم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-islamic_education-04",
        "grade": "2AP",
        "subject": "islamic_education",
        "unit": "آداب الطعام",
        "titleAr": "آداب الطعام",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم آداب الطعام",
          "يطبق آداب الطعام في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح آداب الطعام بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-islamic_education-05",
        "grade": "2AP",
        "subject": "islamic_education",
        "unit": "سور قصيرة",
        "titleAr": "سور قصيرة",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم سور قصيرة",
          "يطبق سور قصيرة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح سور قصيرة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-islamic_education-06",
        "grade": "2AP",
        "subject": "islamic_education",
        "unit": "التعاون والإحسان",
        "titleAr": "التعاون والإحسان",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم التعاون والإحسان",
          "يطبق التعاون والإحسان في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التعاون والإحسان بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-islamic_education-07",
        "grade": "2AP",
        "subject": "islamic_education",
        "unit": "المحافظة على البيئة",
        "titleAr": "المحافظة على البيئة",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم المحافظة على البيئة",
          "يطبق المحافظة على البيئة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المحافظة على البيئة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-islamic_education-08",
        "grade": "2AP",
        "subject": "islamic_education",
        "unit": "سيرة مبسطة",
        "titleAr": "سيرة مبسطة",
        "titleFr": "Éducation islamique",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم سيرة مبسطة",
          "يطبق سيرة مبسطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح سيرة مبسطة بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "social_studies": [
      {
        "id": "2AP-social_studies-01",
        "grade": "2AP",
        "subject": "social_studies",
        "unit": "المدرسة والحي",
        "titleAr": "المدرسة والحي",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم المدرسة والحي",
          "يطبق المدرسة والحي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المدرسة والحي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-social_studies-02",
        "grade": "2AP",
        "subject": "social_studies",
        "unit": "المهن والخدمات",
        "titleAr": "المهن والخدمات",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم المهن والخدمات",
          "يطبق المهن والخدمات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المهن والخدمات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-social_studies-03",
        "grade": "2AP",
        "subject": "social_studies",
        "unit": "قواعد المرور",
        "titleAr": "قواعد المرور",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم قواعد المرور",
          "يطبق قواعد المرور في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح قواعد المرور بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-social_studies-04",
        "grade": "2AP",
        "subject": "social_studies",
        "unit": "الخريطة البسيطة",
        "titleAr": "الخريطة البسيطة",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الخريطة البسيطة",
          "يطبق الخريطة البسيطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الخريطة البسيطة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-social_studies-05",
        "grade": "2AP",
        "subject": "social_studies",
        "unit": "الأسرة والتعاون",
        "titleAr": "الأسرة والتعاون",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الأسرة والتعاون",
          "يطبق الأسرة والتعاون في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأسرة والتعاون بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-social_studies-06",
        "grade": "2AP",
        "subject": "social_studies",
        "unit": "حقوق وواجبات الطفل",
        "titleAr": "حقوق وواجبات الطفل",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم حقوق وواجبات الطفل",
          "يطبق حقوق وواجبات الطفل في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح حقوق وواجبات الطفل بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-social_studies-07",
        "grade": "2AP",
        "subject": "social_studies",
        "unit": "المرافق العمومية",
        "titleAr": "المرافق العمومية",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم المرافق العمومية",
          "يطبق المرافق العمومية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المرافق العمومية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "2AP-social_studies-08",
        "grade": "2AP",
        "subject": "social_studies",
        "unit": "الزمن اليومي",
        "titleAr": "الزمن اليومي",
        "titleFr": "Éveil social",
        "durationMinutes": 8,
        "objectives": [
          "يفهم المتعلم مفهوم الزمن اليومي",
          "يطبق الزمن اليومي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الزمن اليومي بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ]
  },
  "3AP": {
    "math": [
      {
        "id": "3AP-math-01",
        "grade": "3AP",
        "subject": "math",
        "unit": "الأعداد إلى 9999",
        "titleAr": "الأعداد إلى 9999",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الأعداد إلى 9999",
          "يطبق الأعداد إلى 9999 في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأعداد إلى 9999 بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-math-02",
        "grade": "3AP",
        "subject": "math",
        "unit": "الضرب والقسمة البسيطة",
        "titleAr": "الضرب والقسمة البسيطة",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الضرب والقسمة البسيطة",
          "يطبق الضرب والقسمة البسيطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الضرب والقسمة البسيطة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-math-03",
        "grade": "3AP",
        "subject": "math",
        "unit": "الكسور الأولى",
        "titleAr": "الكسور الأولى",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الكسور الأولى",
          "يطبق الكسور الأولى في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الكسور الأولى بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-math-04",
        "grade": "3AP",
        "subject": "math",
        "unit": "المحيط والمساحة الأولى",
        "titleAr": "المحيط والمساحة الأولى",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المحيط والمساحة الأولى",
          "يطبق المحيط والمساحة الأولى في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المحيط والمساحة الأولى بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-math-05",
        "grade": "3AP",
        "subject": "math",
        "unit": "الزوايا والأشكال",
        "titleAr": "الزوايا والأشكال",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الزوايا والأشكال",
          "يطبق الزوايا والأشكال في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الزوايا والأشكال بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-math-06",
        "grade": "3AP",
        "subject": "math",
        "unit": "القياس والتحويلات البسيطة",
        "titleAr": "القياس والتحويلات البسيطة",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القياس والتحويلات البسيطة",
          "يطبق القياس والتحويلات البسيطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القياس والتحويلات البسيطة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-math-07",
        "grade": "3AP",
        "subject": "math",
        "unit": "الجداول والمخططات",
        "titleAr": "الجداول والمخططات",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الجداول والمخططات",
          "يطبق الجداول والمخططات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الجداول والمخططات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-math-08",
        "grade": "3AP",
        "subject": "math",
        "unit": "استراتيجيات حل المسائل",
        "titleAr": "استراتيجيات حل المسائل",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم استراتيجيات حل المسائل",
          "يطبق استراتيجيات حل المسائل في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح استراتيجيات حل المسائل بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "arabic": [
      {
        "id": "3AP-arabic-01",
        "grade": "3AP",
        "subject": "arabic",
        "unit": "النص السردي",
        "titleAr": "النص السردي",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم النص السردي",
          "يطبق النص السردي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح النص السردي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-arabic-02",
        "grade": "3AP",
        "subject": "arabic",
        "unit": "الفعل والفاعل",
        "titleAr": "الفعل والفاعل",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الفعل والفاعل",
          "يطبق الفعل والفاعل في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الفعل والفاعل بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-arabic-03",
        "grade": "3AP",
        "subject": "arabic",
        "unit": "المفعول به",
        "titleAr": "المفعول به",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المفعول به",
          "يطبق المفعول به في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المفعول به بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-arabic-04",
        "grade": "3AP",
        "subject": "arabic",
        "unit": "علامات الترقيم",
        "titleAr": "علامات الترقيم",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم علامات الترقيم",
          "يطبق علامات الترقيم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح علامات الترقيم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-arabic-05",
        "grade": "3AP",
        "subject": "arabic",
        "unit": "الهمزة البسيطة",
        "titleAr": "الهمزة البسيطة",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الهمزة البسيطة",
          "يطبق الهمزة البسيطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الهمزة البسيطة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-arabic-06",
        "grade": "3AP",
        "subject": "arabic",
        "unit": "تلخيص فقرة",
        "titleAr": "تلخيص فقرة",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم تلخيص فقرة",
          "يطبق تلخيص فقرة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح تلخيص فقرة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-arabic-07",
        "grade": "3AP",
        "subject": "arabic",
        "unit": "كتابة رسالة قصيرة",
        "titleAr": "كتابة رسالة قصيرة",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم كتابة رسالة قصيرة",
          "يطبق كتابة رسالة قصيرة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح كتابة رسالة قصيرة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-arabic-08",
        "grade": "3AP",
        "subject": "arabic",
        "unit": "التعبير الوصفي",
        "titleAr": "التعبير الوصفي",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التعبير الوصفي",
          "يطبق التعبير الوصفي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التعبير الوصفي بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "french": [
      {
        "id": "3AP-french-01",
        "grade": "3AP",
        "subject": "french",
        "unit": "Lecture compréhension",
        "titleAr": "Lecture compréhension",
        "titleFr": "Lecture compréhension",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Lecture compréhension",
          "Appliquer Lecture compréhension dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Lecture compréhension بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-french-02",
        "grade": "3AP",
        "subject": "french",
        "unit": "Verbes du 1er groupe",
        "titleAr": "Verbes du 1er groupe",
        "titleFr": "Verbes du 1er groupe",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Verbes du 1er groupe",
          "Appliquer Verbes du 1er groupe dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Verbes du 1er groupe بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-french-03",
        "grade": "3AP",
        "subject": "french",
        "unit": "Accord sujet-verbe",
        "titleAr": "Accord sujet-verbe",
        "titleFr": "Accord sujet-verbe",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Accord sujet-verbe",
          "Appliquer Accord sujet-verbe dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Accord sujet-verbe بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-french-04",
        "grade": "3AP",
        "subject": "french",
        "unit": "Noms et adjectifs",
        "titleAr": "Noms et adjectifs",
        "titleFr": "Noms et adjectifs",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Noms et adjectifs",
          "Appliquer Noms et adjectifs dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Noms et adjectifs بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-french-05",
        "grade": "3AP",
        "subject": "french",
        "unit": "Passé composé simple",
        "titleAr": "Passé composé simple",
        "titleFr": "Passé composé simple",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Passé composé simple",
          "Appliquer Passé composé simple dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Passé composé simple بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-french-06",
        "grade": "3AP",
        "subject": "french",
        "unit": "Dialogue guidé",
        "titleAr": "Dialogue guidé",
        "titleFr": "Dialogue guidé",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Dialogue guidé",
          "Appliquer Dialogue guidé dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Dialogue guidé بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-french-07",
        "grade": "3AP",
        "subject": "french",
        "unit": "Texte narratif court",
        "titleAr": "Texte narratif court",
        "titleFr": "Texte narratif court",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Texte narratif court",
          "Appliquer Texte narratif court dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Texte narratif court بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-french-08",
        "grade": "3AP",
        "subject": "french",
        "unit": "Rédaction courte",
        "titleAr": "Rédaction courte",
        "titleFr": "Rédaction courte",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Rédaction courte",
          "Appliquer Rédaction courte dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Rédaction courte بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "science": [
      {
        "id": "3AP-science-01",
        "grade": "3AP",
        "subject": "science",
        "unit": "جسم الإنسان والحواس",
        "titleAr": "جسم الإنسان والحواس",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم جسم الإنسان والحواس",
          "يطبق جسم الإنسان والحواس في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح جسم الإنسان والحواس بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-science-02",
        "grade": "3AP",
        "subject": "science",
        "unit": "التنفس والحركة",
        "titleAr": "التنفس والحركة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التنفس والحركة",
          "يطبق التنفس والحركة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التنفس والحركة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-science-03",
        "grade": "3AP",
        "subject": "science",
        "unit": "النبات ودورة الحياة",
        "titleAr": "النبات ودورة الحياة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم النبات ودورة الحياة",
          "يطبق النبات ودورة الحياة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح النبات ودورة الحياة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-science-04",
        "grade": "3AP",
        "subject": "science",
        "unit": "السلاسل الغذائية البسيطة",
        "titleAr": "السلاسل الغذائية البسيطة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم السلاسل الغذائية البسيطة",
          "يطبق السلاسل الغذائية البسيطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح السلاسل الغذائية البسيطة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-science-05",
        "grade": "3AP",
        "subject": "science",
        "unit": "المواد وخصائصها",
        "titleAr": "المواد وخصائصها",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المواد وخصائصها",
          "يطبق المواد وخصائصها في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المواد وخصائصها بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-science-06",
        "grade": "3AP",
        "subject": "science",
        "unit": "الماء والطاقة",
        "titleAr": "الماء والطاقة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الماء والطاقة",
          "يطبق الماء والطاقة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الماء والطاقة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-science-07",
        "grade": "3AP",
        "subject": "science",
        "unit": "الكهرباء الآمنة",
        "titleAr": "الكهرباء الآمنة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الكهرباء الآمنة",
          "يطبق الكهرباء الآمنة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الكهرباء الآمنة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-science-08",
        "grade": "3AP",
        "subject": "science",
        "unit": "منهجية الملاحظة",
        "titleAr": "منهجية الملاحظة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم منهجية الملاحظة",
          "يطبق منهجية الملاحظة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح منهجية الملاحظة بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "islamic_education": [
      {
        "id": "3AP-islamic_education-01",
        "grade": "3AP",
        "subject": "islamic_education",
        "unit": "الصلاة والسلوك",
        "titleAr": "الصلاة والسلوك",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الصلاة والسلوك",
          "يطبق الصلاة والسلوك في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الصلاة والسلوك بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-islamic_education-02",
        "grade": "3AP",
        "subject": "islamic_education",
        "unit": "الأخلاق في المعاملة",
        "titleAr": "الأخلاق في المعاملة",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الأخلاق في المعاملة",
          "يطبق الأخلاق في المعاملة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأخلاق في المعاملة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-islamic_education-03",
        "grade": "3AP",
        "subject": "islamic_education",
        "unit": "القرآن والتدبر المبسط",
        "titleAr": "القرآن والتدبر المبسط",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القرآن والتدبر المبسط",
          "يطبق القرآن والتدبر المبسط في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القرآن والتدبر المبسط بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-islamic_education-04",
        "grade": "3AP",
        "subject": "islamic_education",
        "unit": "السيرة النبوية",
        "titleAr": "السيرة النبوية",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم السيرة النبوية",
          "يطبق السيرة النبوية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح السيرة النبوية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-islamic_education-05",
        "grade": "3AP",
        "subject": "islamic_education",
        "unit": "التضامن",
        "titleAr": "التضامن",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التضامن",
          "يطبق التضامن في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التضامن بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-islamic_education-06",
        "grade": "3AP",
        "subject": "islamic_education",
        "unit": "آداب الحوار",
        "titleAr": "آداب الحوار",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم آداب الحوار",
          "يطبق آداب الحوار في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح آداب الحوار بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-islamic_education-07",
        "grade": "3AP",
        "subject": "islamic_education",
        "unit": "المسؤولية",
        "titleAr": "المسؤولية",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المسؤولية",
          "يطبق المسؤولية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المسؤولية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-islamic_education-08",
        "grade": "3AP",
        "subject": "islamic_education",
        "unit": "قيم المواطنة",
        "titleAr": "قيم المواطنة",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم قيم المواطنة",
          "يطبق قيم المواطنة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح قيم المواطنة بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "social_studies": [
      {
        "id": "3AP-social_studies-01",
        "grade": "3AP",
        "subject": "social_studies",
        "unit": "المغرب: رموز ومؤسسات",
        "titleAr": "المغرب: رموز ومؤسسات",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المغرب: رموز ومؤسسات",
          "يطبق المغرب: رموز ومؤسسات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المغرب: رموز ومؤسسات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-social_studies-02",
        "grade": "3AP",
        "subject": "social_studies",
        "unit": "القرية والمدينة",
        "titleAr": "القرية والمدينة",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القرية والمدينة",
          "يطبق القرية والمدينة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القرية والمدينة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-social_studies-03",
        "grade": "3AP",
        "subject": "social_studies",
        "unit": "موارد الماء",
        "titleAr": "موارد الماء",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم موارد الماء",
          "يطبق موارد الماء في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح موارد الماء بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-social_studies-04",
        "grade": "3AP",
        "subject": "social_studies",
        "unit": "النقل والتواصل",
        "titleAr": "النقل والتواصل",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم النقل والتواصل",
          "يطبق النقل والتواصل في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح النقل والتواصل بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-social_studies-05",
        "grade": "3AP",
        "subject": "social_studies",
        "unit": "المهن والاقتصاد المحلي",
        "titleAr": "المهن والاقتصاد المحلي",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المهن والاقتصاد المحلي",
          "يطبق المهن والاقتصاد المحلي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المهن والاقتصاد المحلي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-social_studies-06",
        "grade": "3AP",
        "subject": "social_studies",
        "unit": "قراءة خريطة بسيطة",
        "titleAr": "قراءة خريطة بسيطة",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم قراءة خريطة بسيطة",
          "يطبق قراءة خريطة بسيطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح قراءة خريطة بسيطة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-social_studies-07",
        "grade": "3AP",
        "subject": "social_studies",
        "unit": "البيئة المحلية",
        "titleAr": "البيئة المحلية",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم البيئة المحلية",
          "يطبق البيئة المحلية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح البيئة المحلية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "3AP-social_studies-08",
        "grade": "3AP",
        "subject": "social_studies",
        "unit": "العيش المشترك",
        "titleAr": "العيش المشترك",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم العيش المشترك",
          "يطبق العيش المشترك في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح العيش المشترك بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ]
  },
  "4AP": {
    "math": [
      {
        "id": "4AP-math-01",
        "grade": "4AP",
        "subject": "math",
        "unit": "الأعداد الكبيرة",
        "titleAr": "الأعداد الكبيرة",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الأعداد الكبيرة",
          "يطبق الأعداد الكبيرة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأعداد الكبيرة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-math-02",
        "grade": "4AP",
        "subject": "math",
        "unit": "العمليات الأربع",
        "titleAr": "العمليات الأربع",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم العمليات الأربع",
          "يطبق العمليات الأربع في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح العمليات الأربع بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-math-03",
        "grade": "4AP",
        "subject": "math",
        "unit": "الكسور الاعتيادية",
        "titleAr": "الكسور الاعتيادية",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الكسور الاعتيادية",
          "يطبق الكسور الاعتيادية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الكسور الاعتيادية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-math-04",
        "grade": "4AP",
        "subject": "math",
        "unit": "الأعداد العشرية الأولى",
        "titleAr": "الأعداد العشرية الأولى",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الأعداد العشرية الأولى",
          "يطبق الأعداد العشرية الأولى في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأعداد العشرية الأولى بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-math-05",
        "grade": "4AP",
        "subject": "math",
        "unit": "الهندسة: مستقيمات وزوايا",
        "titleAr": "الهندسة: مستقيمات وزوايا",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الهندسة: مستقيمات وزوايا",
          "يطبق الهندسة: مستقيمات وزوايا في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الهندسة: مستقيمات وزوايا بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-math-06",
        "grade": "4AP",
        "subject": "math",
        "unit": "المحيط والمساحة",
        "titleAr": "المحيط والمساحة",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المحيط والمساحة",
          "يطبق المحيط والمساحة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المحيط والمساحة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-math-07",
        "grade": "4AP",
        "subject": "math",
        "unit": "القياس والتحويل",
        "titleAr": "القياس والتحويل",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القياس والتحويل",
          "يطبق القياس والتحويل في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القياس والتحويل بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-math-08",
        "grade": "4AP",
        "subject": "math",
        "unit": "التناسب الأولي",
        "titleAr": "التناسب الأولي",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التناسب الأولي",
          "يطبق التناسب الأولي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التناسب الأولي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-math-09",
        "grade": "4AP",
        "subject": "math",
        "unit": "الإحصاء البسيط",
        "titleAr": "الإحصاء البسيط",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الإحصاء البسيط",
          "يطبق الإحصاء البسيط في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الإحصاء البسيط بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-math-10",
        "grade": "4AP",
        "subject": "math",
        "unit": "مسائل مركبة",
        "titleAr": "مسائل مركبة",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم مسائل مركبة",
          "يطبق مسائل مركبة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح مسائل مركبة بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "arabic": [
      {
        "id": "4AP-arabic-01",
        "grade": "4AP",
        "subject": "arabic",
        "unit": "النص الحجاجي البسيط",
        "titleAr": "النص الحجاجي البسيط",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم النص الحجاجي البسيط",
          "يطبق النص الحجاجي البسيط في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح النص الحجاجي البسيط بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-arabic-02",
        "grade": "4AP",
        "subject": "arabic",
        "unit": "النص الوصفي",
        "titleAr": "النص الوصفي",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم النص الوصفي",
          "يطبق النص الوصفي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح النص الوصفي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-arabic-03",
        "grade": "4AP",
        "subject": "arabic",
        "unit": "الجملة وأنواعها",
        "titleAr": "الجملة وأنواعها",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الجملة وأنواعها",
          "يطبق الجملة وأنواعها في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الجملة وأنواعها بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-arabic-04",
        "grade": "4AP",
        "subject": "arabic",
        "unit": "النواسخ الأولى",
        "titleAr": "النواسخ الأولى",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم النواسخ الأولى",
          "يطبق النواسخ الأولى في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح النواسخ الأولى بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-arabic-05",
        "grade": "4AP",
        "subject": "arabic",
        "unit": "الإعراب الأساسي",
        "titleAr": "الإعراب الأساسي",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الإعراب الأساسي",
          "يطبق الإعراب الأساسي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الإعراب الأساسي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-arabic-06",
        "grade": "4AP",
        "subject": "arabic",
        "unit": "الإملاء: الهمزات",
        "titleAr": "الإملاء: الهمزات",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الإملاء: الهمزات",
          "يطبق الإملاء: الهمزات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الإملاء: الهمزات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-arabic-07",
        "grade": "4AP",
        "subject": "arabic",
        "unit": "كتابة موضوع منظم",
        "titleAr": "كتابة موضوع منظم",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم كتابة موضوع منظم",
          "يطبق كتابة موضوع منظم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح كتابة موضوع منظم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-arabic-08",
        "grade": "4AP",
        "subject": "arabic",
        "unit": "التواصل الشفهي",
        "titleAr": "التواصل الشفهي",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التواصل الشفهي",
          "يطبق التواصل الشفهي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التواصل الشفهي بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "french": [
      {
        "id": "4AP-french-01",
        "grade": "4AP",
        "subject": "french",
        "unit": "Compréhension écrite",
        "titleAr": "Compréhension écrite",
        "titleFr": "Compréhension écrite",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Compréhension écrite",
          "Appliquer Compréhension écrite dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Compréhension écrite بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-french-02",
        "grade": "4AP",
        "subject": "french",
        "unit": "Présent et futur proche",
        "titleAr": "Présent et futur proche",
        "titleFr": "Présent et futur proche",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Présent et futur proche",
          "Appliquer Présent et futur proche dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Présent et futur proche بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-french-03",
        "grade": "4AP",
        "subject": "french",
        "unit": "Adjectifs qualificatifs",
        "titleAr": "Adjectifs qualificatifs",
        "titleFr": "Adjectifs qualificatifs",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Adjectifs qualificatifs",
          "Appliquer Adjectifs qualificatifs dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Adjectifs qualificatifs بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-french-04",
        "grade": "4AP",
        "subject": "french",
        "unit": "Compléments essentiels",
        "titleAr": "Compléments essentiels",
        "titleFr": "Compléments essentiels",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Compléments essentiels",
          "Appliquer Compléments essentiels dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Compléments essentiels بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-french-05",
        "grade": "4AP",
        "subject": "french",
        "unit": "Accords simples",
        "titleAr": "Accords simples",
        "titleFr": "Accords simples",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Accords simples",
          "Appliquer Accords simples dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Accords simples بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-french-06",
        "grade": "4AP",
        "subject": "french",
        "unit": "Production écrite guidée",
        "titleAr": "Production écrite guidée",
        "titleFr": "Production écrite guidée",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Production écrite guidée",
          "Appliquer Production écrite guidée dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Production écrite guidée بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-french-07",
        "grade": "4AP",
        "subject": "french",
        "unit": "Lexique thématique",
        "titleAr": "Lexique thématique",
        "titleFr": "Lexique thématique",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Lexique thématique",
          "Appliquer Lexique thématique dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Lexique thématique بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-french-08",
        "grade": "4AP",
        "subject": "french",
        "unit": "Lecture expressive",
        "titleAr": "Lecture expressive",
        "titleFr": "Lecture expressive",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Lecture expressive",
          "Appliquer Lecture expressive dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Lecture expressive بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "science": [
      {
        "id": "4AP-science-01",
        "grade": "4AP",
        "subject": "science",
        "unit": "الجهاز الهضمي",
        "titleAr": "الجهاز الهضمي",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الجهاز الهضمي",
          "يطبق الجهاز الهضمي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الجهاز الهضمي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-science-02",
        "grade": "4AP",
        "subject": "science",
        "unit": "التغذية والصحة",
        "titleAr": "التغذية والصحة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التغذية والصحة",
          "يطبق التغذية والصحة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التغذية والصحة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-science-03",
        "grade": "4AP",
        "subject": "science",
        "unit": "دورة الماء",
        "titleAr": "دورة الماء",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم دورة الماء",
          "يطبق دورة الماء في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح دورة الماء بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-science-04",
        "grade": "4AP",
        "subject": "science",
        "unit": "الحرارة والمواد",
        "titleAr": "الحرارة والمواد",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الحرارة والمواد",
          "يطبق الحرارة والمواد في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الحرارة والمواد بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-science-05",
        "grade": "4AP",
        "subject": "science",
        "unit": "الكهرباء البسيطة",
        "titleAr": "الكهرباء البسيطة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الكهرباء البسيطة",
          "يطبق الكهرباء البسيطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الكهرباء البسيطة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-science-06",
        "grade": "4AP",
        "subject": "science",
        "unit": "النبات والوسط",
        "titleAr": "النبات والوسط",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم النبات والوسط",
          "يطبق النبات والوسط في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح النبات والوسط بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-science-07",
        "grade": "4AP",
        "subject": "science",
        "unit": "التلوث والحماية",
        "titleAr": "التلوث والحماية",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التلوث والحماية",
          "يطبق التلوث والحماية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التلوث والحماية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-science-08",
        "grade": "4AP",
        "subject": "science",
        "unit": "التجربة والقياس",
        "titleAr": "التجربة والقياس",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التجربة والقياس",
          "يطبق التجربة والقياس في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التجربة والقياس بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "islamic_education": [
      {
        "id": "4AP-islamic_education-01",
        "grade": "4AP",
        "subject": "islamic_education",
        "unit": "أركان الإسلام",
        "titleAr": "أركان الإسلام",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم أركان الإسلام",
          "يطبق أركان الإسلام في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح أركان الإسلام بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-islamic_education-02",
        "grade": "4AP",
        "subject": "islamic_education",
        "unit": "قيم الصبر والشكر",
        "titleAr": "قيم الصبر والشكر",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم قيم الصبر والشكر",
          "يطبق قيم الصبر والشكر في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح قيم الصبر والشكر بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-islamic_education-03",
        "grade": "4AP",
        "subject": "islamic_education",
        "unit": "السيرة: مواقف وعبر",
        "titleAr": "السيرة: مواقف وعبر",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم السيرة: مواقف وعبر",
          "يطبق السيرة: مواقف وعبر في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح السيرة: مواقف وعبر بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-islamic_education-04",
        "grade": "4AP",
        "subject": "islamic_education",
        "unit": "العبادات والسلوك",
        "titleAr": "العبادات والسلوك",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم العبادات والسلوك",
          "يطبق العبادات والسلوك في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح العبادات والسلوك بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-islamic_education-05",
        "grade": "4AP",
        "subject": "islamic_education",
        "unit": "الصدق والعدل",
        "titleAr": "الصدق والعدل",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الصدق والعدل",
          "يطبق الصدق والعدل في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الصدق والعدل بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-islamic_education-06",
        "grade": "4AP",
        "subject": "islamic_education",
        "unit": "آداب الاختلاف",
        "titleAr": "آداب الاختلاف",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم آداب الاختلاف",
          "يطبق آداب الاختلاف في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح آداب الاختلاف بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-islamic_education-07",
        "grade": "4AP",
        "subject": "islamic_education",
        "unit": "القرآن والقيم",
        "titleAr": "القرآن والقيم",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القرآن والقيم",
          "يطبق القرآن والقيم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القرآن والقيم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-islamic_education-08",
        "grade": "4AP",
        "subject": "islamic_education",
        "unit": "المحافظة على النعم",
        "titleAr": "المحافظة على النعم",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المحافظة على النعم",
          "يطبق المحافظة على النعم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المحافظة على النعم بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "social_studies": [
      {
        "id": "4AP-social_studies-01",
        "grade": "4AP",
        "subject": "social_studies",
        "unit": "جهات المغرب",
        "titleAr": "جهات المغرب",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم جهات المغرب",
          "يطبق جهات المغرب في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح جهات المغرب بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-social_studies-02",
        "grade": "4AP",
        "subject": "social_studies",
        "unit": "التضاريس والمناخ",
        "titleAr": "التضاريس والمناخ",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التضاريس والمناخ",
          "يطبق التضاريس والمناخ في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التضاريس والمناخ بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-social_studies-03",
        "grade": "4AP",
        "subject": "social_studies",
        "unit": "السكان والأنشطة",
        "titleAr": "السكان والأنشطة",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم السكان والأنشطة",
          "يطبق السكان والأنشطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح السكان والأنشطة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-social_studies-04",
        "grade": "4AP",
        "subject": "social_studies",
        "unit": "التاريخ المحلي",
        "titleAr": "التاريخ المحلي",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التاريخ المحلي",
          "يطبق التاريخ المحلي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التاريخ المحلي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-social_studies-05",
        "grade": "4AP",
        "subject": "social_studies",
        "unit": "المؤسسات المحلية",
        "titleAr": "المؤسسات المحلية",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المؤسسات المحلية",
          "يطبق المؤسسات المحلية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المؤسسات المحلية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-social_studies-06",
        "grade": "4AP",
        "subject": "social_studies",
        "unit": "الحقوق والواجبات",
        "titleAr": "الحقوق والواجبات",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الحقوق والواجبات",
          "يطبق الحقوق والواجبات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الحقوق والواجبات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-social_studies-07",
        "grade": "4AP",
        "subject": "social_studies",
        "unit": "التراث المغربي",
        "titleAr": "التراث المغربي",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التراث المغربي",
          "يطبق التراث المغربي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التراث المغربي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "4AP-social_studies-08",
        "grade": "4AP",
        "subject": "social_studies",
        "unit": "قراءة وثيقة وخريطة",
        "titleAr": "قراءة وثيقة وخريطة",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم قراءة وثيقة وخريطة",
          "يطبق قراءة وثيقة وخريطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح قراءة وثيقة وخريطة بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ]
  },
  "5AP": {
    "math": [
      {
        "id": "5AP-math-01",
        "grade": "5AP",
        "subject": "math",
        "unit": "الأعداد الطبيعية والعشرية",
        "titleAr": "الأعداد الطبيعية والعشرية",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الأعداد الطبيعية والعشرية",
          "يطبق الأعداد الطبيعية والعشرية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأعداد الطبيعية والعشرية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-math-02",
        "grade": "5AP",
        "subject": "math",
        "unit": "الكسور والعمليات",
        "titleAr": "الكسور والعمليات",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الكسور والعمليات",
          "يطبق الكسور والعمليات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الكسور والعمليات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-math-03",
        "grade": "5AP",
        "subject": "math",
        "unit": "التناسب والنسبة",
        "titleAr": "التناسب والنسبة",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التناسب والنسبة",
          "يطبق التناسب والنسبة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التناسب والنسبة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-math-04",
        "grade": "5AP",
        "subject": "math",
        "unit": "الهندسة والإنشاءات",
        "titleAr": "الهندسة والإنشاءات",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الهندسة والإنشاءات",
          "يطبق الهندسة والإنشاءات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الهندسة والإنشاءات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-math-05",
        "grade": "5AP",
        "subject": "math",
        "unit": "المساحات والحجوم الأولى",
        "titleAr": "المساحات والحجوم الأولى",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المساحات والحجوم الأولى",
          "يطبق المساحات والحجوم الأولى في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المساحات والحجوم الأولى بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-math-06",
        "grade": "5AP",
        "subject": "math",
        "unit": "القياسات والتحويلات",
        "titleAr": "القياسات والتحويلات",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القياسات والتحويلات",
          "يطبق القياسات والتحويلات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القياسات والتحويلات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-math-07",
        "grade": "5AP",
        "subject": "math",
        "unit": "الإحصاء والاحتمال البسيط",
        "titleAr": "الإحصاء والاحتمال البسيط",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الإحصاء والاحتمال البسيط",
          "يطبق الإحصاء والاحتمال البسيط في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الإحصاء والاحتمال البسيط بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-math-08",
        "grade": "5AP",
        "subject": "math",
        "unit": "المعادلات اللفظية",
        "titleAr": "المعادلات اللفظية",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المعادلات اللفظية",
          "يطبق المعادلات اللفظية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المعادلات اللفظية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-math-09",
        "grade": "5AP",
        "subject": "math",
        "unit": "مسائل متعددة الخطوات",
        "titleAr": "مسائل متعددة الخطوات",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم مسائل متعددة الخطوات",
          "يطبق مسائل متعددة الخطوات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح مسائل متعددة الخطوات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-math-10",
        "grade": "5AP",
        "subject": "math",
        "unit": "استعداد للتقويم",
        "titleAr": "استعداد للتقويم",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم استعداد للتقويم",
          "يطبق استعداد للتقويم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح استعداد للتقويم بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "arabic": [
      {
        "id": "5AP-arabic-01",
        "grade": "5AP",
        "subject": "arabic",
        "unit": "تحليل نص سردي",
        "titleAr": "تحليل نص سردي",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم تحليل نص سردي",
          "يطبق تحليل نص سردي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح تحليل نص سردي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-arabic-02",
        "grade": "5AP",
        "subject": "arabic",
        "unit": "تحليل نص تفسيري",
        "titleAr": "تحليل نص تفسيري",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم تحليل نص تفسيري",
          "يطبق تحليل نص تفسيري في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح تحليل نص تفسيري بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-arabic-03",
        "grade": "5AP",
        "subject": "arabic",
        "unit": "التوابع الأساسية",
        "titleAr": "التوابع الأساسية",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التوابع الأساسية",
          "يطبق التوابع الأساسية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التوابع الأساسية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-arabic-04",
        "grade": "5AP",
        "subject": "arabic",
        "unit": "النواسخ والجملة",
        "titleAr": "النواسخ والجملة",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم النواسخ والجملة",
          "يطبق النواسخ والجملة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح النواسخ والجملة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-arabic-05",
        "grade": "5AP",
        "subject": "arabic",
        "unit": "الصرف والتحويل",
        "titleAr": "الصرف والتحويل",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الصرف والتحويل",
          "يطبق الصرف والتحويل في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الصرف والتحويل بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-arabic-06",
        "grade": "5AP",
        "subject": "arabic",
        "unit": "الإملاء المتقدم",
        "titleAr": "الإملاء المتقدم",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الإملاء المتقدم",
          "يطبق الإملاء المتقدم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الإملاء المتقدم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-arabic-07",
        "grade": "5AP",
        "subject": "arabic",
        "unit": "التعبير الكتابي المنهجي",
        "titleAr": "التعبير الكتابي المنهجي",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التعبير الكتابي المنهجي",
          "يطبق التعبير الكتابي المنهجي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التعبير الكتابي المنهجي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-arabic-08",
        "grade": "5AP",
        "subject": "arabic",
        "unit": "التلخيص وإبداء الرأي",
        "titleAr": "التلخيص وإبداء الرأي",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التلخيص وإبداء الرأي",
          "يطبق التلخيص وإبداء الرأي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التلخيص وإبداء الرأي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-arabic-09",
        "grade": "5AP",
        "subject": "arabic",
        "unit": "القراءة الوظيفية",
        "titleAr": "القراءة الوظيفية",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القراءة الوظيفية",
          "يطبق القراءة الوظيفية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القراءة الوظيفية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-arabic-10",
        "grade": "5AP",
        "subject": "arabic",
        "unit": "مشروع لغوي",
        "titleAr": "مشروع لغوي",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم مشروع لغوي",
          "يطبق مشروع لغوي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح مشروع لغوي بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "french": [
      {
        "id": "5AP-french-01",
        "grade": "5AP",
        "subject": "french",
        "unit": "Texte informatif",
        "titleAr": "Texte informatif",
        "titleFr": "Texte informatif",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Texte informatif",
          "Appliquer Texte informatif dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Texte informatif بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-french-02",
        "grade": "5AP",
        "subject": "french",
        "unit": "Imparfait et futur",
        "titleAr": "Imparfait et futur",
        "titleFr": "Imparfait et futur",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Imparfait et futur",
          "Appliquer Imparfait et futur dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Imparfait et futur بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-french-03",
        "grade": "5AP",
        "subject": "french",
        "unit": "Pronoms personnels",
        "titleAr": "Pronoms personnels",
        "titleFr": "Pronoms personnels",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Pronoms personnels",
          "Appliquer Pronoms personnels dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Pronoms personnels بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-french-04",
        "grade": "5AP",
        "subject": "french",
        "unit": "Compléments circonstanciels",
        "titleAr": "Compléments circonstanciels",
        "titleFr": "Compléments circonstanciels",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Compléments circonstanciels",
          "Appliquer Compléments circonstanciels dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Compléments circonstanciels بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-french-05",
        "grade": "5AP",
        "subject": "french",
        "unit": "Accords et conjugaison",
        "titleAr": "Accords et conjugaison",
        "titleFr": "Accords et conjugaison",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Accords et conjugaison",
          "Appliquer Accords et conjugaison dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Accords et conjugaison بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-french-06",
        "grade": "5AP",
        "subject": "french",
        "unit": "Production écrite organisée",
        "titleAr": "Production écrite organisée",
        "titleFr": "Production écrite organisée",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Production écrite organisée",
          "Appliquer Production écrite organisée dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Production écrite organisée بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-french-07",
        "grade": "5AP",
        "subject": "french",
        "unit": "Compréhension de consignes",
        "titleAr": "Compréhension de consignes",
        "titleFr": "Compréhension de consignes",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Compréhension de consignes",
          "Appliquer Compréhension de consignes dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Compréhension de consignes بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-french-08",
        "grade": "5AP",
        "subject": "french",
        "unit": "Vocabulaire scientifique",
        "titleAr": "Vocabulaire scientifique",
        "titleFr": "Vocabulaire scientifique",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Vocabulaire scientifique",
          "Appliquer Vocabulaire scientifique dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Vocabulaire scientifique بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-french-09",
        "grade": "5AP",
        "subject": "french",
        "unit": "Dialogue argumenté",
        "titleAr": "Dialogue argumenté",
        "titleFr": "Dialogue argumenté",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Dialogue argumenté",
          "Appliquer Dialogue argumenté dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Dialogue argumenté بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-french-10",
        "grade": "5AP",
        "subject": "french",
        "unit": "Révision structurée",
        "titleAr": "Révision structurée",
        "titleFr": "Révision structurée",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Révision structurée",
          "Appliquer Révision structurée dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Révision structurée بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "science": [
      {
        "id": "5AP-science-01",
        "grade": "5AP",
        "subject": "science",
        "unit": "الدورة الدموية والتنفس",
        "titleAr": "الدورة الدموية والتنفس",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الدورة الدموية والتنفس",
          "يطبق الدورة الدموية والتنفس في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الدورة الدموية والتنفس بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-science-02",
        "grade": "5AP",
        "subject": "science",
        "unit": "التوازن الغذائي",
        "titleAr": "التوازن الغذائي",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التوازن الغذائي",
          "يطبق التوازن الغذائي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التوازن الغذائي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-science-03",
        "grade": "5AP",
        "subject": "science",
        "unit": "التكاثر عند النباتات",
        "titleAr": "التكاثر عند النباتات",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التكاثر عند النباتات",
          "يطبق التكاثر عند النباتات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التكاثر عند النباتات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-science-04",
        "grade": "5AP",
        "subject": "science",
        "unit": "البيئة والسلاسل الغذائية",
        "titleAr": "البيئة والسلاسل الغذائية",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم البيئة والسلاسل الغذائية",
          "يطبق البيئة والسلاسل الغذائية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح البيئة والسلاسل الغذائية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-science-05",
        "grade": "5AP",
        "subject": "science",
        "unit": "المواد والتحولات",
        "titleAr": "المواد والتحولات",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المواد والتحولات",
          "يطبق المواد والتحولات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المواد والتحولات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-science-06",
        "grade": "5AP",
        "subject": "science",
        "unit": "الطاقة والكهرباء",
        "titleAr": "الطاقة والكهرباء",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الطاقة والكهرباء",
          "يطبق الطاقة والكهرباء في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الطاقة والكهرباء بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-science-07",
        "grade": "5AP",
        "subject": "science",
        "unit": "الأرض والفضاء",
        "titleAr": "الأرض والفضاء",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الأرض والفضاء",
          "يطبق الأرض والفضاء في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأرض والفضاء بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-science-08",
        "grade": "5AP",
        "subject": "science",
        "unit": "البحث العلمي المصغر",
        "titleAr": "البحث العلمي المصغر",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم البحث العلمي المصغر",
          "يطبق البحث العلمي المصغر في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح البحث العلمي المصغر بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-science-09",
        "grade": "5AP",
        "subject": "science",
        "unit": "قراءة رسم علمي",
        "titleAr": "قراءة رسم علمي",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم قراءة رسم علمي",
          "يطبق قراءة رسم علمي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح قراءة رسم علمي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-science-10",
        "grade": "5AP",
        "subject": "science",
        "unit": "السلامة والتجربة",
        "titleAr": "السلامة والتجربة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم السلامة والتجربة",
          "يطبق السلامة والتجربة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح السلامة والتجربة بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "islamic_education": [
      {
        "id": "5AP-islamic_education-01",
        "grade": "5AP",
        "subject": "islamic_education",
        "unit": "الإيمان والعمل الصالح",
        "titleAr": "الإيمان والعمل الصالح",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الإيمان والعمل الصالح",
          "يطبق الإيمان والعمل الصالح في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الإيمان والعمل الصالح بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-islamic_education-02",
        "grade": "5AP",
        "subject": "islamic_education",
        "unit": "العبادات وأثرها",
        "titleAr": "العبادات وأثرها",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم العبادات وأثرها",
          "يطبق العبادات وأثرها في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح العبادات وأثرها بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-islamic_education-03",
        "grade": "5AP",
        "subject": "islamic_education",
        "unit": "السيرة والقيم",
        "titleAr": "السيرة والقيم",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم السيرة والقيم",
          "يطبق السيرة والقيم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح السيرة والقيم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-islamic_education-04",
        "grade": "5AP",
        "subject": "islamic_education",
        "unit": "القرآن والتزكية",
        "titleAr": "القرآن والتزكية",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القرآن والتزكية",
          "يطبق القرآن والتزكية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القرآن والتزكية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-islamic_education-05",
        "grade": "5AP",
        "subject": "islamic_education",
        "unit": "المسؤولية والأمانة",
        "titleAr": "المسؤولية والأمانة",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المسؤولية والأمانة",
          "يطبق المسؤولية والأمانة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المسؤولية والأمانة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-islamic_education-06",
        "grade": "5AP",
        "subject": "islamic_education",
        "unit": "التسامح والتعايش",
        "titleAr": "التسامح والتعايش",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التسامح والتعايش",
          "يطبق التسامح والتعايش في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التسامح والتعايش بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-islamic_education-07",
        "grade": "5AP",
        "subject": "islamic_education",
        "unit": "فقه السلوك اليومي",
        "titleAr": "فقه السلوك اليومي",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم فقه السلوك اليومي",
          "يطبق فقه السلوك اليومي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح فقه السلوك اليومي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-islamic_education-08",
        "grade": "5AP",
        "subject": "islamic_education",
        "unit": "مشروع قيمي",
        "titleAr": "مشروع قيمي",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم مشروع قيمي",
          "يطبق مشروع قيمي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح مشروع قيمي بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "social_studies": [
      {
        "id": "5AP-social_studies-01",
        "grade": "5AP",
        "subject": "social_studies",
        "unit": "المغرب الطبيعي",
        "titleAr": "المغرب الطبيعي",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المغرب الطبيعي",
          "يطبق المغرب الطبيعي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المغرب الطبيعي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-social_studies-02",
        "grade": "5AP",
        "subject": "social_studies",
        "unit": "الموارد والتنمية",
        "titleAr": "الموارد والتنمية",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الموارد والتنمية",
          "يطبق الموارد والتنمية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الموارد والتنمية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-social_studies-03",
        "grade": "5AP",
        "subject": "social_studies",
        "unit": "التاريخ المغربي المبسط",
        "titleAr": "التاريخ المغربي المبسط",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التاريخ المغربي المبسط",
          "يطبق التاريخ المغربي المبسط في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التاريخ المغربي المبسط بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-social_studies-04",
        "grade": "5AP",
        "subject": "social_studies",
        "unit": "السكان والهجرة",
        "titleAr": "السكان والهجرة",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم السكان والهجرة",
          "يطبق السكان والهجرة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح السكان والهجرة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-social_studies-05",
        "grade": "5AP",
        "subject": "social_studies",
        "unit": "الاقتصاد المحلي والوطني",
        "titleAr": "الاقتصاد المحلي والوطني",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الاقتصاد المحلي والوطني",
          "يطبق الاقتصاد المحلي والوطني في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الاقتصاد المحلي والوطني بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-social_studies-06",
        "grade": "5AP",
        "subject": "social_studies",
        "unit": "المواطنة والمشاركة",
        "titleAr": "المواطنة والمشاركة",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المواطنة والمشاركة",
          "يطبق المواطنة والمشاركة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المواطنة والمشاركة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-social_studies-07",
        "grade": "5AP",
        "subject": "social_studies",
        "unit": "قراءة مبيان وخريطة",
        "titleAr": "قراءة مبيان وخريطة",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم قراءة مبيان وخريطة",
          "يطبق قراءة مبيان وخريطة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح قراءة مبيان وخريطة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-social_studies-08",
        "grade": "5AP",
        "subject": "social_studies",
        "unit": "حماية البيئة",
        "titleAr": "حماية البيئة",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم حماية البيئة",
          "يطبق حماية البيئة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح حماية البيئة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-social_studies-09",
        "grade": "5AP",
        "subject": "social_studies",
        "unit": "التراث والهوية",
        "titleAr": "التراث والهوية",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التراث والهوية",
          "يطبق التراث والهوية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التراث والهوية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "5AP-social_studies-10",
        "grade": "5AP",
        "subject": "social_studies",
        "unit": "مشروع اجتماعي",
        "titleAr": "مشروع اجتماعي",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم مشروع اجتماعي",
          "يطبق مشروع اجتماعي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح مشروع اجتماعي بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ]
  },
  "6AP": {
    "math": [
      {
        "id": "6AP-math-01",
        "grade": "6AP",
        "subject": "math",
        "unit": "الأعداد والعمليات المتقدمة",
        "titleAr": "الأعداد والعمليات المتقدمة",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الأعداد والعمليات المتقدمة",
          "يطبق الأعداد والعمليات المتقدمة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأعداد والعمليات المتقدمة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-math-02",
        "grade": "6AP",
        "subject": "math",
        "unit": "الكسور والأعداد العشرية",
        "titleAr": "الكسور والأعداد العشرية",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الكسور والأعداد العشرية",
          "يطبق الكسور والأعداد العشرية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الكسور والأعداد العشرية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-math-03",
        "grade": "6AP",
        "subject": "math",
        "unit": "التناسبية والنسب المئوية",
        "titleAr": "التناسبية والنسب المئوية",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التناسبية والنسب المئوية",
          "يطبق التناسبية والنسب المئوية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التناسبية والنسب المئوية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-math-04",
        "grade": "6AP",
        "subject": "math",
        "unit": "الهندسة والبرهان الأولي",
        "titleAr": "الهندسة والبرهان الأولي",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الهندسة والبرهان الأولي",
          "يطبق الهندسة والبرهان الأولي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الهندسة والبرهان الأولي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-math-05",
        "grade": "6AP",
        "subject": "math",
        "unit": "المساحات والحجوم",
        "titleAr": "المساحات والحجوم",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المساحات والحجوم",
          "يطبق المساحات والحجوم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المساحات والحجوم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-math-06",
        "grade": "6AP",
        "subject": "math",
        "unit": "القياس والتحويلات المركبة",
        "titleAr": "القياس والتحويلات المركبة",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القياس والتحويلات المركبة",
          "يطبق القياس والتحويلات المركبة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القياس والتحويلات المركبة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-math-07",
        "grade": "6AP",
        "subject": "math",
        "unit": "الإحصاء وتمثيل البيانات",
        "titleAr": "الإحصاء وتمثيل البيانات",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الإحصاء وتمثيل البيانات",
          "يطبق الإحصاء وتمثيل البيانات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الإحصاء وتمثيل البيانات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-math-08",
        "grade": "6AP",
        "subject": "math",
        "unit": "حل مسائل مركبة",
        "titleAr": "حل مسائل مركبة",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم حل مسائل مركبة",
          "يطبق حل مسائل مركبة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح حل مسائل مركبة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-math-09",
        "grade": "6AP",
        "subject": "math",
        "unit": "استعداد للامتحان الإشهادي",
        "titleAr": "استعداد للامتحان الإشهادي",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم استعداد للامتحان الإشهادي",
          "يطبق استعداد للامتحان الإشهادي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح استعداد للامتحان الإشهادي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-math-10",
        "grade": "6AP",
        "subject": "math",
        "unit": "جسر نحو الإعدادي",
        "titleAr": "جسر نحو الإعدادي",
        "titleFr": "Mathématiques",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم جسر نحو الإعدادي",
          "يطبق جسر نحو الإعدادي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "math_understanding",
          "math_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح جسر نحو الإعدادي بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "arabic": [
      {
        "id": "6AP-arabic-01",
        "grade": "6AP",
        "subject": "arabic",
        "unit": "القراءة التحليلية",
        "titleAr": "القراءة التحليلية",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القراءة التحليلية",
          "يطبق القراءة التحليلية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القراءة التحليلية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-arabic-02",
        "grade": "6AP",
        "subject": "arabic",
        "unit": "النص الحجاجي",
        "titleAr": "النص الحجاجي",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم النص الحجاجي",
          "يطبق النص الحجاجي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح النص الحجاجي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-arabic-03",
        "grade": "6AP",
        "subject": "arabic",
        "unit": "القواعد والتركيب",
        "titleAr": "القواعد والتركيب",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القواعد والتركيب",
          "يطبق القواعد والتركيب في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القواعد والتركيب بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-arabic-04",
        "grade": "6AP",
        "subject": "arabic",
        "unit": "الصرف والتحويل",
        "titleAr": "الصرف والتحويل",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الصرف والتحويل",
          "يطبق الصرف والتحويل في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الصرف والتحويل بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-arabic-05",
        "grade": "6AP",
        "subject": "arabic",
        "unit": "الإملاء والترقيم",
        "titleAr": "الإملاء والترقيم",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الإملاء والترقيم",
          "يطبق الإملاء والترقيم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الإملاء والترقيم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-arabic-06",
        "grade": "6AP",
        "subject": "arabic",
        "unit": "الإنشاء المنهجي",
        "titleAr": "الإنشاء المنهجي",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الإنشاء المنهجي",
          "يطبق الإنشاء المنهجي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الإنشاء المنهجي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-arabic-07",
        "grade": "6AP",
        "subject": "arabic",
        "unit": "تلخيص وتوسيع فكرة",
        "titleAr": "تلخيص وتوسيع فكرة",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم تلخيص وتوسيع فكرة",
          "يطبق تلخيص وتوسيع فكرة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح تلخيص وتوسيع فكرة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-arabic-08",
        "grade": "6AP",
        "subject": "arabic",
        "unit": "التواصل والعرض",
        "titleAr": "التواصل والعرض",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التواصل والعرض",
          "يطبق التواصل والعرض في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التواصل والعرض بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-arabic-09",
        "grade": "6AP",
        "subject": "arabic",
        "unit": "نماذج امتحان",
        "titleAr": "نماذج امتحان",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم نماذج امتحان",
          "يطبق نماذج امتحان في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح نماذج امتحان بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-arabic-10",
        "grade": "6AP",
        "subject": "arabic",
        "unit": "جسر نحو الإعدادي",
        "titleAr": "جسر نحو الإعدادي",
        "titleFr": "Arabe",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم جسر نحو الإعدادي",
          "يطبق جسر نحو الإعدادي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "arabic_understanding",
          "arabic_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح جسر نحو الإعدادي بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "french": [
      {
        "id": "6AP-french-01",
        "grade": "6AP",
        "subject": "french",
        "unit": "Compréhension approfondie",
        "titleAr": "Compréhension approfondie",
        "titleFr": "Compréhension approfondie",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Compréhension approfondie",
          "Appliquer Compréhension approfondie dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Compréhension approfondie بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-french-02",
        "grade": "6AP",
        "subject": "french",
        "unit": "Conjugaison systématique",
        "titleAr": "Conjugaison systématique",
        "titleFr": "Conjugaison systématique",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Conjugaison systématique",
          "Appliquer Conjugaison systématique dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Conjugaison systématique بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-french-03",
        "grade": "6AP",
        "subject": "french",
        "unit": "Grammaire de la phrase",
        "titleAr": "Grammaire de la phrase",
        "titleFr": "Grammaire de la phrase",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Grammaire de la phrase",
          "Appliquer Grammaire de la phrase dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Grammaire de la phrase بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-french-04",
        "grade": "6AP",
        "subject": "french",
        "unit": "Expression écrite complète",
        "titleAr": "Expression écrite complète",
        "titleFr": "Expression écrite complète",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Expression écrite complète",
          "Appliquer Expression écrite complète dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Expression écrite complète بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-french-05",
        "grade": "6AP",
        "subject": "french",
        "unit": "Production orale",
        "titleAr": "Production orale",
        "titleFr": "Production orale",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Production orale",
          "Appliquer Production orale dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Production orale بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-french-06",
        "grade": "6AP",
        "subject": "french",
        "unit": "Lecture fonctionnelle",
        "titleAr": "Lecture fonctionnelle",
        "titleFr": "Lecture fonctionnelle",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Lecture fonctionnelle",
          "Appliquer Lecture fonctionnelle dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Lecture fonctionnelle بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-french-07",
        "grade": "6AP",
        "subject": "french",
        "unit": "Vocabulaire avancé",
        "titleAr": "Vocabulaire avancé",
        "titleFr": "Vocabulaire avancé",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Vocabulaire avancé",
          "Appliquer Vocabulaire avancé dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Vocabulaire avancé بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-french-08",
        "grade": "6AP",
        "subject": "french",
        "unit": "Préparation examen",
        "titleAr": "Préparation examen",
        "titleFr": "Préparation examen",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Préparation examen",
          "Appliquer Préparation examen dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Préparation examen بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-french-09",
        "grade": "6AP",
        "subject": "french",
        "unit": "Projet écrit",
        "titleAr": "Projet écrit",
        "titleFr": "Projet écrit",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Projet écrit",
          "Appliquer Projet écrit dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Projet écrit بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-french-10",
        "grade": "6AP",
        "subject": "french",
        "unit": "Transition collège",
        "titleAr": "Transition collège",
        "titleFr": "Transition collège",
        "durationMinutes": 12,
        "objectives": [
          "Comprendre: Transition collège",
          "Appliquer Transition collège dans une consigne simple",
          "Produire une réponse courte correcte"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "french_understanding",
          "french_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح Transition collège بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "science": [
      {
        "id": "6AP-science-01",
        "grade": "6AP",
        "subject": "science",
        "unit": "جسم الإنسان والصحة",
        "titleAr": "جسم الإنسان والصحة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم جسم الإنسان والصحة",
          "يطبق جسم الإنسان والصحة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح جسم الإنسان والصحة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-science-02",
        "grade": "6AP",
        "subject": "science",
        "unit": "التكاثر والنمو",
        "titleAr": "التكاثر والنمو",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التكاثر والنمو",
          "يطبق التكاثر والنمو في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التكاثر والنمو بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-science-03",
        "grade": "6AP",
        "subject": "science",
        "unit": "البيئة والتنمية المستدامة",
        "titleAr": "البيئة والتنمية المستدامة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم البيئة والتنمية المستدامة",
          "يطبق البيئة والتنمية المستدامة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح البيئة والتنمية المستدامة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-science-04",
        "grade": "6AP",
        "subject": "science",
        "unit": "المادة والطاقة",
        "titleAr": "المادة والطاقة",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المادة والطاقة",
          "يطبق المادة والطاقة في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المادة والطاقة بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-science-05",
        "grade": "6AP",
        "subject": "science",
        "unit": "الكهرباء والمغناطيسية الأولى",
        "titleAr": "الكهرباء والمغناطيسية الأولى",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الكهرباء والمغناطيسية الأولى",
          "يطبق الكهرباء والمغناطيسية الأولى في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الكهرباء والمغناطيسية الأولى بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-science-06",
        "grade": "6AP",
        "subject": "science",
        "unit": "الأرض والكون",
        "titleAr": "الأرض والكون",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الأرض والكون",
          "يطبق الأرض والكون في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأرض والكون بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-science-07",
        "grade": "6AP",
        "subject": "science",
        "unit": "المنهج التجريبي",
        "titleAr": "المنهج التجريبي",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المنهج التجريبي",
          "يطبق المنهج التجريبي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المنهج التجريبي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-science-08",
        "grade": "6AP",
        "subject": "science",
        "unit": "تحليل وثائق علمية",
        "titleAr": "تحليل وثائق علمية",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم تحليل وثائق علمية",
          "يطبق تحليل وثائق علمية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح تحليل وثائق علمية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-science-09",
        "grade": "6AP",
        "subject": "science",
        "unit": "تقييم إشهادي",
        "titleAr": "تقييم إشهادي",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم تقييم إشهادي",
          "يطبق تقييم إشهادي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح تقييم إشهادي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-science-10",
        "grade": "6AP",
        "subject": "science",
        "unit": "جسر نحو SVT/Physique",
        "titleAr": "جسر نحو SVT/Physique",
        "titleFr": "Activité scientifique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم جسر نحو SVT/Physique",
          "يطبق جسر نحو SVT/Physique في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "science_understanding",
          "science_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح جسر نحو SVT/Physique بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "islamic_education": [
      {
        "id": "6AP-islamic_education-01",
        "grade": "6AP",
        "subject": "islamic_education",
        "unit": "القيم والإيمان",
        "titleAr": "القيم والإيمان",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القيم والإيمان",
          "يطبق القيم والإيمان في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القيم والإيمان بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-islamic_education-02",
        "grade": "6AP",
        "subject": "islamic_education",
        "unit": "العبادات والسلوك",
        "titleAr": "العبادات والسلوك",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم العبادات والسلوك",
          "يطبق العبادات والسلوك في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح العبادات والسلوك بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-islamic_education-03",
        "grade": "6AP",
        "subject": "islamic_education",
        "unit": "السيرة والاقتداء",
        "titleAr": "السيرة والاقتداء",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم السيرة والاقتداء",
          "يطبق السيرة والاقتداء في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح السيرة والاقتداء بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-islamic_education-04",
        "grade": "6AP",
        "subject": "islamic_education",
        "unit": "القرآن والفهم",
        "titleAr": "القرآن والفهم",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القرآن والفهم",
          "يطبق القرآن والفهم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القرآن والفهم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-islamic_education-05",
        "grade": "6AP",
        "subject": "islamic_education",
        "unit": "الأسرة والمجتمع",
        "titleAr": "الأسرة والمجتمع",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الأسرة والمجتمع",
          "يطبق الأسرة والمجتمع في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الأسرة والمجتمع بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-islamic_education-06",
        "grade": "6AP",
        "subject": "islamic_education",
        "unit": "المواطنة والقيم",
        "titleAr": "المواطنة والقيم",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المواطنة والقيم",
          "يطبق المواطنة والقيم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المواطنة والقيم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-islamic_education-07",
        "grade": "6AP",
        "subject": "islamic_education",
        "unit": "التواصل الأخلاقي",
        "titleAr": "التواصل الأخلاقي",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التواصل الأخلاقي",
          "يطبق التواصل الأخلاقي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التواصل الأخلاقي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-islamic_education-08",
        "grade": "6AP",
        "subject": "islamic_education",
        "unit": "الاستعداد للتقويم",
        "titleAr": "الاستعداد للتقويم",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الاستعداد للتقويم",
          "يطبق الاستعداد للتقويم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الاستعداد للتقويم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-islamic_education-09",
        "grade": "6AP",
        "subject": "islamic_education",
        "unit": "مشروع قيمي",
        "titleAr": "مشروع قيمي",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم مشروع قيمي",
          "يطبق مشروع قيمي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح مشروع قيمي بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-islamic_education-10",
        "grade": "6AP",
        "subject": "islamic_education",
        "unit": "جسر نحو الإعدادي",
        "titleAr": "جسر نحو الإعدادي",
        "titleFr": "Éducation islamique",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم جسر نحو الإعدادي",
          "يطبق جسر نحو الإعدادي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "islamic_education_understanding",
          "islamic_education_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح جسر نحو الإعدادي بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ],
    "social_studies": [
      {
        "id": "6AP-social_studies-01",
        "grade": "6AP",
        "subject": "social_studies",
        "unit": "المغرب: المجال والموارد",
        "titleAr": "المغرب: المجال والموارد",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المغرب: المجال والموارد",
          "يطبق المغرب: المجال والموارد في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المغرب: المجال والموارد بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-social_studies-02",
        "grade": "6AP",
        "subject": "social_studies",
        "unit": "التاريخ الوطني",
        "titleAr": "التاريخ الوطني",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التاريخ الوطني",
          "يطبق التاريخ الوطني في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التاريخ الوطني بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-social_studies-03",
        "grade": "6AP",
        "subject": "social_studies",
        "unit": "الجغرافيا البشرية",
        "titleAr": "الجغرافيا البشرية",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الجغرافيا البشرية",
          "يطبق الجغرافيا البشرية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الجغرافيا البشرية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-social_studies-04",
        "grade": "6AP",
        "subject": "social_studies",
        "unit": "المواطنة والمؤسسات",
        "titleAr": "المواطنة والمؤسسات",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم المواطنة والمؤسسات",
          "يطبق المواطنة والمؤسسات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح المواطنة والمؤسسات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-social_studies-05",
        "grade": "6AP",
        "subject": "social_studies",
        "unit": "حقوق الإنسان والطفل",
        "titleAr": "حقوق الإنسان والطفل",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم حقوق الإنسان والطفل",
          "يطبق حقوق الإنسان والطفل في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح حقوق الإنسان والطفل بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-social_studies-06",
        "grade": "6AP",
        "subject": "social_studies",
        "unit": "الخرائط والمبيانات",
        "titleAr": "الخرائط والمبيانات",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم الخرائط والمبيانات",
          "يطبق الخرائط والمبيانات في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح الخرائط والمبيانات بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-social_studies-07",
        "grade": "6AP",
        "subject": "social_studies",
        "unit": "القضايا البيئية",
        "titleAr": "القضايا البيئية",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم القضايا البيئية",
          "يطبق القضايا البيئية في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح القضايا البيئية بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-social_studies-08",
        "grade": "6AP",
        "subject": "social_studies",
        "unit": "التراث والتنوع",
        "titleAr": "التراث والتنوع",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم التراث والتنوع",
          "يطبق التراث والتنوع في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح التراث والتنوع بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-social_studies-09",
        "grade": "6AP",
        "subject": "social_studies",
        "unit": "استعداد للتقويم",
        "titleAr": "استعداد للتقويم",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم استعداد للتقويم",
          "يطبق استعداد للتقويم في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح استعداد للتقويم بجملة قصيرة.",
        "masteryThreshold": 75
      },
      {
        "id": "6AP-social_studies-10",
        "grade": "6AP",
        "subject": "social_studies",
        "unit": "جسر نحو الإعدادي",
        "titleAr": "جسر نحو الإعدادي",
        "titleFr": "Éveil social",
        "durationMinutes": 12,
        "objectives": [
          "يفهم المتعلم مفهوم جسر نحو الإعدادي",
          "يطبق جسر نحو الإعدادي في وضعية بسيطة",
          "يعبّر عن طريقة الحل بكلمات قصيرة"
        ],
        "prerequisites": [
          "الانتباه للتعليمة",
          "معرفة الكلمات الأساسية",
          "محاولة الجواب قبل رؤية الحل"
        ],
        "competencies": [
          "social_studies_understanding",
          "social_studies_practice",
          "short_reasoning"
        ],
        "misconceptions": [
          "الجواب بسرعة دون فهم السؤال",
          "نسيان خطوة أساسية",
          "الخلط بين المثال والقاعدة"
        ],
        "microSteps": [
          "تهيئة قصيرة",
          "شرح بصري أو شفهي",
          "مثال واحد",
          "سؤال سريع",
          "تصحيح مشجع",
          "نجمة تقدم"
        ],
        "exerciseTypes": [
          "oral_prompt",
          "picture_choice",
          "guided_practice",
          "mini_game",
          "quick_check"
        ],
        "parentSignal": "راقب هل يستطيع الطفل شرح جسر نحو الإعدادي بجملة قصيرة.",
        "masteryThreshold": 75
      }
    ]
  }
} as Record<PrimaryGrade, Record<PrimarySubject, PrimaryLesson[]>>;

export function getPrimaryLessons(grade: PrimaryGrade, subject?: PrimarySubject) {
  const gradeLessons = primaryCurriculum[grade] ?? primaryCurriculum["1AP"];
  if (subject) return gradeLessons[subject] ?? [];
  return Object.values(gradeLessons).flat();
}

export function normalizePrimaryGrade(level?: number | string | null): PrimaryGrade {
  const raw = String(level ?? "").toLowerCase();
  if (raw.includes("6")) return "6AP";
  if (raw.includes("5")) return "5AP";
  if (raw.includes("4")) return "4AP";
  if (raw.includes("3")) return "3AP";
  if (raw.includes("2")) return "2AP";
  return "1AP";
}

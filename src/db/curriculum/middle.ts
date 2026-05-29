import type { SubjectData } from "./types";

export const grade1ac: SubjectData[] = [
  {
    slug: "arabic", titleAr: "اللغة العربية", icon: "BookOpen", color: "#059669", orderIndex: 1,
    units: [{
      slug: "nass-adabi", titleAr: "النص الأدبي", orderIndex: 1,
      lessons: [
        {
          slug: "tahleel-nass", titleAr: "تحليل النص الأدبي", difficulty: "medium", durationMin: 35,
          objectives: ["تحديد نوع النص", "استخراج الأفكار الرئيسية", "تحليل الأسلوب الأدبي"],
          explanation: `خطوات تحليل النص الأدبي:\n\n1️⃣ القراءة الأولى: الفهم العام\n2️⃣ نوع النص: شعر / نثر / مسرح\n3️⃣ الموضوع: ما يتحدث عنه النص\n4️⃣ الأفكار الرئيسية: الفكرة المحورية + الأفكار الفرعية\n5️⃣ الأسلوب: الصور البيانية + الأساليب الإنشائية\n6️⃣ القيم: ما يعلمنا النص\n\nالصور البيانية في النص:\n- التشبيه: مقارنة بأداة\n- الاستعارة: تشبيه بدون أداة\n- الكناية: التعبير غير المباشر`,
          vocabulary: [
            { word: "نص أدبي", definition: "كلام يتميز بالجمال والإبداع ويعبر عن مشاعر وأفكار" },
            { word: "فكرة محورية", definition: "الفكرة الأساسية التي يدور حولها النص" },
            { word: "كناية", definition: "تعبير يُقصد به غير معناه الحقيقي مع جواز المعنيين" },
          ],
          examples: [{ text: "هو كثير الرماد (كناية عن الكرم)", note: "الكناية تعبر بشيء وتقصد غيره" }, { text: "أفكار رئيسية: وطنية + تضحية", note: "استخراج الأفكار" }],
          summary: "تحليل النص: قراءة → تحديد النوع → الموضوع → الأفكار → الأسلوب → القيم. الصور البيانية: تشبيه + استعارة + كناية.",
          exercises: [
            { type: "mcq", question: "الخطوة الأولى في تحليل النص:", options: ["الأسلوب", "القراءة الأولى", "القيم", "النوع"], correctAnswer: "القراءة الأولى", explanation: "نبدأ دائماً بالقراءة العامة لفهم النص", points: 10 },
            { type: "mcq", question: "'هو كثير الرماد' كناية عن:", options: ["الفقر", "الكرم", "الغضب", "الكذب"], correctAnswer: "الكرم", explanation: "كثير الرماد كناية عن الكرم (الطعام الكثير يُخلّف رماداً)", points: 10 },
            { type: "true_false", question: "الفكرة المحورية هي الفكرة الأساسية للنص", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الفكرة المحورية هي العمود الفقري للنص", points: 10 },
          ],
        },
      ],
    }],
  },
  {
    slug: "math", titleAr: "الرياضيات", icon: "Calculator", color: "#2563eb", orderIndex: 2,
    units: [{
      slug: "jabr", titleAr: "الجبر", orderIndex: 1,
      lessons: [
        {
          slug: "muaddilaat-daraja1", titleAr: "معادلات الدرجة الأولى", difficulty: "medium", durationMin: 35,
          objectives: ["حل معادلات الدرجة الأولى بمجهول واحد", "التحقق من الحل", "تطبيقات"],
          explanation: `معادلة الدرجة الأولى: درجة المجهول 1\n\nشكلها: أ×س + ب = 0\n\nخطوات الحل:\n1️⃣ نقل الأعداد المجردة لطرف\n2️⃣ نقل الأعداد ذات س للطرف الآخر\n3️⃣ القسمة على معامل س\n\nمثال:\n3س + 7 = 22\n3س = 22 - 7 = 15\nس = 15 ÷ 3 = 5\n\nتحقق: 3(5) + 7 = 15 + 7 = 22 ✓`,
          vocabulary: [
            { word: "معادلة الدرجة الأولى", definition: "معادلة أعلى قوة للمجهول فيها هي 1" },
            { word: "معامل", definition: "العدد المضروب في المجهول" },
            { word: "حد مستقل", definition: "العدد في المعادلة غير المتصل بالمجهول" },
          ],
          examples: [{ text: "2س - 4 = 10 → 2س = 14 → س = 7", note: "حل خطوة بخطوة" }, { text: "5س + 3 = 28 → 5س = 25 → س = 5", note: "نتحقق: 5×5+3=28 ✓" }],
          summary: "معادلة الدرجة الأولى: أ×س + ب = ج. نعزل س: نقل الأعداد → نقسم على معامل س. تحقق دائماً!",
          exercises: [
            { type: "mcq", question: "حل: 2س + 5 = 17", options: ["5", "6", "7", "8"], correctAnswer: "6", explanation: "2س = 17-5=12 → س=12÷2=6. تحقق: 2×6+5=17 ✓", points: 10 },
            { type: "mcq", question: "حل: 4س - 8 = 20", options: ["5", "6", "7", "8"], correctAnswer: "7", explanation: "4س = 20+8=28 → س=28÷4=7. تحقق: 4×7-8=20 ✓", points: 10 },
            { type: "fill_blank", question: "حل: 3س = 27 → س = ___", correctAnswer: "9", explanation: "س = 27÷3 = 9. تحقق: 3×9=27 ✓", points: 15 },
            { type: "true_false", question: "التحقق ضروري بعد حل المعادلة", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — نتحقق بتعويض الجواب في المعادلة الأصلية", points: 10 },
          ],
        },
        {
          slug: "mutawaaziyaat-ams", titleAr: "المتتاليات الحسابية", difficulty: "hard", durationMin: 35,
          objectives: ["تعريف المتتالية الحسابية", "إيجاد الحد العام", "مجموع حدود المتتالية"],
          explanation: `المتتالية الحسابية:\nسلسلة أعداد الفرق بين كل حدين متتاليين ثابت\n\nمثال: 2، 5، 8، 11، 14...\nالفرق الثابت (d) = 3\n\nالحد العام: u(n) = u(1) + (n-1) × d\nu(1) = 2، d = 3\nu(5) = 2 + 4×3 = 14 ✓\n\nمجموع n حد:\nS(n) = n/2 × (u(1) + u(n))\nS(5) = 5/2 × (2+14) = 5/2 × 16 = 40`,
          vocabulary: [
            { word: "متتالية حسابية", definition: "سلسلة أعداد الفرق بين كل حدين متتاليين ثابت" },
            { word: "الفرق الأساسي", definition: "الفرق الثابت (d) بين كل حدين متتاليين" },
            { word: "الحد العام", definition: "الصيغة التي تعطي أي حد في المتتالية" },
          ],
          examples: [{ text: "3، 7، 11، 15... الفرق d=4", note: "المتتالية الحسابية وفرقها" }, { text: "u(6) = 3 + 5×4 = 23", note: "الحد السادس" }],
          summary: "المتتالية الحسابية: فرق ثابت d. الحد العام: u(n) = u(1) + (n-1)×d. المجموع: S(n) = n/2 × (u(1)+u(n)).",
          exercises: [
            { type: "mcq", question: "في المتتالية 5، 9، 13... الفرق الأساسي هو:", options: ["3", "4", "5", "9"], correctAnswer: "4", explanation: "9-5=4، 13-9=4 → الفرق الأساسي d=4", points: 10 },
            { type: "mcq", question: "الحد الخامس في 2، 5، 8...", options: ["11", "14", "17", "20"], correctAnswer: "14", explanation: "u(5) = 2 + 4×3 = 14", points: 10 },
            { type: "fill_blank", question: "في 10، 15، 20... الفرق d = ___", correctAnswer: "5", explanation: "15-10=5، 20-15=5 → d=5", points: 15 },
          ],
        },
      ],
    }],
  },
  {
    slug: "english", titleAr: "اللغة الإنجليزية", icon: "Languages", color: "#dc2626", orderIndex: 4,
    units: [{
      slug: "grammar", titleAr: "قواعد اللغة الإنجليزية", orderIndex: 1,
      lessons: [
        {
          slug: "present-simple", titleAr: "زمن المضارع البسيط", difficulty: "medium", durationMin: 30,
          objectives: ["استخدام المضارع البسيط", "تصريف الفعل", "الأفعال المساعدة do/does"],
          explanation: `Present Simple — للأفعال المعتادة والحقائق:\n\nاستخدامات:\n✅ عادات: I wake up at 7. (أستيقظ في 7)\n✅ حقائق: The sun rises in the east. (الشمس تشرق من الشرق)\n✅ برامج: The train leaves at 9. (القطار يغادر 9)\n\nالتصريف:\nI/You/We/They + الفعل الأصلي: I eat\nHe/She/It + الفعل + s/es: He eats, She goes\n\nالنفي:\nI/You/We/They → don't + فعل\nHe/She/It → doesn't + فعل\n\nالسؤال:\nDo + I/You/We/They + فعل؟\nDoes + He/She/It + فعل؟`,
          vocabulary: [
            { word: "Present Simple", definition: "زمن المضارع البسيط — للعادات والحقائق والجداول" },
            { word: "don't", definition: "do not — للنفي مع I/You/We/They" },
            { word: "doesn't", definition: "does not — للنفي مع He/She/It" },
          ],
          examples: [{ text: "She reads every day. (تقرأ كل يوم)", note: "She+فعل+s" }, { text: "They don't watch TV. (لا يشاهدون التلفاز)", note: "نفي مع They" }],
          summary: "مضارع بسيط: عادات وحقائق. He/She/It + s/es. نفي: don't/doesn't. سؤال: Do/Does.",
          exercises: [
            { type: "mcq", question: "He ___ to school every day. (go)", options: ["go", "goes", "going", "went"], correctAnswer: "goes", explanation: "He/She/It يضاف لهم s/es في المضارع البسيط", points: 10 },
            { type: "mcq", question: "نفي: They study English. → They ___ study English.", options: ["don't", "doesn't", "isn't", "aren't"], correctAnswer: "don't", explanation: "They → نستخدم don't للنفي", points: 10 },
            { type: "fill_blank", question: "She ___ not like coffee. (النفي)", correctAnswer: "does", explanation: "She → doesn't = does not", points: 15 },
            { type: "true_false", question: "'Does he play football?' سؤال صحيح", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "He → Does في صيغة السؤال", points: 10 },
          ],
        },
      ],
    }],
  },
];

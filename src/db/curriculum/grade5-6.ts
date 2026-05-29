import type { SubjectData } from "./types";

export const grade5: SubjectData[] = [
  {
    slug: "arabic", titleAr: "اللغة العربية", icon: "BookOpen", color: "#059669", orderIndex: 1,
    units: [{
      slug: "adab", titleAr: "الأدب والبلاغة", orderIndex: 1,
      lessons: [
        {
          slug: "istiara", titleAr: "الاستعارة", difficulty: "medium", durationMin: 25,
          objectives: ["تعريف الاستعارة", "الاستعارة المكنية والتصريحية", "التمييز بينها وبين التشبيه"],
          explanation: `الاستعارة: تشبيه حُذف أحد طرفيه\n\nإذا حُذف المشبه به → استعارة تصريحية:\n"رأيتُ أسداً في الحرب" (أي رجلاً شجاعاً)\n\nإذا حُذف المشبه → استعارة مكنية:\n"خاضت السفينةُ البحرَ بشجاعة"\n(السفينة كالإنسان الشجاع)\n\nالفرق عن التشبيه:\nتشبيه: الولد كالأسد\nاستعارة: رأيتُ أسداً (أي ولداً شجاعاً)`,
          vocabulary: [
            { word: "استعارة", definition: "تشبيه حذف أحد طرفيه مع قرينة تمنع المعنى الحقيقي" },
            { word: "تصريحية", definition: "استعارة ذُكر فيها المشبه به وحُذف المشبه" },
            { word: "مكنية", definition: "استعارة ذُكر فيها المشبه وحُذف المشبه به مع لوازمه" },
          ],
          examples: [{ text: "نشرَ الليلُ جناحيه (الليل كطائر يبسط جناحيه)", note: "استعارة مكنية" }, { text: "رأيتُ بحراً يتكلم (أي عالماً)", note: "استعارة تصريحية" }],
          summary: "الاستعارة = تشبيه بدون أداة وحُذف أحد طرفيه. تصريحية: حُذف المشبه. مكنية: حُذف المشبه به.",
          exercises: [
            { type: "mcq", question: "في 'نشرَ الليلُ جناحيه' — الاستعارة:", options: ["تشبيه", "مكنية", "تصريحية", "بليغة"], correctAnswer: "مكنية", explanation: "المشبه (الليل) موجود والمشبه به (الطائر) محذوف ومعنا 'جناحيه' من لوازمه", points: 10 },
            { type: "mcq", question: "الفرق بين التشبيه والاستعارة:", options: ["لا فرق", "الاستعارة تحذف أحد الطرفين", "التشبيه أقوى", "الاستعارة للمدح فقط"], correctAnswer: "الاستعارة تحذف أحد الطرفين", explanation: "الاستعارة = تشبيه حُذف منه المشبه أو المشبه به", points: 10 },
            { type: "true_false", question: "الاستعارة أبلغ من التشبيه", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الاستعارة أبلغ لأنها تجعل الصورة أقوى بالحذف", points: 10 },
          ],
        },
      ],
    }],
  },
  {
    slug: "math", titleAr: "الرياضيات", icon: "Calculator", color: "#2563eb", orderIndex: 2,
    units: [{
      slug: "nisbamia", titleAr: "النسب المئوية والتناسب", orderIndex: 1,
      lessons: [
        {
          slug: "nisba-miia", titleAr: "النسبة المئوية", difficulty: "medium", durationMin: 30,
          objectives: ["تعريف النسبة المئوية", "تحويل الكسور إلى نسب مئوية", "حسابات عملية"],
          explanation: `النسبة المئوية: جزء من مئة\n\n% تعني "من مئة"\n50% = 50/100 = ½\n25% = 25/100 = ¼\n\nتحويل كسر → نسبة مئوية:\n3/5 = 3/5 × 100% = 60%\n\nتحويل نسبة → كسر:\n75% = 75/100 = ¾\n\nتطبيق:\n20% من 50 = 50 × 20/100 = 10`,
          vocabulary: [
            { word: "نسبة مئوية", definition: "نسبة من مئة — يُعبر عنها بالرمز %" },
            { word: "خصم", definition: "تخفيض من السعر الأصلي — غالباً بنسبة مئوية" },
          ],
          examples: [{ text: "خصم 20% على 150 درهم = 30 درهم خصم", note: "150 × 20/100 = 30" }, { text: "4/5 = 80%", note: "4÷5 × 100 = 80%" }],
          summary: "% = من مئة. لتحويل كسر: اضرب في 100. لحساب نسبة من عدد: عدد × نسبة÷100.",
          exercises: [
            { type: "mcq", question: "½ يساوي كم بالمئة؟", options: ["25%", "50%", "75%", "100%"], correctAnswer: "50%", explanation: "½ = 1÷2 × 100 = 50%", points: 10 },
            { type: "mcq", question: "10% من 200 = ؟", options: ["10", "20", "30", "40"], correctAnswer: "20", explanation: "200 × 10/100 = 20", points: 10 },
            { type: "fill_blank", question: "¼ = ___% ", correctAnswer: "25", explanation: "¼ = 1÷4 × 100 = 25%", points: 15 },
            { type: "true_false", question: "100% يعني الكل كله", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "100/100 = 1 = الكل", points: 10 },
          ],
        },
      ],
    }],
  },
  {
    slug: "science", titleAr: "العلوم", icon: "Microscope", color: "#0891b2", orderIndex: 3,
    units: [{
      slug: "mada-khawass", titleAr: "المادة وخصائصها", orderIndex: 1,
      lessons: [
        {
          slug: "halaat-mada", titleAr: "حالات المادة الثلاث", difficulty: "medium", durationMin: 25,
          objectives: ["تعريف حالات المادة الثلاث", "خصائص كل حالة", "التحولات بين الحالات"],
          explanation: `المادة توجد في ثلاث حالات:\n\n💧 السائل:\n• له حجم ثابت ولا شكل ثابت\n• يأخذ شكل إنائه\n• أمثلة: ماء، زيت، عصير\n\n🧊 الصلب:\n• له حجم وشكل ثابتان\n• أمثلة: خشب، حجر، جليد\n\n💨 الغاز:\n• لا حجم ولا شكل ثابتان\n• ينتشر في كل الاتجاهات\n• أمثلة: هواء، بخار ماء، أكسجين\n\nالتحولات:\n🔥 التسخين: صلب → سائل (انصهار) → غاز (تبخر)\n❄️ التبريد: غاز → سائل (تكاثف) → صلب (تجمد)`,
          vocabulary: [
            { word: "انصهار", definition: "تحول المادة من حالة صلبة إلى سائلة بالتسخين" },
            { word: "تبخر", definition: "تحول المادة من حالة سائلة إلى غازية" },
            { word: "تجمد", definition: "تحول المادة من حالة سائلة إلى صلبة بالتبريد" },
          ],
          examples: [{ text: "الجليد (صلب) يذوب → ماء (سائل)", note: "انصهار بالحرارة" }, { text: "الماء (سائل) يتبخر → بخار (غاز)", note: "تبخر بالحرارة" }],
          summary: "صلب (شكل ثابت) | سائل (شكل إنائه) | غاز (ينتشر). الحرارة تحوّل من صلب→سائل→غاز. البرودة العكس.",
          exercises: [
            { type: "mcq", question: "أيٌّ من التالية في الحالة الصلبة؟", options: ["الماء", "الزيت", "الخشب", "الهواء"], correctAnswer: "الخشب", explanation: "الخشب مادة صلبة لها شكل وحجم ثابتان", points: 10 },
            { type: "mcq", question: "تحول الجليد إلى ماء يُسمى:", options: ["تبخر", "انصهار", "تجمد", "تكاثف"], correctAnswer: "انصهار", explanation: "الانصهار: تحول الصلب إلى سائل بالتسخين", points: 10 },
            { type: "true_false", question: "الغاز لا شكل له ولا حجم ثابتان", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الغاز يملأ أي إناء ويأخذ شكله وحجمه", points: 10 },
            { type: "fill_blank", question: "تحول السائل إلى غاز يُسمى: ___", correctAnswer: "تبخر", explanation: "التبخر: سائل → غاز (عند التسخين)", points: 15 },
          ],
        },
      ],
    }],
  },
];

export const grade6: SubjectData[] = [
  {
    slug: "arabic", titleAr: "اللغة العربية", icon: "BookOpen", color: "#059669", orderIndex: 1,
    units: [{
      slug: "nahw-mutaqadim", titleAr: "النحو المتقدم", orderIndex: 1,
      lessons: [
        {
          slug: "haal-tamyiiz", titleAr: "الحال والتمييز", difficulty: "hard", durationMin: 30,
          objectives: ["تعريف الحال والتمييز", "التمييز بينهما", "الإعراب"],
          explanation: `الحال: وصف لحالة الفاعل أو المفعول وقت الفعل\n• جاءَ الطالبُ مبتسماً\n  (مبتسماً: حال — يصف حالة الطالب عند المجيء)\n• نكرة منصوبة دائماً\n\nالتمييز: يُبيّن إبهام اسم أو نسبة\n• عندي عشرون كتاباً\n  (كتاباً: تمييز — أوضح ماهية العشرين)\n• اشتريتُ لتراً حليباً\n  (حليباً: تمييز للنسبة)`,
          vocabulary: [
            { word: "حال", definition: "اسم نكرة منصوب يبين هيئة الفاعل أو المفعول عند وقوع الفعل" },
            { word: "تمييز", definition: "اسم نكرة منصوب يزيل إبهام اسم أو نسبة قبله" },
          ],
          examples: [{ text: "وقفَ الطالبُ مُنتبهاً (حال)", note: "منتبهاً تصف حالة الطالب" }, { text: "عندي خمسةٌ وعشرون طالباً (تمييز)", note: "طالباً أوضحت ماهية العدد" }],
          summary: "الحال: نكرة منصوبة تصف هيئة الفاعل/المفعول. التمييز: نكرة منصوبة تزيل الإبهام عن عدد أو نسبة.",
          exercises: [
            { type: "mcq", question: "في 'جاءَ أحمدُ مسرعاً' — الحال هو:", options: ["جاء", "أحمد", "مسرعاً", "في"], correctAnswer: "مسرعاً", explanation: "مسرعاً حال — تصف هيئة أحمد عند المجيء", points: 10 },
            { type: "mcq", question: "التمييز في 'اشتريتُ كيلوغراماً تمراً':", options: ["اشتريت", "كيلوغراماً", "تمراً", "في"], correctAnswer: "تمراً", explanation: "تمراً تمييز — أوضح ماهية الكيلوغرام", points: 10 },
            { type: "true_false", question: "الحال دائماً نكرة منصوبة", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — الحال نكرة منصوبة تصف هيئة صاحبها", points: 10 },
          ],
        },
      ],
    }],
  },
  {
    slug: "math", titleAr: "الرياضيات", icon: "Calculator", color: "#2563eb", orderIndex: 2,
    units: [{
      slug: "jabr-muqaddima", titleAr: "مقدمة في الجبر", orderIndex: 1,
      lessons: [
        {
          slug: "muaddilaat-basita", titleAr: "المعادلات البسيطة", difficulty: "hard", durationMin: 35,
          objectives: ["فهم مفهوم المعادلة", "حل معادلات بسيطة", "التحقق من الحل"],
          explanation: `المعادلة: تعبير رياضي فيه مجهول (س) ويحقق المساواة\n\nمبدأ المساواة:\nما تفعله لطرف تفعله للطرف الآخر!\n\nحل المعادلة:\nس + 5 = 12\n⬇️ نطرح 5 من الطرفين\nس + 5 - 5 = 12 - 5\nس = 7\n\nتحقق: 7 + 5 = 12 ✓\n\nأنواع:\nس + أ = ب → س = ب - أ\nس - أ = ب → س = ب + أ\nأ × س = ب → س = ب ÷ أ`,
          vocabulary: [
            { word: "معادلة", definition: "علاقة رياضية تُعبّر عن مساواة بين طرفين" },
            { word: "مجهول", definition: "الكمية غير المعروفة نرمز لها بـ (س)" },
            { word: "حل المعادلة", definition: "إيجاد قيمة المجهول التي تحقق المساواة" },
          ],
          examples: [{ text: "س + 8 = 15 → س = 15 - 8 = 7", note: "معادلة جمع" }, { text: "3 × س = 24 → س = 24 ÷ 3 = 8", note: "معادلة ضرب" }],
          summary: "المعادلة: طرفان متساويان. المجهول (س). لحلها: عزل س بعمليات معاكسة. تحقق دائماً!",
          exercises: [
            { type: "mcq", question: "حل المعادلة: س + 7 = 15", options: ["6", "7", "8", "9"], correctAnswer: "8", explanation: "س = 15 - 7 = 8. تحقق: 8+7=15 ✓", points: 10 },
            { type: "mcq", question: "حل: 4 × س = 32", options: ["6", "7", "8", "9"], correctAnswer: "8", explanation: "س = 32 ÷ 4 = 8. تحقق: 4×8=32 ✓", points: 10 },
            { type: "fill_blank", question: "حل: س - 9 = 11 → س = ___", correctAnswer: "20", explanation: "س = 11 + 9 = 20. تحقق: 20-9=11 ✓", points: 15 },
            { type: "true_false", question: "حل معادلة: ما تفعله لطرف تفعله للآخر", options: ["صحيح", "خطأ"], correctAnswer: "صحيح", explanation: "نعم — هذا مبدأ المساواة الأساسي في حل المعادلات", points: 10 },
          ],
        },
      ],
    }],
  },
];

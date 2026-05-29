import type { PrimaryLesson, PrimaryLessonBlock } from "./types";

export function buildPrimaryMicroLesson(lesson: PrimaryLesson): PrimaryLessonBlock[] {
  const objective = lesson.objectives[0] ?? `فهم ${lesson.titleAr}`;
  const misconception = lesson.misconceptions[0] ?? "التسرع قبل فهم السؤال";

  return [
    {
      kind: "warmup",
      title: "تهيئة لطيفة",
      body: `اليوم غادي نتعلمو ${lesson.titleAr}. الهدف الصغير هو: ${objective}.`,
    },
    {
      kind: "visual_explain",
      title: "شرح بصري قصير",
      body: "ليلى تبدأ بصورة أو مثال من البيت أو المدرسة، ثم تعطي قاعدة صغيرة واحدة فقط.",
    },
    {
      kind: "voice_prompt",
      title: "سؤال شفهي",
      body: "جاوب بصوتك أو بكلمة قصيرة: شنو أول خطوة؟",
      expectedAnswer: "محاولة قصيرة مرتبطة بالدرس.",
      childFriendlyHint: "إلى كان صعيب، نعطيك اختيارين وتختار واحد.",
    },
    {
      kind: "mini_game",
      title: "لعبة دقيقة واحدة",
      body: "اختيار، ترتيب، مطابقة، أو عدّ سريع للحصول على نجمة.",
    },
    {
      kind: "guided_practice",
      title: "تطبيق موجه",
      body: `إذا ظهر خطأ مثل: ${misconception}، ليلى تعيد الشرح بلطف وبمثال أسهل.`,
    },
    {
      kind: "encouragement",
      title: "تشجيع",
      body: "برافو! المهم هو المحاولة. دابا نجربو سؤال واحد آخر أو نوقفو بنجاح صغير.",
    },
    {
      kind: "parent_note",
      title: "ملاحظة للولي",
      body: lesson.parentSignal,
    },
  ];
}

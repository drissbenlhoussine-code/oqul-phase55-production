export const primaryQualityDepth = {
  lessonShape: {
    maxExplanationSeconds: 45,
    maxTextLines: 4,
    voiceFirst: true,
    defaultLanguage: "darija",
    fallbackLanguage: "simple_formal_arabic",
  },
  emotionalRules: [
    "شجّع الطفل بعد كل محاولة.",
    "لا تستعمل كلمات مثل خطأ بشكل قاسٍ.",
    "حوّل الفشل إلى لعبة: جرب مرة أخرى.",
    "استعمل أمثلة من البيت، المدرسة، السوق، واللعب.",
  ],
  microLessonLoop: [
    "hook_story",
    "tiny_explanation",
    "one_question",
    "instant_feedback",
    "mini_reward",
    "repeat_or_level_up",
  ],
  rewardSystem: {
    stars: true,
    stickers: true,
    dailyQuest: true,
    mascotFeedback: true,
  },
};
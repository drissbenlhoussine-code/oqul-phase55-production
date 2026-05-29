export type EmotionalMemoryInput = {
  childName?: string;
  preferredExamples?: string[];
  motivationStyle?: "encouragement" | "challenge" | "play" | "storytelling";
  recentEmotion?: "confident" | "frustrated" | "tired" | "curious" | "neutral";
};

export function chooseExampleContext(input: EmotionalMemoryInput) {
  const examples = input.preferredExamples ?? [];
  if (examples.includes("football")) return "football";
  if (examples.includes("food")) return "food";
  if (examples.includes("money")) return "money";
  if (examples.includes("stories")) return "stories";
  return "daily-life";
}

export function buildEmotionAwareTeachingHint(input: EmotionalMemoryInput) {
  const name = input.childName ? `${input.childName}، ` : "";
  const context = chooseExampleContext(input);

  if (input.recentEmotion === "frustrated") {
    return `${name}نبدلو الطريقة ونشرحها بمثال قريب ليك من ${context}. ماشي مشكل نرجعو خطوة صغيرة.`;
  }

  if (input.recentEmotion === "tired") {
    return `${name}نديرو غير تمرين خفيف وبسيط باش ما نتعبوش.`;
  }

  if (input.motivationStyle === "challenge") {
    return `${name}واش واجد لتحدي صغير؟ نخليه ممتع وسهل البداية.`;
  }

  if (input.motivationStyle === "storytelling") {
    return `${name}نشرحها بحكاية صغيرة باش تبقى فبالك.`;
  }

  return `${name}نكملو بهدوء وتشجيع، خطوة بخطوة.`;
}

export function mergeEmotionalPreferences(input: {
  currentPreferredExamples: string[];
  newPreferredExample?: string;
}) {
  const merged = new Set(input.currentPreferredExamples);
  if (input.newPreferredExample) merged.add(input.newPreferredExample);
  return Array.from(merged).slice(0, 8);
}

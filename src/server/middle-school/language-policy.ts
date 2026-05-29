import type { LearningLanguage } from "./types";

const darijaSignals = ["دارجة", "بالدارجة", "مغربية", "اشرح مزيان", "واش", "علاش"];
const frenchSignals = ["français", "french", "en français", "explique en français", "فرنسية"];
const englishSignals = ["english", "anglais", "explain in english", "إنجليزية"];
const fushaSignals = ["فصحى", "العربية", "اشرح بالعربية", "لغة عربية"];

export function detectLearningLanguage(message?: string | null, preferred: LearningLanguage = "auto"): Exclude<LearningLanguage, "auto"> {
  const text = (message ?? "").toLowerCase();
  if (preferred && preferred !== "auto") return preferred;
  if (darijaSignals.some((s) => text.includes(s))) return "darija";
  if (frenchSignals.some((s) => text.includes(s))) return "fr";
  if (englishSignals.some((s) => text.includes(s))) return "en";
  if (fushaSignals.some((s) => text.includes(s))) return "ar_fusha";
  return "ar_fusha";
}

export function getLanguageInstruction(language: Exclude<LearningLanguage, "auto">): string {
  switch (language) {
    case "darija":
      return "استعملي الدارجة المغربية الواضحة مع الحفاظ على المصطلح العلمي بالفصحى بين قوسين عند الحاجة.";
    case "fr":
      return "Réponds en français clair, avec de petites explications en arabe si l'élève semble bloqué.";
    case "en":
      return "Respond in simple English, and keep scientific terms precise. Add Arabic support only when useful.";
    case "ar_fusha":
    default:
      return "استعملي العربية الفصحى السلسة والذكية، لا تكوني رسمية جدًا، واستعملي الدارجة فقط عندما يطلبها التلميذ أو يحتاج تشجيعًا عاطفيًا سريعًا.";
  }
}

export function getLanguageSwitchRule(): string {
  return "ابدئي بالفصحى السلسة للإعدادي. إذا طلب التلميذ: اشرح بالدارجة، Explain in French، Explain in English، غيّري اللغة فورًا داخل نفس المحادثة دون مقاومة.";
}

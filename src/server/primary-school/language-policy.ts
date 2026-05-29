import type { PrimaryLanguage } from "./types";

const frenchSignals = ["français", "french", "en français", "فرنسية"];
const fushaSignals = ["فصحى", "العربية الفصحى", "لغة عربية"];
const darijaSignals = ["دارجة", "مغربية", "اشرح بحال", "واش", "علاش", "بالمغربية"];

export function detectPrimaryLanguage(message?: string | null, preferred: PrimaryLanguage = "auto"): Exclude<PrimaryLanguage, "auto"> {
  const text = (message ?? "").toLowerCase();
  if (preferred && preferred !== "auto") return preferred;
  if (frenchSignals.some((s) => text.includes(s))) return "fr";
  if (fushaSignals.some((s) => text.includes(s))) return "ar_fusha";
  if (darijaSignals.some((s) => text.includes(s))) return "darija";
  return "darija";
}

export function getPrimaryLanguageInstruction(language: Exclude<PrimaryLanguage, "auto">): string {
  switch (language) {
    case "fr":
      return "Parle en français très simple, phrases courtes, encouragement doux, et explique les consignes comme à un enfant du primaire.";
    case "ar_fusha":
      return "استعملي عربية فصحى سهلة جدًا، جمل قصيرة، أمثلة بصرية، وتشجيع مستمر دون إطالة.";
    case "darija":
    default:
      return "استعملي الدارجة المغربية الدافئة مع المصطلح المدرسي بالفصحى بين قوسين عند الحاجة. الجمل قصيرة، مشجعة، ومناسبة لطفل صغير.";
  }
}

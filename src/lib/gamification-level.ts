export interface LevelInfo {
  level: number;
  title: string;
  xpRequired: number;
  xpToNext: number;
  progress: number;
}

const LEVEL_THRESHOLDS = [
  0, 100, 250, 500, 900, 1400, 2100, 3000, 4200, 5800, 7800,
];

const LEVEL_TITLES = [
  "مبتدئ",
  "طالب نشيط",
  "متعلم جيد",
  "متميز",
  "نجم الفصل",
  "موهبة",
  "عبقري صغير",
  "أستاذ المستقبل",
  "خبير",
  "عالم",
  "أسطورة عقول",
];

export function getLevelInfo(xp: number): LevelInfo {
  let level = 0;

  for (let index = LEVEL_THRESHOLDS.length - 1; index >= 0; index -= 1) {
    if (xp >= LEVEL_THRESHOLDS[index]) {
      level = index;
      break;
    }
  }

  const xpRequired = LEVEL_THRESHOLDS[level] ?? 0;
  const xpForNext = LEVEL_THRESHOLDS[level + 1] ?? xpRequired + 1000;
  const xpInLevel = xp - xpRequired;
  const xpNeeded = Math.max(1, xpForNext - xpRequired);

  return {
    level: level + 1,
    title: LEVEL_TITLES[level] ?? "خبير",
    xpRequired,
    xpToNext: Math.max(0, xpForNext - xp),
    progress: Math.max(0, Math.min(100, Math.round((xpInLevel / xpNeeded) * 100))),
  };
}

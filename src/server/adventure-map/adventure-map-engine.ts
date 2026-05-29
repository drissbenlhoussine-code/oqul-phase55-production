export type AdventureNode = {
  nodeId: string;
  grade: number;
  subject: string;
  skillId?: string;
  world: string;
  title: string;
  description: string;
  unlockOrder: number;
};

const worldsBySubject: Record<string, string[]> = {
  math: ["جزيرة الجمع", "قلعة الجداول", "جبل الكسور", "وادي الهندسة"],
  arabic: ["غابة القراءة", "قلعة القصص", "نهر القواعد"],
  french: ["مدينة الكلمات", "محطة الحوار"],
  science: ["مختبر الاكتشاف", "حديقة الطبيعة"],
};

export function createAdventureNode(input: {
  grade: number;
  subject: string;
  skillId?: string;
  title: string;
  order: number;
}): AdventureNode {
  const worlds = worldsBySubject[input.subject] ?? ["طريق التعلم"];
  const world = worlds[input.order % worlds.length];

  return {
    nodeId: `g${input.grade}-${input.subject}-${input.order}`,
    grade: input.grade,
    subject: input.subject,
    skillId: input.skillId,
    world,
    title: input.title,
    description: `افتح ${world} عبر إتقان: ${input.title}`,
    unlockOrder: input.order,
  };
}

export function buildAdventureReward(input: { completed: boolean; stars: number }) {
  if (!input.completed) return "كمّل المهمة باش تفتح الطريق القادم ✨";
  if (input.stars >= 3) return "إنجاز رائع! حصلت على 3 نجوم وفتحت مرحلة جديدة 🌟";
  return "ممتاز! فتحت خطوة جديدة في خريطة التعلم 👏";
}

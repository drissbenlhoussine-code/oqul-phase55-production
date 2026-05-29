import type { EmotionalSignal, LearningMission, MasteryBand, Phase40LearningSnapshot, TutorState } from "./types";

type ProgressLike = {
  status: string;
  score?: number | null;
  lesson?: { titleAr?: string | null } | null;
};

type WeakPointLike = { topic?: string | null; severity?: number | null };

export type BuildPhase40SnapshotInput = {
  childId: string;
  childName?: string;
  xp?: number;
  streak?: number;
  progress: ProgressLike[];
  weakPoints: WeakPointLike[];
};

function clamp(value: number, min = 0, max = 100) {
  return Math.max(min, Math.min(max, Math.round(value)));
}

function getMasteryBand(score: number): MasteryBand {
  if (score >= 85) return "master";
  if (score >= 65) return "practice";
  if (score >= 40) return "review";
  return "discover";
}

function inferEmotion(input: BuildPhase40SnapshotInput, masteryScore: number): EmotionalSignal {
  const reviewCount = input.progress.filter((p) => p.status === "needs_review").length;
  const weakSeverity = input.weakPoints.reduce((sum, w) => sum + (w.severity ?? 1), 0);
  const streak = input.streak ?? 0;

  if (reviewCount >= 3 || weakSeverity >= 6) return "frustrated";
  if (masteryScore >= 80 && streak >= 3) return "confident";
  if (streak >= 2) return "excited";
  if (masteryScore < 45) return "hesitant";
  return "calm";
}

function chooseTutorState(emotion: EmotionalSignal, masteryScore: number): TutorState {
  if (emotion === "frustrated" || emotion === "hesitant") return "REINFORCE";
  if (masteryScore < 45) return "EXPLAIN";
  if (masteryScore < 75) return "QUESTION";
  return "ADAPT";
}

function buildMissions(input: BuildPhase40SnapshotInput, masteryBand: MasteryBand): LearningMission[] {
  const needsReview = input.progress.filter((p) => p.status === "needs_review").slice(0, 2);
  const weakTopics = input.weakPoints.slice(0, 2).map((w) => w.topic).filter(Boolean) as string[];
  const missions: LearningMission[] = [];

  if (needsReview.length > 0) {
    missions.push({
      id: "mission-review-first-gap",
      title: "مهمة إنقاذ الفهم",
      description: `راجع مع ليلى: ${needsReview[0]?.lesson?.titleAr ?? "درس يحتاج تثبيت"}`,
      xpReward: 35,
      estimatedMinutes: 8,
      type: "review",
    });
  }

  if (weakTopics.length > 0) {
    missions.push({
      id: "mission-weak-point-mini-quest",
      title: "تحدي نقطة الضعف",
      description: `تمرين قصير على: ${weakTopics[0]}`,
      xpReward: 45,
      estimatedMinutes: 10,
      type: "confidence",
    });
  }

  missions.push({
    id: "mission-daily-learning-star",
    title: masteryBand === "master" ? "افتح تحدي المتفوقين" : "نجمة اليوم التعليمية",
    description: masteryBand === "discover"
      ? "شرح صغير ثم سؤال واحد فقط حتى لا يشعر الطفل بالضغط."
      : "تعلّم قصير مع سؤال ذكي وتغذية راجعة من ليلى.",
    xpReward: masteryBand === "master" ? 60 : 30,
    estimatedMinutes: masteryBand === "discover" ? 6 : 12,
    type: masteryBand === "master" ? "quiz" : "lesson",
  });

  return missions.slice(0, 3);
}

function nextTeacherMove(state: TutorState, emotion: EmotionalSignal): string {
  if (emotion === "frustrated") return "ليلى تبدأ بتشجيع قصير ثم تعيد الشرح بمثال من الحياة اليومية المغربية.";
  if (emotion === "hesitant") return "ليلى تطرح سؤالًا صغيرًا جدًا وتمنح الطفل اختيارين لتقليل الخوف.";
  if (state === "ADAPT") return "ليلى ترفع الصعوبة تدريجيًا وتفتح تحديًا قصيرًا بمكافأة.";
  if (state === "QUESTION") return "ليلى تسأل سؤالًا واحدًا، تنتظر الإجابة، ثم تحدد نوع الخطأ قبل الشرح التالي.";
  return "ليلى تشرح في أقل من دقيقة ثم تنتقل مباشرة إلى تطبيق بسيط.";
}

export function buildPhase40LearningSnapshot(input: BuildPhase40SnapshotInput): Phase40LearningSnapshot {
  const completed = input.progress.filter((p) => p.status === "completed");
  const scored = input.progress.filter((p) => typeof p.score === "number");
  const averageScore = scored.length
    ? scored.reduce((sum, p) => sum + Number(p.score ?? 0), 0) / scored.length
    : 0;
  const completionSignal = input.progress.length ? (completed.length / input.progress.length) * 100 : 0;
  const weakPenalty = input.weakPoints.reduce((sum, w) => sum + (w.severity ?? 1), 0) * 4;

  const masteryScore = clamp((averageScore * 0.65) + (completionSignal * 0.35) - weakPenalty);
  const confidenceScore = clamp(masteryScore + ((input.streak ?? 0) * 3) - (input.weakPoints.length * 5));
  const masteryBand = getMasteryBand(masteryScore);
  const emotionalSignal = inferEmotion(input, masteryScore);
  const tutorState = chooseTutorState(emotionalSignal, masteryScore);

  return {
    childId: input.childId,
    masteryScore,
    confidenceScore,
    masteryBand,
    emotionalSignal,
    tutorState,
    nextTeacherMove: nextTeacherMove(tutorState, emotionalSignal),
    missions: buildMissions(input, masteryBand),
    parentInsight: confidenceScore < 50
      ? "الطفل يحتاج جلسات قصيرة جدًا مع تشجيع متكرر بدل ضغط أو تمارين كثيرة."
      : "المسار جيد؛ حافظ على عادة يومية قصيرة حتى تتراكم الثقة والفهم.",
    safetyNote: "Phase40 يقرأ المؤشرات الحالية فقط ولا يغيّر بيانات الطفل أو المصادقة أو البنية الحساسة.",
  };
}

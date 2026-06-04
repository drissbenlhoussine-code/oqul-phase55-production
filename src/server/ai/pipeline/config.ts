export type PipelineFlowId = "full" | "research" | "analysis" | "quick" | "lesson" | "edu";

export type AgentId =
  | "orchestrator"
  | "researcher"
  | "analyst"
  | "pedagogue"
  | "writer"
  | "checker"
  | "exercise_gen";

export const PIPELINE_FLOWS: Array<{
  id: PipelineFlowId;
  nameAr: string;
  descriptionAr: string;
  icon: string;
  agents: AgentId[];
  estimatedSeconds: number;
}> = [
  {
    id: "edu",
    nameAr: "بحث تعليمي",
    descriptionAr: "جميع الوكلاء — ملخص + شرح + تمارين + خطة مراجعة",
    icon: "🧠",
    agents: ["orchestrator", "researcher", "analyst", "pedagogue", "checker", "exercise_gen"],
    estimatedSeconds: 60,
  },
  {
    id: "full",
    nameAr: "بحث شامل",
    descriptionAr: "منسق + باحث + محلل + معلم تربوي + كاتب نهائي",
    icon: "🔭",
    agents: ["orchestrator", "researcher", "analyst", "pedagogue", "writer"],
    estimatedSeconds: 45,
  },
  {
    id: "lesson",
    nameAr: "تحويل إلى درس",
    descriptionAr: "يحوّل أي موضوع إلى درس مغربي واضح مع تمارين وأسئلة",
    icon: "📚",
    agents: ["orchestrator", "researcher", "pedagogue", "writer"],
    estimatedSeconds: 35,
  },
  {
    id: "research",
    nameAr: "بحث وملخص",
    descriptionAr: "بحث عميق ثم تلخيص منظم وسهل القراءة",
    icon: "🔍",
    agents: ["orchestrator", "researcher", "writer"],
    estimatedSeconds: 25,
  },
  {
    id: "analysis",
    nameAr: "تحليل عميق",
    descriptionAr: "تحليل أفكار، مشاكل، بيانات، أو قرارات تعليمية",
    icon: "📊",
    agents: ["orchestrator", "analyst", "writer"],
    estimatedSeconds: 25,
  },
  {
    id: "quick",
    nameAr: "إجابة فورية",
    descriptionAr: "رد سريع لكن منظم ومفيد",
    icon: "⚡",
    agents: ["orchestrator", "writer"],
    estimatedSeconds: 12,
  },
];

export const AGENTS: Record<AgentId, { nameAr: string; roleAr: string; icon: string; color: string }> = {
  orchestrator: {
    nameAr: "منظم الخطة",
    roleAr: "يفهم الطلب، يحدد الهدف، ويضع خطة العمل",
    icon: "⬡",
    color: "#6366f1",
  },
  researcher: {
    nameAr: "الباحث",
    roleAr: "يجمع المعطيات والمعرفة ويكشف النواقص",
    icon: "◎",
    color: "#3b82f6",
  },
  analyst: {
    nameAr: "المحلل",
    roleAr: "يرتب الأفكار ويستخرج الأسباب والحلول",
    icon: "◈",
    color: "#8b5cf6",
  },
  pedagogue: {
    nameAr: "الشارح",
    roleAr: "يحوّل المعرفة إلى شرح واضح مناسب للطالب المغربي",
    icon: "🌸",
    color: "#ec4899",
  },
  checker: {
    nameAr: "المدقق",
    roleAr: "يتحقق من دقة المعلومات وجودتها قبل إنتاج النتيجة",
    icon: "✓",
    color: "#f59e0b",
  },
  exercise_gen: {
    nameAr: "مولد التمارين",
    roleAr: "ينتج تمارين مقترحة وخطة مراجعة منظمة",
    icon: "📝",
    color: "#06b6d4",
  },
  writer: {
    nameAr: "الكاتب النهائي",
    roleAr: "ينتج جوابًا منظمًا وعمليًا باللغة المناسبة",
    icon: "◆",
    color: "#10b981",
  },
};

export function getPipelineAgents(flow: PipelineFlowId): AgentId[] {
  return PIPELINE_FLOWS.find((f) => f.id === flow)?.agents ?? ["orchestrator", "writer"];
}

export const PIPELINE_MODELS = [
  { id: "llama-3.3-70b-versatile", label: "جودة عالية" },
  { id: "llama-3.1-8b-instant", label: "سريع" },
] as const;

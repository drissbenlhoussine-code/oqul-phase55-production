export type LoadScenario = {
  name: string;
  target: string;
  virtualUsers: number;
  durationSeconds: number;
};

export const loadScenarios: LoadScenario[] = [
  {
    name: "AI streaming pressure",
    target: "/api/ai/leila",
    virtualUsers: 25,
    durationSeconds: 60,
  },
  {
    name: "Rate limit stress",
    target: "/api/ai/leila",
    virtualUsers: 100,
    durationSeconds: 30,
  },
  {
    name: "Learning dashboard read load",
    target: "/api/analytics/learning",
    virtualUsers: 50,
    durationSeconds: 60,
  },
];

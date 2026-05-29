export type TutorMessage = {
  id: string;
  role: "child" | "leila";
  content: string;
  status?: "sending" | "streaming" | "done" | "error";
  createdAt: string;
};

export function createChildMessage(content: string): TutorMessage {
  return {
    id: crypto.randomUUID(),
    role: "child",
    content,
    status: "done",
    createdAt: new Date().toISOString(),
  };
}

export function createStreamingLeilaMessage(): TutorMessage {
  return {
    id: crypto.randomUUID(),
    role: "leila",
    content: "",
    status: "streaming",
    createdAt: new Date().toISOString(),
  };
}

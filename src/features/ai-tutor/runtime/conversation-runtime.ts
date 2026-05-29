import type { TutorMessage } from "./message-runtime";

export function appendTutorMessage(messages: TutorMessage[], message: TutorMessage) {
  return [...messages, message];
}

export function replaceTutorMessage(
  messages: TutorMessage[],
  messageId: string,
  updater: (message: TutorMessage) => TutorMessage
) {
  return messages.map((message) =>
    message.id === messageId ? updater(message) : message
  );
}

export function clearConversation() {
  return [];
}

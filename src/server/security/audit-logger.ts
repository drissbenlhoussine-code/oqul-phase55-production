export type AuditEvent = {
  action: string;
  actorId?: string;
  target?: string;
  createdAt: string;
  metadata?: Record<string, unknown>;
};

export function logAuditEvent(event: AuditEvent) {
  console.log("[OQUL_AUDIT]", event);
}

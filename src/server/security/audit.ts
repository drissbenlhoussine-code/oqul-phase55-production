/**
 * Audit logger — records security-sensitive events.
 * Logs to console in dev, would send to observability platform in prod.
 */
export type AuditEvent =
  | "login_success" | "login_failure" | "register"
  | "auth_failed"   | "ownership_violation" | "quota_exceeded"
  | "ai_chat"       | "quiz_submit"         | "password_change";

export interface AuditLog {
  event:    AuditEvent;
  userId?:  string;
  childId?: string;
  ip?:      string;
  meta?:    Record<string, unknown>;
}

export async function audit(log: AuditLog) {
  const entry = {
    ...log,
    timestamp: new Date().toISOString(),
    env:       process.env.NODE_ENV,
  };

  // Always log to console (structured for log aggregators)
  console.info("[AUDIT]", JSON.stringify(entry));

  // In production: send to your observability platform
  // await fetch("https://your-logging-service/audit", { method: "POST", body: JSON.stringify(entry) });
}

/**
 * Email Service — Resend provider.
 *
 * Never logs secrets or reset tokens.
 */

export interface SendEmailOptions {
  to: string;
  subject: string;
  html: string;
}

export interface SendEmailResult {
  id: string | null;
}

export type EmailDeliveryErrorCode =
  | "EMAIL_CONFIG_MISSING"
  | "RESEND_INVALID_API_KEY"
  | "RESEND_SENDER_REJECTED"
  | "RESEND_RATE_LIMITED"
  | "RESEND_API_ERROR"
  | "EMAIL_NETWORK_ERROR";

export class EmailDeliveryError extends Error {
  readonly code: EmailDeliveryErrorCode;
  readonly status?: number;
  readonly details?: string;

  constructor(code: EmailDeliveryErrorCode, message: string, options: { status?: number; details?: string; cause?: unknown } = {}) {
    super(message);
    this.name = "EmailDeliveryError";
    this.code = code;
    this.status = options.status;
    this.details = options.details;
    this.cause = options.cause;
  }
}

export function getEmailConfigDiagnostics() {
  return {
    RESEND_API_KEY: process.env.RESEND_API_KEY ? "PRESENT" : "MISSING",
    NEXT_PUBLIC_APP_URL: process.env.NEXT_PUBLIC_APP_URL ? "PRESENT" : "MISSING",
    EMAIL_FROM: process.env.EMAIL_FROM ? "PRESENT" : "MISSING",
  } as const;
}

export function validateEmailConfig(): void {
  const diagnostics = getEmailConfigDiagnostics();
  const missing = Object.entries(diagnostics)
    .filter(([name, status]) => status === "MISSING" && name !== "EMAIL_FROM")
    .map(([name]) => name);

  if (missing.length === 0) return;

  const message = `[Email] Missing required env vars: ${missing.join(", ")}`;

  if (process.env.NODE_ENV === "production") {
    throw new EmailDeliveryError("EMAIL_CONFIG_MISSING", message);
  }

  console.warn(`[Email:dev] ${message}`);
}

function classifyResendError(status: number, body: string): EmailDeliveryErrorCode {
  const text = body.toLowerCase();

  if (status === 401 || text.includes("api key") || text.includes("unauthorized")) {
    return "RESEND_INVALID_API_KEY";
  }

  if (
    status === 403 ||
    text.includes("domain") ||
    text.includes("sender") ||
    text.includes("from")
  ) {
    return "RESEND_SENDER_REJECTED";
  }

  if (status === 429) return "RESEND_RATE_LIMITED";

  return "RESEND_API_ERROR";
}

function safeResendDetails(body: string): string {
  return body.replace(/re_[A-Za-z0-9_]+/g, "[REDACTED_RESEND_KEY]").slice(0, 800);
}

function appUrl() {
  validateEmailConfig();
  return process.env.NEXT_PUBLIC_APP_URL ?? "http://localhost:3000";
}

function baseTemplate(title: string, body: string): string {
  return `<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>${title}</title>
</head>
<body style="margin:0;padding:0;background:#F7F0E3;font-family:Arial,sans-serif;direction:rtl;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#F7F0E3;padding:40px 20px;">
    <tr><td align="center">
      <table width="560" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:20px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">
        <tr>
          <td style="background:linear-gradient(135deg,#1A1025,#2D1B4E);padding:32px;text-align:center;">
            <div style="display:inline-block;background:linear-gradient(135deg,#C4622D,#D4A843);border-radius:14px;width:52px;height:52px;line-height:52px;font-size:26px;margin-bottom:12px;">📚</div>
            <h1 style="color:#FDF8EE;margin:0;font-size:24px;font-weight:900;">Oqul</h1>
            <p style="color:rgba(255,255,255,0.6);margin:6px 0 0;font-size:13px;">تعلم مع أستاذة ليلى</p>
          </td>
        </tr>
        <tr>
          <td style="padding:36px 40px;">
            ${body}
          </td>
        </tr>
        <tr>
          <td style="background:#F8F5F0;padding:20px 40px;text-align:center;border-top:1px solid #EDE8DE;">
            <p style="color:#777;font-size:12px;margin:0;line-height:1.7;">
              هذه الرسالة أرسلت بواسطة Oqul — تعليم ذكي للأطفال المغاربة.<br/>
              إذا لم تطلب هذا، يمكنك تجاهل الرسالة بأمان.
            </p>
          </td>
        </tr>
      </table>
    </td></tr>
  </table>
</body>
</html>`;
}

async function send(opts: SendEmailOptions): Promise<SendEmailResult> {
  validateEmailConfig();

  const apiKey = process.env.RESEND_API_KEY;
  const from = process.env.EMAIL_FROM ?? "Oqul <no-reply@oqul.tech>";

  if (!apiKey) {
    console.info("[EMAIL:dev]", { to: opts.to, subject: opts.subject });
    console.info("[EMAIL:dev] HTML preview:\n", opts.html.replace(/<[^>]+>/g, "").slice(0, 400));
    return { id: null };
  }

  let response: Response;

  try {
    response = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ from, to: opts.to, subject: opts.subject, html: opts.html }),
    });
  } catch (error) {
    throw new EmailDeliveryError("EMAIL_NETWORK_ERROR", "Failed to reach Resend email API.", { cause: error });
  }

  if (!response.ok) {
    const body = await response.text();
    const code = classifyResendError(response.status, body);
    throw new EmailDeliveryError(code, `Resend email delivery failed with status ${response.status}.`, {
      status: response.status,
      details: safeResendDetails(body),
    });
  }

  const body = await response.text();
  if (!body.trim()) return { id: null };

  try {
    const json = JSON.parse(body) as { id?: unknown };
    return { id: typeof json.id === "string" ? json.id : null };
  } catch {
    return { id: null };
  }
}

export const emailService = {
  async sendVerification(opts: { to: string; name: string; token: string }) {
    const link = `${appUrl()}/api/auth/verify-email?token=${opts.token}`;

    return send({
      to: opts.to,
      subject: "تأكيد بريدك الإلكتروني — Oqul",
      html: baseTemplate("تأكيد البريد الإلكتروني", `
        <h2 style="color:#1A1025;font-size:22px;margin:0 0 12px;">مرحباً ${opts.name}</h2>
        <p style="color:#555;line-height:1.8;margin:0 0 24px;">
          شكراً لانضمامك إلى Oqul. اضغط على الزر أدناه لتأكيد بريدك الإلكتروني.
        </p>
        <div style="text-align:center;margin:32px 0;">
          <a href="${link}" style="background:#C4622D;color:#ffffff;text-decoration:none;padding:16px 36px;border-radius:14px;font-size:16px;font-weight:700;display:inline-block;">
            تأكيد البريد الإلكتروني
          </a>
        </div>
      `),
    });
  },

  async sendPasswordReset(opts: { to: string; name: string; token: string }) {
    const link = `${appUrl()}/reset-password?token=${opts.token}`;

    return send({
      to: opts.to,
      subject: "إعادة تعيين كلمة المرور — Oqul",
      html: baseTemplate("إعادة تعيين كلمة المرور", `
        <h2 style="color:#1A1025;font-size:22px;margin:0 0 12px;">إعادة تعيين كلمة المرور</h2>
        <p style="color:#555;line-height:1.8;margin:0 0 24px;">
          طلبت إعادة تعيين كلمة المرور لحسابك. اضغط على الزر أدناه لإنشاء كلمة مرور جديدة.
        </p>
        <div style="text-align:center;margin:32px 0;">
          <a href="${link}" style="background:#C4622D;color:#ffffff;text-decoration:none;padding:16px 36px;border-radius:14px;font-size:16px;font-weight:700;display:inline-block;">
            إعادة تعيين كلمة المرور
          </a>
        </div>
        <p style="color:#777;font-size:12px;text-align:center;margin:0;line-height:1.7;">
          الرابط صالح لمدة ساعة واحدة فقط. إذا لم تطلب هذا، تجاهل الرسالة.
        </p>
      `),
    });
  },
};

/**
 * Email Service — Resend provider
 * Phase 31: Launch Safety
 *
 * Uses Resend (resend.com) — simple, reliable, Arabic-friendly.
 * Falls back to console.log in development when RESEND_API_KEY is absent.
 */

export interface SendEmailOptions {
  to:      string;
  subject: string;
  html:    string;
}

async function send(opts: SendEmailOptions): Promise<void> {
  const apiKey = process.env.RESEND_API_KEY;
  const from   = process.env.EMAIL_FROM ?? "Oqul <no-reply@oqul.ma>";

  // Dev fallback — log instead of send
  if (!apiKey) {
    console.info("[EMAIL:dev]", { to: opts.to, subject: opts.subject });
    console.info("[EMAIL:dev] HTML preview:\n", opts.html.replace(/<[^>]+>/g, "").slice(0, 400));
    return;
  }

  const res = await fetch("https://api.resend.com/emails", {
    method:  "POST",
    headers: {
      "Authorization": `Bearer ${apiKey}`,
      "Content-Type":  "application/json",
    },
    body: JSON.stringify({ from, to: opts.to, subject: opts.subject, html: opts.html }),
  });

  if (!res.ok) {
    const body = await res.text();
    throw new Error(`[Email] Resend error ${res.status}: ${body}`);
  }
}

// ─── Templates ────────────────────────────────────────────────────────────────

const appUrl = () => process.env.NEXT_PUBLIC_APP_URL ?? "http://localhost:3000";

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
        <!-- Header -->
        <tr>
          <td style="background:linear-gradient(135deg,#1A1025,#2D1B4E);padding:32px;text-align:center;">
            <div style="display:inline-block;background:linear-gradient(135deg,#C4622D,#D4A843);border-radius:14px;width:52px;height:52px;line-height:52px;font-size:26px;margin-bottom:12px;">📚</div>
            <h1 style="color:#FDF8EE;margin:0;font-size:24px;font-weight:900;">Oqul</h1>
            <p style="color:rgba(255,255,255,0.6);margin:6px 0 0;font-size:13px;">تعلم مع أستاذة ليلى</p>
          </td>
        </tr>
        <!-- Body -->
        <tr>
          <td style="padding:36px 40px;">
            ${body}
          </td>
        </tr>
        <!-- Footer -->
        <tr>
          <td style="background:#F8F5F0;padding:20px 40px;text-align:center;border-top:1px solid #EDE8DE;">
            <p style="color:#999;font-size:12px;margin:0;">
              هذه الرسالة أُرسلت بواسطة Oqul — تعليم ذكي للأطفال المغاربة 🇲🇦<br/>
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

// ─── Public API ───────────────────────────────────────────────────────────────

export const emailService = {
  /**
   * Send email verification link after registration.
   */
  async sendVerification(opts: { to: string; name: string; token: string }) {
    const link = `${appUrl()}/api/auth/verify-email?token=${opts.token}`;

    await send({
      to:      opts.to,
      subject: "✅ تأكيد بريدك الإلكتروني — Oqul",
      html: baseTemplate("تأكيد البريد الإلكتروني", `
        <h2 style="color:#1A1025;font-size:22px;margin:0 0 12px;">مرحباً ${opts.name}! 👋</h2>
        <p style="color:#555;line-height:1.8;margin:0 0 24px;">
          شكراً لانضمامك إلى Oqul. اضغط على الزر أدناه لتأكيد بريدك الإلكتروني وبدء رحلتك التعليمية مع أستاذة ليلى.
        </p>
        <div style="text-align:center;margin:32px 0;">
          <a href="${link}" style="background:#C4622D;color:#ffffff;text-decoration:none;padding:16px 36px;border-radius:14px;font-size:16px;font-weight:700;display:inline-block;">
            تأكيد البريد الإلكتروني ✉️
          </a>
        </div>
        <p style="color:#999;font-size:12px;text-align:center;margin:0;">
          الرابط صالح لمدة 24 ساعة فقط.<br/>
          إذا لم تنشئ حساباً، تجاهل هذه الرسالة.
        </p>
      `),
    });
  },

  /**
   * Send password reset link.
   */
  async sendPasswordReset(opts: { to: string; name: string; token: string }) {
    const link = `${appUrl()}/reset-password?token=${opts.token}`;

    await send({
      to:      opts.to,
      subject: "🔑 إعادة تعيين كلمة المرور — Oqul",
      html: baseTemplate("إعادة تعيين كلمة المرور", `
        <h2 style="color:#1A1025;font-size:22px;margin:0 0 12px;">إعادة تعيين كلمة المرور</h2>
        <p style="color:#555;line-height:1.8;margin:0 0 24px;">
          طلبت إعادة تعيين كلمة المرور لحسابك (${opts.to}). اضغط على الزر أدناه لإنشاء كلمة مرور جديدة.
        </p>
        <div style="text-align:center;margin:32px 0;">
          <a href="${link}" style="background:#C4622D;color:#ffffff;text-decoration:none;padding:16px 36px;border-radius:14px;font-size:16px;font-weight:700;display:inline-block;">
            إعادة تعيين كلمة المرور 🔑
          </a>
        </div>
        <p style="color:#999;font-size:12px;text-align:center;margin:0;">
          الرابط صالح لمدة ساعة واحدة فقط.<br/>
          إذا لم تطلب هذا، تجاهل الرسالة — كلمة مرورك آمنة.
        </p>
      `),
    });
  },
};

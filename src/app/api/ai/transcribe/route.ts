/**
 * POST /api/ai/transcribe
 * Voice → Text using Groq Whisper large-v3
 * From v13, adapted to v35 auth patterns.
 *
 * Accepts: multipart/form-data with "audio" field (Blob/File)
 * Returns: { text: string }
 *
 * Limits: 25MB max, 30 calls/minute per user
 */
import { type NextRequest, NextResponse } from "next/server";
import Groq from "groq-sdk";
import { getSession }    from "@/server/auth/session";
import { aiChatLimiter } from "@/server/security/rate-limit";

export const runtime    = "nodejs";
export const maxDuration = 30;

export async function POST(request: NextRequest) {
  // Auth
  const session = await getSession();
  if (!session) {
    return NextResponse.json(
      { success: false, message: "غير مصرح — يجب تسجيل الدخول", code: "UNAUTHORIZED" },
      { status: 401 }
    );
  }

  // Rate limit: 30 transcriptions per minute
  const limit = await aiChatLimiter(`transcribe:${session.sub}`);
  if (!limit.allowed) {
    return NextResponse.json(
      { success: false, message: "طلبات كثيرة — انتظر دقيقة", code: "RATE_LIMITED" },
      { status: 429 }
    );
  }

  const apiKey = process.env.GROQ_API_KEY;
  if (!apiKey) {
    return NextResponse.json(
      { success: false, message: "خدمة الصوت غير متوفرة حالياً" },
      { status: 503 }
    );
  }

  try {
    const formData  = await request.formData();
    const audioFile = formData.get("audio") as File | null;

    if (!audioFile) {
      return NextResponse.json(
        { success: false, message: "لم يُرسل ملف صوتي" },
        { status: 400 }
      );
    }

    // 25MB limit (Groq Whisper max)
    if (audioFile.size > 25 * 1024 * 1024) {
      return NextResponse.json(
        { success: false, message: "الملف الصوتي كبير جداً (الحد 25MB)" },
        { status: 400 }
      );
    }

    const groq = new Groq({ apiKey });

    const transcription = await groq.audio.transcriptions.create({
      file:            audioFile,
      model:           "whisper-large-v3",
      language:        "ar",     // Arabic-first; Whisper auto-detects Darija
      response_format: "json",
    });

    return NextResponse.json({
      success: true,
      text:    transcription.text,
    });
  } catch (err) {
    console.error("[Transcribe]", err);
    return NextResponse.json(
      { success: false, message: "فشل تحويل الصوت — حاول مرة أخرى" },
      { status: 500 }
    );
  }
}

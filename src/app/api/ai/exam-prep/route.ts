/**
 * POST /api/ai/exam-prep
 *
 * Dedicated single-pass exam preparation endpoint.
 * Returns a topic-specific exam preparation plan as a streaming SSE response.
 *
 * Events: { event:"delta", delta:"..." } | { event:"end" } | { event:"error", message:"..." }
 */
import { NextResponse } from "next/server";
import Groq from "groq-sdk";
import { z } from "zod";
import { getSession } from "@/server/auth/session";
import { aiChatLimiter } from "@/server/security/rate-limit";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

const inputSchema = z.object({
  prompt: z.string().min(20, "الطلب قصير جداً").max(8000),
});

const EXAM_PREP_SYSTEM = `أنت أستاذ مغربي خبير في إعداد التلاميذ للفروض والامتحانات الرسمية: الفرض المحروس، الامتحان الموحد الإقليمي، الامتحان الموحد الجهوي، والامتحان الوطني للبكالوريا.

قواعد صارمة:
1. ابق داخل المادة والمحور والمستوى المذكور في طلب المستخدم فقط.
2. إذا كانت المادة هي اللغة العربية أو الفلسفة، فلا تولد معادلات رياضية.
3. إذا كان المحور حول الدوال، فاستعمل تمارين مرتبطة بالدوال فقط: مجال التعريف، الصور، السوابق، قراءة البيان، جدول التغيرات، النهايات، الاشتقاق أو التحليل المناسب للمستوى.
4. استعمل سياق المدرسة المغربية والفرض أو الامتحان الوطني أو البكالوريا عند الحاجة.
5. طابق مستوى الصعوبة المطلوب: إعدادي، جذع مشترك، أولى باك، ثانية باك، أو مستوى آخر يذكره المستخدم.
6. أدرج حلولاً كاملة ومفصلة لكل تمرين.
7. تجنب أي placeholders مثل: [أدخل الحل هنا] أو [نص التمرين].
8. لا تخترع قواعد امتحان غير موجودة، ولا تخرج عن المادة المختارة.

أنتج الخطة بالترتيب التالي:

## نقاط الضعف المحتملة
اذكر المفاهيم التي يخطئ فيها التلاميذ عادة في هذا المحور تحديداً، مع توضيح الخطأ الشائع وكيف يتجنبه الطالب.

## خطة مراجعة قصيرة
اقترح خطة عملية ومختصرة مقسمة إلى محاور فرعية أو أيام، مع ترتيب الأولويات حسب الوقت المتاح.

## نموذج فرض مصغر
أنشئ نموذج فرض مصغر من ثلاثة تمارين متدرجة من نفس المحور:
- التمرين 1: سهل، مع الحل الكامل.
- التمرين 2: متوسط، مع الحل الكامل.
- التمرين 3: متقدم، مع الحل الكامل.

## تمارين إضافية مع الحلول
اقترح تمرينين أو ثلاثة تمارين إضافية تحاكي أسلوب الفرض أو الامتحان الرسمي، مع حلول كاملة وخطوات واضحة.

## نصائح للفرض والامتحان
قدم نصائح حول إدارة الوقت، ترتيب الأجوبة، الأخطاء الشائعة، وما يجب مراجعته في آخر يوم قبل الامتحان.

## مستوى التوقعات
وضح ما المتوقع من طالب هذا المستوى في هذا المحور: المفاهيم الإلزامية، نوع الأسئلة، مستوى الصعوبة، وطريقة عرض الحل التي ينتظرها الأستاذ أو المصحح.`;

function hasMojibake(text: string): boolean {
  return ["Ø", "Ù", "Ã", "â", "�"].some((marker) => text.includes(marker));
}

function sse(data: Record<string, unknown>) {
  return new TextEncoder().encode(`data: ${JSON.stringify(data)}\n\n`);
}

export async function POST(request: Request) {
  const session = await getSession();
  if (!session) {
    return NextResponse.json({ success: false, message: "يجب تسجيل الدخول أولاً" }, { status: 401 });
  }

  const limit = await aiChatLimiter(`${session.sub}:exam-prep`);
  if (!limit.allowed) {
    return NextResponse.json(
      { success: false, message: "طلبات كثيرة. انتظر دقيقة ثم جرّب مرة أخرى." },
      { status: 429 },
    );
  }

  const parsed = inputSchema.safeParse(await request.json().catch(() => null));
  if (!parsed.success) {
    return NextResponse.json(
      { success: false, message: parsed.error.errors[0]?.message ?? "طلب غير صالح" },
      { status: 400 },
    );
  }

  const apiKey = process.env.GROQ_API_KEY;
  if (!apiKey) {
    return NextResponse.json(
      {
        success: false,
        message: "مفتاح GROQ_API_KEY غير موجود. تحقق من ملف .env.local أو إعدادات Vercel.",
      },
      { status: 503 },
    );
  }

  if (hasMojibake(EXAM_PREP_SYSTEM)) {
    console.error("[exam-prep] Mojibake detected in EXAM_PREP_SYSTEM");
    return NextResponse.json(
      { success: false, message: "خطأ داخلي في ترميز نص إعداد الامتحان." },
      { status: 500 },
    );
  }

  const { prompt } = parsed.data;
  const groq = new Groq({ apiKey });

  const stream = new ReadableStream<Uint8Array>({
    async start(controller) {
      try {
        const completion = await groq.chat.completions.create({
          model: "llama-3.3-70b-versatile",
          temperature: 0.6,
          max_tokens: 2500,
          stream: true,
          messages: [
            { role: "system", content: EXAM_PREP_SYSTEM },
            { role: "user", content: prompt },
          ],
        });

        for await (const chunk of completion) {
          const delta = chunk.choices[0]?.delta?.content ?? "";
          if (!delta) continue;
          controller.enqueue(sse({ event: "delta", delta }));
        }

        controller.enqueue(sse({ event: "end" }));
      } catch (error) {
        console.error("[exam-prep]", error);
        controller.enqueue(sse({
          event: "error",
          message: "حدث خطأ أثناء توليد خطة المراجعة. تحقق من إعدادات GROQ_API_KEY أو جرّب مرة أخرى.",
        }));
      } finally {
        controller.close();
      }
    },
  });

  return new Response(stream, {
    headers: {
      "Content-Type": "text/event-stream; charset=utf-8",
      "Cache-Control": "no-cache, no-transform",
      "Connection": "keep-alive",
      "X-Accel-Buffering": "no",
    },
  });
}

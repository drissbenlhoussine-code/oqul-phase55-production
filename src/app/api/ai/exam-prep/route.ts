/**
 * POST /api/ai/exam-prep
 *
 * Dedicated single-pass exam preparation endpoint.
 * Returns a topic-specific exam preparation plan as a streaming SSE response.
 *
 * Events: { event:"delta", delta:"..." } | { event:"end" } | { event:"error", message:"..." }
 */
import { NextResponse }          from "next/server";
import Groq                      from "groq-sdk";
import { z }                     from "zod";
import { getSession }            from "@/server/auth/session";
import { aiChatLimiter }         from "@/server/security/rate-limit";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

const inputSchema = z.object({
  prompt: z.string().min(20, "الطلب قصير جداً").max(8000),
});

const EXAM_PREP_SYSTEM = `أنت أستاذ مغربي خبير في إعداد الطلاب للامتحانات الرسمية (الفرض المحروس، الامتحان الموحد الإقليمي، الامتحان الموحد الجهوي، الباكالوريا).

**قواعد صارمة لا استثناء فيها:**
1. كل مثال وتمرين وسؤال يجب أن يرتبط حصرياً بالمادة والمحور المحدد في الطلب.
2. إذا كان المحور "الدوال العددية": لا تكتب معادلات منفصلة مثل "2x+3=5" — كل تمرين يجب أن يدور حول الدوال (مجال التعريف، الصور، السوابق، قراءة البيان، جدول التغيرات).
3. إذا كان المحور "الكسور": جميع التمارين تتعلق بالكسور فقط.
4. إذا كان المحور "اللغة العربية" أو "الفلسفة": أنتج تمارين لغوية أو فلسفية ملائمة، لا معادلات رياضية.
5. الأرقام والحسابات يجب أن تكون حقيقية وواضحة — لا نص إرشادي عام مثل "[أدخل الحل هنا]".
6. استخدم مستوى الصعوبة المناسب للمرحلة المحددة في الطلب (إعدادي، جذع مشترك، أولى باك، ثانية باك).

**أنتج بالترتيب الآتي حصرياً هذه الأقسام:**

## نقاط الضعف المحتملة
قائمة بالمفاهيم التي يخطئ فيها الطلاب عادةً في هذا المحور تحديداً. اذكر الخطأ الشائع وكيف يتجنبه الطالب.

## خطة مراجعة قصيرة
مقسمة على محاور فرعية أو أيام (3–5 أيام). عملية وقابلة للتطبيق. ركّز على الأولويات حسب الوقت المتاح.

## نموذج فرض مصغر
فرض محروس مصغر مكون من 3 تمارين متدرجة — جميعها من المحور المحدد:
- **التمرين 1 (سهل — 4 نقط):** [نص التمرين] | **الحل:** [حل كامل مفصّل]
- **التمرين 2 (متوسط — 6 نقط):** [نص التمرين] | **الحل:** [حل كامل مفصّل]
- **التمرين 3 (متقدم — 10 نقط):** [نص التمرين] | **الحل:** [حل كامل مفصّل]

## تمارين مقترحة إضافية مع الحلول
تمرينان أو ثلاثة تمارين إضافية تحاكي أسلوب الامتحان الرسمي، مع الحلول الكاملة.

## نصائح للفرض والامتحان
إدارة الوقت، ترتيب الأجوبة، الأخطاء الشائعة التي يجب تجنبها، ما يُنصح به في آخر يوم قبل الامتحان.

## مستوى التوقعات
ما الذي يُتوقع تحديداً من طالب هذا المستوى في هذا المحور: المفاهيم الإلزامية، نوع الأسئلة، مستوى الصعوبة في الامتحان الرسمي.`;

function sse(data: Record<string, unknown>) {
  return new TextEncoder().encode(`data: ${JSON.stringify(data)}\n\n`);
}

export async function POST(request: Request) {
  const session = await getSession();
  if (!session) {
    return NextResponse.json({ success: false, message: "يجب تسجيل الدخول أولًا" }, { status: 401 });
  }

  const limit = await aiChatLimiter(`${session.sub}:exam-prep`);
  if (!limit.allowed) {
    return NextResponse.json({ success: false, message: "طلبات كثيرة. انتظر دقيقة ثم جرّب مرة أخرى." }, { status: 429 });
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
      { success: false, message: "GROQ_API_KEY غير موجود — تحقق من إعدادات البيئة." },
      { status: 503 },
    );
  }

  const { prompt } = parsed.data;
  const groq = new Groq({ apiKey });

  const stream = new ReadableStream<Uint8Array>({
    async start(controller) {
      try {
        const completion = await groq.chat.completions.create({
          model:       "llama-3.3-70b-versatile",
          temperature: 0.6,
          max_tokens:  2500,
          stream:      true,
          messages: [
            { role: "system", content: EXAM_PREP_SYSTEM },
            { role: "user",   content: prompt },
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
          event:   "error",
          message: "حدث خطأ أثناء توليد الخطة. تحقق من إعدادات GROQ_API_KEY أو جرّب مرة أخرى.",
        }));
      } finally {
        controller.close();
      }
    },
  });

  return new Response(stream, {
    headers: {
      "Content-Type":    "text/event-stream; charset=utf-8",
      "Cache-Control":   "no-cache, no-transform",
      "Connection":      "keep-alive",
      "X-Accel-Buffering": "no",
    },
  });
}

import { NextResponse } from "next/server";
import Groq from "groq-sdk";
import { z } from "zod";
import { getSession } from "@/server/auth/session";
import { aiChatLimiter } from "@/server/security/rate-limit";
import { AGENT_PROMPTS, buildAgentContext } from "@/server/ai/pipeline/prompts";
import { getPipelineAgents } from "@/server/ai/pipeline/config";
import type { AgentId, PipelineFlowId } from "@/server/ai/pipeline/config";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

const inputSchema = z.object({
  input: z.string().min(3, "اكتب طلبًا أو سؤالًا واضحًا").max(5000),
  flow: z.enum(["full", "research", "analysis", "quick", "lesson", "edu"]).default("full"),
  model: z.string().min(3).default("llama-3.3-70b-versatile"),
});

function sse(data: Record<string, unknown>) {
  return new TextEncoder().encode(`data: ${JSON.stringify(data)}\n\n`);
}

export async function POST(request: Request) {
  const session = await getSession();
  if (!session) {
    return NextResponse.json({ success: false, message: "يجب تسجيل الدخول أولًا" }, { status: 401 });
  }

  const limit = await aiChatLimiter(`${session.sub}:pipeline`);
  if (!limit.allowed) {
    return NextResponse.json({ success: false, message: "طلبات كثيرة. انتظر دقيقة ثم جرّب مرة أخرى." }, { status: 429 });
  }

  const parsed = inputSchema.safeParse(await request.json().catch(() => null));
  if (!parsed.success) {
    return NextResponse.json({ success: false, message: parsed.error.errors[0]?.message ?? "طلب غير صالح" }, { status: 400 });
  }

  const apiKey = process.env.GROQ_API_KEY;
  if (!apiKey) {
    return NextResponse.json({ success: false, message: "GROQ_API_KEY غير موجود في البيئة" }, { status: 503 });
  }

  const { input, model } = parsed.data as { input: string; flow: PipelineFlowId | "edu"; model: string };
  const flow = parsed.data.flow === "edu" ? "lesson" : parsed.data.flow as PipelineFlowId;
  const agentIds = getPipelineAgents(flow);
  const groq = new Groq({ apiKey });

  const stream = new ReadableStream<Uint8Array>({
    async start(controller) {
      const runId = crypto.randomUUID();
      const startedAt = Date.now();
      const previousOutputs: Partial<Record<AgentId, string>> = {};

      controller.enqueue(sse({ event: "start", runId, flow, agents: agentIds }));

      try {
        for (const agentId of agentIds) {
          const agentStart = Date.now();
          controller.enqueue(sse({ event: "agent_start", agentId, agent_id: agentId, ts: agentStart }));

          const completion = await groq.chat.completions.create({
            model,
            temperature: agentId === "writer" ? 0.55 : 0.7,
            max_tokens: agentId === "writer" ? 1800 : 900,
            stream: true,
            messages: [
              { role: "system", content: AGENT_PROMPTS[agentId] },
              { role: "user", content: buildAgentContext(agentId, input, previousOutputs) },
            ],
          });

          let output = "";
          for await (const chunk of completion) {
            const delta = chunk.choices[0]?.delta?.content ?? "";
            if (!delta) continue;
            output += delta;
            controller.enqueue(sse({ event: "agent_delta", agentId, agent_id: agentId, delta }));
          }

          previousOutputs[agentId] = output;
          controller.enqueue(sse({
            event: "agent_done",
            agentId,
            agent_id: agentId,
            output,
            durationMs: Date.now() - agentStart,
            duration_ms: Date.now() - agentStart,
          }));
        }

        const finalAgent = agentIds[agentIds.length - 1];
        controller.enqueue(sse({
          event: "end",
          status: "done",
          totalMs: Date.now() - startedAt,
          finalOutput: previousOutputs[finalAgent] ?? "",
          final_output: previousOutputs[finalAgent] ?? "",
        }));
      } catch (error) {
        console.error("[Oqul Pipeline]", error);
        controller.enqueue(sse({ event: "error", message: "حدث خطأ أثناء تشغيل الوكلاء. تحقق من GROQ_API_KEY أو جرّب نموذجًا آخر." }));
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

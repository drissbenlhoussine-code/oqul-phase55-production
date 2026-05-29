import { NextRequest } from "next/server";
import { z } from "zod";
import { requireAuth } from "@/server/http/guards/auth-guard";
import { errorResponse, ok } from "@/server/http/response";
import { childrenRepo } from "@/server/repositories/children";

const createSchema = z.object({
  name: z.string().min(2, "الاسم يجب أن يكون حرفين على الأقل"),
  gradeId: z.string().uuid().optional(),
});

export async function GET() {
  try {
    const session = await requireAuth();
    const data = await childrenRepo.findByUser(session.sub);
    return ok(data);
  } catch (e) {
    return errorResponse(e);
  }
}

export async function POST(request: NextRequest) {
  try {
    const session = await requireAuth();
    const body = createSchema.parse(await request.json());
    const child = await childrenRepo.create({ userId: session.sub, ...body });
    return ok(child, 201);
  } catch (e) {
    return errorResponse(e);
  }
}

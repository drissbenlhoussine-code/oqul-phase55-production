import { NextResponse } from "next/server";
import { AppError } from "@/server/errors";
import { ZodError } from "zod";

export function ok<T>(data: T, status = 200) {
  return NextResponse.json({ success: true, data }, { status });
}

export function created<T>(data: T) {
  return ok(data, 201);
}

export function errorResponse(error: unknown) {
  if (error instanceof AppError) {
    return NextResponse.json(
      { success: false, message: error.message, code: error.code },
      { status: error.status }
    );
  }

  if (error instanceof ZodError) {
    const message = error.errors.map((e) => e.message).join(". ");
    return NextResponse.json({ success: false, message, code: "VALIDATION_ERROR" }, { status: 422 });
  }

  if (error instanceof Error && error.message === "UNAUTHORIZED") {
    return NextResponse.json({ success: false, message: "يجب تسجيل الدخول", code: "UNAUTHORIZED" }, { status: 401 });
  }

  if (error instanceof Error) {
    console.error("[API Error]", error.message, error.stack?.slice(0, 300));
  }

  return NextResponse.json(
    { success: false, message: "حدث خطأ داخلي، يرجى المحاولة مجدداً", code: "INTERNAL_ERROR" },
    { status: 500 }
  );
}

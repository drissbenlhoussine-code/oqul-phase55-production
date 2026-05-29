import { NextResponse, type NextRequest } from "next/server";
import { AppError } from "@/server/errors/app-error";
import { createRequestContext, type RequestContext } from "@/server/context/request-context";

export type RouteHandlerContext = {
  request: NextRequest;
  context: RequestContext;
};

export async function routeHandler<T>(
  callback: (ctx: RouteHandlerContext) => Promise<T>,
  request?: NextRequest
) {
  const safeRequest =
    request ??
    ({
      headers: new Headers(),
      nextUrl: new URL("http://localhost"),
    } as NextRequest);

  const context = createRequestContext(safeRequest);

  try {
    const result = await callback({ request: safeRequest, context });

    return NextResponse.json({
      success: true,
      data: result,
      requestId: context.requestId,
    });
  } catch (error) {
    if (error instanceof AppError) {
      return NextResponse.json(
        {
          success: false,
          error: error.message,
          code: error.code,
          requestId: context.requestId,
        },
        { status: error.statusCode }
      );
    }

    return NextResponse.json(
      {
        success: false,
        error: "internal_server_error",
        requestId: context.requestId,
      },
      { status: 500 }
    );
  }
}

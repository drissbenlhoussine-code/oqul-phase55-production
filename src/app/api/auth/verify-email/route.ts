/**
 * GET /api/auth/verify-email?token=...
 * Verifies email address via token sent after registration.
 */
import { type NextRequest, NextResponse } from "next/server";
import { usersEmailRepo } from "@/server/repositories/users-email-repo";
import { isExpired } from "@/server/auth/tokens";
import { audit } from "@/server/security/audit";

export async function GET(request: NextRequest) {
  const token = request.nextUrl.searchParams.get("token");

  if (!token || token.length !== 64) {
    return NextResponse.redirect(
      new URL("/login?error=invalid_token", request.url)
    );
  }

  try {
    const user = await usersEmailRepo.findByVerificationToken(token);

    if (!user) {
      return NextResponse.redirect(
        new URL("/login?error=invalid_token", request.url)
      );
    }

    if (user.emailVerified) {
      // Already verified — just redirect to login
      return NextResponse.redirect(new URL("/login?verified=1", request.url));
    }

    // Token sent more than 24 hours ago → expired
    if (isExpired(user.emailVerificationSentAt
      ? new Date(user.emailVerificationSentAt.getTime() + 24 * 60 * 60 * 1000)
      : null)) {
      return NextResponse.redirect(
        new URL("/login?error=token_expired", request.url)
      );
    }

    await usersEmailRepo.markEmailVerified(user.id);
    await audit({ event: "register", userId: user.id, meta: { action: "email_verified" } });

    return NextResponse.redirect(new URL("/login?verified=1", request.url));
  } catch (err) {
    console.error("[verify-email]", err);
    return NextResponse.redirect(
      new URL("/login?error=server_error", request.url)
    );
  }
}

import { signToken } from "@/server/auth/jwt";

export class AuthService {
  async generateSession(userId: string, role: string, extra?: { email?: string; plan?: string }) {
    return signToken({
      sub: userId,
      email: extra?.email ?? "",
      role,
      plan: extra?.plan ?? "free",
    });
  }
}

export const authService = new AuthService();

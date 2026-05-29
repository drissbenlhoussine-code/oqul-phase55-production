import { describe, it, expect } from "vitest";
import { signToken, verifyToken, signAccessToken } from "@/server/auth/jwt";

describe("JWT Auth", () => {
  const payload = { sub: "user-123", email: "test@oqul.ma", role: "user", plan: "free" };

  it("signToken creates a valid 3-part JWT", async () => {
    const token = await signToken(payload);
    expect(token.split(".")).toHaveLength(3);
  });

  it("signAccessToken is an alias for signToken", () => {
    expect(signAccessToken).toBe(signToken);
  });

  it("verifyToken decodes all fields correctly", async () => {
    const token = await signToken(payload);
    const decoded = await verifyToken(token);
    expect(decoded.sub).toBe("user-123");
    expect(decoded.email).toBe("test@oqul.ma");
    expect(decoded.role).toBe("user");
    expect(decoded.plan).toBe("free");
  });

  it("verifyToken throws on garbage string", async () => {
    await expect(verifyToken("not.a.token")).rejects.toThrow();
  });

  it("verifyToken throws on tampered signature", async () => {
    const token = await signToken(payload);
    const [h, p] = token.split(".");
    await expect(verifyToken(`${h}.${p}.INVALIDSIG`)).rejects.toThrow();
  });

  it("verifyToken throws on token with wrong secret", async () => {
    // Simulate a token signed with a different secret
    const { SignJWT } = await import("jose");
    const fakeKey = new TextEncoder().encode("a-completely-different-secret-!!!!");
    const fakeToken = await new SignJWT({ sub: "hacker" })
      .setProtectedHeader({ alg: "HS256" })
      .setExpirationTime("1h")
      .sign(fakeKey);
    await expect(verifyToken(fakeToken)).rejects.toThrow();
  });
});

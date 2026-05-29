import { describe, it, expect } from "vitest";
import { AppError, Errors } from "@/server/errors";

describe("AppError", () => {
  it("Errors.unauthorized() returns 401", () => {
    const e = Errors.unauthorized();
    expect(e.status).toBe(401);
    expect(e.code).toBe("UNAUTHORIZED");
  });

  it("Errors.forbidden() returns 403", () => {
    expect(Errors.forbidden().status).toBe(403);
  });

  it("Errors.notFound() returns 404 with resource name", () => {
    const e = Errors.notFound("الدرس");
    expect(e.status).toBe(404);
    expect(e.message).toContain("الدرس");
  });

  it("Errors.quota() returns 429", () => {
    expect(Errors.quota().status).toBe(429);
    expect(Errors.quota().code).toBe("QUOTA_EXCEEDED");
  });

  it("statusCode getter matches status", () => {
    const e = new AppError("test", "FORBIDDEN", 403);
    expect(e.statusCode).toBe(e.status);
  });

  it("AppError is instanceof Error", () => {
    expect(new AppError("x", "NOT_FOUND", 404) instanceof Error).toBe(true);
  });
});

import { describe, it, expect } from "vitest";
import { AppError } from "@/server/errors";

// Test the ownership logic in isolation (no DB needed)
async function mockAssertOwnsChild(
  ownedIds: string[],
  requestedId: string
) {
  const found = ownedIds.find((id) => id === requestedId);
  if (!found) {
    throw new AppError("ليس لديك صلاحية الوصول لهذا الطفل", "FORBIDDEN", 403);
  }
  return { id: found };
}

describe("Child Ownership Guard", () => {
  const userId = "user-abc";
  const myChildren = ["child-111", "child-222"];
  const strangerChild = "child-999";

  it("allows access to own child", async () => {
    const result = await mockAssertOwnsChild(myChildren, "child-111");
    expect(result.id).toBe("child-111");
  });

  it("allows access to second child", async () => {
    const result = await mockAssertOwnsChild(myChildren, "child-222");
    expect(result.id).toBe("child-222");
  });

  it("throws FORBIDDEN for stranger's child", async () => {
    await expect(mockAssertOwnsChild(myChildren, strangerChild))
      .rejects.toMatchObject({ code: "FORBIDDEN", status: 403 });
  });

  it("throws FORBIDDEN when user has no children", async () => {
    await expect(mockAssertOwnsChild([], "child-111"))
      .rejects.toMatchObject({ code: "FORBIDDEN" });
  });

  it("throws FORBIDDEN for empty childId", async () => {
    await expect(mockAssertOwnsChild(myChildren, ""))
      .rejects.toMatchObject({ code: "FORBIDDEN" });
  });
});

describe("AppError structure", () => {
  it("has correct message, code, and status", () => {
    const err = new AppError("test error", "NOT_FOUND", 404);
    expect(err.message).toBe("test error");
    expect(err.code).toBe("NOT_FOUND");
    expect(err.status).toBe(404);
    expect(err.statusCode).toBe(404); // backward-compat getter
  });

  it("is instanceof Error", () => {
    const err = new AppError("test", "INTERNAL_ERROR", 500);
    expect(err instanceof Error).toBe(true);
  });
});

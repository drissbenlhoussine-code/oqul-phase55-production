import { describe, expect, it } from "vitest";
import { getPrimaryLessons, primarySubjects } from "@/server/primary-school/curriculum";
import { buildPhase46PrimaryProfile } from "@/server/primary-school/phase46-engine";

describe("Phase46 primary school layer", () => {
  it("covers six subjects for all primary grades", () => {
    for (const grade of ["1AP", "2AP", "3AP", "4AP", "5AP", "6AP"] as const) {
      expect(getPrimaryLessons(grade).length).toBeGreaterThanOrEqual(48);
    }
    expect(primarySubjects.length).toBe(6);
  });

  it("builds a child-first tutoring profile", () => {
    const profile = buildPhase46PrimaryProfile({ childId: "child-1", gradeLevel: "3AP", message: "شرح بالدارجة" });
    expect(profile.uxMode).toBe("primary_child_first");
    expect(profile.targetLanguage).toBe("darija");
    expect(profile.suggestedMicroLesson.length).toBeGreaterThan(3);
  });
});

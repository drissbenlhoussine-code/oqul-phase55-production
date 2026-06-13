import { describe, expect, it } from "vitest";
import { buildStudentKnowledgeProfile } from "@/server/adaptive/student-knowledge-model";

function progress(lessonTitle: string, status: string, score?: number, updatedAt = "2026-06-10T10:00:00Z") {
  return {
    lessonId: lessonTitle.toLowerCase().replace(/\s+/g, "-"),
    status,
    score,
    updatedAt,
    lesson: { titleAr: lessonTitle },
  };
}

function quiz(lessonTitle: string, score: number) {
  return {
    lessonId: lessonTitle.toLowerCase().replace(/\s+/g, "-"),
    score,
    lesson: { titleAr: lessonTitle },
  };
}

function weakPoint(topic: string, severity = 2) {
  return { topic, severity };
}

describe("student knowledge model", () => {
  it("returns low confidence safely for empty data", () => {
    const profile = buildStudentKnowledgeProfile({
      childId: "child-1",
      lessonProgress: [],
      quizAttempts: [],
      weakPoints: [],
      learningProfile: null,
    });

    expect(profile.childId).toBe("child-1");
    expect(profile.readinessScore).toBeLessThan(45);
    expect(profile.confidenceLevel).toBe("low");
    expect(profile.riskLevel).toBe("high");
    expect(profile.evidence).toEqual({
      completedLessons: 0,
      quizAttempts: 0,
      weakPoints: 0,
      averageScore: null,
    });
  });

  it("produces high readiness for completed lessons and high quiz scores", () => {
    const profile = buildStudentKnowledgeProfile({
      childId: "child-2",
      lessonProgress: [
        progress("Numbers to 100", "completed", 95),
        progress("Addition", "completed", 90),
        progress("Subtraction", "completed", 88),
      ],
      quizAttempts: [
        quiz("Numbers to 100", 95),
        quiz("Addition", 92),
        quiz("Subtraction", 90),
      ],
      weakPoints: [],
      learningProfile: { confidenceScore: "80" },
    });

    expect(profile.readinessScore).toBeGreaterThanOrEqual(75);
    expect(profile.confidenceLevel).toBe("high");
    expect(profile.riskLevel).toBe("low");
    expect(profile.masteredConcepts).toContain("Numbers to 100");
    expect(profile.nextBestActions).toContain("Try challenge or exam-style exercises");
  });

  it("reduces readiness and recommends review when weak points exist", () => {
    const profile = buildStudentKnowledgeProfile({
      childId: "child-3",
      lessonProgress: [progress("Data tables", "completed", 90), progress("Counting objects", "completed", 88)],
      quizAttempts: [quiz("Data tables", 90)],
      weakPoints: [weakPoint("Reading simple tables", 3), weakPoint("Comparing more and less", 3)],
    });

    expect(profile.readinessScore).toBeLessThan(70);
    expect(profile.riskLevel).toBe("high");
    expect(profile.weaknesses).toContain("Reading simple tables");
    expect(profile.recommendedReview).toContain("Comparing more and less");
    expect(profile.nextBestActions[0]).toContain("Review:");
  });

  it("creates easier-practice recommendations for low quiz scores", () => {
    const profile = buildStudentKnowledgeProfile({
      childId: "child-4",
      lessonProgress: [progress("Simple addition", "completed", 45)],
      quizAttempts: [quiz("Simple addition", 40), quiz("Simple subtraction", 55)],
      weakPoints: [],
    });

    expect(profile.confidenceLevel).toBe("low");
    expect(profile.strugglingConcepts).toContain("Simple addition");
    expect(profile.nextBestActions).toContain("Practice easier exercises before moving forward");
  });

  it("does not mutate input arrays or records", () => {
    const input = {
      childId: "child-5",
      lessonProgress: [progress("Shapes", "completed", 85)],
      quizAttempts: [quiz("Shapes", 85)],
      weakPoints: [weakPoint("Triangles", 1)],
      learningProfile: { confidenceScore: 60 },
    };
    const before = JSON.stringify(input);

    buildStudentKnowledgeProfile(input);

    expect(JSON.stringify(input)).toBe(before);
  });

  it("applies risk level thresholds", () => {
    const lowRisk = buildStudentKnowledgeProfile({
      childId: "child-6",
      lessonProgress: [
        progress("Measurement", "completed", 95),
        progress("Length", "completed", 90),
        progress("Mass", "completed", 90),
      ],
      quizAttempts: [quiz("Measurement", 92), quiz("Length", 88)],
      weakPoints: [],
    });
    const mediumRisk = buildStudentKnowledgeProfile({
      childId: "child-7",
      lessonProgress: [progress("Measurement", "completed", 80)],
      quizAttempts: [quiz("Measurement", 70)],
      weakPoints: [weakPoint("Length units", 1), weakPoint("Mass units", 1)],
    });
    const highRisk = buildStudentKnowledgeProfile({
      childId: "child-8",
      lessonProgress: [progress("Measurement", "needs_review", 35)],
      quizAttempts: [quiz("Measurement", 35)],
      weakPoints: [weakPoint("Length units", 3), weakPoint("Mass units", 3)],
    });

    expect(lowRisk.riskLevel).toBe("low");
    expect(mediumRisk.riskLevel).toBe("medium");
    expect(highRisk.riskLevel).toBe("high");
  });
});

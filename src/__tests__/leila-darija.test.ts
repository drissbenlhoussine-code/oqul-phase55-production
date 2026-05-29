/**
 * Leila Darija Quality tests
 * Tests that the Moroccan personality is authentically configured.
 */
import { describe, it, expect } from "vitest";
import { buildLeilaSystemPrompt } from "@/server/ai/leila";

describe("Leila Persona Architecture", () => {
  it("includes Moroccan Darija few-shot examples", () => {
    const prompt = buildLeilaSystemPrompt({ childName: "يوسف", gradeLevel: 1 });
    expect(prompt).toContain("واخا");    // Moroccan "okay/fine"
    expect(prompt).toContain("نشرحوها"); // "let's explain it"
    expect(prompt).toContain("هيا");     // "come on"
  });

  it("uses primary persona for grade 1-6", () => {
    const prompt = buildLeilaSystemPrompt({ childName: "فاطمة", gradeLevel: 3 });
    expect(prompt).toContain("6");   // age range mentioned
    expect(prompt).toContain("أصابع"); // fingers example for young children
  });

  it("uses middle persona for grade 7-9", () => {
    const prompt = buildLeilaSystemPrompt({ childName: "أمين", gradeLevel: 8 });
    expect(prompt).toContain("إعدادي");
    expect(prompt).toContain("واش تقدر"); // challenge phrasing for middle school
  });

  it("uses high school persona for grade 10-12", () => {
    const prompt = buildLeilaSystemPrompt({ childName: "سلمى", gradeLevel: 11 });
    expect(prompt).toContain("ثانوي");
    expect(prompt).toContain("باك"); // reference to Bac exam
  });

  it("includes child name in prompt", () => {
    const prompt = buildLeilaSystemPrompt({ childName: "محمد", gradeLevel: 5 });
    expect(prompt).toContain("محمد");
  });

  it("adapts language for young learners (grade 1-3)", () => {
    const prompt = buildLeilaSystemPrompt({ childName: "ريم", gradeLevel: 2 });
    expect(prompt).toContain("3-5 كلمات");
  });

  it("includes weak points when provided", () => {
    const prompt = buildLeilaSystemPrompt({
      childName: "علي", gradeLevel: 4,
      weakPoints: ["الكسور", "الجمع"],
    });
    expect(prompt).toContain("الكسور");
  });

  it("includes lesson content when provided", () => {
    const prompt = buildLeilaSystemPrompt({
      childName: "نور", gradeLevel: 1,
      lessonTitle: "حرف الألف",
      lessonContent: "الألف هو أول الحروف",
    });
    expect(prompt).toContain("حرف الألف");
    expect(prompt).toContain("الألف هو أول الحروف");
  });

  it("adapts mood for frustrated students", () => {
    const prompt = buildLeilaSystemPrompt({
      childName: "كريم", gradeLevel: 6,
      mood: "frustrated",
    });
    expect(prompt).toContain("محبط");
    expect(prompt).toContain("حناناً");
  });
});

describe("Darija Vocabulary Coverage", () => {
  const prompt = buildLeilaSystemPrompt({ childName: "x", gradeLevel: 3 });

  const darijaWords = ["مزيان", "برافو", "واخا", "هيا", "شوف", "واش"];

  for (const word of darijaWords) {
    it(`includes Darija word: "${word}"`, () => {
      expect(prompt).toContain(word);
    });
  }

  it("explicitly bans formal Arabic openers", () => {
    // The prompt should instruct NOT to start with formal Arabic
    expect(prompt).toContain("ابدئي");
    expect(prompt).toContain("دارجة");
  });
});

import grade1 from "./grade1-school-companion.json";
import grade2 from "./grade2-school-companion.json";
import grade3 from "./grade3-school-companion.json";
import grade4 from "./grade4-school-companion.json";
import grade5 from "./grade5-school-companion.json";
import grade6 from "./grade6-school-companion.json";

export const moroccoSchoolCompanionCurriculum = {
  country: "Morocco",
  strategy: "Prepare before school, revise after school.",
  alignment: "Moroccan primary school companion draft for teacher review.",
  grades: {
    1: grade1,
    2: grade2,
    3: grade3,
    4: grade4,
    5: grade5,
    6: grade6,
  },
};

export type MoroccoCompanionGrade = keyof typeof moroccoSchoolCompanionCurriculum.grades;

export function getMoroccoCompanionGrade(grade: MoroccoCompanionGrade) {
  return moroccoSchoolCompanionCurriculum.grades[grade];
}

export function listMoroccoCompanionGrades() {
  return Object.values(moroccoSchoolCompanionCurriculum.grades);
}

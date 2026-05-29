import { curriculumRepo } from "@/server/repositories/curriculum";
import { OnboardingWizard } from "@/features/onboarding/onboarding-wizard";

export default async function OnboardingPage() {
  const grades = await curriculumRepo.getGrades();
  return <OnboardingWizard grades={grades} />;
}

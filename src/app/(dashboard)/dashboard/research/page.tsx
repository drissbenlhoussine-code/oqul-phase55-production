/**
 * /dashboard/research — Research page
 * Path: src/app/(dashboard)/dashboard/research/page.tsx
 */
import { ResearchPage } from "@/features/research/research-page";

export const metadata = {
  title: "البحث الذكي — عقول",
  description: "نظام بحث متعدد الوكلاء",
};

export default function ResearchDashboardPage() {
  return <ResearchPage />;
}

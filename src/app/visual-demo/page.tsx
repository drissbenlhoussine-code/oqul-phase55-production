import { notFound } from "next/navigation";

import { OqulVisualSystem } from "@/components/experience/oqul-visual-system";

function OriginalPage() {
  return <OqulVisualSystem />;
}


export default function Page() {
  if (process.env.NODE_ENV === "production") notFound();
  return <OriginalPage />;
}

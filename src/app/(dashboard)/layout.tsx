"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Sidebar, type GradeLevel } from "@/components/layout/sidebar";
import { Header } from "@/components/layout/header";

interface Child { id: string; name: string; xp: number; grade?: { slug?: string } }

// ── Grade slug → level ─────────────────────────────────────────────────────────

function detectGradeLevel(slug: string | undefined): GradeLevel {
  if (!slug) return "unknown";
  const s = slug.toLowerCase().trim();

  // Primary: ap, 1ap–6ap, ap1–ap6
  if (s === "ap" || s.startsWith("ap") || /^\dap/.test(s)) return "primary";

  // Middle school: 1ac–3ac, ac, college, collège, middle, اعدادي, الإعدادي
  if (
    s === "ac" || /^\dac/.test(s) || s.startsWith("ac") ||
    s.includes("college") || s.includes("collège") ||
    s.includes("middle") ||
    s.includes("اعدادي") || s.includes("الإعدادي")
  ) return "middle";

  // Secondary: tc, common-core, trunk-common, 1bac, 2bac, lycee, lycée, secondary, ثانوي, الجذع
  if (
    s === "tc" || s.startsWith("tc") ||
    s.includes("common-core") || s.includes("trunk-common") ||
    s.includes("bac") ||
    s.includes("lycee") || s.includes("lycée") ||
    s.includes("secondary") ||
    s.includes("ثانوي") || s.includes("الجذع")
  ) return "secondary";

  return "unknown";
}

// ── Layout ─────────────────────────────────────────────────────────────────────

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const [activeChild, setActiveChild] = useState<Child | null>(null);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [isAdmin,     setIsAdmin]     = useState(false);
  const [gradeLevel,  setGradeLevel]  = useState<GradeLevel>("unknown");

  useEffect(() => {
    fetch("/api/children")
      .then((r) => r.json())
      .then((d) => {
        if (d.success && d.data?.length) {
          const child = d.data[0] as Child;
          setActiveChild(child);
          setGradeLevel(detectGradeLevel(child.grade?.slug));
        }
      })
      .catch(() => {});
    fetch("/api/me")
      .then((r) => r.json())
      .then((d) => { if (d.success && d.data?.role === "admin") setIsAdmin(true); })
      .catch(() => {});
  }, []);

  async function handleLogout() {
    await fetch("/api/auth/logout", { method: "POST" });
    router.push("/login");
    router.refresh();
  }

  return (
    <div className="flex h-screen overflow-hidden bg-background">
      <Sidebar
        onLogout={handleLogout}
        isOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
        isAdmin={isAdmin}
        gradeLevel={gradeLevel}
      />
      <div className="flex flex-col flex-1 overflow-hidden min-w-0">
        <Header
          childName={activeChild?.name}
          xp={activeChild?.xp}
          onMenuToggle={() => setSidebarOpen((o) => !o)}
        />
        <main className="flex-1 overflow-y-auto p-4 md:p-6">
          {children}
        </main>
      </div>
    </div>
  );
}

"use client";
/**
 * DashboardLayout — Phase 34 Fix
 * Path: src/app/(dashboard)/layout.tsx
 *
 * Fix: sidebarOpen state was not wired to Sidebar and Header.
 * The mobile hamburger button did nothing.
 * Now passes isOpen/onClose to Sidebar and onMenuToggle to Header.
 *
 * All other logic (child fetch, handleLogout) unchanged.
 */
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Sidebar } from "@/components/layout/sidebar";
import { Header }  from "@/components/layout/header";

interface Child { id: string; name: string; xp: number; grade?: { slug?: string } }

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const [activeChild,  setActiveChild]  = useState<Child | null>(null);
  const [sidebarOpen,  setSidebarOpen]  = useState(false);
  const [isAdmin,      setIsAdmin]      = useState(false);
  const [isPrimary,    setIsPrimary]    = useState(false);

  useEffect(() => {
    fetch("/api/children")
      .then((r) => r.json())
      .then((d) => {
        if (d.success && d.data?.length) {
          const child = d.data[0] as Child;
          setActiveChild(child);
          // Primary school: grade slugs ap1–ap6
          setIsPrimary(Boolean(child.grade?.slug?.startsWith("ap")));
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
        isPrimary={isPrimary}
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

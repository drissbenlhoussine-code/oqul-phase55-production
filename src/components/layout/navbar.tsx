"use client";
/**
 * Navbar — Phase 34 Fix
 * Path: src/components/layout/navbar.tsx
 *
 * Fix: "تسجيل الدخول" and "ابدأ مجاناً" buttons had no href/Link.
 * Clicking them did nothing. Now they navigate to /login and /register.
 *
 * Also fixed: Logo was <a href="#"> — now navigates to "/" properly.
 * All styling unchanged.
 */
import Link from "next/link";
import { Brain } from "lucide-react";
import { Button } from "@/components/ui/button";

export function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-border/70 bg-background/85 backdrop-blur-2xl">
      <div className="container flex h-20 items-center justify-between gap-4">

        {/* Logo → home */}
        <Link href="/" className="flex items-center gap-3" aria-label="عقول">
          <span className="grid h-12 w-12 place-items-center rounded-2xl bg-primary text-primary-foreground shadow-sm">
            <Brain className="h-7 w-7" />
          </span>
          <span className="text-3xl font-black tracking-tight">عقول</span>
        </Link>

        {/* Desktop nav */}
        <nav className="hidden items-center gap-8 text-sm font-bold text-muted-foreground md:flex">
          <a href="#features"      className="transition hover:text-foreground">المزايا</a>
          <a href="#how"           className="transition hover:text-foreground">كيف يعمل</a>
          <a href="#testimonials"  className="transition hover:text-foreground">آراء الطلاب</a>
          <a href="#pricing"       className="transition hover:text-foreground">الأسعار</a>
        </nav>

        {/* CTA buttons — FIXED: now use Link for real navigation */}
        <div className="flex items-center gap-3">
          <Link href="/login" className="hidden md:inline-flex">
            <Button variant="ghost">تسجيل الدخول</Button>
          </Link>
          <Link href="/register">
            <Button>ابدأ مجانًا</Button>
          </Link>
        </div>

      </div>
    </header>
  );
}

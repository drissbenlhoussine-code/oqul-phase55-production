"use client";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { ParentDashboard } from "@/features/parent/parent-dashboard";

export default function ParentPage() {
  return (
    <div className="min-h-screen bg-background p-6">
      <div className="max-w-4xl mx-auto">
        <div className="flex items-center gap-2 mb-6">
          <Link href="/dashboard" className="p-2 rounded-xl hover:bg-secondary transition-colors">
            <ArrowRight className="w-5 h-5" />
          </Link>
          <span className="text-sm text-muted-foreground">/ لوحة الأهل</span>
        </div>
        <ParentDashboard />
      </div>
    </div>
  );
}

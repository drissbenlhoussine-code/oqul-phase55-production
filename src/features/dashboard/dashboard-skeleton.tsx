/**
 * DashboardSkeleton — Phase 32
 * New file: src/features/dashboard/dashboard-skeleton.tsx
 *
 * Shows on first dashboard load instead of a spinning wheel.
 * Matches the exact layout of StudentDashboard sections.
 */
import { Skeleton } from "@/components/ui/skeleton";

function SkeletonCard({ className = "" }: { className?: string }) {
  return (
    <div className={`rounded-2xl border bg-card p-5 ${className}`}>
      <Skeleton className="h-4 w-1/3 mb-3" />
      <Skeleton className="h-3 w-full mb-2" />
      <Skeleton className="h-3 w-4/5" />
    </div>
  );
}

export function DashboardSkeleton() {
  return (
    <div className="max-w-3xl mx-auto space-y-4 animate-pulse" aria-label="جار التحميل...">
      {/* Leila card */}
      <div className="rounded-2xl border bg-gradient-to-r from-primary/10 to-emerald-50 p-5 flex items-center gap-4">
        <Skeleton className="h-14 w-14 rounded-full shrink-0" />
        <div className="flex-1 space-y-2">
          <Skeleton className="h-4 w-1/4" />
          <Skeleton className="h-3 w-3/4" />
        </div>
      </div>

      {/* Greeting + XP bar */}
      <div className="rounded-2xl border bg-card p-5 space-y-3">
        <div className="flex items-center gap-3">
          <Skeleton className="h-10 w-10 rounded-xl" />
          <div className="flex-1 space-y-1.5">
            <Skeleton className="h-4 w-1/3" />
            <Skeleton className="h-2 w-full rounded-full" />
          </div>
        </div>
      </div>

      {/* Daily loop */}
      <SkeletonCard />

      {/* Quick action grid */}
      <div className="grid grid-cols-3 gap-3">
        {[1, 2, 3].map((i) => (
          <div key={i} className="rounded-2xl border bg-card p-4 flex flex-col items-center gap-2">
            <Skeleton className="h-10 w-10 rounded-xl" />
            <Skeleton className="h-3 w-12" />
            <Skeleton className="h-2 w-16" />
          </div>
        ))}
      </div>

      {/* Recommendations */}
      <div className="space-y-2">
        <Skeleton className="h-4 w-32" />
        {[1, 2].map((i) => (
          <div key={i} className="rounded-2xl border bg-card p-4 flex items-center gap-3">
            <Skeleton className="h-9 w-9 rounded-xl shrink-0" />
            <div className="flex-1 space-y-1.5">
              <Skeleton className="h-3 w-1/2" />
              <Skeleton className="h-2 w-3/4" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

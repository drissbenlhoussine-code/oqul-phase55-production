"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/cn";
import {
  LayoutDashboard, BookOpen, MessageCircle, BarChart3,
  Settings, LogOut, Star, Users, Sparkles, X, Brain, FlaskConical,
  Activity, Wand2, Layers, ClipboardCheck, GitBranch, AlignLeft,
  TrendingUp, Zap, GraduationCap, BookMarked,
} from "lucide-react";

// ── Nav types ──────────────────────────────────────────────────────────────────

type NavItem    = { href: string; icon: React.ElementType; label: string };
type NavSection = { title: string; items: NavItem[] };

export type GradeLevel = "primary" | "middle" | "secondary" | "unknown";

// ── Base learning section (all authenticated users) ────────────────────────────

const learnSection: NavSection = {
  title: "التعلم",
  items: [
    { href: "/dashboard",          icon: LayoutDashboard, label: "الرئيسية" },
    { href: "/dashboard/lessons",  icon: BookOpen,         label: "الدروس" },
    { href: "/dashboard/leila",    icon: MessageCircle,    label: "اسألي ليلى" },
    { href: "/dashboard/progress", icon: BarChart3,         label: "تقدمي" },
  ],
};

// ── AI tools — middle school and above (hidden for primary) ────────────────────

const aiToolsSection: NavSection = {
  title: "أدوات ذكية",
  items: [
    { href: "/dashboard/research",        icon: FlaskConical,  label: "البحث الذكي متعدد الوكلاء" },
    { href: "/dashboard/lesson-helper",   icon: BookMarked,    label: "مولد الدروس" },
    { href: "/dashboard/learning-paths",  icon: GitBranch,     label: "مساري التعليمي" },
    { href: "/dashboard/exam-prediction", icon: TrendingUp,    label: "استعداد للامتحان" },
  ],
};

// ── Secondary-only item ────────────────────────────────────────────────────────

const secondarySection: NavSection = {
  title: "الثانوي",
  items: [
    { href: "/dashboard/secondary-school", icon: GraduationCap, label: "الثانوي والباكالوريا" },
  ],
};

// ── Parent section ─────────────────────────────────────────────────────────────

const parentSection: NavSection = {
  title: "الأهل",
  items: [
    { href: "/parent", icon: Users, label: "لوحة الأهل" },
  ],
};

// ── Admin sections ─────────────────────────────────────────────────────────────

const adminSections: NavSection[] = [
  {
    title: "الجودة",
    items: [
      { href: "/dashboard/phase55",            icon: Activity,       label: "Phase55" },
      { href: "/dashboard/curriculum-quality", icon: ClipboardCheck, label: "جودة المنهج" },
      { href: "/dashboard/quality-depth",      icon: Layers,         label: "عمق الجودة" },
      { href: "/dashboard/exam-intelligence",  icon: Zap,            label: "ذكاء الامتحان" },
    ],
  },
  {
    title: "إدارة المحتوى",
    items: [
      { href: "/admin",                         icon: Sparkles,   label: "محتوى AI" },
      { href: "/admin/curriculum-progress",     icon: BarChart3,  label: "تقدم المنهج" },
      { href: "/dashboard/pipeline",            icon: Brain,      label: "عقول المتعدد" },
      { href: "/dashboard/content-enhancement", icon: Wand2,      label: "تحسين المحتوى" },
      { href: "/dashboard/official-alignment",  icon: AlignLeft,  label: "المواءمة الرسمية" },
    ],
  },
];

// ── Sidebar props ──────────────────────────────────────────────────────────────

interface SidebarProps {
  onLogout?:   () => void;
  isOpen?:     boolean;
  onClose?:    () => void;
  isAdmin?:    boolean;
  gradeLevel?: GradeLevel;
}

// ── Section renderer ───────────────────────────────────────────────────────────

function SidebarSection({
  section, pathname, onClose,
}: {
  section:  NavSection;
  pathname: string;
  onClose?: () => void;
}) {
  return (
    <div className="mb-1">
      <p className="px-3 pb-1 pt-3 text-[10px] font-semibold uppercase tracking-widest text-muted-foreground/50">
        {section.title}
      </p>
      {section.items.map(({ href, icon: Icon, label }) => {
        const active =
          pathname === href ||
          (href !== "/dashboard" && pathname.startsWith(href));
        return (
          <Link
            key={href}
            href={href}
            onClick={onClose}
            className={cn(
              "flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm transition-colors",
              active
                ? "bg-primary/10 text-primary font-medium"
                : "text-muted-foreground hover:bg-secondary hover:text-foreground"
            )}
          >
            <Icon className="w-4 h-4 flex-shrink-0" />
            {label}
          </Link>
        );
      })}
    </div>
  );
}

// ── Sidebar ────────────────────────────────────────────────────────────────────

export function Sidebar({
  onLogout, isOpen = false, onClose, isAdmin = false, gradeLevel = "unknown",
}: SidebarProps) {
  const pathname = usePathname();

  // Visibility flags
  const showAiTools  = gradeLevel !== "primary";
  const showSecondary = gradeLevel === "secondary";

  const content = (
    <>
      {/* Logo */}
      <div className="flex items-center gap-3 px-6 py-5 border-b border-border">
        <Link href="/dashboard" onClick={onClose} className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-primary flex items-center justify-center">
            <Star className="w-5 h-5 text-white" />
          </div>
          <span className="text-xl font-bold text-foreground">عقول</span>
        </Link>
        <button
          onClick={onClose}
          className="mr-auto rounded-lg p-2 text-muted-foreground hover:bg-secondary md:hidden"
          aria-label="إغلاق القائمة"
          type="button"
        >
          <X className="h-5 w-5" />
        </button>
      </div>

      {/* Streak */}
      {onLogout && (
        <div className="mx-3 mt-3 mb-1 bg-orange-50 border border-orange-100 rounded-xl px-3 py-2 flex items-center gap-2">
          <span className="text-lg">🔥</span>
          <div className="flex-1 min-w-0">
            <p className="text-xs font-semibold text-orange-800">حافظ على سلسلتك!</p>
            <p className="text-xs text-orange-600">درس يومي = تقدم مستمر</p>
          </div>
        </div>
      )}

      {/* Nav sections */}
      <nav className="flex-1 px-3 py-2 overflow-y-auto">
        <SidebarSection section={learnSection} pathname={pathname} onClose={onClose} />
        {showAiTools && (
          <SidebarSection section={aiToolsSection} pathname={pathname} onClose={onClose} />
        )}
        {showSecondary && (
          <SidebarSection section={secondarySection} pathname={pathname} onClose={onClose} />
        )}
        <SidebarSection section={parentSection} pathname={pathname} onClose={onClose} />
        {isAdmin && adminSections.map((section) => (
          <SidebarSection key={section.title} section={section} pathname={pathname} onClose={onClose} />
        ))}
      </nav>

      {/* Footer */}
      <div className="px-3 py-4 border-t border-border space-y-1">
        <Link
          href="/dashboard/settings"
          onClick={onClose}
          className="flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm text-muted-foreground hover:bg-secondary hover:text-foreground transition-colors"
        >
          <Settings className="w-4 h-4" />
          الإعدادات
        </Link>
        <button
          onClick={onLogout}
          className="flex w-full items-center gap-3 px-3 py-2.5 rounded-xl text-sm text-muted-foreground hover:bg-red-50 hover:text-red-600 transition-colors"
          type="button"
        >
          <LogOut className="w-4 h-4" />
          تسجيل الخروج
        </button>
      </div>
    </>
  );

  return (
    <>
      {isOpen && (
        <button
          className="fixed inset-0 z-40 bg-black/40 md:hidden"
          onClick={onClose}
          aria-label="إغلاق القائمة الجانبية"
          type="button"
        />
      )}
      <aside
        className={cn(
          "fixed inset-y-0 right-0 z-50 flex w-64 flex-col bg-card border-l border-border transition-transform duration-200 md:static md:translate-x-0",
          isOpen ? "translate-x-0" : "translate-x-full md:translate-x-0"
        )}
      >
        {content}
      </aside>
    </>
  );
}

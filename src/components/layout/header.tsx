"use client";
import { Menu } from "lucide-react";
import { HabitBar } from "./habit-bar";

interface HeaderProps {
  childName?: string;
  xp?:        number;
  streak?:    number;
  onMenuToggle?: () => void;
}

export function Header({ childName, xp = 0, streak = 0, onMenuToggle }: HeaderProps) {
  return (
    <header className="h-16 border-b border-border bg-card/90 backdrop-blur-sm flex items-center justify-between px-6 sticky top-0 z-20">
      <div className="flex items-center gap-3">
        <button
          onClick={onMenuToggle}
          className="md:hidden p-2 rounded-lg hover:bg-secondary transition-colors"
        >
          <Menu className="w-5 h-5" />
        </button>
        {childName && (
          <div>
            <p className="text-sm font-semibold text-foreground">{childName}</p>
          </div>
        )}
      </div>

      {/* Persistent habit indicators */}
      <HabitBar streak={streak} xp={xp} />
    </header>
  );
}

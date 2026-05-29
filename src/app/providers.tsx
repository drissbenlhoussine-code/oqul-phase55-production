"use client";

import { ToastProvider } from "@/components/ui/toast";

import { ReactNode } from "react";
import { QueryProvider } from "@/lib/query/query-client";

export function AppProviders({ children }: { children: ReactNode }) {
  return <QueryProvider><ToastProvider>{children}</ToastProvider></QueryProvider>;
}

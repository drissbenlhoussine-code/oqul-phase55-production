import type { Metadata } from "next";
import { headers } from "next/headers";
import "./globals.css";
import { ToastProvider } from "@/components/ui/toast";

export const metadata: Metadata = {
  title: "عقول — التعليم الذكي المغربي",
  description: "منصة تعليمية ذكية للأطفال المغاربة مع المعلمة ليلى",
  metadataBase: new URL(process.env.NEXT_PUBLIC_APP_URL ?? "http://localhost:3000"),
};

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  // Read nonce set by middleware for this request
  const headersList = await headers();
  const nonce = headersList.get("x-nonce") ?? "";

  return (
    <html lang="ar" dir="rtl">
      <head>
        {/* Google Fonts with nonce */}
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;500;600;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body>
        <ToastProvider nonce={nonce}>
          {children}
        </ToastProvider>
      </body>
    </html>
  );
}

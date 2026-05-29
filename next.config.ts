import type { NextConfig } from "next";

const isDev = process.env.NODE_ENV === "development";

/**
 * Security headers — applied globally via Next.js headers().
 * CSP script-src uses 'nonce-based' approach via middleware.
 * No 'unsafe-inline' in production.
 */
const securityHeaders = [
  // CSP is set dynamically in middleware with per-request nonce.
  // The header below is a fallback for routes not handled by middleware.
  {
    key: "Content-Security-Policy",
    value: [
      "default-src 'self'",
      // In production, nonce is required — inline scripts without it are blocked.
      // Middleware sets the real per-request CSP with 'nonce-{nonce} strict-dynamic'.
      isDev ? "script-src 'self' 'unsafe-eval' 'unsafe-inline'" : "script-src 'self'",
      "style-src 'self' https://fonts.googleapis.com",
      "font-src 'self' https://fonts.gstatic.com",
      "img-src 'self' data: blob: https:",
      "connect-src 'self' https://api.groq.com https://*.neon.tech",
      "media-src 'self'",
      "frame-ancestors 'none'",
      "base-uri 'self'",
      "form-action 'self'",
    ].join("; "),
  },
  { key: "X-Frame-Options",           value: "DENY" },
  { key: "X-Content-Type-Options",    value: "nosniff" },
  { key: "Referrer-Policy",           value: "strict-origin-when-cross-origin" },
  { key: "X-DNS-Prefetch-Control",    value: "on" },
  { key: "Permissions-Policy",        value: "camera=(), microphone=(), geolocation=()" },
  { key: "Strict-Transport-Security", value: "max-age=63072000; includeSubDomains; preload" },
  { key: "X-XSS-Protection",          value: "1; mode=block" },
];

const nextConfig: NextConfig = {
  serverExternalPackages: ["bcryptjs", "postgres", "pg"],
  images: {
    remotePatterns: [],
  },
  async headers() {
    return [
      {
        source: "/(.*)",
        headers: securityHeaders,
      },
      {
        // Allow SSE streaming — no buffering
        source: "/api/ai/:path*",
        headers: [
          { key: "Cache-Control",     value: "no-cache, no-transform" },
          { key: "X-Accel-Buffering", value: "no" },
        ],
      },
    ];
  },
};

export default nextConfig;

